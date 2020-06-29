import torch
import random

import numpy as np

from .vocab import create_and_save_dictionary_from_csv

np.random.seed(0)

class Tokenizer:
    '''
    DataLoader class to load dictionary and perform tokenization tasks
    '''

    def __init__(self, saved_location, csv_source=None, word_dict=None):

        self.EOS = 0
        self.UNK = 1

        if saved_location:
            print(f'Loading saved dictionary from {saved_location}')
            word_dict, sentences, max_len = create_and_save_dictionary_from_csv(saved_location, csv_source)

        assert sentences is not None and word_dict is not None, "Please provide a file to extract dictionary from."

        self.VOCAB_SIZE = len(word_dict)
        self.MAX_LEN = max_len + 1
        self.word_dict = word_dict
        print("Creating reverse dictionary")
        self.reverse_map = list(self.word_dict.items())

    def convert_sentence_to_indices(self, sentence, return_with_cuda=True):
        '''
        Converts a sentence to its indices
        '''

        indices = [
            self.word_dict.get(w) if self.word_dict.get(w, self.VOCAB_SIZE + 1) < self.VOCAB_SIZE else self.UNK
            for w in sentence.split()
        ][: self.MAX_LEN - 1]
        
        length = len(indices)
        indices += [self.EOS] * (self.MAX_LEN - len(indices))

        if return_with_cuda:
            indices = np.array(indices)
            indices = torch.tensor(indices).cuda()

        return indices, length

    def convert_batch_sentences_to_indices(self, sentences):
        '''
        Converts a batch of sentences to indices
        '''

        indices_batch = []
        lengths_batch = []
        for sentence in sentences:
            token_label, length = self.convert_sentence_to_indices(sentence, False)
            indices_batch.append(token_label)
            lengths_batch.append(length)

        indices_batch = np.array(indices_batch)
        indices_batch = torch.tensor(indices_batch).cuda()

        return indices_batch, lengths_batch

    def __preprocess_sentence(self, sentence):
        '''
        Preprocesses sentences to match dictionary format
        '''

        return sentence.replace('.', ' .').replace(',', ' ,').replace("'", " '")
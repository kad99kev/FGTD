import torch
import random

import numpy as np

from .vocab import (
    create_and_save_dictionary_from_csv,
    create_and_save_dictionary_from_df,
)

np.random.seed(0)


class Tokenizer:
    """
    Tokenizer class to load dictionary and perform tokenization tasks
    """

    def __init__(self, saved_location, csv_source=None, df=None, word_dict=None):

        self.EOS = 0
        self.UNK = 1

        if saved_location:
            print(f"Loading saved dictionary from {saved_location}")
            assert (
                csv_source is not None or df is not None
            ), "Please provide a single source to read from"
            if csv_source is not None:
                word_dict, max_len = create_and_save_dictionary_from_csv(
                    saved_location, csv_source
                )
            if df is not None:
                word_dict, max_len = create_and_save_dictionary_from_df(
                    saved_location, df
                )

        assert (
            word_dict is not None
        ), "Please provide a file to extract dictionary from."

        self.VOCAB_SIZE = len(word_dict)
        self.MAX_LEN = max_len + 1
        self.word_dict = word_dict
        print("Creating reverse dictionary")
        self.reverse_map = list(self.word_dict.items())
        self.use_cuda = torch.cuda.is_available()

    def convert_sentence_to_indices(self, sentence, return_as_tensor=True):
        """
        Converts a sentence to its indices
        """

        sentence = self.__preprocess_sentence(sentence)

        indices = [
            self.word_dict.get(w)
            if self.word_dict.get(w, self.VOCAB_SIZE + 1) < self.VOCAB_SIZE
            else self.UNK
            for w in sentence.split()
        ][: self.MAX_LEN - 1]

        length = len(indices)
        indices += [self.EOS] * (self.MAX_LEN - len(indices))

        if return_as_tensor:
            indices = np.array(indices)
            indices = torch.tensor(indices)
            if self.use_cuda:
                indices = indices.cuda()

        return indices, length

    def convert_batch_sentences_to_indices(self, sentences):
        """
        Converts a batch of sentences to indices
        """

        indices_batch = []
        lengths_batch = []
        for sentence in sentences:
            token_label, length = self.convert_sentence_to_indices(sentence, False)
            indices_batch.append(token_label)
            lengths_batch.append(length)

        indices_batch = np.array(indices_batch)
        indices_batch = torch.tensor(indices_batch)
        if self.use_cuda:
            indices_batch = indices_batch.cuda()

        return indices_batch, lengths_batch

    def convert_indices_to_sentence(self, indices, length=None):
        """
        Converts an array of indices to its respective sentence
        """

        if length is not None:
            indices = indices[:length]

        def convert_index_to_word(idx):

            idx = idx.data
            if idx == 0:
                return "EOS"
            elif idx == 1:
                return "UNK"

            search_idx = idx - 2
            if search_idx >= len(self.reverse_map):
                return "NA"

            word, idx_ = self.reverse_map[search_idx]

            assert idx_ == idx
            return word

        words = [convert_index_to_word(idx) for idx in indices]

        return " ".join(words)

    def convert_batch_indices_to_sentences(self, batch_indices, lengths=None):
        """
        Converts a batch of indices to sentences
        """

        sentences = []
        for i, indices in enumerate(batch_indices):
            if lengths is not None:
                length = lengths[i]
                sentence = self.convert_indices_to_sentence(indices, length)
            else:
                sentence = self.convert_indices_to_sentence(indices)
            sentences.append(sentence)

        return sentences

    def __preprocess_sentence(self, sentence):
        """
        Preprocesses sentences to match dictionary format
        """

        return sentence.replace(".", " .").replace(",", " ,").replace("'", " '")

import pickle

import pandas as pd

from collections import OrderedDict


def _create_dictionary(text):
    """
    Creating dictionary given text
    """

    max_len = 0
    word_counts = {}
    for line in text:
        line = (
            line.replace(".", " .").replace(",", " ,").replace("'", " '")
        )  # To add , . and ' separately into dictionary
        words = line.split()
        if len(words) > max_len:
            max_len = len(words)
        for word in words:
            if word not in word_counts:
                word_counts[word] = 0
        word_counts[word] += 1

    sorted_words = sorted(
        list(word_counts.keys()), key=lambda x: word_counts[x], reverse=True
    )

    word_dict = OrderedDict()
    for index, word in enumerate(sorted_words):
        word_dict[word] = index + 2  # 0: <eos>, 1: <unk>

    return word_dict, word_counts, max_len


def _save_dictionary(word_dict, word_counts, max_len, saved_location):
    """
    Saves a new dictionary at a given location
    """

    with open(saved_location, "wb") as f:
        pickle.dump(word_dict, f)
        pickle.dump(word_counts, f)
    with open(saved_location[:-4] + ".txt", "w") as f:
        f.write(str(max_len))


def _load_dictionary(saved_location):
    """
    Loads a saved dictionary from a given location
    """

    with open(saved_location, "rb") as f:
        word_dict = pickle.load(f)
    with open(saved_location[:-4] + ".txt", "r") as f:
        max_len = int(f.read())
    return word_dict, max_len


def create_and_save_dictionary_from_df(source, df):
    """
    Loads/Creates a dictionary from input DataFrame
    """

    saved_location = source + ".pkl"
    try:
        cached, max_len = _load_dictionary(saved_location)
        print(f"Using saved dictionary at {saved_location}")

        return cached, max_len
    except:
        print(f"Unable to find saved dictionary at {saved_location}\nCreating new...")

        text = df["text_description"].values

        word_dict, word_counts, max_len = _create_dictionary(text)
        print(f"Found {len(word_dict)} unique words")
        print(f"Saving dictionary at {saved_location}")
        print(f"Maximum length of sequence found is {max_len}")
        _save_dictionary(word_dict, word_counts, max_len, saved_location)

        return word_dict, max_len


def create_and_save_dictionary_from_csv(source, csv_source):
    """
    Loads/Creates a dictionary from input csv
    """

    saved_location = source + ".pkl"
    try:
        cached, max_len = _load_dictionary(saved_location)
        print(f"Using saved dictionary at {saved_location}")

        return cached, max_len
    except:
        print(f"Unable to find saved dictionary at {saved_location}\nCreating new...")

        descr_df = pd.read_csv(csv_source)
        text = descr_df["text_description"].values

        word_dict, word_counts, max_len = _create_dictionary(text)
        print(f"Found {len(word_dict)} unique words")
        print(f"Saving dictionary at {saved_location}")
        print(f"Maximum length of sequence found is {max_len}")
        _save_dictionary(word_dict, word_counts, max_len, saved_location)

        return word_dict, max_len

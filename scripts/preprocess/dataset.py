import torch
import os
import random

import pandas as pd
import numpy as np

from PIL import Image
from tqdm.notebook import tqdm

np.random.seed(0)
torch.manual_seed(0)


class ImageTextDataset(torch.utils.data.Dataset):
    """
    Meant for CelebA Dataset'.
    Pairs True Image, True Text and Wrong Image
    """

    def __init__(self, root_dir, csv_file, transform=None):
        """
        Args:
            root_dir (string): Directory with all the images.
            csv_file (string): Path to the csv file with annotations.
            transform (callable, optional): Optional transform to be applied on a sample.
        """
        self.text_df = pd.read_csv(csv_file)
        self.length = len(self.text_df)
        self.root_dir = root_dir
        self.transform = transform

    def __len__(self):
        return len(self.text_df)

    def __getitem__(self, idx):
        if torch.is_tensor(idx):
            idx = idx.tolist()

        # Real Images
        img_name = os.path.join(self.root_dir, self.text_df.iloc[idx, 0])
        image = Image.open(img_name)

        true_text = self.text_df.iloc[idx, 1:].values[0]

        if self.transform:
            true_image = self.transform(image)

        # Wrong Images
        wrong_idx = random.randint(0, self.length - 1)
        while wrong_idx == idx:
            # To get a different index incase it is same
            wrong_idx = random.randint(0, self.length - 1)
        wrong_img_name = os.path.join(self.root_dir, self.text_df.iloc[wrong_idx, 0])
        wrong_image = Image.open(wrong_img_name)

        if self.transform:
            wrong_image = self.transform(wrong_image)

        return true_image, true_text, wrong_image


def process_data(attribute_csv_path):
    """
    Cleans attributes dataframe based on the preprocessing performed for text generation.
    """

    # Read from csv files
    attributes_df = pd.read_csv(attribute_csv_path)

    # Drop columns
    drop_cols = {"Bags_Under_Eyes", "Bangs", "Blurry", "No_Beard"}
    attributes_df = attributes_df.drop(columns=drop_cols)
    only_attributes = attributes_df.drop(columns="image_id")
    classes = set(only_attributes)
    print("Classes present: ", classes)
    print("Number of classes: ", len(classes))

    return only_attributes, classes


def generate_weights(arr, num_classes):
    """
    Generates weights based on the counts of each label.
    """

    # To get the count of each label
    counts = np.zeros(num_classes)
    for row in tqdm(arr):
        idxs = np.where(row == 1)
        counts[idxs] += 1

    # Calculating weight per class
    N = float(sum(counts))
    weight_per_class = np.zeros(num_classes)
    for i in range(num_classes):
        weight_per_class[i] = N / counts[i]

    # Calculating final weights
    weights = [0.0] * len(arr)
    for i, row in tqdm(enumerate(arr)):
        idxs = np.where(row == 1)
        weights[i] = sum(weight_per_class[idxs])
    return weights


def get_weighted_dataloader(
    attribute_csv_path,
    custom_dataset=None,
    image_location=None,
    text_desc_location=None,
    transform=None,
    subset_size=10000,
    batch_size=64,
):
    """
    Computes weights based on labels and creates a weighted dataloader.
    Get a weighted dataloader for:
        [1] Default ImageTextDataset: Returns -> Real Image, Real Text, Wrong Image
            Requires: image_location, text_desc_location in specified format
        [2] Custom Dataset
    """

    # Get random indices
    random_indices = torch.randperm(subset_size)
    print("Length of random indices:", len(random_indices))

    only_attributes, classes = process_data(attribute_csv_path)

    only_attributes = only_attributes.iloc[random_indices]
    print("Length of subset dataset:", len(only_attributes))

    # Generate weights
    weights = generate_weights(only_attributes.values, len(classes))

    # Sample based on weights
    sampler = torch.utils.data.sampler.WeightedRandomSampler(weights, len(weights))

    # Create dataset
    if custom_dataset is not None:
        print("Using Custom Dataset Loader...")
        dataset = custom_dataset
    else:
        if image_location is None:
            raise NotImplementedError("Image directory not specified")
        if text_desc_location is None:
            raise NotImplementedError("Text path not specified")
        print("Using ImageTextDataset loader...")
        dataset = ImageTextDataset(
            image_location, text_desc_location, transform=transform
        )

    # Create subset of dataset
    subset_dataset = torch.utils.data.Subset(dataset, random_indices)

    # Create weighted loader
    weighted_dataloader = torch.utils.data.DataLoader(
        subset_dataset,
        batch_size=batch_size,
        shuffle=False,
        sampler=sampler,
        pin_memory=True,
    )

    return weighted_dataloader, iter(weighted_dataloader)

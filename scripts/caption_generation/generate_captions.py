import random

random.seed(0)

import pandas as pd
import numpy as np

from tqdm import tqdm

""" Creating sets for categorizing """
# Facial Structure
face_structure = {"Chubby", "Double_Chin", "Oval_Face", "High_Cheekbones"}

# Facial Hair
facial_hair = {"5_o_Clock_Shadow", "Goatee", "Mustache", "Sideburns"}

# Hairstyle
hairstyle = {
    "Bald",
    "Straight_Hair",
    "Wavy_Hair",
    "Black_Hair",
    "Blond_Hair",
    "Brown_Hair",
    "Gray_Hair",
    "Receding_Hairline",
}

# Facial Features
facial_features = {
    "Big_Lips",
    "Big_Nose",
    "Pointy_Nose",
    "Narrow_Eyes",
    "Arched_Eyebrows",
    "Bushy_Eyebrows",
    "Mouth_Slightly_Open",
}

# Appearance
appearance = {
    "Young",
    "Attractive",
    "Smiling",
    "Pale_Skin",
    "Heavy_Makeup",
    "Rosy_Cheeks",
}

# Accessories
accessories = {
    "Wearing_Earrings",
    "Wearing_Hat",
    "Wearing_Lipstick",
    "Wearing_Necklace",
    "Wearing_Necktie",
    "Eyeglasses",
}

# attribute_dict = {
#     'Bags_Under_Eyes' : "had bags under eyes",
#     'Bangs' : "with bangs",
#     'Blurry' : "...........",
#     'No_Beard' : " ",
# }

""" 
Functions to convert attributes to sentences

1. Each function has its own base case and scenarios.
2. To introduce variations, different choice of words are used, however it is ensured that the grammatical structure is maintained.

"""

# Face Strucute
def generate_face_structure(face_attributes, is_male):
    """
    Generates a sentence based on the attributes that describe the facial structure
    """

    features = {
        "Chubby": ["has a chubby face", "is chubby", "looks chubby"],
        "High_Cheekbones": ["high cheekbones", "pretty high cheekbones"],
        "Oval_Face": ["an oval face"],
        "Double_Chin": ["a double chin"],
    }

    if is_male:
        sentence = "The " + random.choice(["man", "gentleman", "male"])
    else:
        sentence = "The " + random.choice(["woman", "lady", "female"])

    if len(face_attributes) == 1:
        attribute = random.choice(features[face_attributes[0]])
        if face_attributes[0] != "Chubby":
            sentence += " has"
        return sentence + " " + attribute + "."
    else:
        for i in range(len(face_attributes)):
            attribute = random.choice(features[face_attributes[i]])

            if i < len(face_attributes) - 1:
                if face_attributes[i] != "Chubby":
                    sentence += " has"
                sentence += " " + attribute + ","
            else:
                sentence = sentence[:-1]
                sentence += " and"
                if face_attributes[i - 1] == "Chubby":
                    # For the current attribute to be grammatically correct incase the previous attribute was chubby
                    sentence += " has"
                sentence += " " + attribute + "."

        return sentence


# Facial Hair
def generate_facial_hair(facial_hair_attributes, is_male):
    """
    Generates a sentence based on the attributes that describe facial hair
    """

    build = ["has a", "wears a", "sports a", "grows a"]

    sentence = "He" if is_male else "She"

    if len(facial_hair_attributes) == 1:
        attribute = (
            facial_hair_attributes[0].lower()
            if facial_hair_attributes[0] != "5_o_Clock_Shadow"
            else "5 o' clock shadow"
        )
        conj = random.choice(build)

        if attribute == "sideburns":
            # Sideburns is plural, dropping 'a'
            conj = "has"

        return sentence + " " + conj + " " + attribute + "."
    else:
        for i in range(len(facial_hair_attributes)):
            attribute = (
                facial_hair_attributes[i].lower()
                if facial_hair_attributes[i] != "5_o_Clock_Shadow"
                else "5 o' clock shadow"
            )
            conj = random.choice(build)

            if attribute == "sideburns":
                # Sideburns is plural, dropping 'a'
                conj = "has"

            if i < len(facial_hair_attributes) - 1:
                sentence = sentence + " " + conj + " " + attribute + ","
            else:
                sentence = sentence[:-1]
                sentence = sentence + " and " + conj + " " + attribute + "."
        return sentence


# Hairstyle
def generate_hairstyle(hairstyle_attributes, is_male):
    """
    Generates a sentence based on the attributes that describe the hairstyle
    """

    hair_type = {"Bald", "Straight_Hair", "Wavy_Hair", "Receding_Hairline"}

    # To create grammatically correct order of description
    arranged_attributes = []
    colours = list(set(hairstyle_attributes) - hair_type)
    if len(colours) > 1:
        # Combines two colours into one attribute
        colour = ""
        for i, _colour in enumerate(colours):
            if i == 0:
                _colour = _colour.lower().split("_")[0] + "ish"
            _colour = _colour.lower().split("_")[0]
            colour += _colour + " "
        arranged_attributes.append(
            colour.strip()
        )  # Strip to remove trailing whitespace
    elif len(colours) == 1:
        colour = colours[0].lower().split("_")[0]
        arranged_attributes.append(colour)
    style = set(hairstyle_attributes) & {"Straight_Hair", "Wavy_Hair"}
    arranged_attributes.extend(list(style))
    bald_rec = set(hairstyle_attributes) & {"Receding_Hairline", "Bald"}
    arranged_attributes.extend(list(bald_rec))

    if len(arranged_attributes) == 1:
        attribute = arranged_attributes[0].lower().split("_")[0]
        if attribute == "bald":
            return "He is bald." if is_male else "She is bald."
        if random.random() <= 0.5:
            sentence = "His" if is_male else "Her"
            return sentence + " hair is " + attribute + "."
        else:
            sentence = "He" if is_male else "She"
            return sentence + " has " + attribute + " hair."

    # Adding variation in sentence structure
    if random.random() <= 0.5:
        sentence = "His" if is_male else "Her"
        sentence += " hair is"
        for i, attribute in enumerate(arranged_attributes):
            attribute = attribute.lower().split("_")[0]
            if len(arranged_attributes) - 1 == i:
                sentence = sentence[:-1]
                if attribute == "bald":
                    attribute = "he" if is_male else "she"
                    attribute += (
                        " is " + random.choice(["going", "partially"]) + " bald"
                    )
                    return sentence + " and " + attribute + "."
                return sentence + " and " + attribute + "."
            sentence += " " + attribute + ","
    else:
        sentence = "He" if is_male else "She"
        sentence += " has"
        for i, attribute in enumerate(arranged_attributes):
            attribute = attribute.lower().split("_")[0]
            if len(arranged_attributes) - 1 == i:
                sentence = sentence[:-1]
                if attribute == "bald":
                    sentence += " hair"
                    attribute = "he" if is_male else "she"
                    attribute += (
                        " is " + random.choice(["going", "partially"]) + " bald"
                    )
                    return sentence + " and " + attribute + "."
                return sentence + " and " + attribute + " hair."
            sentence += " " + attribute + ","


# Facial Features
def generate_facial_features(facial_features, is_male):
    """
    Generates a sentence based on the attributes that describe the facial features
    """

    sentence = "He" if is_male else "She"
    sentence += " has"

    def nose_and_mouth(attribute):
        """
        Returns a grammatically correct sentence based on the attribute
        """

        if attribute == "big nose" or attribute == "pointy nose":
            return "a " + attribute
        elif attribute == "mouth slightly open":
            return "a slightly open mouth"
        return attribute

    if len(facial_features) == 1:
        attribute = nose_and_mouth(" ".join(facial_features[0].lower().split("_")))
        return sentence + " " + attribute + "."

    for i, attribute in enumerate(facial_features):
        attribute = nose_and_mouth(" ".join(attribute.lower().split("_")))

        if i == len(facial_features) - 1:
            sentence = sentence[:-1]
            sentence += " and " + attribute + "."
        else:
            sentence += " " + attribute + ","

    return sentence


# Appearance
def generate_appearance(appearance, is_male):
    """
    Generates a sentence based on the attributes that describe the appearance
    """

    # Further divides into 3 sections
    # is_smiling for smile, this comes either before qualities, or after. It always comes before extras
    # qualities for young and attractive
    # extras for remaining
    is_smiling = "Smiling" in appearance
    smile_begin = False if not is_smiling else True if random.random() <= 0.5 else False
    qualities = list(set(appearance) & {"Young", "Attractive"})
    extras = list(set(appearance) & {"Pale_Skin", "Heavy_Makeup", "Rosy_Cheeks"})

    sentence = (
        random.choice(["He", "The man", "The gentleman", "The male"])
        if is_male
        else random.choice(["She", "The woman", "The lady", "The female"])
    )

    if is_smiling and len(qualities) == 0 and len(extras) == 0:
        # If the person is only smiling
        return sentence + " is smiling."

    if is_smiling and smile_begin:
        # If there are other attributes but sentence should begin with is smiling
        sentence += " is smiling"
        sentence += "," if len(qualities) > 0 or len(extras) > 1 else ""

    # print(f'After check smiling begin: {sentence}')

    if len(qualities) == 1:
        if len(extras) == 0 and smile_begin:
            # To remove the comma from above
            sentence = sentence[:-1]
            sentence += " and"
        sentence += (
            random.choice([" looks", " is", " seems"]) + " " + qualities[0].lower()
        )
        sentence += (
            "," if len(extras) > 1 or (is_smiling and not smile_begin) else ""
        )  # To add a comma for smiling
    elif len(qualities) > 1:
        sentence += random.choice([" looks", " is", " seems"])
        for i in range(len(qualities)):
            attribute = qualities[i].lower()

            if i == len(qualities) - 1 and len(extras) == 0:
                sentence = sentence[:-1]
                sentence += " and " + attribute
            else:
                sentence += " " + attribute + ","

    # print(f'After qualities: {sentence}')

    if is_smiling and not smile_begin:
        # If there are other attributes but is smiling comes later
        if len(extras) == 0:
            sentence = sentence.replace(",", " and")
        sentence += " is smiling"
        sentence += "," if len(extras) > 1 else ""

    extras = [" ".join(e.split("_")) for e in extras]

    if len(extras) == 0:
        return sentence + "."
    elif len(extras) == 1:
        if len(qualities) > 0 or is_smiling:
            # If smiling or qualities exist, then add an and
            if len(qualities) > 1 and ((is_smiling and smile_begin) or not is_smiling):
                # To remove the last comma from the qualities if smiling is at beginning
                sentence = sentence[:-1]
            sentence += " and"
        return sentence + " has " + extras[0].lower() + "."
    else:
        sentence += " has"
        for i in range(len(extras)):
            attribute = extras[i].lower()

            if i == len(extras) - 1:
                sentence = sentence[:-1]
                sentence += " and " + attribute
            else:
                sentence += " " + attribute + ","

        return sentence + "."


# Accessories
def generate_accessories(accessories, is_male):
    """
    Generates a sentence based on the accessories defined by the attributes
    """

    sentence = "He" if is_male else "She"
    sentence += " is wearing"

    def necktie_and_hat(attribute):
        """
        Returns a grammatically correct sentence based on the attribute
        """

        if attribute == "necktie" or attribute == "hat" or attribute == "necklace":
            return "a " + attribute
        return attribute

    if len(accessories) == 1:
        attribute = (
            accessories[0].lower()
            if accessories[0] == "Eyeglasses"
            else necktie_and_hat(accessories[0].lower().split("_")[1])
        )
        return sentence + " " + attribute + "."

    for i, attribute in enumerate(accessories):
        attribute = (
            attribute.lower()
            if attribute == "Eyeglasses"
            else necktie_and_hat(attribute.lower().split("_")[1])
        )

        if i == len(accessories) - 1:
            sentence = sentence[:-1]
            sentence += " and " + attribute + "."
        else:
            sentence += " " + attribute + ","

    return sentence


def generate_one_to_one_caption(df, path="dataset/text_descr_celeba.csv"):
    # New dict for storing image_ids and their description
    new_dict = {"image_id": [], "text_description": []}

    for i in tqdm(df.index):

        image_id = df.loc[i, "image_id"]

        face_structure_arr = []
        facial_hair_arr = []
        hairstyle_arr = []
        facial_features_arr = []
        appearance_arr = []
        accessories_arr = []
        is_male = False

        description = ""

        for attr in df.loc[i, "attributes"]:
            # Creating feature array

            if attr in face_structure:
                face_structure_arr.append(attr)

            elif attr in facial_hair:
                facial_hair_arr.append(attr)

            elif attr in hairstyle:
                hairstyle_arr.append(attr)

            elif attr in facial_features:
                facial_features_arr.append(attr)

            elif attr in appearance:
                appearance_arr.append(attr)

            elif attr in accessories:
                accessories_arr.append(attr)

            elif attr == "Male":
                is_male = True

        # Generating sentences for each set of attributes
        if face_structure_arr != []:
            face_structure_txt = generate_face_structure(face_structure_arr, is_male)
            description += face_structure_txt + " "

        if facial_hair_arr != []:
            facial_hair_txt = generate_facial_hair(facial_hair_arr, is_male)
            description += facial_hair_txt + " "

        if hairstyle_arr != []:
            hairstyle_txt = generate_hairstyle(hairstyle_arr, is_male)
            description += hairstyle_txt + " "

        if facial_features_arr != []:
            facial_features_txt = generate_facial_features(facial_features_arr, is_male)
            description += facial_features_txt + " "

        if appearance_arr != []:
            appearance_txt = generate_appearance(appearance_arr, is_male)
            description += appearance_txt + " "

        if accessories_arr != []:
            accessories_txt = generate_accessories(accessories_arr, is_male)
            description += accessories_txt + " "

        if description == "":
            # All attributes are not present, then only use gender to construct simple sentence
            if is_male:
                description = (
                    "There is a " + random.choice(["man", "gentleman", "male"]) + "."
                )
            else:
                description = (
                    "There is a " + random.choice(["woman", "lady", "female"]) + "."
                )

        # Adding to new dict
        new_dict["image_id"].append(image_id)
        new_dict["text_description"].append(description.strip())

    # Saving into csv
    pd.DataFrame(data=new_dict).to_csv(path, index=False)


def generate_one_to_N_caption(df, N=5, dataset_size=10_000):
    # New dict for storing image_ids and their description
    new_dict = {"image_id": [], "text_description": []}

    for i in tqdm(range(dataset_size)):

        image_id = df.loc[i, "image_id"]
        total_description = ""

        for j in range(N):

            face_structure_arr = []
            facial_hair_arr = []
            hairstyle_arr = []
            facial_features_arr = []
            appearance_arr = []
            accessories_arr = []
            is_male = False

            description = ""

            for attr in df.loc[i, "attributes"]:
                # Creating feature array

                if attr in face_structure:
                    face_structure_arr.append(attr)

                elif attr in facial_hair:
                    facial_hair_arr.append(attr)

                elif attr in hairstyle:
                    hairstyle_arr.append(attr)

                elif attr in facial_features:
                    facial_features_arr.append(attr)

                elif attr in appearance:
                    appearance_arr.append(attr)

                elif attr in accessories:
                    accessories_arr.append(attr)

                elif attr == "Male":
                    is_male = True

            # Generating sentences for each set of attributes
            if face_structure_arr != []:
                face_structure_txt = generate_face_structure(
                    face_structure_arr, is_male
                )
                description += face_structure_txt + " "

            if facial_hair_arr != []:
                facial_hair_txt = generate_facial_hair(facial_hair_arr, is_male)
                description += facial_hair_txt + " "

            if hairstyle_arr != []:
                hairstyle_txt = generate_hairstyle(hairstyle_arr, is_male)
                description += hairstyle_txt + " "

            if facial_features_arr != []:
                facial_features_txt = generate_facial_features(
                    facial_features_arr, is_male
                )
                description += facial_features_txt + " "

            if appearance_arr != []:
                appearance_txt = generate_appearance(appearance_arr, is_male)
                description += appearance_txt + " "

            if accessories_arr != []:
                accessories_txt = generate_accessories(accessories_arr, is_male)
                description += accessories_txt + " "

            if description == "":
                # All attributes are not present, then only use gender to construct simple sentence
                if is_male:
                    description = (
                        "There is a "
                        + random.choice(["man", "gentleman", "male"])
                        + "."
                    )
                else:
                    description = (
                        "There is a " + random.choice(["woman", "lady", "female"]) + "."
                    )

            total_description += description + "\n"

        # Adding to new dict
        new_dict["image_id"].append(image_id)
        new_dict["text_description"].append(total_description.strip())

    # Saving into csv
    pd.DataFrame(data=new_dict).to_csv(
        f"dataset/text_{N}_descr_celeba.csv", index=False
    )


if __name__ == "__main__":
    # Read CSV
    df = pd.read_csv("dataset/list_attr_celeba.csv")

    # Numpy array of dataframe column names
    cols = np.array(df.columns)

    # Boolean array to mark where dataframe values equal 1
    b = df.values == 1

    # List comprehension to join column names for each boolean row result
    df["attributes"] = [cols[(row_index)] for row_index in b]

    generate_one_to_N_caption(df)

import pandas as pd
import numpy as np

df = pd.read_csv('./dataset/list_attr_celeba.csv')
df = df.head(2)
# numpy array of dataframe column names
cols = np.array(df.columns)
# boolean array to mark where dataframe values equal 1
b = (df.values == 1)
# list comprehension to join column names for each boolean row result
df['attributes'] = [', '.join(cols[(row_index)]) for row_index in b]
df['attributes'] = df['attributes'].str.split(", ", expand = True).values.tolist()

# what is the structure of the face
face_structure = {
    'Chubby' : "has a chubby face",
    'Double_Chin' : "has a double chin",
    'Oval_Face' : "has an oval face",
    'High_Cheekbones' : 'has high cheekbones'
}

#what facial hairstyle does the person sport
facial_hairstyle = {
    '5_o_Clock_Shadow' : "a 5 o'clock shadow",
    'Goatee' : "a goatee",
    'Mustache' : "with a mustache",
    'Sideburns' : "sideburns"
}

#what hairstyle does the person sport 
hairstyle = {
    'Bald' : "is bald",
    'Straight_Hair' : "has straight hair",
    'Wavy_Hair' : "has wavy hair",
    'Black_Hair' : "has black hair", 
    'Blond_Hair' : "has blonde hair",
    'Brown_Hair' : "has brown hair",
    'Gray_Hair' : "has gray hair",
    'Receding_Hairline' : "has a receding hariline"
}

#what is the description of other facial features
facial_features = {
    'Big_Lips' : "big lips",
    'Big_Nose' : "big nose",
    'Pointy_Nose' : "pointy nose",
    'Narrow_Eyes' : "narrow eyes",
    'Arched_Eyebrows' : "arched eyebrows",
    'Bushy_Eyebrows' : "bushy eyebrows",
    'Mouth_Slightly_Open' : "mouth slightly open"
}

#what are the attributes that enhance their appearance
appearance = {
    'Young' : "young",
    'Attractive' : "is attractive",
    'Smiling' : "smiling",
    'Pale_Skin' : "pale skin",
    'Heavy_Makeup' : "wore heavy makeup",
    'Rosy_Cheeks' : "with rosy cheeks"
}

#what are the accessories worn
accessories = {
    'Wearing_Earrings' : "wearing earings",
    'Wearing_Hat' : "wearing a hat",
    'Wearing_Lipstick' : "wearing lipstick",
    'Wearing_Necklace' : "wearing a necklace",
    'Wearing_Necktie' : "wearing a necktie",
    'Eyeglasses' : "wears eyeglasses",

}

attribute_dict = {
    'Bags_Under_Eyes' : "had bags under eyes",
    'Bangs' : "with bangs",
    'Blurry' : "...........",
    'No_Beard' : " ",
}


#face structure 
def face(face_attributes, gender):
    if gender:
        sentence = 'The man'
    else:
        sentence = 'The woman'
    
    if len(face_attributes) == 1:
        return (sentence + ' ' + face_structure[face_attributes[0]])
    else:
        for i in range(len(face_attributes)):
            if i < len(face_attributes) - 1:
                sentence = sentence + ' ' + face_structure[face_attributes[i]] + ', '
            else:
                sentence = sentence[:-2]
                sentence = sentence + ' and ' + face_structure[face_attributes[-1]] + '.'
        return sentence

#facial hair
def face_hair(face_hair_attr, gender):
    if gender:
        sentence = 'He'
    else:
        sentence = 'She'
    if len(face_hair_attr) == 1:
        return (sentence + ' ' + facial_hairstyle[face_hair_attr[0]])
    else:
        for i in range(len(face_hair_attr)):
            if i < len(face_hair_attr) - 1:
                sentence = sentence + ' ' + face_structure[face_hair_attr[i]] + ', '
            else:
                sentence = sentence[:-2]
                sentence = sentence + ' and ' + face_structure[face_hair_attr[-1]] + '.'
        return sentence

#hair 
def hair(hair_attr, gender):
    if gender:
        sentence = 'He'
    else:
        sentence = 'She'

    if len(hair_attr) == 1:
        return (sentence + ' ' + hairstyle[hair_attr[0]])
    else:
        for i in range(len(hair_attr)):
            if i < len(hair_attr) - 1:
                sentence = sentence + ' ' + hairstyle[hair_attr[i]] + ', '
            else:
                sentence = sentence[:-2]
                sentence = sentence + ' and ' + hairstyle[hair_attr[-1]] + '.'
        return sentence
    
#faical features
def face_features(face_feature, gender):
    if gender:
        sentence = 'He'
    else:
        sentence = 'She'

    if len(face_feature) == 1:
        return (sentence + ' ' + facial_features[face_feature[0]])
    else:
        for i in range(len(face_feature)):
            if i < len(face_feature) - 1:
                sentence = sentence + ' ' + facial_features[face_feature[i]] + ', '
            else:
                sentence = sentence[:-2]
                sentence = sentence + ' and ' + facial_features[face_feature[-1]] + '.'
        return sentence



for i in range(len(df)):
    _face_attributes = []
    _face_hair = []
    _hair = []
    _face_features = []
    _appearance = []
    _accessories = []
    _male = False
    for ele in df.loc[i , 'attributes']:
        if ele in face_structure.keys():
            _face_attributes.append(ele)
        elif ele in facial_hairstyle.keys():
            _face_hair.append(ele)
        elif ele in hairstyle.keys():
            _hair.append(ele)
        elif ele in facial_features.keys():
            _face_features.append(ele)
        elif ele in accessories.keys():
            _accessories.append(ele)
        elif ele in appearance.keys():
            _appearance.append(ele)
        elif ele is 'Male':
            _male = True
    print(i)
    if _face_attributes != []:
        face_attr = face(_face_attributes, _male)
        print(face_attr)
    elif _face_hair != []:
        face_hair_attr = face_hair(_face_hair, _male)
        print(face_hair_attr)
    elif _hair != []:
        print('yes')
        hair_attr = hair(_hair, _male)
        print(hair_attr)
    elif _face_features != []:
        face_features_attr = face_features(_face_features, _male)
        print(face_features_attr)
    print('Face_structure : ' ,_face_attributes)
    print('Facial hair : ', _face_hair)
    print('Hairstyle : ', _hair)
    print('Facial features : ', _face_features)
    print('Appearance : ', _appearance)
    print('Accessories : ', _accessories)








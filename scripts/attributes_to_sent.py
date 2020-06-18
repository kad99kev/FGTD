import pandas as pd
import numpy as np

df = pd.read_csv('./dataset/list_attr_celeba.csv')
df = df.head(5)
# numpy array of dataframe column names
cols = np.array(df.columns)
# boolean array to mark where dataframe values equal 1
b = (df.values == 1)
# list comprehension to join column names for each boolean row result
df['attributes'] = [', '.join(cols[(row_index)]) for row_index in b]
print(df.loc[0, 'attributes'])
df['attributes'] = df['attributes'].str.split(", ", expand = True).values.tolist()


attribute_dict = {
    '5_o_Clock_Shadow' : "a 5 o'clock shadow",
    'Arched_Eyebrows' : "arched eyebrows",
    'Attractive' : "is attractive",
    'Bags_Under_Eyes' : "had bags under eyes",
    'Bald' : "was bald",
    'Big_Lips' : "had big lips",
    'Bangs' : "with bangs",
    'Big_Nose' : "with a big nose",
    'Black_Hair' : "had black hair", 
    'Blond_Hair' : "had blonde hair",
    'Brown_Hair' : "had brown hair",
    'Blurry' : "...........",
    'Bushy_Eyebrows' : "had bushy eyebrows",
    'Chubby' : "was chubby",
    'Double_Chin' : "had a double chin",
    'Eyeglasses' : "wears eyeglasses",
    'Goatee' : "had a goatee",
    'Heavy_Makeup' : "wore heavy makeup",
    'High_Cheekbones' : 'had high cheekbones',
    'Mouth_Slightly_Open' : "had mouth slightly open",
    'Mustache' : "with a mustache",
    'Narrow_Eyes' : "had narrow eyes",
    'No_Beard' : " ",
    'Oval_Face' : "had an oval face",
    'Pale_Skin' : "had pale skin",
    'Pointy_Nose' : "had a pointy nose",
    'Receding_Hairline' : "had a receding hariline",
    'Rosy_Cheeks' : "with rosy cheeks",
    'Sideburns' : "had sideburns",
    'Smiling' : "was smiling",
    'Straight_Hair' : "had straight hair",
    'Wavy_Hair' : "had wavy hair",
    'Wearing_Earrings' : "was wearing earings",
    'Wearing_Hat' : "was wearing a hat",
    'Wearing_Lipstick' : "was wearing lipstick",
    'Wearing_Necklace' : "was wearing a necklace",
    'Wearing_Necktie' : "was wearing a necktie",
    'Young' : "was young"


}



for i in range(len(df)):
    attributes = [i for i in df.loc[i, 'attributes'] if i] 
    if 'Male' in attributes:
        attributes.remove('Male')
        sentence = 'He sports '
    else:
        sentence = 'He sports '
    for ele in attributes:
            sentence = sentence + attribute_dict[ele] + ", "
    sentence = sentence[:-2]
    sentence = sentence + '.'
    print(sentence)
    

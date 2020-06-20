import random

# import pandas as pd
import numpy as np

# df = pd.read_csv('./dataset/list_attr_celeba.csv')
# df = df.head(10)
# # Numpy array of dataframe column names
# cols = np.array(df.columns)

# # Boolean array to mark where dataframe values equal 1
# b = (df.values == 1)

# # List comprehension to join column names for each boolean row result
# df['attributes'] = [', '.join(cols[(row_index)]) for row_index in b]
# df['attributes'] = df['attributes'].str.split(', ', expand = True).values.tolist()


# Facial Structure
face_structure = {'Chubby', 'Double_Chin', 'Oval_Face', 'High_Cheekbones'}

# Facial Hair
facial_hair = {'5_o_Clock_Shadow', 'Goatee', 'Mustache', 'Sideburns'}

# Hairstyle
hairstyle = {'Bald', 'Straight_Hair', 'Wavy_Hair', 'Black_Hair', 'Blond_Hair', 'Brown_Hair', 'Gray_Hair', 'Receding_Hairline'}

# Facial Features
facial_features = {'Big_Lips', 'Big_Nose', 'Pointy_Nose', 'Narrow_Eyes', 'Arched_Eyebrows', 'Bushy_Eyebrows', 'Mouth_Slightly_Open'}

# Appearance
appearance = {'Young', 'Attractive', 'Smiling', 'Pale_Skin', 'Heavy_Makeup', 'Rosy_Cheeks'}

# Accessories
accessories = {'Wearing_Earrings', 'Wearing_Hat', 'Wearing_Lipstick', 'Wearing_Necklace', 'Wearing_Necktie', 'Eyeglasses'}

# attribute_dict = {
#     'Bags_Under_Eyes' : "had bags under eyes",
#     'Bangs' : "with bangs",
#     'Blurry' : "...........",
#     'No_Beard' : " ",
# }


# Face Strucute 
def generate_face_structure(face_attributes, gender):
	features = {
		'Chubby': ['has a chubby face', 'is chubby', 'looks chubby'],
		'High_Cheekbones': ['high cheekbones', 'pretty high cheekbones'],
		'Oval_Face': ['an oval face'],
		'Double_Chin': ['a double chin']
	}

	if gender:
		sentence = 'The ' + random.choice(['man', 'gentleman', 'male'])
	else:
		sentence = 'The ' + random.choice(['woman', 'lady', 'female'])
	
	if len(face_attributes) == 1:
		attribute = random.choice(features[face_attributes[0]])
		if face_attributes[0] != 'Chubby':
			sentence += ' has'
		return sentence + ' ' + attribute + '.'
	else:
		for i in range(len(face_attributes)):
			attribute = random.choice(features[face_attributes[i]])
			
			if i < len(face_attributes) - 1:
				if face_attributes[i] != 'Chubby':
					sentence += ' has'
				sentence += ' ' + attribute + ','
			else:
				sentence = sentence[:-1]
				sentence += ' and'
				if face_attributes[i - 1] == 'Chubby':
					sentence += ' has'
				sentence += ' ' + attribute + '.'
		
		return sentence

# Facial Hair
def generate_facial_hair(facial_hair_attributes, gender):
	build = ['has a', 'wears a', 'sports a', 'grows a']

	sentence = 'He' if gender else 'She'
	
	if len(facial_hair_attributes) == 1:
		attribute = ' '.join(facial_hair_attributes[0].lower().split('_')) if facial_hair_attributes[0] != '5_o_Clock_Shadow' else '5 o\' clock shadow'
		return sentence + ' ' + random.choice(build) + ' ' + attribute + '.'
	else:
		for i in range(len(facial_hair_attributes)):
			attribute = ' '.join(facial_hair_attributes[i].lower().split('_')) if facial_hair_attributes[i] != '5_o_Clock_Shadow' else '5 o\' clock shadow'
			conj = random.choice(build)

			if attribute == 'sideburns':
				conj = 'has'

			if i < len(facial_hair_attributes) - 1:
				sentence = sentence + ' ' + conj + ' ' + attribute + ','
			else:
				sentence = sentence[:-1]
				sentence = sentence + ' and ' + conj + ' ' + attribute + '.'
		return sentence

# Hairstyle 
def generate_hairstyle(hairstyle_attributes, gender):
	hair_type = {'Bald', 'Straight_Hair', 'Wavy_Hair', 'Receding_Hairline'}

	def return_formation(gender, style=None, colour=None):
		
		if random.random() <= 0.5:
			sentence = 'His' if gender else 'Her'

			if style is not None and colour is not None:
				if random.random() <= 0.5:
					return sentence + ' ' + random.choice([f'hair is {style} and {colour} in colour.', f'hair is {style} and {colour}.'])
				else:
					return sentence + ' ' + random.choice([f'hair is {colour} and {style}.', f'hair is {colour} and {style} in style.'])

			if style is not None:
				return sentence + ' hair is ' + style + '.'
			else:
				return sentence + ' hair is ' + colour + ' in colour.'
		else:
			sentence = 'He' if gender else 'She'
			
			if style is not None and colour is not None:
				if random.random() <= 0.5:
					return sentence + ' ' + random.choice([f'has {style} hair which is {colour} in colour.', f'has {style} hair which is {colour}.', f'has {style} {colour} hair.'])
				else:
					return sentence + ' ' + random.choice([f'has {colour} hair which is {style} in style.', f'has {colour} hair which is {style}.', f'has {colour} {style} hair.'])
			
			if style is not None:
				return sentence + ' has ' + style + ' hair.'
			else:
				return sentence + ' hair ' + colour + ' hair.'

	if len(hairstyle_attributes) == 1:
	
		attribute = ' '.join(hairstyle_attributes[0].lower().split('_'))
		
		if attribute == 'bald':
			if gender:
				sentence = 'He'
			else:
				sentence = 'She'
			return sentence + ' is ' + attribute + '.' 
		
		if hairstyle_attributes[0] in hair_type:
			return return_formation(gender, style=attribute)
		else:
			return return_formation(gender, colour=attribute)

	else:
		if hairstyle_attributes[0] in hair_type:
			style = hairstyle_attributes[0].lower().split('_')[0]
			colour = hairstyle_attributes[1].lower().split('_')[0]
			return return_formation(gender, style, colour)
		else:
			style = hairstyle_attributes[1].lower().split('_')[0]
			colour = hairstyle_attributes[0].lower().split('_')[0]
			return return_formation(gender, style, colour)
	
# Appearance
def generate_appearance(face_feature, gender):

	is_smiling = 'Smiling' in face_feature
	smile_begin = False if not is_smiling else True if random.random() <= 0.5 else False
	qualities = list(set(face_feature) & {'Young', 'Attractive'})
	extras = list(set(face_feature) & {'Pale_Skin', 'Heavy_Makeup', 'Rosy_Cheeks'})

	sentence = random.choice(['He', 'The man', 'The gentleman', 'The male']) if gender else random.choice(['She', 'The woman', 'The lady', 'The female'])
	
	if is_smiling and smile_begin:
		sentence += ' is smiling'
		sentence += ' and' if len(qualities) == 0 else ',' if len(qualities) > 0 else ''

	if len(qualities) == 1:
		sentence += random.choice([' looks', ' is', ' seems']) + ' ' + qualities[0].lower()
		sentence += ' and' if len(extras) == 1 and smile_begin else ',' if len(extras) > 0 else ''
	elif len(qualities) > 1:
		sentence += random.choice([' looks', ' is', ' seems'])
		for i in range(len(qualities)):
			attribute = qualities[i].lower()

			if i == len(qualities) - 1 and len(extras) == 0:
				sentence = sentence[:-1]
				sentence += ' and ' + attribute
			else:
				sentence += ' ' +  attribute + ','

	if is_smiling and not smile_begin:
		if len(extras) == 0:
			sentence = sentence.replace(' and', ',')
			sentence += ' and'
		sentence += ' is smiling'
		sentence += ',' if len(extras) > 1 else ' and' if len(extras) == 1 else ''


	extras = [' '.join(e.split('_')) for e in extras]

	if len(extras) == 0:
		return sentence + '.'
	elif len(extras) == 1:
		return sentence + ' has ' + extras[0].lower() + '.'
	else:
		sentence += ' has'
		for i in range(len(extras)):
			attribute = extras[i].lower()
			
			if i == len(extras) - 1:
				sentence = sentence[:-1]
				sentence += ' and ' + attribute
			else:
				sentence += ' ' + attribute + ','

		return sentence + '.'



#################### Test ####################

# test_features = [['High_Cheekbones', 'Oval_Face'], ['Chubby'], ['Chubby', 'Double_Chin'], ['High_Cheekbones', 'Chubby'], ['High_Cheekbones', 'Chubby', 'Oval_Face']]
# for f in test_features:
# 	print(generate_face_structure(f, False))

# test_features = [['5_o_Clock_Shadow', 'Goatee'], ['Mustache'], ['Goatee', '5_o_Clock_Shadow'], ['Mustache', 'Sideburns'], ['5_o_Clock_Shadow', 'Sideburns', 'Mustache']]
# for f in test_features:
# 	print(generate_facial_hair(f, True))

# test_features = [['Straight_Hair', 'Brown_Hair'], ['Bald'], ['Receding_Hairline', 'Brown_Hair'], ['Wavy_Hair', 'Gray_Hair'], ['Straight_Hair', 'Blond_Hair']]
# for f in test_features:
# 	print(generate_hairstyle(f, True))

test_features = [['Attractive', 'Young', 'Pale_Skin', 'Smiling', 'Rosy_Cheeks'], ['Smiling', 'Rosy_Cheeks'], ['Attractive', 'Smiling', 'Rosy_Cheeks', 'Heavy_Makeup'], ['Attractive', 'Smiling', 'Heavy_Makeup'], ['Young', 'Smiling', 'Heavy_Makeup'], ['Attractive', 'Smiling', 'Young'], ['Attractive', 'Young']]
for f in test_features:
	print(generate_appearance(f, True))


#################### Working ####################

# for i in df.index:
	
# 	_face_attributes = []
# 	_face_hair = []
# 	_hair = []
# 	_face_features = []
# 	_appearance = []
# 	_accessories = []
# 	_male = False
	
# 	for ele in df.loc[i , 'attributes']:
# 		if ele in face_structure:
# 			_face_attributes.append(ele)
		
# 		elif ele in facial_hair:
# 			_face_hair.append(ele)
		
# 		elif ele in hairstyle:
# 			_hair.append(ele)
		
# 		elif ele in facial_features:
# 			_face_features.append(ele)
		
# 		elif ele in accessories:
# 			_accessories.append(ele)
		
# 		elif ele in appearance:
# 			_appearance.append(ele)
		
# 		elif ele is 'Male':
# 			_male = True
	
# 	print(i)
	
# 	if _face_attributes != []:
# 		face_attr = face(_face_attributes, _male)
# 		print(face_attr)
	
# 	# elif _face_hair != []:
# 	#     face_hair_attr = face_hair(_face_hair, _male)
# 	#     print(face_hair_attr)
	
# 	# elif _hair != []:
# 	#     print('yes')
# 	#     hair_attr = hair(_hair, _male)
# 	#     print(hair_attr)
	
# 	# elif _face_features != []:
# 	#     face_features_attr = face_features(_face_features, _male)
# 	#     print(face_features_attr)
	
# 	print('Face_structure : ' ,_face_attributes)
# 	print('Facial hair : ', _face_hair)
# 	print('Hairstyle : ', _hair)
# 	print('Facial features : ', _face_features)
# 	print('Appearance : ', _appearance)
# 	print('Accessories : ', _accessories)
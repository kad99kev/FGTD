# Text2Face 📝 -> 👧👱

## 🤞 Motivation

Powerful Generative Adverserial Networks have been used in the past to automatically synthesize realistic images from text. However, these existing task have been used for simple tasks such as flowers and birds.
So, our aim is to focus on a less addressed domain of face generation from fine-granined textual description of faces.

However, as we are still undergrad students, we decided to not only build our main GAN, but also a ladder of GANs that helped strengthen our understanding, in hopes to inspire others.

## 📈 Our Progress Ladder 

**Step 1. We started with Simple GANs on the MNIST digit dataset** 🔢

🔗 [Code, References and Output](https://github.com/kad99kev/Face-Generator/tree/master/MNIST-GANs/GAN)

**Step 2. Progressed our way up to understanding other GAN architectures on the digit and fashion MNIST datasets.** 👗 👕

🔗 [Conditional GANS Code, References and Output](https://github.com/kad99kev/Face-Generator/tree/master/MNIST-GANs/CGAN)

🔗 [Auxillary Conditional GANS Code, References and Output](https://github.com/kad99kev/Face-Generator/tree/master/MNIST-GANs/ACGAN)

🔗 [Deep Convolution GANS Code, References and Output](https://github.com/kad99kev/Face-Generator/tree/master/MNIST-GANs/DCGAN)

**Step 3. Researched about past implementations on the topic**
(Some of the research paper links)

* [FTGAN : A fully Generative Adverserial Network for Text to Face Generation](https://arxiv.org/pdf/1904.05729.pdf)
* [Text2FaceGAN : Face Generation from Fine Grained Description](https://arxiv.org/pdf/1911.11378.pdf) 
* [Generative Adverserial Text to Image Synthesis](https://arxiv.org/pdf/1605.05396.pdf)


**Step 4. Created a meaningful text dataset using Celeb-A**

Here, the challenege faced was to create meaningful sentences using a mutli-labelled dataset. We considered the following 6 cateogeries 

  🔸 The structure of the face
  
  🔸 The facical hairstyle the person sports
  
  🔸 The description of other facical features
  
  🔸 The hairstyle of the person
  
  🔸 Attriubutes that enhance his appearance
  
  🔸 Accessories worn (if any)
  
  An example of one of the sentences from the dataset
   <img src = "assets/dataset.png">
  
  




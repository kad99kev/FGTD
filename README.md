# Face Generation from Textual Description using Generative Adverserial Networks 📝  2️⃣ 👧👱 [![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/ELITA04/FGTD-Streamlit/app.py/)

*Under Construction!*

---

🔹 [Abstract](#abstract)

🔹 [Notebooks](#progress-ladder)

🔹 [Results](#results)

🔹 [Future Scope](#future-scope)

🔹 [Reference Papers](#reference-papers)

---

## Abstract  

Majority of current text-to-image generation tasks are limited to creating images like flowers (Oxford 102 Flower), birds (CUB-200-2011), and Common Objects (COCO) from captions. The existing face datasets such as Labeled Faces in the Wild and MegaFace lack description while datasets like CelebA have attributes associated but do not provide feature descriptions. Thus, in this paper we build upon an existing algorithm to create captions with the attributes provided in the CelebA dataset, which can not only generate one caption but it can also be extended to generate N captions per image. We utilise Sentence BERT to encode these descriptions into sentence embeddings. We then perform a comparative study of three models - DCGAN, SAGAN and DFGAN, by using these sentence embeddings along with a latent noise as the inputs to the different architectures. Finally, we calculate the Inception Scores and the FID values to compare the output images across different architectures.

---

## Notebooks

### MNIST
| Model        | Colab Link     |
| ------------- |-------------|
| [Vanilla GAN](MNIST-GANs/GAN)      | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1setqmENPRRriznB8j2XL55RjSkMfMWCf?usp=sharing) |
| [DCGAN](MNIST-GANs/DCGAN)     | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1cBsnZTL0bp7o9lfBez1FyedDxo2Yf6wh?usp=sharing)      |
| [CGAN](MNIST-GANs/CGAN) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1X7xD1sX3iJggqMuDvnn7EtIUIsc5GDDn?usp=sharing)      |
| [ACGAN](MNIST-GANs/ACGAN) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1-OGeMxST6jFvSc5cq_Oc_-9ItqJ86taP?usp=sharing)      |

### Face

---

## Results
 <img src = "assets/result.png" >

## Future Scope
1. We did try self attention along with spectral normalization, however the results obtained were not upto expectations. However, we still believe this avenue could potentially lead to better results.

2. Using a Progressive or Hierarchical structure gave promising results, however it also consumes a lot of resources at the same time often leading to CUDA out of resource errors.

3. We’ve only maintained a wandb report for the initial MNIST GANs which we mentioned earlier. Nevertheless, we also have plans to make one for our Face GANs.

---

## Reference Papers

* [FTGAN : A fully Generative Adverserial Network for Text to Face Generation](https://arxiv.org/pdf/1904.05729.pdf)
* [Text2FaceGAN : Face Generation from Fine Grained Description](https://arxiv.org/pdf/1911.11378.pdf) 
* [Generative Adverserial Text to Image Synthesis](https://arxiv.org/pdf/1605.05396.pdf)
* [StackGAN: Text to Photo-realistic Image Synthesis with Stacked Generative Adversarial Networks](https://arxiv.org/pdf/1612.03242.pdf)
* [Skip-Thought Vectors](https://arxiv.org/pdf/1506.06726.pdf)




# Face Generation from Textual Description using Generative Adversarial Networks 📝  2️⃣ 👧👱 
[![Open in Streamlit](https://img.shields.io/badge/Open%20In%20Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://share.streamlit.io/ELITA04/FGTD-Streamlit/app.py/) [![Visualize in WandB](https://raw.githubusercontent.com/wandb/assets/main/wandb-github-badge-28.svg)](https://wandb.ai/ekkm/text-to-face?workspace=user-) ![PyTorch](https://img.shields.io/badge/Made%20With%20PyTorch-EE4C2C?style=for-the-badge&logo=PyTorch&logoColor=white)

---

## Table of Contents

🔹 [Abstract](#abstract)

🔹 [Process Flow](#process-flow)

🔹 [Description Categories](#description-categories)

🔹 [Notebooks](#progress-ladder)

🔹 [Results](#results)

🔹 [Future Scope](#future-scope)

🔹 [Research Paper and Citation](#research-paper-and-citation)

🔹 [Acknowledgement](#acknowledgement)

---

## Abstract  
![Real and Generated](assets/real-generated.png)

Majority of current text-to-image generation tasks are limited to creating images like flowers (Oxford 102 Flower), birds (CUB-200-2011), and Common Objects (COCO) from captions. The existing face datasets such as Labeled Faces in the Wild and MegaFace lack description while datasets like CelebA have attributes associated but do not provide feature descriptions. Thus, in this paper we build upon an existing algorithm to create captions with the attributes provided in the CelebA dataset, which can not only generate one caption but it can also be extended to generate N captions per image. We utilise Sentence BERT to encode these descriptions into sentence embeddings. We then perform a comparative study of three models - DCGAN, SAGAN and DFGAN, by using these sentence embeddings along with a latent noise as the inputs to the different architectures. Finally, we calculate the Inception Scores and the FID values to compare the output images across different architectures.

---

## Process Flow

![Process Flow](assets/processflow.png)

---

## Description Categories

![Description Categories](assets/categories.png)

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
| Model        | Single Caption     | N Caption     |
| ------------- |-------------|-------------|
| [DCGAN](Face-GANs/DCGAN)      | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/17l9Tgz90NC0WMfCCGZGiGSHU4Qi4ghgO?usp=sharing) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1L58f-Yh8nGcee9bCNAy8JXeQl6HLeTo6?usp=sharing) |
| [SAGAN](Face-GANs/SAGAN)     | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1OvjgKGH72Z0gvebrOG5m4SDsaNgevf9p?usp=sharing)      | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1EXhHHv915o2dWUmJWOGORks_W4yOgNbB?usp=sharing)      |
| [DFGAN](Face-GANs/DFGAN) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1GUVmdRSuJ3HM6mlihDdZZrrj_ePleI7q?usp=sharing)      | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/12Tww7kj0d1ohCmcf-88SlbcW-zSjhAJ0?usp=sharing)      |

---

## Results
### Generated Faces
![Generated Faces](assets/result.png)

### Scores from the Different Models
![Scores from the Different Models](assets/scores.png)

### Loss vs Epoch
![Loss vs Epoch](assets/loss.png)

---

## Future Scope
We believe that this work can be further improved by:

1. Introducing a better dataset balancing strategy that considers very short and extremely long descriptions.
2. Increasing the training steps for these models.
3. Extending the resolution of images to 256x256, 512x512 or further.
4. Using a transformer based model like DALL-E.

---

## Research Paper and Citation

* You can find our research paper [here.](assets/FGTD.pdf)
* Paper has successfully been presented at the [5th International Conference on Inventive Communication and Computational Technologies.](http://icicct.org/2021/index.html)
* Link to Paper - https://link.springer.com/chapter/10.1007/978-981-16-5529-6_43

## Citation
```bibtex
@inproceedings{Deorukhkar_Kadamala_Menezes_2022, 
  place={Singapore}, 
  series={Lecture Notes in Networks and Systems}, 
  title={FGTD: Face Generation from Textual Description}, 
  ISBN={9789811655296}, 
  DOI={10.1007/978-981-16-5529-6_43}, 
  publisher={Springer}, 
  author={Deorukhkar, Kalpana and Kadamala, Kevlyn and Menezes, Elita}, 
  editor={Ranganathan, G. and Fernando, Xavier and Shi, Fuqian}, 
  year={2022}, 
  pages={547–562}, 
  collection={Lecture Notes in Networks and Systems} 
}
```

---

## Acknowledgement
We would like to thank our mentor Prof. Kalpana Deorukhkar for her constant support and guidance throughout the project.


# Research

---

### 버전

- Python : 3.6.8
- Tensorflow : 1.14.0
- numpy : 1.16.6 (1.17버전에서 오류 발생하여 다운그레이드)
- matplotlib : 3.3.4
- dlib : 19.7.0 (최신 버전에서 설치 오류 발생하여 다운그레이드)
- opencv-python : 4.5.4.58

dlib 다운 방법 : 정상적인 방법으로는 계속 오류가 발생하여 링크를 통한 직접 다운로드

```
pip install https://pypi.python.org/packages/da/06/bd3e241c4eb0a662914b3b4875fc52dd176a9db0d4a2c915ac2ad8800e9e/dlib-19.7.0-cp36-cp36m-win_amd64.whl#md5=b7330a5b2d46420343fbed5df69e6a3f
```

---

### ML Model

**U-GAT-IT: Unsupervised Generative Attentional Networks with Adaptive Layer-Instance Normalization for Image-to-Image Translation**
Junho Kim (NCSOFT), Minjae Kim (NCSOFT), Hyeonwoo Kang (NCSOFT), Kwanghee Lee (Boeing Korea)

**Abstract** _We propose a novel method for unsupervised image-to-image translation, which incorporates a new attention module and a new learnable normalization function in an end-to-end manner. The attention module guides our model to focus on more important regions distinguishing between source and target domains based on the attention map obtained by the auxiliary classifier. Unlike previous attention-based methods which cannot handle the geometric changes between domains, our model can translate both images requiring holistic changes and images requiring large shape changes. Moreover, our new AdaLIN (Adaptive Layer-Instance Normalization) function helps our attention-guided model to flexibly control the amount of change in shape and texture by learned parameters depending on datasets. Experimental results show the superiority of the proposed method compared to the existing state-of-the-art models with a fixed network architecture and hyper-parameters._

## Architecture

<div align="center">
  <img src = './assets/generator_fix.png' width = '785px' height = '500px'>
</div>

---

<div align="center">
  <img src = './assets/discriminator_fix.png' width = '785px' height = '450px'>
</div>

## Results

### Ablation study

<div align="center">
  <img src = './assets/ablation.png' width = '438px' height = '346px'>
</div>

### User study

<div align="center">
  <img src = './assets/user_study.png' width = '738px' height = '187px'>
</div>

### Kernel Inception Distance (KID)

<div align="center">
  <img src = './assets/kid_fix2.png' width = '750px' height = '400px'>
</div>

## Citation

If you find this code useful for your research, please cite our paper:

```
@inproceedings{
Kim2020U-GAT-IT:,
title={U-GAT-IT: Unsupervised Generative Attentional Networks with Adaptive Layer-Instance Normalization for Image-to-Image Translation},
author={Junho Kim and Minjae Kim and Hyeonwoo Kang and Kwang Hee Lee},
booktitle={International Conference on Learning Representations},
year={2020},
url={https://openreview.net/forum?id=BJlZ5ySKPH}
}
```

# Generative Models Repository

Welcome to the Generative Models Repository! This collection provides an extensive range of generative models, including but not limited to Generative Adversarial Networks (GANs), Diffusion Models, Variational Autoencoders (VAEs), Vision Transformer Vector Quantized Variational AutoEncoders (ViT VQ-VAE), and Vector Quantized Variational AutoEncoders (VQ-VAE).

## Table of Contents

- [Introduction to Generative Modeling](#intro)
- [Generative Adversarial Networks (GANs)](#gan)
- [Diffusion Models](#diffusion)
- [Variational Autoencoders (VAEs)](#vae)
- [ViT VQ-VAE](#vit-vq-vae)
- [VQ-VAE](#vq-vae)

<a id="intro"></a>

## Introduction to Generative Modeling

Generative modeling is a subfield of artificial intelligence that focuses on creating algorithms capable of generating new data instances resembling the input data. These models aim to capture the underlying probability distribution of the training dataset to produce novel data points with slight variations.

<a id="gan"></a>

## Generative Adversarial Networks (GANs)

GANs are composed of two primary components: a generator and a discriminator. The generator is responsible for synthesizing new data instances, while the discriminator assesses their authenticity by determining if the generated data originates from the actual training dataset or not.

<a id="diffusion"></a>

## Diffusion Models

Diffusion models are a category of generative models that generate new samples through a diffusion process. This process iteratively adds noise to the data instances until they reach a state of pure noise, at which point the process is reversed to restore the original structure.

<a id="vae"></a>

## Variational Autoencoders (VAEs)

VAEs are a type of generative model that utilizes deep learning to construct sophisticated representations of the data distribution. They consist of an encoder that compresses input data into a lower-dimensional latent space and a decoder that reconstructs the input from the encoded representation.

The loss function for a VAE, often referred to as the evidence lower bound (ELBO), can be expressed mathematically as follows:

$$
L(\theta, \phi; x^{(i)}) = -E_{z \sim q_{\phi}(z | x^{(i)})}[\log p_{\theta}(x^{(i)} | z)] + \text{KL}(q_{\phi}(z | x^{(i)}) || p(z))
$$

Here,

- $E_{z \sim q_{\phi}(z | x^{(i)})}$ represents the expectation over the latent variable $z$
- $\log p_{\theta}(x^{(i)} | z)$ is the log-likelihood of observing the input data $x^{(i)}$ given $z$
- $\text{KL}$ denotes the Kullback-Leibler divergence, which measures the difference between the learned distribution $q_{\phi}(z | x^{(i)})$ and the prior $p(z)$

<a id="vit-vq-vae"></a>

## ViT VQ-VAE

ViT VQ-VAE is a specialized variant of VQ-VAE that employs Vision Transformers (ViT) as both the encoder and decoder. By leveraging the capabilities of transformers, ViT VQ-VAE can effectively capture long-range dependencies in the data, which is beneficial for tasks like image generation.

<a id="vq-vae"></a>

## VQ-VAE

Vector Quantized Variational AutoEncoders (VQ-VAE) represent another class of VAEs where the continuous latent space is substituted with a discrete one. This modification makes the generation process more predictable and interpretable, as the discrete nature of the latent variables allows for clearer control over the generation process.


**VQ-VAEs** represent another captivating variant of VAEs, introducing a twist: they replace the continuous latent space with a discrete one. This transformation offers several advantages:

- **Enhanced Interpretability:** The discrete nature of the latent space makes the generation process more transparent and understandable, allowing for greater control over the generated outputs.
- **Improved Predictability:** The discrete representation facilitates more predictable generation, as each latent code corresponds to a specific cluster of data points.

The core idea behind VQ-VAEs involves two key steps:

1. **Vector Quantization (VQ):** The continuous latent space is partitioned into a set of discrete latent codes, known as codebook entries. Each data point is then encoded into the nearest codebook entry, achieving a discretized representation.
2. **Autoencoder Learning:** The model employs the encoder and decoder, similar to a standard VAE, but operates within the discrete latent space. The encoder maps input data to codebook entries, and the decoder reconstructs the data from these discrete representations.

VQ-VAEs often utilize an additional loss term, known as the **commitment loss**, to encourage the encoder to map data points close to their corresponding codebook entries. This loss encourages the model to learn informative and meaningful latent representations.

## Conclusion

This Generative Models Repository provides a brief introduction to various generative modeling techniques. Each model offers unique strengths and applications, from the adversarial training of GANs to the interpretability of VQ-VAEs. As you delve deeper into this fascinating field, remember that generative modeling is an active area of research with continuous advancements. Explore the diverse literature, experiment with different models, and unlock the potential of generating new data that pushes the boundaries of what we thought was possible.


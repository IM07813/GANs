## Wasserstein GAN (WGAN) 

**Introduction:**

While DCGANs have paved the way for impressive image generation, they suffer from potential training instabilities due to vanishing gradients in the discriminator loss. Wasserstein GAN (WGAN), also known as W-GAN or Earth Mover's Distance (EMD) GAN, addresses this issue by adopting a different approach to loss formulation and training.

**Core Concepts:**

- **Wasserstein distance:** Measures the minimum cost of transforming one distribution of data points (real images) into another (generated images), akin to moving earth between piles.
- **Gradient penalty:** Enforces Lipschitz continuity on the discriminator, preventing vanishing gradients and improving training stability.

**Mathematical Formulation:**

**1. Wasserstein distance (W):**

$$W(P_r, P_g) = \inf_{\gamma \in \Pi(P_r, P_g)} E_{x \sim P_r, z \sim P_g} ||x - \gamma(z)||$$

- **W:** Wasserstein distance between real data distribution P_r and generated data distribution P_g.
- **γ:** Transport map (optimal way to move probability mass between distributions).
- **Π(P_r, P_g):** Set of all transport maps with source P_r and target P_g.
- **E[]:** Expectation over data samples.
- || ||: Norm (e.g., L1 or L2) measuring distance between data points.

**2. Critic (Discriminator) Loss (L_c):**

$$L_c = W(P_r, P_g) = E[D(x)] - E[D(G(z))]$$

- **D:** Critic (discriminator) function.
- **G:** Generator function.

**3. Gradient penalty term (GP):**

$$GP = \lambda E_{t \sim U[0,1]}[(||\nabla D(\hat{x}(t))||_2 - 1)^2]$$

- **λ:** Hyperparameter controlling the weight of the penalty.
- **U[0,1]:** Uniform distribution between 0 and 1.
- **t:** Randomly sampled value between 0 and 1.
- **^ :** Gradient operator.
- || ||_2: L2 norm.

**Training Process:**

1. **Sample noise:** Draw a random noise vector `z`.
2. **Generate image:** Generate an image `G(z)` using the generator.
3. **Interpolate:** Randomly interpolate between real and generated samples to create intermediate samples `^x`.
4. **Evaluate critic:** Compute the critic's score `D(^x)` for the interpolated samples.
5. **Calculate losses:** Compute the critic loss `L_c` and gradient penalty `GP`.
6. **Update critic:** Backpropagate to update the critic's parameters, enforcing Lipschitz continuity with the gradient penalty.
7. **Generate again:** Generate another batch of images with `G(z)`.
8. **Evaluate critic (again):** Compute the critic's score `D(G(z))` for the generated images.
9. **Update generator:** Backpropagate to update the generator's parameters to minimize `-E[D(G(z))]`.
10. **Repeat:** Iteratively perform steps 1-10 until convergence.

**Key Points:**

- WGAN replaces the log-likelihood discriminator loss with the Wasserstein distance, leading to more stable training.
- The gradient penalty term ensures the critic's gradients remain well-behaved, mitigating vanishing gradients.
- While WGAN offers advantages in training stability, it might require more careful hyperparameter tuning and can be slower to converge compared to DCGANs.

**Additional Notes:**

- Recent variants of WGAN, like WGAN-GP and WGAN-LS, address certain limitations and improve practical usability.
- WGANs are particularly well-suited for generating high-quality and diverse images.
- The choice between DCGANs and WGANs often depends on the specific application and desired trade-offs between training stability, convergence speed, and image quality.



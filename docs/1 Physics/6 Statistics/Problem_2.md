# Problem 2

# 📘 Part 1: Approximating π Using a Circle

## 1. Theoretical Background

### 🧠 Conceptual Insight

Monte Carlo techniques apply randomness to tackle problems that are fundamentally deterministic. To approximate π, we leverage the geometric connection between a circle and the square that encloses it:

- Imagine a **unit circle** (radius = 1) centered at the origin (0, 0).
- This circle fits perfectly within a **square** with a side length of 2, spanning coordinates from (-1, -1) to (1, 1).
- The **area** of the unit circle is:

  $$
  A_{circle} = \pi r^2 = \pi \cdot 1^2 = \pi
  $$

- The **area** of the surrounding square is:

  $$
  A_{square} = (2r)^2 = (2 \cdot 1)^2 = 4
  $$

- The ratio between these areas becomes:

  $$
  \frac{A_{circle}}{A_{square}} = \frac{\pi}{4}
  $$

So, when we uniformly sample points at random within the square, the **likelihood** that a point lands inside the circle is:

  $$
  P(\text{point inside circle}) = \frac{\pi}{4}
  $$

### 🔢 Estimating π via Monte Carlo

To derive π using this probabilistic approach:

1. **Generate** many random coordinate pairs $(x, y)$ in the square $[-1, 1] \times [-1, 1]$.
2. **Determine** whether each point lies within the unit circle using:

   $$
   x^2 + y^2 \leq 1
   $$

3. **Record** the number of points that fall inside the circle: $N_{circle}$
4. **Note** the total number of sampled points: $N_{total}$
5. Estimate π using the expression:

   $$
   \hat{\pi} = 4 \cdot \frac{N_{circle}}{N_{total}}
   $$

### ✅ Key Takeaways

- Monte Carlo estimation of π depends on simulating random events and comparing relative counts.
- The more points you sample ($N_{total}$), the closer the estimate gets to the true value of π.
- This strategy intuitively combines **geometry, probability, and numerical simulation**.

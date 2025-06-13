# 🌊 Interference Patterns of Circular Water Waves from Point Sources

## 🔹 Task Description

A **circular wave** on the water surface, emanating from a point source located at $(x_0, y_0)$, is described by the **Single Disturbance Equation**:

$$
\eta(x, y, t) = \frac{A}{\sqrt{r}} \cdot \cos(kr - \omega t + \phi)
$$

### Where:
- $\eta(x, y, t)$: Displacement of the water surface at point $(x, y)$ and time $t$
- $A$: Amplitude of the wave
- $k = \frac{2\pi}{\lambda}$: Wave number, with $\lambda$ as the wavelength
- $\omega = 2\pi f$: Angular frequency, with $f$ as the wave frequency
- $r = \sqrt{(x - x_0)^2 + (y - y_0)^2}$: Distance from source to the point $(x, y)$
- $\phi$: Initial phase of the wave

---

## ❓ Problem Statement

Your task is to **analyze the interference patterns** on the water surface caused by the **superposition of waves** emitted from point sources placed at the **vertices of a regular polygon**.

---

## ✅ Steps to Follow

### 1. Select a Regular Polygon
Choose a regular polygon:
- Equilateral Triangle (3 vertices)
- Square (4 vertices)
- Regular Pentagon (5 vertices)
- etc.

### 2. Position the Sources
Place wave sources at the **vertices** of the polygon. For a polygon centered at the origin:
- Let the radius be $R$
- The $i^{th}$ vertex is at:
  
  $$
  (x_i, y_i) = \left(R\cos\left(\frac{2\pi i}{N}\right), R\sin\left(\frac{2\pi i}{N}\right)\right)
  $$

### 3. Write the Wave Equations
Each source emits a wave described by:

$$
\eta_i(x, y, t) = \frac{A}{\sqrt{r_i}} \cdot \cos(k r_i - \omega t + \phi)
$$

Where:
- $r_i = \sqrt{(x - x_i)^2 + (y - y_i)^2}$

### 4. Superposition of Waves
The total displacement at a point $(x, y)$ and time $t$ is given by:

$$
\eta_{\text{sum}}(x, y, t) = \sum_{i=1}^{N} \eta_i(x, y, t)
$$

Where:
- $N$ is the number of sources (polygon vertices)

---

## 🔬 Analyze Interference Patterns

- Compute $\eta_{\text{sum}}(x, y, t)$ over a grid of $(x, y)$ points for a fixed time $t$
- Identify:
  - **Constructive interference**: Wave amplitudes add up (bright/fringe regions)
  - **Destructive interference**: Wave amplitudes cancel (dark/null regions)

---

## 📊 Visualization

- Use 2D heatmaps or 3D surface plots
- Plot $\eta_{\text{sum}}(x, y, t)$ over a defined region
- Observe symmetrical patterns based on the chosen polygon

---

## 🧠 Optional Enhancements

- Animate $\eta_{\text{sum}}(x, y, t)$ over time
- Explore effects of:
  - Changing phase $\phi$
  - Different frequencies $\omega$
  - Different polygon types
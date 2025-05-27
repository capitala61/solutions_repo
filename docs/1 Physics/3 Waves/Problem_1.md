# Problem 1
# 📐 Regular Pentagon – Academic Notes

A **regular pentagon** is a five-sided polygon with:

- All sides of equal length.
- All internal angles equal.
- All diagonals of equal length.

---

## 🔢 Basic Properties

- **Number of sides**: $n = 5$
- **Length of each side**: $a$
- **Internal angle**:  
  $$
  \theta = \frac{(n - 2) \cdot 180^\circ}{n} = \frac{3 \cdot 180^\circ}{5} = 108^\circ
  $$
- **Central angle** (for inscribed circle):  
  $$
  \phi = \frac{360^\circ}{n} = \frac{360^\circ}{5} = 72^\circ
  $$

---

## 📏 Perimeter

$$
P = n \cdot a = 5a
$$

---

## 📐 Area Formulas

### Using side length $a$:

$$
A = \frac{1}{4} \cdot \sqrt{5(5 + 2\sqrt{5})} \cdot a^2
$$

### Using apothem $a_p$:

$$
A = \frac{1}{2} \cdot P \cdot a_p = \frac{5a \cdot a_p}{2}
$$

---

## 🟠 Apothem of Regular Pentagon

$$
a_p = \frac{a}{2} \cdot \cot\left(\frac{\pi}{5}\right)
$$

or

$$
a_p = \frac{a}{2} \cdot \tan\left(54^\circ\right)
$$

---

## 📐 Diagonals

- **Number of diagonals** in a polygon:
  $$
  d = \frac{n(n - 3)}{2} = \frac{5(5 - 3)}{2} = 5
  $$

- **Length of a diagonal** $D$:
  $$
  D = a \cdot \frac{1 + \sqrt{5}}{2}
  $$
  *(Golden ratio)*

---

## 🔄 Symmetry

- **Lines of symmetry**: 5  
- **Rotational symmetry**: Every $72^\circ$

---

## 🔧 Trigonometric Construction (Useful in Geometry)

- Each vertex angle from the center:
  $$
  \text{Vertex angle} = \frac{2\pi}{5}
  $$

- Coordinates for a unit pentagon centered at origin (optional):
  $$
  (x_k, y_k) = (\cos(\theta_k), \sin(\theta_k)) \quad \text{where} \quad \theta_k = \frac{2\pi k}{5},\ k = 0,1,2,3,4
  $$

---

## 📚 Summary

| Property       | Formula / Value                        |
|----------------|----------------------------------------|
| Sides          | $n = 5$                                |
| Interior Angle | $108^\circ$                            |
| Central Angle  | $72^\circ$                             |
| Perimeter      | $P = 5a$                               |
| Area (side)    | $A = \frac{1}{4}\sqrt{5(5+2\sqrt{5})} a^2$ |
| Diagonals      | $d = 5$, length $= a \cdot \frac{1 + \sqrt{5}}{2}$ |

---

📌 **Applications**:
- Architecture  
- Geometry problems  
- Symbolic usage (stars, flags)

# 📌 Determining Vertex Coordinates of a Regular Polygon

To determine the **vertex coordinates** of a regular polygon, we use **trigonometry** and place the polygon in a **Cartesian coordinate system**, often centered at the origin.

---

## 📐 Assumptions

- **Regular polygon**: all sides and angles are equal.
- **Center at origin**: $(0,0)$
- **Radius** $r$: distance from center to any vertex (circumradius).
- **Number of vertices**: $n$
- **Angle increment** between adjacent vertices: $\theta=\dfrac{2\pi}{n}$

---

## 🧮 General Formula for Vertex Coordinates

For each vertex $k$ $(k=0,1,2,...,n-1)$:

$$
x_k=r\cdot\cos(\theta_k) \\
y_k=r\cdot\sin(\theta_k)
$$

Where:

- $\theta_k=\dfrac{2\pi k}{n}+\phi_0$
- $\phi_0$ is the initial angular offset (optional, default $0$)

---

## 🧷 Step-by-Step Procedure

1. **Choose**:
   - Number of sides $n$
   - Radius $r$
   - Optional: starting rotation angle $\phi_0$ in radians

2. **For each vertex** $k$ from $0$ to $n-1$:
   - Compute angle: $\theta_k=\dfrac{2\pi k}{n}+\phi_0$
   - Get coordinates:
     - $x_k=r\cdot\cos(\theta_k)$
     - $y_k=r\cdot\sin(\theta_k)$

---

## 🧪 Example: Regular Pentagon ($n=5$, $r=1$)

Let $\phi_0=\dfrac{\pi}{2}$ to make one vertex point upward.

- $\theta_k=\dfrac{2\pi k}{5}+\dfrac{\pi}{2}$

Then each vertex is:

- Vertex 0:  
  $x_0=\cos\left(\dfrac{\pi}{2}\right)=0$  
  $y_0=\sin\left(\dfrac{\pi}{2}\right)=1$

- Vertex 1:  
  $\theta_1=\dfrac{2\pi}{5}+\dfrac{\pi}{2}=\dfrac{9\pi}{10}$  
  $x_1=\cos\left(\dfrac{9\pi}{10}\right)$  
  $y_1=\sin\left(\dfrac{9\pi}{10}\right)$

- Repeat similarly for $k=2,3,4$

---

## 🧭 Summary of Vertex Formula

For a regular $n$-gon centered at origin with radius $r$:

$$
(x_k,y_k)=\left(r\cos\left(\dfrac{2\pi k}{n}+\phi_0\right),r\sin\left(\dfrac{2\pi k}{n}+\phi_0\right)\right)
$$

- $k=0,1,2,...,n-1$
- Use $\phi_0=\dfrac{\pi}{2}$ to orient a vertex upward
- All vertices lie on the unit circle if $r=1$

---

## 🛠️ Applications

- Point source placement in physics simulations
- Uniform distribution on circle
- Graphics and game development
- Antenna array geometry

# 🌊 Defining Wave Parameters – Academic Notes

To model and analyze waves, we define key parameters that describe their behavior in space and time. These parameters are essential in **physics**, **engineering**, and **signal processing**.

---

## 📐 Common Wave Parameters

### 🔸 1. Amplitude ($A$)

- Maximum displacement from the equilibrium position.
- Represents the wave's **strength** or **intensity**.
- Units depend on the context (e.g., meters for mechanical waves, volts for EM waves).

---

### 🔸 2. Wavelength ($\lambda$)

- Distance between **two consecutive identical points** (e.g., crests or troughs).
- Determines **spatial periodicity** of the wave.
- Unit: meters ($m$)

**Wave number ($k$)** is defined as:

$$
k=\frac{2\pi}{\lambda}
$$

- Unit: radians per meter ($\text{rad/m}$)

---

### 🔸 3. Frequency ($f$)

- Number of wave cycles per second.
- Describes **temporal periodicity**.
- Unit: Hertz ($Hz$)

**Angular frequency ($\omega$)** is given by:

$$
\omega=2\pi f
$$

- Unit: radians per second ($\text{rad/s}$)

---

### 🔸 4. Initial Phase ($\phi$)

- The **horizontal shift** of the wave at $t=0$, $x=0$.
- Unit: radians
- Common values:
  - $\phi=0$ (in-phase)
  - Same $\phi$ for all wave sources → synchronous emission

---

## 🧾 Summary Table

| Parameter         | Symbol  | Formula                      | Unit              |
|------------------|---------|------------------------------|-------------------|
| Amplitude         | $A$     | —                            | Depends on wave   |
| Wavelength        | $\lambda$ | —                          | $m$               |
| Wave number       | $k$     | $k=\dfrac{2\pi}{\lambda}$    | $\text{rad/m}$    |
| Frequency         | $f$     | —                            | $Hz$              |
| Angular frequency | $\omega$| $\omega=2\pi f$              | $\text{rad/s}$    |
| Initial phase     | $\phi$  | —                            | $\text{rad}$      |

---

## 📝 Typical Wave Equation (1D Traveling Wave)

A sinusoidal wave traveling in the $+x$ direction can be expressed as:

$$
y(x,t)=A\sin(kx-\omega t+\phi)
$$

Where:

- $A$: amplitude  
- $k$: wave number  
- $\omega$: angular frequency  
- $\phi$: initial phase  
- $x$: position  
- $t$: time  

---

## 🛠️ Applications

- Modeling sound, light, water, and electromagnetic waves
- Signal analysis and synthesis
- Vibrations and acoustics

# 🎯 Writing Individual Wave Equations – Academic Notes

In a system with multiple **point sources** located at different positions $(x_i,y_i)$, we can express the **displacement of the wave** from each source using a general wave equation.

---

## 🧱 Assumptions

- Each source emits a **monochromatic sinusoidal wave**.
- All waves propagate in a homogeneous medium at speed $v$.
- Wave parameters:
  - Amplitude: $A$
  - Frequency: $f$
  - Wavelength: $\lambda$
  - Wave number: $k=\dfrac{2\pi}{\lambda}$
  - Angular frequency: $\omega=2\pi f$
  - Initial phase: $\phi_i$

---

## 🔸 Displacement from Each Source

Let a wave be emitted from source $i$ located at $(x_i,y_i)$. The wave propagates spherically outward from that point. The displacement $y_i(P,t)$ of the wave at point $P=(x,y)$ and time $t$ is given by:

$$
y_i(P,t)=A_i\sin\left(k r_i - \omega t + \phi_i\right)
$$

Where:

- $r_i=\sqrt{(x-x_i)^2+(y-y_i)^2}$ is the distance from source $i$ to observation point $P$
- $A_i$ is the amplitude of source $i$
- $\phi_i$ is the initial phase of source $i$
- $k$ is the wave number
- $\omega$ is the angular frequency

---

## 🧮 General Expression for $N$ Sources

If you have $N$ sources, each at $(x_i,y_i)$ with possibly different phases $\phi_i$ and amplitudes $A_i$, the total displacement is:

$$
y_\text{total}(x,y,t)=\sum_{i=1}^{N} A_i\sin\left(k\sqrt{(x-x_i)^2+(y-y_i)^2}-\omega t+\phi_i\right)
$$

---

## 📝 Example: Two In-Phase Sources

Let two identical point sources be placed at:

- Source 1 at $(x_1,y_1)=(0,0)$  
- Source 2 at $(x_2,y_2)=(d,0)$  
- $A_1=A_2=A$, $\phi_1=\phi_2=0$

Then:

- $r_1=\sqrt{x^2+y^2}$  
- $r_2=\sqrt{(x-d)^2+y^2}$

The individual displacements:

$$
y_1(x,y,t)=A\sin\left(k\sqrt{x^2+y^2}-\omega t\right)
$$

$$
y_2(x,y,t)=A\sin\left(k\sqrt{(x-d)^2+y^2}-\omega t\right)
$$

---

## 🛠️ Applications

- Interference pattern modeling (e.g., Young’s double-slit)
- Acoustic or EM wave superposition from multiple antennas or sources
- Simulating sound fields and spatial audio
- Holography and wavefront reconstruction

---

## 🔚 Summary

Each point source contributes a **radially-propagating wave** whose phase depends on the **distance** to the point of observation. Superposing these contributions allows us to model **interference**, **constructive/destructive patterns**, and wavefront behaviors.

# Superposition Principle in Wave Dynamics

The superposition principle states that the net displacement caused by multiple waves is the algebraic sum of the individual wave displacements.

## Mathematical Formulation

For a system with $N$ waves, the total displacement $\eta_{sum}$ at any point $(x,y)$ and time $t$ is given by:

$$
\eta_{sum}(x,y,t) = \sum_{i=1}^{N} \eta_i(x,y,t)
$$

where:
- $\eta_i(x,y,t)$ is the displacement due to the $i^{th}$ wave
- $N$ is the total number of waves

## Key Properties

### Linear Systems
* Applies to linear wave equations
* Valid when the wave equation satisfies:
  $$
  \mathcal{L}(\eta_1 + \eta_2) = \mathcal{L}(\eta_1) + \mathcal{L}(\eta_2)
  $$
  where $\mathcal{L}$ is the linear wave operator

### Important Consequences
1. **Constructive Interference**
   - Occurs when waves are in phase:
     $$
     \eta_{sum} \approx N\eta \quad \text{(for identical waves in phase)}
     $$

2. **Destructive Interference**
   - Occurs when waves are out of phase:
     $$
     \eta_{sum} \approx 0 \quad \text{(for identical waves with phase difference } \pi)
     $$

## Applications

* Ocean wave modeling
* Quantum mechanics (wavefunction superposition)
* Acoustics and sound wave analysis
* Electromagnetic wave propagation

## Example Calculation

For two sinusoidal waves:
$$
\eta_1(x,t) = A\sin(kx - \omega t)
$$
$$
\eta_2(x,t) = A\sin(kx - \omega t + \phi)
$$

The superposition gives:
$$
\eta_{sum} = 2A\cos\left(\frac{\phi}{2}\right)\sin\left(kx - \omega t + \frac{\phi}{2}\right)
$$

## Limitations

- Only valid for linear systems
- Breaks down for:
  * Very large amplitudes (nonlinear effects)
  * Dissipative systems with significant energy loss

  # Spatial Grid Setup for Wave Simulation

## Grid Definition
To model wave propagation, we first define a discrete spatial grid over the water surface:

$$\Omega = \{(x_i, y_j) \mid x_i \in [x_{min}, x_{max}], y_j \in [y_{min}, y_{max}]\}$$

where:
-$x_i = x_{min} + i\Delta x$ for $i = 0,1,...,N_x-1$
-$y_j = y_{min} + j\Delta y$ for $j = 0,1,...,N_y-1$

## Parameters

### Domain Specifications
* **Physical boundaries**:
  -$x \in [x_{min}, x_{max}]$ (longitudinal direction)
  -$y \in [y_{min}, y_{max}]$ (transverse direction)
* **Typical marine applications**:
  -$x_{max} - x_{min} = 1000\text{m}$ (along-wave direction)
  -$y_{max} - y_{min} = 500\text{m}$ (cross-wave direction)

### Resolution Parameters
* **Grid spacing**:
  -$\Delta x = \frac{x_{max} - x_{min}}{N_x - 1}$
  -$\Delta y = \frac{y_{max} - y_{min}}{N_y - 1}$
* **Nyquist criterion**:
$$\Delta x \leq \frac{\lambda_{min}}{2} \quad \text{and} \quad \Delta y \leq \frac{\lambda_{min}}{2}$$
where $\lambda_{min}$ is the shortest wavelength to resolve

## Implementation Steps

1. **Choose domain size**:
```python
x_min, x_max = 0.0, 1000.0  # meters
y_min, y_max = 0.0, 500.0   # meters
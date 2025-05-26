# Problem 3

# Theoretical Analysis

## 1. Equations of Motion
The payload's trajectory is governed by **Newton's Law of Gravitation** and **Newton's Second Law**:

- **Newton's Law of Gravitation**:
  $$\mathbf{F} = -\frac{GMm}{r^2}\hat{\mathbf{r}}$$
  where:
  - $G$ = Gravitational constant ($6.674 \times 10^{-11}\,\text{m}^3\text{kg}^{-1}\text{s}^{-2}$)
  - $M$ = Mass of Earth ($5.972 \times 10^{24}\,\text{kg}$)
  - $m$ = Mass of payload (neglected for trajectory analysis)
  - $r$ = Distance between payload and Earth's center

- **Equation of Motion (2D Polar Coordinates)**:
  $$\frac{d^2\mathbf{r}}{dt^2} = -\frac{GM}{r^3}\mathbf{r}$$
  Decomposed into Cartesian coordinates ($x, y$):
  $$\frac{d^2x}{dt^2} = -\frac{GMx}{(x^2 + y^2)^{3/2}}, \quad \frac{d^2y}{dt^2} = -\frac{GMy}{(x^2 + y^2)^{3/2}}$$

---

## 2. Trajectory Types
The shape of the orbit depends on the **specific orbital energy** ($E$) and **eccentricity** ($e$):

- **Elliptical Orbit** ($E < 0$, $0 \leq e < 1$):
  - Bound orbit (e.g., satellites)
  - Initial velocity below escape velocity: $v < v_{\text{esc}} = \sqrt{\frac{2GM}{r}}$

- **Parabolic Orbit** ($E = 0$, $e = 1$):
  - Escape trajectory (minimum escape condition)
  - Initial velocity equals escape velocity: $v = v_{\text{esc}}$

- **Hyperbolic Orbit** ($E > 0$, $e > 1$):
  - Unbound trajectory (e.g., interplanetary probes)
  - Initial velocity exceeds escape velocity: $v > v_{\text{esc}}$

---

## 3. Initial Velocity Impact
Key velocity thresholds for a payload at altitude $h = r - R_E$ (Earth's radius $R_E = 6371\,\text{km}$):

| **Scenario**       | **Velocity Condition**               | **Outcome**                     |
|--------------------|--------------------------------------|---------------------------------|
| Suborbital         | $v < \sqrt{\frac{GM}{r}}$           | Reentry (ballistic trajectory)  |
| Circular Orbit     | $v = \sqrt{\frac{GM}{r}}$           | Stable orbit                    |
| Elliptical Orbit   | $\sqrt{\frac{GM}{r}} < v < v_{\text{esc}}$ | Apogee/perigee variation |
| Escape             | $v \geq v_{\text{esc}}$             | Leaves Earth's influence        |

**Note**:
- **Orbital Insertion**: Requires precise $v$ to match desired orbit
- **Reentry**: Achieved by reducing $v$ (e.g., retrograde thrust or atmospheric drag)
- **Escape**: Requires $v \geq \sqrt{\frac{2GM}{r}}$ (parabolic/hyperbolic)

---

## Python Code Snippet (Symbolic Derivation)
```python
import sympy as sp

# Define variables
t, G, M = sp.symbols('t G M')
x, y = sp.Function('x')(t), sp.Function('y')(t)

# Equations of motion
eq1 = sp.Eq(sp.diff(x, t, 2), -G * M * x / (x**2 + y**2)**(3/2))
eq2 = sp.Eq(sp.diff(y, t, 2), -G * M * y / (x**2 + y**2)**(3/2))

print("Equation for x:", eq1)
print("Equation for y:", eq2)
```

# Numerical Simulation Setup

## 1. Initial Conditions
We define the payload's initial state in Cartesian coordinates:

- **Position**:
$$x_0=(R_E+h)\cos\theta$$
$$y_0=(R_E+h)\sin\theta$$
where:
-$R_E=6371\,\text{km}$ (Earth's radius)
-$h$=altitude above surface
-$\theta$=angular position from reference axis

- **Velocity**:
$$v_{x0}=v_0\cos\phi$$
$$v_{y0}=v_0\sin\phi$$
where:
-$v_0$=initial speed
-$\phi$=launch angle from horizontal

## 2. Numerical Method Selection
We solve the coupled ODEs using the **4th-order Runge-Kutta method** (RK4) for higher accuracy:

The general RK4 formulation for $\frac{dy}{dt}=f(t,y)$:
$$k_1=f(t_n,y_n)$$
$$k_2=f(t_n+\frac{h}{2},y_n+\frac{h}{2}k_1)$$
$$k_3=f(t_n+\frac{h}{2},y_n+\frac{h}{2}k_2)$$
$$k_4=f(t_n+h,y_n+hk_3)$$
$$y_{n+1}=y_n+\frac{h}{6}(k_1+2k_2+2k_3+k_4)$$

## 3. Implementation Framework

### Python Implementation
```python
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Constants
G = 6.67430e-11  # m^3 kg^-1 s^-2
M = 5.972e24     # kg
R_E = 6371e3      # m

def equations_of_motion(t, state):
    """ODE system for payload trajectory"""
    x, y, vx, vy = state
    r = np.sqrt(x**2 + y**2)
    ax = -G * M * x / r**3
    ay = -G * M * y / r**3
    return [vx, vy, ax, ay]

def simulate_trajectory(h, v0, theta, phi, t_span, dt):
    """Run trajectory simulation"""
    # Initial conditions
    r0 = R_E + h
    x0 = r0 * np.cos(theta)
    y0 = r0 * np.sin(theta)
    vx0 = v0 * np.cos(phi)
    vy0 = v0 * np.sin(phi)
    
    # Time points
    t_eval = np.arange(t_span[0], t_span[1], dt)
    
    # Solve ODE
    sol = solve_ivp(equations_of_motion, t_span, 
                   [x0, y0, vx0, vy0], 
                   t_eval=t_eval, 
                   method='RK45')
    
    return sol

# Example usage
h = 500e3  # 500 km altitude
v0 = 7.5e3  # 7.5 km/s
theta = 0  # Initial angle
phi = np.pi/4  # 45 degree launch angle
t_span = [0, 3600*2]  # 2 hour simulation
dt = 10  # 10 second timestep

solution = simulate_trajectory(h, v0, theta, phi, t_span, dt)
```

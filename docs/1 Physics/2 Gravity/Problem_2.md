# Problem 2

# Cosmic Velocities: Definitions and Physical Meaning

## 1. First Cosmic Velocity (Orbital Velocity)
**Definition**:  
The minimum velocity required for an object to maintain a stable circular orbit around a celestial body (e.g., Earth) without propulsion.  

**Purpose**:  
- Enables satellites to orbit without falling back to the surface.  
- Balances centripetal force and gravitational pull.  

**Mathematical Formulation**:  
The first cosmic velocity $v_1$ is derived from the equilibrium of forces:  
$$F_{\text{centripetal}} = F_{\text{gravitational}}$$  
$$\frac{m v_1^2}{r} = \frac{G M m}{r^2}$$  
$$v_1 = \sqrt{\frac{G M}{r}}$$  
where:  
- $G$ = Gravitational constant ($6.674 \times 10^{-11} \text{m}^3 \text{kg}^{-1} \text{s}^{-2}$)  
- $M$ = Mass of the celestial body (kg)  
- $r$ = Distance from the center of the body (m)  

---

## 2. Second Cosmic Velocity (Escape Velocity)
**Definition**:  
The minimum velocity needed for an object to break free from a celestial body’s gravitational influence (i.e., reach infinity with zero residual speed).  

**Significance**:  
- Critical for missions leaving Earth (e.g., Moon landings, Mars missions).  
- Determines the energy required for unbound trajectories.  

**Mathematical Formulation**:  
Escape velocity $v_2$ is found by equating kinetic energy to gravitational potential energy:  
$$\frac{1}{2} m v_2^2 = \frac{G M m}{r}$$  
$$v_2 = \sqrt{\frac{2 G M}{r}} = \sqrt{2} \cdot v_1$$  

---

## 3. Third Cosmic Velocity (Solar System Escape Velocity)
**Definition**:  
The velocity required for an object to escape the Sun’s gravitational pull *after already leaving Earth*.  

**Application**:  
- Necessary for interstellar probes (e.g., Voyager 1, 2).  
- Depends on Earth’s orbital velocity around the Sun (~29.8 km/s).  

**Mathematical Formulation**:  
Approximated by:  
$$v_3 \approx \sqrt{v_{\text{Earth orbit}}^2 + \left(\sqrt{2} - 1\right)^2 v_{\text{Sun escape}}^2$$  
where:  
- $v_{\text{Earth orbit}}$ = Earth’s orbital speed around the Sun.  
- $v_{\text{Sun escape}}$ = Escape velocity from the Sun at Earth’s orbit (~42.1 km/s).  

---

## Python Code: Calculating Cosmic Velocities
```python
import numpy as np

# Constants
G = 6.67430e-11  # Gravitational constant (m^3 kg^-1 s^-2)

def cosmic_velocities(M, r):
    """Calculate first (v1) and second (v2) cosmic velocities."""
    v1 = np.sqrt(G * M / r)          # First cosmic velocity (m/s)
    v2 = np.sqrt(2 * G * M / r)      # Second cosmic velocity (m/s)
    return v1, v2

# Example: Earth
M_Earth = 5.972e24     # Mass (kg)
r_Earth = 6.371e6      # Radius (m)
v1, v2 = cosmic_velocities(M_Earth, r_Earth)
print(f"Earth: v1 = {v1/1000:.2f} km/s, v2 = {v2/1000:.2f} km/s")
```
# Mathematical Derivations and Parameters of Cosmic Velocities

## 1. Derivation of First Cosmic Velocity (Circular Orbital Velocity)

**Physical Principle**:  
Balance between centripetal force and gravitational attraction.

**Step-by-Step Derivation**:
1. Equate centripetal force to gravitational force:
   $$F_c=F_g$$
   $$\frac{mv_1^2}{r}=\frac{GMm}{r^2}$$

2. Cancel common terms ($m$ and one $r$):
   $$v_1^2=\frac{GM}{r}$$

3. Final expression:
   $$v_1=\sqrt{\frac{GM}{r}}$$

**Key Parameters**:
- $G$: Gravitational constant ($6.674\times10^{-11}\text{m}^3\text{kg}^{-1}\text{s}^{-2}$)
- $M$: Mass of celestial body (kg)
- $r$: Orbital radius from center (m)

---

## 2. Derivation of Second Cosmic Velocity (Escape Velocity)

**Physical Principle**:  
Energy conservation - kinetic energy equals gravitational potential energy.

**Step-by-Step Derivation**:
1. Set kinetic energy equal to work needed against gravity:
   $$\frac{1}{2}mv_2^2=\int_r^\infty\frac{GMm}{r'^2}dr'$$

2. Solve the integral:
   $$\frac{1}{2}mv_2^2=\frac{GMm}{r}$$

3. Final expression:
   $$v_2=\sqrt{\frac{2GM}{r}}$$

**Relation to First Cosmic Velocity**:
$$v_2=\sqrt{2}\cdot v_1$$

---

## 3. Concept of Third Cosmic Velocity (Solar System Escape)

**Physical Principle**:  
Combination of Earth's escape velocity and Solar system escape requirements.

**Key Components**:
1. Earth's orbital velocity around Sun:
   $$v_{\text{Earth}}\approx29.8\text{km/s}$$

2. Solar escape velocity at Earth's orbit:
   $$v_{\text{Sun esc}}\approx42.1\text{km/s}$$

3. Optimal escape condition:
  $$v_3\approx\sqrt{v_{\text{Earth}}^2+(\sqrt{2}-1)^2v_{\text{Sun esc}}^2}$$

**Practical Value**:
- Approximately 16.6 km/s from Earth's surface
- Accounts for Earth's gravity and Solar system escape

---

## Key Parameters Affecting Cosmic Velocities

**Primary Parameters**:
- $M$: Mass of primary body
  - Directly proportional to $v_1$ and $v_2$
  - Example: Jupiter's large mass → high escape velocity
- $r$: Distance from center
  - Inversely proportional to velocities
  - Higher orbits require lower velocities

**Secondary Factors**:
- Body's rotation (affects effective $r$)
- Atmospheric drag (for surface launches)
- Relativistic effects (for extreme gravity)

---

## Python Implementation

```python
import numpy as np

# Universal constants
G = 6.67430e-11  # Gravitational constant (m^3 kg^-1 s^-2)

def calculate_velocities(M, r):
    """Calculate all three cosmic velocities"""
    v1 = np.sqrt(G * M / r)               # First cosmic
    v2 = np.sqrt(2 * G * M / r)           # Second cosmic
    v3 = np.sqrt(29.8e3**2 + (np.sqrt(2)-1)**2 * 42.1e3**2)  # Third cosmic approx
    return v1, v2, v3

# Example: Earth values
M_earth = 5.972e24  # kg
r_earth = 6.371e6   # m
v1, v2, v3 = calculate_velocities(M_earth, r_earth)

print(f"Earth's cosmic velocities:")
print(f"v1 = {v1/1000:.2f} km/s (orbital)")
print(f"v2 = {v2/1000:.2f} km/s (escape)")
print(f"v3 ≈ {v3/1000:.2f} km/s (solar escape)")

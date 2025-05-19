# Problem 2
# Problem 2  
# Cosmic Velocities: Derivations, Calculations, and Comparisons  

## 1. Definitions of Cosmic Velocities  

Cosmic velocities are critical thresholds in astrodynamics, defining minimum speeds for orbital and escape maneuvers:  

- **First Cosmic Velocity (\(v_1\))**:  
  - **Definition**: The speed required for an object to maintain a circular orbit near a celestial body's surface.  
  - **Equation**: \(v_1 = \sqrt{\frac{GM}{R}}\)  

- **Second Cosmic Velocity (\(v_2\))**:  
  - **Definition**: The speed required to escape a celestial body's gravitational pull.  
  - **Equation**: \(v_2 = \sqrt{\frac{2GM}{R}}\)  

- **Third Cosmic Velocity (\(v_3\))**:  
  - **Definition**: The speed required to escape a star system from a planet's orbit.  
  - **Equation**: \(v_3 = \sqrt{v_2^2 + (v_{\text{esc,Sun}} - v_{\text{orbit}})^2}\)  

## 2. Derivations  

### 2.1 First Cosmic Velocity (\(v_1\))  
**Derivation**:  
Gravitational force equals centripetal force:  
\[
\frac{GMm}{R^2} = \frac{mv_1^2}{R} \implies v_1 = \sqrt{\frac{GM}{R}}
\]

### 2.2 Second Cosmic Velocity (\(v_2\))  
**Derivation**:  
Energy conservation (kinetic + potential = 0 at infinity):  
\[
\frac{1}{2}mv_2^2 - \frac{GMm}{R} = 0 \implies v_2 = \sqrt{\frac{2GM}{R}}
\]

### 2.3 Third Cosmic Velocity (\(v_3\))  
**Derivation**:  
1. Escape Sun's gravity at planet's orbital distance:  
   \[
   v_{\text{esc,Sun}} = \sqrt{\frac{2GM_{\text{Sun}}}{R_{\text{orbit}}}}
   \]  
2. Planet's orbital velocity around Sun:  
   \[
   v_{\text{orbit}} = \sqrt{\frac{GM_{\text{Sun}}}{R_{\text{orbit}}}}
   \]  
3. Total velocity from planet's surface:  
   \[
   v_3 = \sqrt{v_2^2 + (v_{\text{esc,Sun}} - v_{\text{orbit}})^2}
   \]  

## 3. Cosmic Velocities for Earth  

**Parameters**:  
- \(M_{\text{Earth}} = 5.972 \times 10^{24} \text{ kg}\)  
- \(R_{\text{Earth}} = 6.371 \times 10^6 \text{ m}\)  
- \(R_{\text{Earth-Sun}} = 1.496 \times 10^{11} \text{ m}\)  

**Calculations**:  
- \(v_1 = \sqrt{\frac{GM_{\text{Earth}}}{R_{\text{Earth}}}} \approx 7.91 \text{ km/s}\)  
- \(v_2 = \sqrt{2} \cdot v_1 \approx 11.19 \text{ km/s}\)  
- \(v_3 = \sqrt{v_2^2 + (\sqrt{\frac{2GM_{\text{Sun}}}{R_{\text{Earth-Sun}}}} - \sqrt{\frac{GM_{\text{Sun}}}{R_{\text{Earth-Sun}}}})^2} \approx 16.64 \text{ km/s}\)  

## 4. Comparison with Moon, Mars, and Jupiter  

**Parameters**:  
| Body    | Mass (kg)          | Radius (m)       | Orbital Radius (m)     |  
|---------|--------------------|------------------|------------------------|  
| Moon    | \(7.342 \times 10^{22}\)  | \(1.737 \times 10^6\)  | \(1.496 \times 10^{11}\) (Earth's)|  
| Mars    | \(6.417 \times 10^{23}\)  | \(3.390 \times 10^6\)  | \(2.279 \times 10^{11}\) |  
| Jupiter | \(1.899 \times 10^{27}\)  | \(6.991 \times 10^7\)  | \(7.785 \times 10^{11}\) |  

**Calculated Velocities (km/s)**:  
| Body    | \(v_1\) | \(v_2\) | \(v_3\)  |  
|---------|--------|--------|---------|  
| Earth   | 7.91   | 11.19  | 16.64   |  
| Moon    | 1.68   | 2.38   | 16.51   |  
| Mars    | 3.55   | 5.03   | 13.09   |  
| Jupiter | 42.14  | 59.57  | 9.67    |  

## 5. Visualizations  

### 5.1 Cosmic Velocities Comparison  
```python
import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.67430e-11  
M_sun = 1.989e30  

# Celestial body parameters: [mass (kg), radius (m), orbital radius (m)]
bodies = {
    'Earth': [5.972e24, 6.371e6, 1.496e11],
    'Moon': [7.342e22, 1.737e6, 1.496e11],
    'Mars': [6.417e23, 3.390e6, 2.279e11],
    'Jupiter': [1.899e27, 6.991e7, 7.785e11]
}

# Calculate cosmic velocities
velocities = {'v1': {}, 'v2': {}, 'v3': {}}
for body, (M, R, R_orbit) in bodies.items():
    v1 = np.sqrt(G * M / R) / 1000
    v2 = np.sqrt(2 * G * M / R) / 1000
    v_esc_sun = np.sqrt(2 * G * M_sun / R_orbit) / 1000
    v_orbit = np.sqrt(G * M_sun / R_orbit) / 1000
    v3 = np.sqrt(v2**2 + (v_esc_sun - v_orbit)**2)
    velocities['v1'][body] = v1
    velocities['v2'][body] = v2
    velocities['v3'][body] = v3

# Plot
fig, ax = plt.subplots(figsize=(12, 7))
x = np.arange(len(bodies))
width = 0.25

bars1 = ax.bar(x - width, velocities['v1'].values(), width, label='$v_1$')
bars2 = ax.bar(x, velocities['v2'].values(), width, label='$v_2$')
bars3 = ax.bar(x + width, velocities['v3'].values(), width, label='$v_3$')

# Annotations
for bars in [bars1, bars2, bars3]:
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:.2f}', xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3), textcoords="offset points", ha='center', va='bottom')

ax.set_yscale('log')
ax.set_xlabel('Celestial Body')
ax.set_ylabel('Velocity (km/s, log scale)')
ax.set_title('Cosmic Velocities Comparison')
ax.set_xticks(x)
ax.set_xticklabels(bodies.keys())
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('cosmic_velocities_comparison.png')
plt.show()
# Problem 1
# **Wave Interference Patterns on a Water Surface**

## **1. Selecting a Regular Polygon**

### **Introduction**
In wave physics, interference occurs when two or more waves overlap, resulting in regions of constructive and destructive interference. To systematically analyze these patterns, we consider multiple point wave sources positioned at the vertices of a **regular polygon**. This setup allows us to explore how symmetric arrangements of sources influence the resulting wave field.

### **Mathematical Definition of a Regular Polygon**
A **regular polygon** with $N$ sides is a closed geometric figure where all sides are of equal length and all internal angles are equal. The vertices of such a polygon, when inscribed in a circle of radius $R$, can be determined using trigonometric functions.

For a polygon centered at the origin, the coordinates of the $i$-th vertex are given by:

$$x_i=R\cos\left(\frac{2\pi i}{N}\right),\quad y_i=R\sin\left(\frac{2\pi i}{N}\right),\quad i=0,1,2,\dots,N-1$$

where:
- $R$ is the circumradius of the polygon,

- $N$ is the number of sides (hence, the number of sources),

- $i$ indexes the vertices counterclockwise starting from an initial reference point.
### **Choosing the Regular Polygon**

The choice of $N$ influences the symmetry of the interference pattern. Common selections include:

- **Equilateral Triangle ($N=3$)**: Yields a threefold symmetric interference pattern.

- **Square ($N=4$)**: Produces a fourfold symmetric pattern with central and diagonal wave reinforcements.

- **Pentagon ($N=5$)**: Generates more complex wave interactions with fivefold rotational symmetry.

- **Hexagon ($N=6$)**: Approximates circular symmetry while retaining noticeable interference fringes.

---

## **2. Positioning the Sources**

### **Determining the Coordinates of the Polygonal Vertices**
To systematically analyze interference, we must precisely position the wave sources at the vertices of a chosen regular polygon. Given a polygon inscribed within a circle of radius $R$, the coordinates of its vertices are:

$$x_i=R\cos\left(\frac{2\pi i}{N}\right),\quad y_i=R\sin\left(\frac{2\pi i}{N}\right),\quad i=0,1,2,\dots,N-1$$

### **Assigning Each Vertex as a Wave Source**
Each vertex serves as a point source emitting circular waves with identical amplitude and frequency. The total wave field results from the superposition of these waves.

Each wave propagates outward from its source with a displacement function:

$$\eta_i(x,y,t)=\frac{A}{r_i}\cos\left(kr_i-\omega t+\phi_i\right)$$

where:

- $r_i=\sqrt{(x-x_i)^2+(y-y_i)^2}$ is the radial distance to the observation point.

---
## **3. Defining the Wave Equations**

### **Mathematical Representation of Wave Motion**
Each wave emitted from a point source follows the equation:

$$\eta_i(x,y,t)=\frac{A}{r_i}\cos\left(kr_i-\omega t+\phi_i\right)$$

where:

- $A$ is the amplitude,

- $k=\frac{2\pi}{\lambda}$ is the wave number,

- $\omega=2\pi f$ is the angular frequency,

- $\phi_i$ is the phase,

- $r_i$ is the radial distance from the $i$-th source.

### **Uniformity Assumptions**
To maintain coherence in interference analysis, we assume:

- All waves have **the same amplitude**, i.e., $A$ is constant.

- All waves have **the same wavelength** $\lambda$ and frequency $f$.

- Initial phase differences between sources remain fixed.

---
## **4. Applying the Superposition Principle**

### **Summation of Wave Displacements**

According to the principle of superposition, the resultant displacement at any point on the water surface is the sum of individual wave contributions:

$$\eta_{\text{sum}}(x,y,t)=\sum_{i=1}^{N}\eta_i(x,y,t)$$

This summation captures constructive and destructive interference effects.

### **Constructive and Destructive Interference Conditions**

- **Constructive interference:** Occurs when phase differences satisfy:

$$kr_i-\omega t+\phi_i=2m\pi,\quad m\in\mathbb{Z}$$

- **Destructive interference:** Occurs when phase differences satisfy:

$$kr_i-\omega t+\phi_i=(2m+1)\pi,\quad m\in\mathbb{Z}$$

---

## **5. Analyzing the Interference Patterns**

### **Identifying Interference Zones**
By computing $\eta_{\text{sum}}(x,y,t)$, we can classify different regions:
- **High amplitude zones:** Result from constructive interference.
- **Low amplitude zones:** Result from destructive interference.
### **Temporal Evolution of the Pattern**
As time progresses, the interference pattern evolves dynamically, influenced by wave frequency and phase differences.

---

## **6. Visualization and Simulation**

### **Graphical Representations**
Using numerical simulations, we generate:
- **Static interference maps** for different polygons.
- **Time-evolving wave fields** to observe changing interference dynamics.

### **Python Implementation**

A Python script implementing the above equations will:
1. Define wave parameters.
2. Compute the interference pattern on a 2D grid.
3. Visualize results using heatmaps and contour plots.

The next step is to implement and analyze these interference patterns computationally.

# Python/Models

--- 2D Interference Pattern Animation (Sunrise Horizon) ---

![alt text](image-4.png)

--- 3D Interference Pattern Animation (Sunrise Horizon) ---

![alt text](image-3.png)

```python
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation
from IPython.display import Image, HTML
from google.colab import files

# --- Parameters (KEEPING AS IS) ---
A = 1.0  # Amplitude
k = 2 * np.pi / 1.0  # Wave number
omega = 1.0  # Angular frequency
phi = 0.0  # Initial phase

# Define triangle's vertices (KEEPING AS IS)
sources = np.array([
    [0, np.sqrt(3)],  # Top vertex
    [-1, 0],          # Bottom-left
    [1, 0]            # Bottom-right
])

# Create a smaller grid (KEEPING AS IS)
x = np.linspace(-2, 2, 50)
y = np.linspace(-2, 2, 50)
X, Y = np.meshgrid(x, y)

# Wave equation for a single source (KEEPING AS IS)
def wave(X, Y, x0, y0, t):
    r = np.sqrt((X - x0)**2 + (Y - y0)**2)
    r = np.maximum(r, 1e-10)  # Avoid division by zero
    return (A / np.sqrt(r)) * np.cos(k * r - omega * t + phi)

# Compute total wave (KEEPING AS IS)
def get_total_wave(t):
    eta_total = np.zeros_like(X)
    for x0, y0 in sources:
        eta_total += wave(X, Y, x0, y0, t)
    return eta_total

# --- Function to Create and Save 2D Animation ---
def create_2d_animation(filename='triangle_interference_2d_enhanced.gif'):
    plt.close('all')

    fig2d, ax2d = plt.subplots(figsize=(10, 8), facecolor='#1B263B') # Dark desaturated blue
    ax2d.set_facecolor('#1B263B')
    ax2d.tick_params(colors='#A0A0A0') # Medium grey ticks
    ax2d.xaxis.label.set_color('#A0A0A0')
    ax2d.yaxis.label.set_color('#A0A0A0')
    ax2d.title.set_color('#F0F0F0') # Light grey title

    # Using 'hot' or 'YlOrRd' for fiery effect
    contour = ax2d.contourf(X, Y, get_total_wave(0), levels=50, cmap='YlOrRd', extend='both')
    cbar = plt.colorbar(contour, ax=ax2d, label='Wave Displacement', pad=0.03)
    cbar.ax.yaxis.set_tick_params(color='#A0A0A0')
    cbar.ax.yaxis.label.set_color('#A0A0A0')
    cbar.outline.set_edgecolor('#A0A0A0')

    ax2d.scatter(sources[:, 0], sources[:, 1], c='#FFD700', marker='*', s=250, edgecolor='white', linewidth=1.5, label='Sources') # Gold star markers
    ax2d.set_title('Dynamic Interference Pattern (2D)', fontsize=16, fontweight='bold')
    ax2d.set_xlabel('X-axis')
    ax2d.set_ylabel('Y-axis')
    ax2d.legend(facecolor='#2F4F4F', edgecolor='none', labelcolor='#F0F0F0', loc='upper right') # Styled legend
    ax2d.grid(True, linestyle='--', alpha=0.4, color='#667788') # Even softer grid

    def update_2d(frame):
        t = frame * 0.05
        ax2d.clear()
        ax2d.set_facecolor('#1B263B')
        ax2d.tick_params(colors='#A0A0A0')
        ax2d.xaxis.label.set_color('#A0A0A0')
        ax2d.yaxis.label.set_color('#A0A0A0')
        ax2d.title.set_color('#F0F0F0')

        eta_total = get_total_wave(t)
        contour = ax2d.contourf(X, Y, eta_total, levels=50, cmap='YlOrRd', extend='both')
        ax2d.scatter(sources[:, 0], sources[:, 1], c='#FFD700', marker='*', s=250, edgecolor='white', linewidth=1.5, label='Sources')
        ax2d.set_title(f'Dynamic Interference Pattern (2D) | Time: {t:.2f}s', fontsize=16, fontweight='bold')
        ax2d.set_xlabel('X-axis')
        ax2d.set_ylabel('Y-axis')
        ax2d.legend(facecolor='#2F4F4F', edgecolor='none', labelcolor='#F0F0F0', loc='upper right')
        ax2d.grid(True, linestyle='--', alpha=0.4, color='#667788')
        return []

    ani2d = animation.FuncAnimation(fig2d, update_2d, frames=50, interval=50, blit=False)
    writer2d = animation.PillowWriter(fps=10)
    ani2d.save(filename, writer=writer2d, dpi=100)
    plt.close(fig2d)
    print(f"Saved {filename}")

# --- Function to Create and Save 3D Animation ---
def create_3d_animation(filename='triangle_interference_3d_enhanced.gif'):
    plt.close('all')

    fig3d = plt.figure(figsize=(10, 8), facecolor='#1B263B')
    ax3d = fig3d.add_subplot(111, projection='3d', facecolor='#1B263B')
    ax3d.tick_params(colors='#A0A0A0')
    ax3d.xaxis.label.set_color('#A0A0A0')
    ax3d.yaxis.label.set_color('#A0A0A0')
    ax3d.zaxis.label.set_color('#A0A0A0')
    ax3d.title.set_color('#F0F0F0')

    eta_total = get_total_wave(0)
    surf = ax3d.plot_surface(X, Y, eta_total, cmap='YlOrRd', rstride=1, cstride=1, antialiased=True, alpha=0.9)
    cbar3d = fig3d.colorbar(surf, ax=ax3d, shrink=0.6, aspect=20, label='Wave Displacement', pad=0.03)
    cbar3d.ax.yaxis.set_tick_params(color='#A0A0A0')
    cbar3d.ax.yaxis.label.set_color('#A0A0A0')
    cbar3d.outline.set_edgecolor('#A0A0A0')

    ax3d.set_title('Dynamic Interference Pattern (3D)', fontsize=16, fontweight='bold')
    ax3d.set_xlabel('X-axis')
    ax3d.set_ylabel('Y-axis')
    ax3d.set_zlabel('Wave Displacement')

    def update_3d(frame):
        t = frame * 0.05
        ax3d.clear()
        ax3d.set_facecolor('#1B263B')
        ax3d.tick_params(colors='#A0A0A0')
        ax3d.xaxis.label.set_color('#A0A0A0')
        ax3d.yaxis.label.set_color('#A0A0A0')
        ax3d.zaxis.label.set_color('#A0A0A0')
        ax3d.title.set_color('#F0F0F0')

        eta_total = get_total_wave(t)
        surf = ax3d.plot_surface(X, Y, eta_total, cmap='YlOrRd', rstride=1, cstride=1, antialiased=True, alpha=0.9)
        ax3d.set_title(f'Dynamic Interference Pattern (3D) | Time: {t:.2f}s', fontsize=16, fontweight='bold')
        ax3d.set_xlabel('X-axis')
        ax3d.set_ylabel('Y-axis')
        ax3d.set_zlabel('Wave Displacement')
        return [surf]

    ani3d = animation.FuncAnimation(fig3d, update_3d, frames=50, interval=50, blit=False)
    writer3d = animation.PillowWriter(fps=10)
    ani3d.save(filename, writer=writer3d, dpi=100)
    plt.close(fig3d)
    print(f"Saved {filename}")

# --- Execute and Display Animations ---
gif_2d_filename = 'triangle_interference_2d_enhanced_option2.gif'
gif_3d_filename = 'triangle_interference_3d_enhanced_option2.gif'

print("Generating 2D Animation (Option 2)...")
create_2d_animation(gif_2d_filename)
print("Generating 3D Animation (Option 2)...")
create_3d_animation(gif_3d_filename)

print("\n--- 2D Interference Pattern Animation (Sunrise Horizon) ---")
display(Image(filename=gif_2d_filename))
print("\n--- 3D Interference Pattern Animation (Sunrise Horizon) ---")
display(Image(filename=gif_3d_filename))

files.download(gif_2d_filename)
files.download(gif_3d_filename)
```
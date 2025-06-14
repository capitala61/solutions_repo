# Problem 1

# 📊 Simulating Sampling Distributions


### 🎯 Objective
To demonstrate the Central Limit Theorem (CLT), we begin by generating large populations from various distributions:

- Uniform Distribution
- Exponential Distribution
- Binomial Distribution

Each dataset will represent a "population", from which we will later draw repeated random samples to study the behavior of their means.

---

## 🔢 Step 1: Generate Populations

Let:
- $N = 100000$ be the size of each simulated population.

We will define each population as follows:

- **Uniform Distribution**:  

$$X \sim \text{Uniform}(a=0, b=1)$$

- **Exponential Distribution**:  

$$X \sim \text{Exponential}(\lambda=1)$$

- **Binomial Distribution**:  

$$X \sim \text{Binomial}(n=10, p=0.5)$$

---

### 🧪 Python Code/ Visual

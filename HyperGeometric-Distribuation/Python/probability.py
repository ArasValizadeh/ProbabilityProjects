from math import comb
import matplotlib.pyplot as plt

def hypergeometric_pmf(k, N, K, n):
    numerator = comb(K, k) * comb(N - K, n - k)
    denominator = comb(N, n)
    return numerator / denominator

def hypergeometric_cdf(k, N, K, n):
    cumulative_prob = 0
    for i in range(k, n + 1):
        cumulative_prob += hypergeometric_pmf(i, N, K, n)
    return cumulative_prob

N = 10000  # Total number of devices
K = 200    # Total number of infected devices
n = 500    # Number of devices selected for inspection
k = 10     # Number of infected devices we want to detect

x = []
y = []

for i in range (200):
    x.append(i)
    y.append(hypergeometric_pmf(i, N, K, n))

y1 = [y[0]]

for i in range(1,200):
    y1.append(y[i]+y1[i-1])

plt.figure(figsize=(10, 6))
plt.plot(x, y, marker='.', linestyle='-', color='b')
plt.xlabel('Number of infected device in sampling')
plt.ylabel('Probability')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(x, y1, marker='.', linestyle='-', color='b')
plt.xlabel('Number of at least k infected device in sampling')
plt.ylabel('Probability')
plt.grid(True)
plt.show()
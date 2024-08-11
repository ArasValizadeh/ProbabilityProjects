from math import comb
import matplotlib.pyplot as plt

def hypergeometric_pmf(k, N, K, n):
    numerator = comb(K, k) * comb(N - K, n - k)
    denominator = comb(N, n)
    return numerator / denominator

def expected_value(x,y):
    sum = 0
    for i in range(len(y)):
        sum += x[i] * y[i]
    return sum 

def expected_value2(x,y):
    sum = 0
    for i in range(len(y)):
        sum += x[i]**2 * y[i]
    return sum

N = 10000  # Total number of devices
K = 200    # Total number of infected devices
n = 500    # Number of devices selected for inspection

x = []
y = []

for i in range(200):
    x.append(i)
    y.append(hypergeometric_pmf(i, N, K, n))

print("expected value is :",expected_value(x,y))
print("variance is : ",expected_value2(x,y) - (expected_value(x,y) ** 2))

y1 = [y[0]]
for i in range(1, 200):
    y1.append(y[i] + y1[i - 1])

plt.figure(figsize=(10, 6))
plt.plot(x, y, marker='.', linestyle='-', color='b')
plt.xlabel('Number of infected devices in sample')
plt.ylabel('Probability (PMF)')
plt.grid(True)
plt.title('Hypergeometric PMF: Exactly k Infected Devices')
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(x, y1, marker='.', linestyle='-', color='r')
plt.xlabel('Number of infected devices in sample')
plt.ylabel('Cumulative Probability (CDF)')
plt.grid(True)
plt.title('Hypergeometric CDF: Up to k Infected Devices')
plt.show()
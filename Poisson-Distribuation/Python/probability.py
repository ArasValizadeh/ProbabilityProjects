import math
import matplotlib.pyplot as plt

def poisson_pmf(k, lambda_rate):
    probability = (lambda_rate**k * math.exp(-lambda_rate)) / math.factorial(k)
    return probability

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

lambda_rate = 30  
x = []
y = []
for i in range (100):
    x.append(i)
    y.append(poisson_pmf(i, lambda_rate))

print("expected value is :",expected_value(x,y))
print("variance is : ",expected_value2(x,y) - (expected_value(x,y) ** 2))

y1 = [y[0]]

for j in range(1,len(y)):
    y1.append(y1[j-1] + y[j])


plt.figure(figsize=(10, 6))
plt.plot(x, y, marker='*', linestyle='-', color='b')
plt.xlabel('Number of calls')
plt.ylabel('Probability of k calls happend in a min')
plt.title('Poisson-Distribuation')
plt.grid(True)
plt.show()



plt.figure(figsize=(10, 6))
plt.plot(x, y1, marker='*', linestyle='-', color='g')
plt.xlabel('Number of calls')
plt.ylabel('Probability of up to k calls happend in a min')
plt.title('Poisson-Distribuation')
plt.grid(True)
plt.show()


prob_less_than_20 = sum(poisson_pmf(k, lambda_rate) for k in range(20))
print(prob_less_than_20)


prob_more_than_35 = 1 - sum(poisson_pmf(k, lambda_rate) for k in range(36))
print(prob_more_than_35)

prob_between_25_and_35 = sum(poisson_pmf(k, lambda_rate) for k in range(25, 36))
print(prob_between_25_and_35)
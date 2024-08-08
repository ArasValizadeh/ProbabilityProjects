import random
import matplotlib.pyplot as plt

def simulate_birthday_paradox(num_people, num_simulations):
    def has_duplicate_birthdays(num_people):
        birthdays = [random.randint(1, 365) for _ in range(num_people)]
        return len(birthdays) != len(set(birthdays))

    duplicate_count = sum(has_duplicate_birthdays(num_people) for _ in range(num_simulations))
    return duplicate_count / num_simulations

x = []
y = []

for i in range(5,100):
    x.append(i)
    y.append(simulate_birthday_paradox(i, 5000))


plt.figure(figsize=(10, 6))
plt.plot(x, y, marker='*', linestyle='-', color='r')
plt.xlabel('Number of People')
plt.ylabel('Probability of at least two people sharing the same birthday')
plt.title('Birthday Problem')
plt.grid(True)
plt.show()

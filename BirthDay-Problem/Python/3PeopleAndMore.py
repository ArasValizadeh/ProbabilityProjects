import random
import matplotlib.pyplot as plt
import math

def simulate_three_same_birthday_paradox(num_people, num_simulations):
    def has_three_same_birthdays(num_people):
        birthdays = [random.randint(1, 365) for _ in range(num_people)]
        birthday_counts = {day: birthdays.count(day) for day in set(birthdays)}
        return any(count >= 3 for count in birthday_counts.values())

    three_same_count = sum(has_three_same_birthdays(num_people) for _ in range(num_simulations))
    return three_same_count / num_simulations

x = []
y = []

for i in range(5,100):
    x.append(i)
    y.append(simulate_three_same_birthday_paradox(i, 5000))

plt.figure(figsize=(10, 6))
plt.plot(x, y, marker='*', linestyle='-', color='b')
plt.xlabel('Number of People')
plt.ylabel('Probability of at least three people sharing the same birthday')
plt.title('Birthday Problem')
plt.grid(True)
plt.show()
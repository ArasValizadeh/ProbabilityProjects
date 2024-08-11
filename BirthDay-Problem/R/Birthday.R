
library(ggplot2)

simulate_three_same_birthday_paradox <- function(num_people, num_simulations) {
  has_three_same_birthdays <- function(num_people) {
    birthdays <- sample(1:365, num_people, replace = TRUE)
    birthday_counts <- table(birthdays)
    return(any(birthday_counts >= 3))
  }
  
  three_same_count <- sum(replicate(num_simulations, has_three_same_birthdays(num_people)))
  return(three_same_count / num_simulations)
}

x <- c()
y <- c()

for (i in 5:99) {
  x <- c(x, i)
  y <- c(y, simulate_three_same_birthday_paradox(i, 5000))
}

data <- data.frame(Number_of_People = x, Probability = y)

ggplot(data, aes(x = Number_of_People, y = Probability)) +
  geom_point(shape = 8, color = "blue") +
  geom_line(color = "blue") +
  labs(title = "Birthday Problem",
       x = "Number of People",
       y = "Probability of at least three people sharing the same birthday") +
  theme_minimal() +
  theme(panel.grid.major = element_line(color = "grey"),
        panel.grid.minor = element_blank())


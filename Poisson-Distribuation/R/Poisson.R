library(ggplot2)

poisson_pmf <- function(k, lambda_rate) {
  probability <- (lambda_rate^k * exp(-lambda_rate)) / factorial(k)
  return(probability)
}

expected_value <- function(x, y) {
  sum(x * y)
}

expected_value2 <- function(x, y) {
  sum((x^2) * y)
}

lambda_rate <- 30  
x <- 0:99
y <- sapply(x, poisson_pmf, lambda_rate)

exp_val <- expected_value(x, y)
variance <- expected_value2(x, y) - (exp_val^2)

cat("Expected value is:", exp_val, "\n")
cat("Variance is:", variance, "\n")

y1 <- cumsum(y)

pmf_plot <- ggplot(data.frame(x = x, y = y), aes(x = x, y = y)) +
  geom_point() +
  geom_line() +
  labs(title = "Poisson Distribution - PMF",
       x = "Number of calls",
       y = "Probability of k calls happening in a min") +
  theme_minimal() +
  theme(panel.grid.major = element_line(color = "grey"),
        panel.grid.minor = element_blank())

print(pmf_plot)

cdf_plot <- ggplot(data.frame(x = x, y = y1), aes(x = x, y = y1)) +
  geom_point() +
  geom_line() +
  labs(title = "Poisson Distribution - CDF",
       x = "Number of calls",
       y = "Probability of up to k calls happening in a min") +
  theme_minimal() +
  theme(panel.grid.major = element_line(color = "grey"),
        panel.grid.minor = element_blank())

print(cdf_plot)

prob_less_than_20 <- sum(sapply(0:19, poisson_pmf, lambda_rate))
cat("Probability of less than 20 calls:", prob_less_than_20, "\n")

prob_more_than_35 <- 1 - sum(sapply(0:35, poisson_pmf, lambda_rate))
cat("Probability of more than 35 calls:", prob_more_than_35, "\n")

prob_between_25_and_35 <- sum(sapply(25:35, poisson_pmf, lambda_rate))
cat("Probability of between 25 and 35 calls:", prob_between_25_and_35, "\n")

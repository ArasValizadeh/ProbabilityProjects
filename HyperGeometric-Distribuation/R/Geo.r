library(ggplot2)

hypergeometric_pmf <- function(k, N, K, n) {
  numerator <- choose(K, k) * choose(N - K, n - k)
  denominator <- choose(N, n)
  print(numerator)
  print(denominator)
  return(numerator / denominator)
}

?choose
hypergeometric_cdf <- function(k, N, K, n) {
  cumulative_prob <- 0
  for (i in k:n) {
    cumulative_prob <- cumulative_prob + hypergeometric_pmf(i, N, K, n)
  }
  return(cumulative_prob)
}

N <- 10000  
K <- 200    
n <- 500    

x <- 0:98
y <- double(length(x))

File <- read.csv("./data.csv")
y0 = as.list(File)
y0 = y0[1][[1]]

for (i in x) {
  y[i] <- y0[[i + 1]]
  print(y[i])
}
y1 <- cumsum(y)

pmf_plot <- ggplot(data.frame(x = x, y = y), aes(x = x, y = y)) +
  geom_point() +
  geom_line() +
  labs(title = "Hypergeometric PMF",
       x = "Number of infected devices in sampling",
       y = "Probability") +
  theme_minimal() +
  theme(panel.grid.major = element_line(color = "grey"),
        panel.grid.minor = element_blank())

print(pmf_plot)

cdf_plot <- ggplot(data.frame(x = x, y = y1), aes(x = x, y = y1)) +
  geom_point() +
  geom_line() +
  labs(title = "Hypergeometric CDF",
       x = "Number of at least k infected devices in sampling",
       y = "Probability") +
  theme_minimal() +
  theme(panel.grid.major = element_line(color = "grey"),
        panel.grid.minor = element_blank())

print(cdf_plot)


library(MASS)
library(tidyverse)
library(ggforce)
library(ExtDist) # extra distributions
library(cowplot) # for combining two plots

library(MASS)
library(tidyverse)
library(ggforce)
library(ExtDist) # extra distributions
library(cowplot) # for combining two plots

# pareto frontier from selecting top N
slope_steps <- 100
pareto_topn <- function(points, num_sample) {
   pareto <- data.frame(x = as.numeric(), y = as.numeric())
   for (slope in 1:slope_steps) {
      points <- points %>%
         mutate(
            # score = x + y * -log(slope / slope_steps),
            score = x + y * tan(2 * 3.1415 * slope / slope_steps),
            rank = rank(desc(score))
         )
      stats <- points %>%
         summarize(
            avg_x = sum(x[rank < num_sample]) / num_sample,
            avg_y = sum(y[rank < num_sample]) / num_sample
         )
      pareto[nrow(pareto) + 1, ] <- list(x = stats$avg_x, y = stats$avg_y)
   }
   ggplot(pareto, aes(x, y)) +
      geom_point(data = points, alpha = .1) +
      geom_density_2d(data = points) +
      geom_point(data = pareto, color = "red", alpha = 1) +
      coord_fixed() +
      xlim(-5, 5) +
      ylim(-5, 5)
}


Sigma <- matrix(c(1, 1, 1, 4), 2, 2) # positive covariance
points <- data.frame(mvrnorm(n = 5000, rep(0, 2), Sigma)) %>%
   rename("x" = 1, "y" = 2)
pareto_topn(points, 1000)

Sigma2 <- matrix(c(4, 1, 1, 1), 2, 2) # negative covariance
points2 <- data.frame(mvrnorm(n = 5000, rep(0, 2), Sigma2)) %>%
   rename("x" = 1, "y" = 2)
pareto_topn(points2, 1000)

points_combined <- rbind(points, points2)
pareto_topn(points_combined, 1000)

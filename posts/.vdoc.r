#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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
# pareto_topn(points, 1000)

# pass this function a set of points and it'll draw a pareto frontier along each axis
pareto_positive <- function(points) {
   slope_steps <- 100
   pareto <- data.frame(x = as.numeric(), y = as.numeric())
   for (slope in 1:slope_steps) { # loop through slopes
      slope_ratio <- slope / slope_steps
      points <- points %>%
         mutate(
            # given an angle between 0 and 2pi, unit vector will be (cos(theta),sin(theta)).
            # can get score by dot product with the unit vector
            score = x * cos(slope_ratio * 3.1415 * 2) + y * sin(slope_ratio * 3.1415 * 2)
         )
      stats <- points %>%
         summarize(
            avg_x = sum(x[score > 0]),
            avg_y = sum(y[score > 0])
         )
      pareto[nrow(pareto) + 1, ] <- list(x = stats$avg_x, y = stats$avg_y)
   }
   p <- ggplot(points, aes(x, y)) +
      geom_point() +
      coord_fixed()
   q <- ggplot(pareto, aes(x, y)) +
      geom_hline(yintercept = 0) +
      geom_vline(xintercept = 0) +
      # geom_point(data = points, alpha = .1) +
      # geom_density_2d(data = points) +
      geom_point(data = pareto, color = "red", alpha = 1) +
      geom_polygon(data = pareto, alpha = 0.1) + # fill
      coord_fixed()
   plot_grid(p, q)
}
#
#
#
#
Sigma <- matrix(c(1, 1, 1, 4), 2, 2) # 2x2 covariance matrix
points <- data.frame(mvrnorm(n = 500, rep(0, 2), Sigma)) %>%
   rename("x" = 1, "y" = 2)
pareto_positive(points)
#
#
#
#
points <- tibble(x = rLaplace(5000), y = rLaplace(5000))
pareto_positive(points)
#
#
#
#
z <- rLaplace(200, mu = 0, b = 3)
Sigma <- matrix(c(1, 0, 0, 1), 2, 2) # 2x2 covariance matrix
points <- data.frame(mvrnorm(n = 200, rep(0, 2), Sigma)) %>%
   rename("x" = 1, "y" = 2) %>%
   cbind(z) %>%
   mutate(x = z + 2 * x, y = z + 2 * y)
pareto_positive(points)
#
#
#
#
points <- tibble(x = runif(5000) - .5, y = runif(5000) - .5)
pareto_positive(points)
#
#
#
#
points <- tibble(x = runif(5000) - .5, y = runif(5000) - .5, z = runif(5000) - .5) %>%
   mutate(
      x = x + .5 * z,
      y = y + .5 * z
   )
pareto_positive(points)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

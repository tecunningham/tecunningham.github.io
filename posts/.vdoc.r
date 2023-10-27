#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
library(tidyverse)
library(laGP)
data <- tribble( # basic datapoints
   ~x, ~y,
   2, 2,
   3, 6,
   4, 5.6,
   5, 8.5,
   6, 11,
   7, 8,
   8, 4,
   9, 2
)

xa <- c(3, 4) # some subsets
ya <- subset(data, x %in% xa)$y
xb <- c(6, 8)
yb <- subset(data, x %in% xb)$y
xc <- c(4, 8)
yc <- subset(data, x %in% xc)$y

xx <- seq(0, 10, length = 1000)
p <- predGP(newGP(matrix(data$x, ncol = 1), data$y, d = 10, g = 1e-8),
   matrix(xx, ncol = 1),
   lite = TRUE
)
pa <- predGP(newGP(matrix(xa, ncol = 1), ya, d = 10, g = 1e-8),
   matrix(xx, ncol = 1),
   lite = TRUE
)
pb <- predGP(newGP(matrix(xb, ncol = 1), yb, d = 10, g = 1e-8),
   matrix(xx, ncol = 1),
   lite = TRUE
)
pc <- predGP(newGP(matrix(xc, ncol = 1), yc, d = 10, g = 1e-8),
   matrix(xx, ncol = 1),
   lite = TRUE
)
pab <- predGP(newGP(matrix(c(xa, xb), ncol = 1), c(ya, yb), d = 10, g = 1e-8),
   matrix(xx, ncol = 1),
   lite = TRUE
)

curves <- tibble(
   x = xx,
   pamax = pa$mean + 2 * sqrt(pa$s2),
   pamin = pa$mean - 2 * sqrt(pa$s2),
   pa = pa$mean,
   pbmax = pb$mean + 2 * sqrt(pb$s2),
   pbmin = pb$mean - 2 * sqrt(pb$s2),
   pb = pb$mean,
   pmax = p$mean + 2 * sqrt(p$s2),
   pmin = p$mean - 2 * sqrt(p$s2),
   p = p$mean,
   pab = pab$mean,
   pc = pc$mean
)

theme_set(theme_bw() +
   theme(
      panel.grid.major = element_blank(),
      panel.grid.minor = element_blank(),
      axis.text.x = element_blank(),
      axis.ticks.x = element_blank(),
      axis.text.y = element_blank(),
      axis.ticks.y = element_blank(),
      axis.title.x = element_blank(),
      axis.title.y = element_blank(),
      axis.line.x = element_line("black"),
      panel.border = element_blank()
   ))
update_geom_defaults("line", list(size = 1))
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# From code in this book: https://bookdown.org/rbg/surrogates/chap5.html
library(tidyverse)
library(laGP)
data <- tribble(
   ~x, ~y,
   #   1, 0,
   2, 2,
   3, 6,
   4, 5.6,
   5, 8.5,
   6, 11, #
   7, 8,
   8, 4,
   9, 2
)

xa <- c(3, 4) # 5
ya <- subset(data, x %in% xa)$y
xb <- c(6, 8)
yb <- subset(data, x %in% xb)$y
xc <- c(4, 8)
yc <- subset(data, x %in% xc)$y

xx <- seq(0, 10, length = 1000)
p <- predGP(newGP(matrix(data$x, ncol = 1), data$y, d = 10, g = 1e-8),
   matrix(xx, ncol = 1),
   lite = TRUE
)
pa <- predGP(newGP(matrix(xa, ncol = 1), ya, d = 10, g = 1e-8),
   matrix(xx, ncol = 1),
   lite = TRUE
)
pb <- predGP(newGP(matrix(xb, ncol = 1), yb, d = 10, g = 1e-8),
   matrix(xx, ncol = 1),
   lite = TRUE
)
pc <- predGP(newGP(matrix(xc, ncol = 1), yc, d = 10, g = 1e-8),
   matrix(xx, ncol = 1),
   lite = TRUE
)
pab <- predGP(newGP(matrix(c(xa, xb), ncol = 1), c(ya, yb), d = 10, g = 1e-8),
   matrix(xx, ncol = 1),
   lite = TRUE
)

curves <- tibble(
   x = xx,
   pamax = pa$mean + 2 * sqrt(pa$s2),
   pamin = pa$mean - 2 * sqrt(pa$s2),
   pa = pa$mean,
   pbmax = pb$mean + 2 * sqrt(pb$s2),
   pbmin = pb$mean - 2 * sqrt(pb$s2),
   pb = pb$mean,
   pmax = p$mean + 2 * sqrt(p$s2),
   pmin = p$mean - 2 * sqrt(p$s2),
   p = p$mean,
   pab = pab$mean,
   pc = pc$mean
)
theme_set(theme_bw() +
   theme(
      panel.grid.major = element_blank(),
      panel.grid.minor = element_blank(),
      axis.text.x = element_blank(),
      axis.ticks.x = element_blank(),
      axis.text.y = element_blank(),
      axis.ticks.y = element_blank(),
      axis.title.x = element_blank(),
      axis.title.y = element_blank(),
      axis.line.x = element_line("black"),
      panel.border = element_blank()
   ))
update_geom_defaults("line", list(size = 1))
#
#
#
#| fig-height: 1
ggplot(curves, aes(x, y)) +
   geom_line(aes(y = p), linewidth = 1) +
   ylim(0, 12)
#
#
#
#
#
#
#| fig-height: 1
ggplot(curves, aes(x, y)) +
   geom_line(aes(y = p), linewidth = 1) +
   geom_line(aes(y = pb), color = "red") +
   geom_point(data = tibble(x = xb, y = yb), color = "red", size = 3) +
   ylim(0, 12)
#
#
#
#
#
ggplot(curves, aes(x, y)) +
   geom_line(aes(y = p), linewidth = 1) +
   geom_line(aes(y = pb), color = "red") +
   geom_line(aes(y = pb + 0.3), color = "#009900", linewidth = 1) +
   geom_point(data = tibble(x = xb, y = yb), color = "red", size = 3) +
   geom_point(data = tibble(x = xb, y = yb + 0.3), color = "#009900", size = 3) +
   ylim(0, 12)
```
#
#
#
#
ggplot(curves, aes(x, y)) +
   geom_line(aes(y = p), linewidth = 1) +
   geom_line(aes(y = pa), color = "blue") +
   geom_line(aes(y = pb), color = "red") +
   geom_point(data = tibble(x = xa, y = ya), color = "blue", size = 3) +
   geom_point(data = tibble(x = xb, y = yb), color = "red", size = 3) +
   ylim(0, 12)
```
#
#
#
#
ggplot(curves, aes(x, y)) +
   geom_line(aes(y = p), linewidth = 1) +
   geom_line(aes(y = pa), color = "blue") +
   geom_line(aes(y = pb), color = "red") +
   geom_line(aes(y = pab), color = "#009900", linewidth = 1) +
   geom_point(data = tibble(x = xa, y = ya), color = "blue", size = 3) +
   geom_point(data = tibble(x = xb, y = yb), color = "red", size = 3) +
   geom_point(data = tibble(x = c(xa, xb), y = c(ya, yb) + 0.2), color = "#009900", size = 3) +
   ylim(0, 12)
```
#
#
#
#
#
#
## make an oscillation
orbit <- 5 + 3 * sin(xx) + cos(xx * 20)
xorbit <- c(2, 3.06, 3.2, 3.5, 4, 4.18, 6, 7)
porbit <- predGP(newGP(matrix(xorbit, ncol = 1), orbit[xorbit * 100], d = 10, g = 1e-8),
   matrix(xx, ncol = 1),
   lite = TRUE
)
#theme_set(theme_bw())
ggplot(tibble(x = xx, y = orbit, p = porbit$mean), aes(x, y)) +
   geom_line(aes(y = y)) +
   geom_line(aes(y = p), color="blue") +
   geom_point(
      data = tibble(x = xorbit, y = orbit[xorbit * 100]),
      color = "blue", size = 3
   ) +
   ylim(0, 12)
```
#
#
#
#
ggplot(curves, aes(x, y)) +
   geom_line(aes(y = p), linewidth = 1, color = "red") +
   geom_line(aes(y = pc), color = "pink") +
   # geom_line(aes(y = pb + 0.3), color = "#009900", linewidth = 1) +
   # geom_point(data = tibble(x = xb, y = yb), color = "red", size = 3) +
   # geom_point(data = tibble(x = xb, y = yb + 0.3), color = "#009900", size = 3) +
   ylim(0, 12)
```
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

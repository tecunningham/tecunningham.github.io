#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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
library(googlesheets4)
library(lubridate)
library(ggrepel)
library(zoo) # for yearmon, used in histograms
library(gt) # for tables
theme_set(theme_light())
theme_update(
   panel.grid.minor.y = element_blank(),
   panel.grid.minor.x = element_blank(),
   legend.position = "bottom"
)

gs4_auth("tom.cunningham@gmail.com")
# suspensions_raw <- read_sheet("https://docs.google.com/spreadsheets/d/1-lch6CvywoV4iAz0Yb61UsC9U6pgXDyYI2qb8jN5wmI/edit#gid=0")
setwd("/Users/tomcunningham/Library/CloudStorage/Dropbox/tecunningham.github.io/tecunningham.github.io/posts/")
# save(suspensions_raw, file='suspensions_raw')
load("suspensions_raw")
suspensions <- suspensions_raw %>% # NOTE: will fail with a cryptic error if a date is mis-formatted
   fill(category, entity) %>%
   subset(!is.na(start)) %>%
   mutate(
      start = as.Date(start),
      end = dplyr::if_else(is.na(end), Sys.Date(), as.Date(end)),
      reason = factor(reason) # this helps with consistent point shapes in visualization
   ) %>% # order them by the date of first suspension
   group_by(entity) %>%
   mutate(
      first_suspension = min(start)
   ) %>%
   ungroup() %>%
   mutate(entity = fct_reorder(entity, first_suspension))

platform_colors <- c(
   "Meta" = "#3b5998",
   "Twitter" = "#1DA1F2",
   "Facebook" = "#3b5998",
   "YouTube" = "#e62117",
   "Snapchat" = "#FFFC00",
   "Tik Tok" = "black",
   "LinkedIn" = "#0072b1",
   "Spotify" = "#1DB954",
   "Instagram" = "#F77737",
   "Clubhouse" = "blue",
   "Twitch" = "lightblue",
   "Gettr" = "orange",
   "Discord" = "purple",
   "other" = "grey"
)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#| fig-height: 3
ggplot(suspensions) +
   # geom_vline(xintercept = as.Date("2021-01-06"), linetype = 3) +
   # geom_vline(xintercept = as.Date("2020-11-20"), linetype = 3) +
   geom_histogram(aes(x = floor_date(start, "month"), fill = platform), binwidth = 30) +
   scale_x_date(date_labels = "%Y", date_breaks = "1 year") +
   ylab("suspensions") +
   theme(
      axis.text.x = element_text(angle = 90, hjust = 1),
      axis.title.x = element_blank(),
      plot.background = element_blank(),
      strip.text.x = element_blank(),
      legend.position = "bottom",
      plot.margin = unit(c(0, 0, 0, 0), "cm"),
      legend.margin = margin(15, 0, 0, 0),
      legend.box.spacing = unit(0, "pt")
   ) +
   scale_fill_manual(values = platform_colors, name = "") +
   guides(fill = guide_legend(nrow = 2))
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#| fig-height: 6
##  | column: page
##  | fig-width: 8
highlighted <- c("Courtney Love", "Donald Trump (R)")
# suspensions %>%
#    arrange(start) %>%
#    head() %>%
#    select(entity,platform,start)
ggplot(
   suspensions,
   aes(start, paste(start, entity, platform))
) +
   geom_segment(aes(
      # x = trunc(start, "month"), xend = ceiling_date(end, "month"),
      x = start, xend = end,
      y = paste(start, entity, platform), yend = paste(start, entity, platform), color = platform
   ), alpha = 1, linewidth = 1) +
   scale_colour_manual(values = platform_colors, name = "") +
   guides(colour = guide_legend(nrow = 1)) +
   geom_point(
      data = . %>% subset(entity %in% highlighted),
      color = "black"
   ) +
   geom_text_repel(
      data = . %>% subset(entity %in% highlighted), aes(label = paste0(entity, "\n", platform)),
      hjust = 1,
      direction = "y", nudge_x = -300
   ) +
   theme(
      axis.text.y = element_blank(),
      plot.background = element_blank(),
      panel.grid.major.x = element_line(color = "grey50"),
      panel.grid.major.y = element_blank(),
      panel.grid.minor.y = element_blank(),
      panel.background = element_blank(),
      legend.position = "bottom",
      plot.margin = unit(c(0, 0, 0, 0), "cm"),
      legend.margin = margin(0, 0, 0, 0),
      legend.box.spacing = unit(0, "pt")
   ) +
   xlab("") +
   ylab("") +
   scale_y_discrete(limits = rev)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#| fig-height: 3

# ggplot(suspensions %>%
#          mutate(yearmon = as.yearmon(start)) %>%
#          group_by(platform,yearmon) %>%
#          tally(),
#          aes(x = yearmon, y = n, fill=platform, group=platform))+
#    geom_col()+
#    scale_fill_manual(values = platform_colors, name = "")+
#    #scale_x_date(date_labels = "%Y", date_breaks = "1 year") +
#    ylab("suspensions") +
#    theme(
#       axis.text.x = element_text(angle = 90, hjust = 1),
#       axis.title.x = element_blank(),
#       plot.background = element_blank(),
#       strip.text.x = element_blank(),
#       legend.position = "bottom",
#       plot.margin = unit(c(0, 0, 0, 0), "cm"),
#       legend.margin = margin(0, 0, 0, 0),
#       legend.box.spacing = unit(0, "pt")
#    )+
#    guides(fill = guide_legend(nrow = 2))

ggplot(suspensions) +
   # geom_vline(xintercept = as.Date("2021-01-06"), linetype = 3) +
   # geom_vline(xintercept = as.Date("2020-11-20"), linetype = 3) +
   geom_histogram(aes(x = floor_date(start, "month"), fill = platform), binwidth = 30) +
   scale_x_date(date_labels = "%Y", date_breaks = "1 year") +
   ylab("suspensions") +
   theme(
      axis.text.x = element_text(angle = 90, hjust = 1),
      axis.title.x = element_blank(),
      plot.background = element_blank(),
      strip.text.x = element_blank(),
      legend.position = "bottom",
      plot.margin = unit(c(0, 0, 0, 0), "cm"),
      legend.margin = margin(0, 0, 0, 0),
      legend.box.spacing = unit(0, "pt")
   ) +
   scale_fill_manual(values = platform_colors, name = "") +
   guides(fill = guide_legend(nrow = 2))
#
#
#
#
#
#
#
#
#
#
#
#
#
#| fig-height: 3
top_platforms <- suspensions %>%
   group_by(platform) %>%
   summarize(total = n()) %>%
   arrange(desc(total)) %>%
   select(platform) %>%
   head(4)
ggplot(suspensions %>% mutate(platform = ifelse(platform %in% top_platforms$platform, platform, "other"))) +
   geom_histogram(aes(x = floor_date(start, "year"), fill = platform), binwidth = 366) +
   facet_grid(platform ~ .) +
   theme(
      strip.text.y.right = element_text(angle = 0, hjust = 0),
      axis.text.x = element_text(angle = 90, hjust = 1),
      axis.title.x = element_blank(),
      axis.title.y = element_blank(),
      strip.background = element_blank()
      # strip.text.x = element_blank(),
      # legend.position = "none"
   ) +
   scale_fill_manual(values = platform_colors) +
   scale_x_date(date_labels = "%Y", date_breaks = "1 year")
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
by_reason <- suspensions %>%
   mutate(reason = as.character(reason)) %>%
   group_by(reason) %>%
   mutate(reason = ifelse(n() < 4, "other", reason)) %>%
   summarize(n = n()) %>%
   mutate(pct = round(100 * n / sum(n))) %>%
   arrange(desc(n))

by_reason |> gt()
#
#
#
#
#| fig-height: 5
#| cap-location: margin
#| fig-cap: Reasons for suspension over time
suspensions <- suspensions %>%
   add_count(reason)

ggplot(suspensions %>% mutate(reason = fct_reorder(reason, -n))) +
   geom_histogram(aes(x = floor_date(start, "year"), fill = reason), binwidth = 366) +
   facet_wrap(reason ~ ., labeller = labeller(reason = label_wrap_gen(15))) +
   theme(
      strip.text.y.right = element_text(angle = 0, hjust = 0),
      legend.position = "none",
      axis.title.x = element_blank(),
      axis.text.x = element_text(angle = 90, hjust = 1),
      axis.title.y = element_blank()
   )
#
#
#
#
#
#
#| fig-height: 3
ggplot(suspensions %>%
   subset(reason %in% c("hate speech", "incitement", "covid misinfo", "election misinfo", "personal information", "hate group", "manipulation") &
      platform %in% c("Meta", "YouTube", "Twitter"))) +
   geom_histogram(aes(x = floor_date(start, "year"), fill = platform), binwidth = 366) +
   facet_grid(platform ~ reason, labeller = labeller(reason = label_wrap_gen(10))) +
   theme(
      strip.text.y.right = element_text(angle = 0, hjust = 0),
      legend.position = "none",
      axis.title.x = element_blank(),
      axis.text.x = element_text(angle = 90, hjust = 1),
      axis.title.y = element_blank()
   ) +
   scale_fill_manual(values = platform_colors) +
   scale_x_date(date_labels = "%Y", date_breaks = "1 year")
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
crawlers <- function(suspensions) {
   suspensions <- suspensions %>% # order them by the date of first suspension
      group_by(entity) %>%
      mutate(
         first_suspension = min(start)
      ) %>%
      ungroup() %>%
      mutate(entity = fct_reorder(entity, first_suspension))
   p <- ggplot(suspensions, aes(start, platform)) +
      geom_segment(aes(
         # x = trunc(start, "month"), xend = ceiling_date(end, "month"),
         x = start, xend = end,
         y = platform, yend = platform, color = platform
      ), linewidth = 1.8, alpha = 0.6) +
      geom_text(data = . %>% subset(start == first_suspension), aes(label = entity, y = 0), hjust = "right", position = position_nudge(x = -51), vjust = "bottom") +
      facet_grid(entity ~ .) +
      geom_point(aes(x = start, shape = factor(reason), color = platform), stroke = 1) +
      # geom_point(aes(x=trunc(start, "month"),shape=factor(reason),color = platform))+
      theme(
         strip.text.y.right = element_blank(),
         panel.border = element_blank(),
         axis.text.y = element_blank(),
         panel.grid.major.y = element_blank(),
         plot.background = element_rect(fill = "white"),
         panel.background = element_rect(fill = "#eeeeee"),
         strip.text.x = element_blank(),
         axis.title.x = element_blank(),
         axis.title.y = element_blank(),
         legend.position = "bottom",
         legend.box = "vertical", # stack legends
         legend.margin = margin()
      ) +
      scale_x_date(
         date_labels = "%Y", date_breaks = "1 year",
         # limits = c(as.Date("2014-06-01"), ceiling_date(Sys.Date(), "month")),
         # expand = c(0, 0)
         sec.axis = dup_axis(),
         expand = expansion(mult = c(.2, 0)) # expand 15% to the left, 0% to the right
      ) +
      scale_colour_manual(values = platform_colors, name = "") +
      #      scale_shape_identity() +
      scale_shape_manual(values = c(1:31), name = "", drop = FALSE) +
      coord_cartesian(clip = "off") +
      guides(colour = guide_legend(ncol = 10))
   return(p)
}
crawlers(suspensions %>% subset(category == "US politicians"))
#
#
#
#
#
#
#| fig-height: 4
crawlers(suspensions %>% subset(category == "Non-US politicians / political groups")) + xlim(as.Date("2016-01-01"), ceiling_date(Sys.Date(), "month"))
#
#
#
#
#
#
#
#| fig-height: 12
crawlers(suspensions %>% subset(category == "US Notable People"))
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#| fig-height: 8
crawlers(suspensions %>% subset(platform == "Meta")) + guides(color = "none")
#
#
#
#
#| fig-height: 14
crawlers(suspensions %>% subset(platform == "Twitter")) + guides(color = "none")
#
#
#
#
#
#
#| fig-height: 5
musk_unsuspensions <- suspensions %>% subset(end > as.Date("2022-10-27") & end < Sys.Date() & start < as.Date("2022-10-27"))
crawlers(suspensions %>% subset(platform == "Twitter" & entity %in% musk_unsuspensions$entity)) + guides(color = "none")
#
#
#
#
#| fig-height: 5
crawlers(suspensions %>% subset(platform == "YouTube"))
#
#
#
#
#| fig-height: 2
crawlers(suspensions %>% subset(platform == "Tik Tok")) + theme(legend.position = "none")
#
#
#
#
#| fig-height: 3
crawlers(suspensions %>% subset(!platform %in% c("Meta", "Twitter", "YouTube", "Tik Tok")))
#
#
#
#
#
#
#| fig-height: 6
crawlers(suspensions %>% subset(reason == "hate speech"))
#
#
#
#
#
#
#
#
#
#
#
#
#
#| fig-width: 10
#| fig-height: 3
#| cap-location: margin
#| fig-cap: Wikipedia-reported Twitter suspension by year
library(rvest)
library(polite)

url_tw <- "https://en.m.wikipedia.org/wiki/Twitter_suspensions"
suspensions_tw <-
   polite::scrape(polite::bow(url_tw)) %>% # scrape web page
   rvest::html_nodes("table.wikitable") %>% # pull out tables
   rvest::html_table(fill = TRUE) %>% # fill empty cells downwards
   data.table::rbindlist(fill = TRUE) %>% # combine all tables into a single table
   mutate(
      followers = as.numeric(str_replace_all(gsub("([0-9,]*)\\[.*", "\\1\\3", `Followers at the time of suspension`), ",", "")),
      start = dmy(Date),
      entity = `Individual/account`,
      entity_short = gsub(" \\(@.*\\)", "", entity)
   )

# histogram
ggplot(suspensions_tw) +
   geom_histogram(aes(floor_date(start, "year")), binwidth = 366) +
   xlab("") +
   scale_x_date(date_labels = "%Y", date_breaks = "1 year")
#
#
#
#| fig-width: 12
#| fig-height: 8
#| cap-location: margin
#| fig-cap: All Wikipedia-reported Twitter suspension, highlighting accounts with more than 1M followers (not all suspensions list the number of followers).

ggplot(
   suspensions_tw %>%
      subset(!is.na(start)) %>%
      mutate(
         entity = fct_reorder(paste(entity, start), start, .desc = TRUE),
         followers = ifelse(is.na(followers), 1, followers)
      ),
   aes(start, entity, label = entity_short)
) +
   geom_point(aes(size = followers), alpha = .4) +
   geom_text_repel(data = . %>% subset(followers > 1000000), hjust = 1, direction = "y", nudge_x = -300) +
   theme(axis.text.y = element_blank()) +
   scale_x_date(date_labels = "%Y", date_breaks = "1 year")

#### list the top 20 by followers
# suspensions_tw %>%
#     subset(!is.na(followers)) %>%
#     arrange(desc(followers)) %>%
#     head(20) %>%
#     select(`Individual/account`, Date, Duration, followers)

##### show dates that failed to parse:
# suspensions_tw %>%
#     subset(is.na(start)) %>%
#     select(Date, start)
#
#
#
#
# twitter_watch_raw= read_csv("https://github.com/travisbrown/twitter-watch/raw/main/data/suspensions.csv", col_names=FALSE)
# save(twitter_watch_raw, file='twitter_watch_raw')
load("twitter_watch_raw")

twitter_watch <- twitter_watch_raw %>%
   rename(
      timestamp = X1,
      reversal = X2,
      user_id = X3,
      created_at = X4,
      screen_name = X5,
      verified = X6,
      protected = X7,
      followers_count = X8,
      profile_image_url = X9,
      withheld_in_countries = X10
   ) %>%
   mutate(
      timestamp = as_datetime(timestamp),
      reversal = as_datetime(reversal),
      created_at = as_datetime(created_at)
   )
#
#
#
#
#| fig-cap: Observations by date of suspension
#| fig-height: 2
#| cap-location: margin
twitter_watch %>%
   mutate(yearmon = as.Date(timestamp)) %>%
   group_by(yearmon) %>%
   tally() %>%
   ggplot(aes(x = yearmon, y = n)) +
   geom_col() +
   scale_x_date(date_labels = "%Y-%m", date_breaks = "1 month") +
   scale_y_continuous(labels = scales::label_number_si()) +
   xlab("")
#
#
#
#| fig-cap: Observation by date of unsuspension
#| fig-height: 2
#| cap-location: margin
twitter_watch %>%
   mutate(yearmon = as.Date(reversal)) %>%
   group_by(yearmon) %>%
   tally() %>%
   ggplot(aes(x = yearmon, y = n)) +
   geom_col() +
   scale_x_date(date_labels = "%Y-%m", date_breaks = "1 month") +
   scale_y_continuous(labels = scales::label_number_si()) +
   xlab("")
#
#
#
#| fig-cap: Observation by date of account creation
#| fig-height: 2
#| cap-location: margin
twitter_watch %>%
   subset(created_at > as.Date("2006-01-01")) %>%
   mutate(yearmon = as.yearmon(created_at)) %>%
   group_by(yearmon) %>%
   tally() %>%
   ggplot(aes(x = yearmon, y = n)) +
   geom_col() +
   scale_y_continuous(labels = scales::label_number_si()) +
   xlab("")
#
#
#
#| fig-cap: Suspensions for accounts with >1M followers
#| fig-height: 4
#| cap-location: margin
ggplot(
   twitter_watch %>% subset(followers_count > 1e6) %>%
      mutate(
         rank = fct_reorder(paste(screen_name, timestamp), timestamp, .desc = TRUE),
         reversal = dplyr::if_else(is.na(reversal), Sys.Date(), as.Date(reversal))
      ),
   aes(as.Date(timestamp), rank, label = screen_name)
) +
   geom_point(aes(size = followers_count), alpha = .4, color = "darkred") +
   geom_point(data = . %>% subset(reversal < Sys.Date()), aes(size = followers_count, x = as.Date(reversal)), alpha = .4, color = "darkred") +
   geom_segment(aes(x = as.Date(timestamp), xend = as.Date(reversal), y = rank, yend = rank), color = "darkred") +
   geom_text_repel(data = . %>% subset(followers_count > 2e6), hjust = 1, direction = "y", nudge_x = -30) +
   theme(axis.text.y = element_blank(), legend.position = "none") +
   xlab("")
#
#
#
#
#
#
#| fig-cap: Observations by date of suspension
#| fig-height: 2
#| cap-location: margin

# tw_unsuspensions_raw <- read_csv("https://github.com/travisbrown/unsuspensions/raw/main/data/timestamps.csv", col_names = FALSE)
# save(tw_unsuspensions_raw, file='tw_unsuspensions_raw')
load("tw_unsuspensions_raw")

tw_unsuspensions <- tw_unsuspensions_raw %>%
   rename(
      twitter_id = X1,
      suspension = X2,
      reversal = X3
   ) %>%
   mutate(
      suspension = as_datetime(suspension),
      reversal = as_datetime(reversal)
   )

tw_unsuspensions %>%
   mutate(yearmon = as.Date(suspension)) %>%
   group_by(yearmon) %>%
   tally() %>%
   ggplot(aes(x = yearmon, y = n)) +
   geom_col() +
   scale_x_date(date_labels = "%Y-%m", date_breaks = "1 month") +
   scale_y_continuous(labels = scales::label_number_si()) +
   xlab("")
#
#
#
#| fig-cap: Observations by date of unsuspension
#| fig-height: 2
#| cap-location: margin
tw_unsuspensions %>%
   mutate(yearmon = as.Date(reversal)) %>%
   group_by(yearmon) %>%
   tally() %>%
   ggplot(aes(x = yearmon, y = n)) +
   geom_col() +
   scale_x_date(date_labels = "%Y-%m", date_breaks = "1 month") +
   scale_y_continuous(labels = scales::label_number_si()) +
   xlab("")
#
#
#
#
#
#
#
#| fig-height: 3
#| fig-cap: Total Accounts Suspended on Twitter by Reason, 2018H2-2021H2
## | column: margin
library(tidyverse)
transparency <- read_csv("/Users/tomcunningham/Downloads/Twitter-Transparency-Report-20-Jul-Dec-2021/Twitter_Transparency-Rules_Enforcement_Jul-Dec-2021.csv", skip = 12, n_max = 87)
names(transparency) <- c("start", "rule", "accounts_actioned", "accounts_suspended", "content_removed")

transparency <- transparency %>%
   mutate_if(is.character, ~ replace(., . == "(null)", 0)) %>%
   mutate(
      accounts_suspended = as.numeric(accounts_suspended),
      content_removed = as.numeric(content_removed)
   )

t <- transparency %>%
   group_by(rule) %>%
   mutate(total = sum(accounts_suspended)) %>%
   ungroup() %>%
   mutate(share = total / sum(accounts_suspended), rule = ifelse(share < .05, "other", rule)) %>%
   group_by(start, rule) %>%
   summarize(accounts_suspended = sum(accounts_suspended)) %>%
   mutate(rule = gsub("/", " / ", rule))
ggplot(t, aes(start, accounts_suspended, fill = rule)) +
   geom_bar(stat = "identity", width = 367 / 2, alpha = .8) +
   facet_wrap(rule ~ ., nrow = 1, labeller = labeller(rule = label_wrap_gen(10))) +
   # geom_text(aes(x=as.Date('2018-01-01'),y=0,label=rule),hjust=0,vjust=0)+
   scale_x_date(date_labels = "%Y-%m", date_breaks = "6 month") +
   scale_y_continuous(labels = scales::label_number_si()) +
   theme(
      strip.text.y.right = element_text(angle = 0, hjust = 0),
      axis.text.x = element_text(angle = 90, hjust = 1),
      # strip.background = element_blank(),
      # strip.text.x = element_blank(),
      axis.title.x = element_blank(),
      axis.title.y = element_blank(),
      legend.position = "none"
   )
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#| column: page
#| fig-width: 16
#| fig-height: 8

transparency_meta <- read_csv("/Users/tomcunningham/Downloads/CSER-2022_Q3.csv") %>%
   mutate(
      value_numeric = as.numeric(str_replace_all(str_replace_all(value, ",", ""), "%", "")),
      metric = str_replace(metric, "Lowerbound Prevalence", "Prevalence - Lower Bound"),
      metric = gsub("^Prevalence", "Prevalence - Upper Bound", metric), # coding this as upper bound for simplicity
      metric = gsub("Upperbound Prevalence", "Prevalence - Upper Bound", metric),
      metric = gsub("UBP", "Prevalence - Upper Bound", metric) # I assume UBP = upper bound prevalence
   )

ggplot(
   transparency_meta %>% subset( # !policy_area %in% c('Spam','Fake Accounts')
      metric %in% c("Content Actioned", "Prevalence - Upper Bound", "Proactive rate", "Prevalence")
   ),
   aes(period, value_numeric, color = app, group = app)
) +
   geom_point(alpha = 1) +
   geom_line() +
   scale_y_log10(labels = scales::label_number_si()) +
   scale_x_discrete(guide = guide_axis(check.overlap = TRUE)) +
   facet_grid(metric ~ policy_area, scales = "free_y", labeller = labeller(policy_area = label_wrap_gen(10))) +
   theme(
      strip.text.y.right = element_text(angle = 0, hjust = 0),
      axis.text.x = element_text(angle = 90, hjust = 1),
      axis.title.x = element_blank(),
      axis.title.y = element_blank(),
      legend.position = "bottom"
   ) +
   scale_colour_manual(values = platform_colors, name = "")

# ggplot(transparency_meta %>% subset(!policy_area %in% c('Spam','Fake Accounts')
#       & metric %in% c('Content Actioned','Upperbound Prevalence','Proactive rate','UBP','Prevalence')),
#    aes(period, value_numeric, color=policy_area, group=policy_area)) +
#     geom_point()+
#     geom_line()+
#     facet_wrap(.~app+metric, scales='free_y')+
#     scale_y_continuous(labels = scales::label_number_si())+
#     theme(
#       strip.text.y.right = element_text(angle = 0, hjust = 0),
#       axis.text.x = element_text(angle=90, hjust = 1),
#       axis.title.x=element_blank(),
#       axis.title.y=element_blank(),
#       legend.position = "bottom"
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#| column: page
#| fig-height: 13

ggplot(
   suspensions # %>%subset(platform %in% c("Twitter", "Facebook", "YouTube")),
   , aes(start, platform)
) +
   geom_segment(aes(
      x = trunc(start, "month"), xend = ceiling_date(end, "month"),
      y = platform, yend = platform, color = platform
   ), linewidth = 1.8) +
   facet_wrap(. ~ entity, labeller = label_wrap_gen(width = 10, multi_line = TRUE)) +
   theme(
      strip.text.y.right = element_blank(),
      #        panel.border = element_blank(),
      panel.border = element_rect(color = "black", fill = NA),
      axis.text.y = element_blank(),
      panel.grid.major.x = element_line(color = "grey"),
      # panel.grid.major.y = element_blank(),
      plot.background = element_rect(fill = "white"),
      panel.background = element_rect(fill = "white"),
      #        strip.text.x = element_blank(),
      strip.text.x = element_text(margin = margin(b = 0)),
      axis.title.x = element_blank(),
      axis.text.x = element_text(angle = 90, hjust = 1),
      axis.title.y = element_blank(),
      legend.position = "bottom"
   ) +
   scale_x_date(
      date_labels = "%Y", date_breaks = "1 year", # , limits = c(as.Date("2014-06-01"), ceiling_date(Sys.Date(), "month")),
      expand = c(0, 0)
   ) +
   scale_colour_manual(values = platform_colors)
#
#
#
#
#
#

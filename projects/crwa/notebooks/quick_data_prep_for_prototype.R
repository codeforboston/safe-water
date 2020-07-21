
# a quick script to prepare data in different format:

library(tidyverse)
library(rio)

samples_raw <- rio::import("../data/sampling_datasets/data_for_prototype.csv")

# --------------- SELECTION
# select only useful variables:
samples_select <- samples_raw %>% 
  select(Date_Collected, Component_Name, Site_Name, Town,
         Latitude_DD, Longitude_DD, Reporting_Result, Unit_Abbreviation) %>%
  mutate(Latitude_DD = as.numeric(Latitude_DD), #convert character values to numeric
         Longitude_DD = as.numeric(Longitude_DD),
         Reporting_Result = as.numeric(Reporting_Result))
# missing: Activity_Type_ID, to keep only "Sample-Routine" (and not "Quality Control Sample")


# --------------- FILTERING
# select only useful variables:
comps_to_keep <- c('Fecal coliform', 'Escherichia coli', 'Phosphorus', 'Chlorophyll a')
samples_filter <- samples_select %>% 
  filter(Component_Name %in% comps_to_keep) 


# --------------- CLEANING

# We transform the Date_Collected to date, so that can order by date, + we don't care about hours:
samples_filter <- samples_filter %>% mutate(Date_Collected = lubridate::as_date(Date_Collected))


# Some localization are NAs !
samples_filter %>%
  summarise_all(list(~sum(is.na(.))))
# for now, we just remove them:
samples_filter <- samples_filter %>% filter(!is.na(Latitude_DD), !is.na(Longitude_DD))
# ==> NEED TO HANDLE THIS BETTER IN THE FUTURE!


# Some sites are 'NAs' ! -> "NULL" or "Unnamed"
# table(samples_filter$Site_Name)
# for now we remove them:
samples_filter <- samples_filter %>% filter(!Site_Name %in% c("NULL", "Unnamed"))
# ==> NEED TO HANDLE THIS BETTER IN THE FUTURE!


# Issue with Phosporus: why umol/l and mg/l?
table(samples_filter$Unit_Abbreviation, samples_filter$Component_Name)
# ==> NEED TO HANDLE THIS IN THE FUTURE!
# there average is quite close though, maybe they are the same?
samples_filter %>% 
  filter(Component_Name == "Phosphorus") %>% 
  group_by(Unit_Abbreviation) %>% 
  summarise(mean_Result = mean(Reporting_Result))

# group E.coli and fecal coliform
samples_clean <- samples_filter %>%
  mutate(Component = case_when(
    Component_Name == "Fecal coliform" ~ "E.coli",
    Component_Name == "Escherichia coli" ~ "E.coli",
    Component_Name == "Phosphorus" ~ "Phosphorus",
    Component_Name == "Chlorophyll a" ~ "Chlorophyll a",
    TRUE ~ "ISSUE_UNKOWN_COMPONENT")
  ) %>% select(-Component_Name) # we stored the info in Component and can get rid of Component_Name


# adding the thresholds:
samples_clean <- samples_clean %>%
  mutate(Limit = case_when(
    Component == "E.coli" & Reporting_Result <+ 126 ~ "safe",
    Component == "E.coli" & Reporting_Result > 126 & Reporting_Result <= 630 ~ "no swimming or fishing",
    Component == "E.coli" & Reporting_Result > 630 ~ "no boating",
    TRUE ~ "Unknown Safety Limit")
  )


# --------------- FORMATTING

## !!! Careful, THIS IS REALLY UGLY, don't burn your eyes!

# we add a new variable to tell the type of result
# rational: we have 3 types: 
#   original == data as is, we will have all the points on the map -> "All Samples"
#   average == average over all sampling events, == one average per site
#   last_sample == only the last sampling event
# we create 3 df that we later bind together after to have data in long format
# we also create a wide df version

averages_by_site <- samples_clean %>% group_by(Site_Name, Component) %>% summarise(averages_by_site = mean(Reporting_Result))
info_samples_clean <- samples_clean %>% select(-Date_Collected, -Reporting_Result, -Limit, -Unit_Abbreviation)  %>% unique()
df_averages_by_site <- info_samples_clean %>% inner_join(averages_by_site, by = c("Site_Name", "Component")) %>% arrange(Site_Name)


last_sampling <- samples_clean %>% .$Date_Collected %>% max() %>% lubridate::ymd(.) # ! NO DISTINCTION OF COMPONENT YET!
last_month_samples <- samples_clean %>% filter(
  (lubridate::month(Date_Collected) == lubridate::month(last_sampling)) & (lubridate::year(Date_Collected) == lubridate::year(last_sampling))
)




samples_wide <- samples_clean %>% 
  left_join(averages_by_site) %>% 
  mutate(is_last_sampling = case_when(
    (lubridate::month(Date_Collected) == lubridate::month(last_sampling)) & (lubridate::year(Date_Collected) == lubridate::year(last_sampling)) ~ "Last Month",
    TRUE ~ "Not Last Month")
  )
  
rio::export(samples_wide, "../data/sampling_datasets/data_for_prototype_reshaped.csv")



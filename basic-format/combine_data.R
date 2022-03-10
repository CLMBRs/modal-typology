library(tidyverse)
library(yaml)
library(here)

all_modals <- data.frame()
all_observations <- data.frame()
all_meta <- data.frame()

for (language in list.dirs(recursive = FALSE, full.names = FALSE)) {
    # ignore hidden directories
    if (!(str_starts(language, "\\."))) {
        # 1. Get metadata
        metadata <- data.frame(
                yaml.load_file(here("basic-format", language, "metadata.yml"))
            ) %>%
            add_column(language = language) %>%
            relocate(language)
        all_meta <- bind_rows(all_meta, metadata)

        # 2. Get modal inventory
        # read raw CSV data
        observations <- read_csv(here("basic-format", language, "modals.csv")) %>%
            # add a column for which language this is
            add_column(language = language) %>%
            # and Glotto-code of language
            add_column(lang_ID = metadata$Glotto.code) %>%
            # move lang, expression to front of table
            relocate(lang_ID, language)
        # make can_express character,
        # for cases where every entry is 1/0 and gets treated as int
        observations$can_express <- as.character(observations$can_express)
        # concatenate all observations together
        all_observations <- bind_rows(all_observations, observations)

        # pivot data to wide format
        modals <- observations %>%
            # expression level data, with force, flavor pairs as columns
            pivot_wider(
                names_from = c(force, flavor),
                names_sep = ".",
                values_from = can_express,
                id_cols = c(lang_ID, language, force, flavor, expression)
            )
        # concatenate with existing data
        all_modals <- bind_rows(all_modals, modals)
    }
}

write_csv(all_observations, here("basic-format", "all_observations.csv"))
write_csv(all_modals, here("basic-format", "all_modals.csv"))
write_csv(all_meta, here("basic-format", "all_metadata.csv"))
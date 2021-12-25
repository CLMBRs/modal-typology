library(tidyverse)
library(yaml)

all_modals <- data.frame()
all_meta <- data.frame()

for (language in list.dirs(recursive = FALSE, full.names = FALSE)) {
    # ignore hidden directories
    if (!(str_starts(language, "\\."))) {
        # 1. Get modal inventory
        # read raw CSV data
        modals <- read_csv(paste(language, "/modals.csv", sep = ""))
        # make can_express character,
        # for cases where every entry is 1/0 and gets treated as int
        modals$can_express <- as.character(modals$can_express)
        # pivot data
        modals <- modals %>%
            # expression level data, with force, flavor pairs as columns
            pivot_wider(
                names_from = c(force, flavor),
                names_sep = ".",
                values_from = can_express,
                id_cols = c(force, flavor, expression)
            ) %>%
            # add a column for which language this is
            add_column(language = language) %>%
            # move lang, expression to front of table
            relocate(language, expression)
        # concatenate with existing data
        all_modals <- bind_rows(all_modals, modals)

        # 2. Get metadata
        metadata <- data.frame(
                yaml.load_file(paste(language, "/metadata.yml", sep = ""))
            ) %>%
            add_column(language = language) %>%
            relocate(language)
        all_meta <- bind_rows(all_meta, metadata)
    }
}

write_csv(all_modals, "all_modals.csv")
write_csv(all_meta, "all_metadata.csv")
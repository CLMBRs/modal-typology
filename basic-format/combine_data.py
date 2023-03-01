import os
import pandas as pd
import yaml

if __name__ == '__main__':
    all_meta = [] 
    all_observations = []
    for language in sorted(os.listdir()):
        if os.path.isdir(language):
            # get and append metadata
            with open(f"{language}/metadata.yml") as lang_file:
                metadata = yaml.load(lang_file, Loader=yaml.CLoader)
                metadata['Language'] = language
                all_meta.append(metadata)
            # get and append observations
            observations = pd.read_csv(f"{language}/modals.csv")
            observations["language"] = language
            observations["lang_ID"] = metadata["Glotto code"]
            all_observations.append(observations)
    #TODO: move 'Language' column to the "front"?
    pd.DataFrame(all_meta).to_csv("all_metadata.csv")
    pd.concat(all_observations).to_csv("all_observations.csv")
#!/bin/sh

cp basic-format/all_observations.csv cldf-format/raw
cp basic-format/all_metadata.csv cldf-format/raw
cp basic-format/forces.csv cldf-format/raw
cp basic-format/flavors.csv cldf-format/raw
cp basic-format/sources.bib cldf-format/raw
cp cldf-format/raw/sources.bib cldf-format/

cd cldf-format
cldfbench makecldf cldfbench_modals.py
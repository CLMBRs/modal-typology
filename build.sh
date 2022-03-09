#!/bin/sh

cp basic-format/all_observations.csv cldf-format/raw
cp basic-format/all_metadata.csv cldf-format/raw
cp basic-format/forces.csv cldf-format/raw
cp basic-format/flavors.csv cldf-format/raw
cp basic-format/ref.bib cldf-format/raw

cd cldf-format
cldfbench makecldf cldfbench_modals.py
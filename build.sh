#!/bin/sh

cd basic-format
python combine_data.py
cd ..

cp basic-format/all_observations.csv cldf-format/raw
cp basic-format/all_metadata.csv cldf-format/raw
cp basic-format/forces.csv cldf-format/raw
cp basic-format/flavors.csv cldf-format/raw
cp basic-format/sources.bib cldf-format/raw
cp cldf-format/raw/sources.bib cldf-format/cldf

cd cldf-format
cldfbench makecldf cldfbench_modaltypology.py
# A Database of Modal Typology

# Structure

Each language has a corresponding directory, with the following minimal structure:

language/  
|- modals.csv  
|- metadata.yml

`modals.csv` is a CSV file assumed to have the following four columns:
* expression
* force
* flavor
* can_express

Each row is one observation: `can_express` has values stating whether or not an `expression` (orthographically represented) is capable of expressing a particular combination of `force` and `flavor`.

`metadata.yml` is a YAML file containing basic data about the language, the references used to generate the data in `modals.csv` and the identity of the contributors.

# TODOs

* detailed README and contribution guide
    - make CONTRIBUTE.md
    - split README across (i) whole repo, (ii) basic-format, (iii) cldf-format
* move all existing data into this format
* improve force / flavor tables
    - add basic tables w/ descriptions in basic-format, and to contribution guide
    - update `cldfbench_modals.py` to reflect this
* GitHub actions for running `combine_data.R` and `build.sh` on commit?
# A Database of Modal Typology

# Structure

Each language has a corresponding directory, with the following minimal structure:

language
|- modals.csv
|- metadata.yml

`modals.csv` is a CSV file assumed to have the following four columns:
* expression
* force
* flavor
* can_express

Each row is one observation: `can_express` has values stating whether or not an expression is capable of expressing a particular combination of force and flavor.

# TODOs

* detailed README and contribution guide
* add metadata for languages (incl reference)
* script for writing big metadata table
* move existing data into this format

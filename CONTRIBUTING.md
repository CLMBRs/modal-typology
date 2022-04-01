

# Contributing

Contribution of modals in other languages can be made to `basic-format/` by following the process described below. The process provides a breif overview of the files that should be included in the language folder. For detailed description of the database schema please go over the paper

## Process

1. Fork the GitHub repository  and edit or create a new folder named after your language in `basic-format/`

2. Add the following files in the created directory

- `metadata.yml` : a YAML file contains information about the language and the source(s) from which the modals data was compiled. In particular:
	- Glotto code: this is an ID for the language from Glottlog (https://glottolog.org/glottolog/language)
	- Reference: a citation for the source
	- Reference_key: a BibTeX key to sources.bib
	- URL: a URL to find the reference
	- Reference_type: the type of reference
		-*At present, the values for this field that exist in our database are ‘paper_journal’ and ‘reference_grammar’. The value indicates whether the information comes from targeted semantics fieldwork (paper_journal) or from descriptive grammar (reference_grammar). The latter usually lacks negative data upon which some analyses may depend, and so those languages may need to be excluded.*
	- Complete_language: whether the reference purports to describe the complete modal system of the language or not.
		-*Many sources only provide data for some, but not all, modals. Such expression-level data is still very useful, but researchers may wish to exclude incomplete languages from analyses at the language level.*

- `modals.csv` : a comma-separated-value (CSV) file, containing the core data in a table where each row is in the format of
	- expression
	- force: a detailed description of flavors can be found in basic-format/force.csv
	- flavor: a detailed description of flavors can be found in basic-format/flavors.csv
	- can_express: 1 means the expression can express the force and flavor value, 0 means cannot, ? means judgement varies. 
	- notes: anything notable for this expression

- `readme.md` : a optional file to include extra notes


3. Edit basic-format/sources.bib with bibtex information of the source of your data. The key should be identical to the reference_key in `metadata.yml`

4. (Optional) run combine_data.R to generate updated all_modals.csv, all_metadata.csv and all_observations.csv

5. Submit a pull request to the main repository from your fork

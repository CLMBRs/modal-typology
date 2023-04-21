# A Database of Modal Typology

This is a database recording (at least) which force-flavor pairs various modal expressions across the world's languages can express.  It is designed to be both easy to use and to contribute to. For more details and motivation, please see the following paper:

Qingxia Guo, Nathaniel Imel, Shane Steinert-Threlkeld, "[A Database for Modal Semantic Typology](https://sigtyp.github.io/workshops/2022/sigtyp/papers/SIGTYP8.pdf)", _Proceedings of the 4th Workshop on Computational Typology and Multilingual NLP (SIGTYP 2022)_, pp 42-51.

# Structure

Each language has a corresponding directory, with the following minimal structure:

language/  
|- modals.csv  
|- metadata.yml

`modals.csv` is a CSV file assumed to have the following four columns:
* expression
* force
* flavor
* can_express: this field will have value in `[1,0,?]`
* polarity
* syntactically_negated: this field will have value in `[high,low,no]`
* full_form

Each row is one observation: `can_express` has values stating whether or not an `expression` (orthographically represented) is capable of expressing a particular combination of `force` and `flavor`.

`metadata.yml` is a YAML file containing basic data about the language, the references used to generate the data in `modals.csv` and the identity of the contributors.

# Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md)

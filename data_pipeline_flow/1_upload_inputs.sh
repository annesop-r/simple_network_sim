python -m data_pipeline_api.registry.upload_input <<HERE
responsible_person: mrow84
root: ../sample_input_files
path: human/compartment-transition/1/data.csv
data_product: input/human/compartment-transition
version: 0.1.0
components:
  - compartment-transition
HERE

python -m data_pipeline_api.registry.upload_input <<HERE
responsible_person: mrow84
root: ../sample_input_files
path: human/population/1/data.csv
data_product: input/human/population
version: 0.1.0
components:
  - population
HERE

python -m data_pipeline_api.registry.upload_input <<HERE
responsible_person: mrow84
root: ../sample_input_files
path: human/commutes/1/data.csv
data_product: input/human/commutes
version: 0.1.0
components:
  - commutes
HERE

python -m data_pipeline_api.registry.upload_input <<HERE
responsible_person: mrow84
root: ../sample_input_files
path: human/mixing-matrix/1/data.csv
data_product: input/human/mixing-matrix
version: 0.1.0
components:
  - mixing-matrix
HERE

python -m data_pipeline_api.registry.upload_input <<HERE
responsible_person: mrow84
root: ../sample_input_files
path: human/infectious-compartments/1/data.csv
data_product: input/human/infectious-compartments
version: 0.1.0
components:
  - infectious-compartments
HERE

python -m data_pipeline_api.registry.upload_input <<HERE
responsible_person: mrow84
root: ../sample_input_files
path: human/infection-probability/1/data.csv
data_product: input/human/infection-probability
version: 0.1.0
components:
  - infection-probability
HERE

python -m data_pipeline_api.registry.upload_input <<HERE
responsible_person: mrow84
root: ../sample_input_files
path: human/movement-multipliers/1/data.csv
data_product: input/human/movement-multipliers
version: 0.1.0
components:
  - movement-multipliers
HERE

python -m data_pipeline_api.registry.upload_input <<HERE
responsible_person: mrow84
root: ../sample_input_files
path: human/initial-infections/1/data.csv
data_product: input/human/initial-infections
version: 0.1.0
components:
  - initial-infections
HERE
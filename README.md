# Kaggle Competition, Digit Recognizer


## [Competition Details](DETAILS.md)

## First goal is to get a kaggle framework up and running.

## To get up and running, install docker, navigate to the root directory of this repository and run `docker-compose up`.

The reason why this is enough is because it will build the container on the fly, and after building it will automatically install according to `setup.py`.

### `requirements.in --> requirements.txt`

Do not modify `requirements.txt`, rather use `pip-compile` to add the meta-dependencies of `requirements.in`.

### To quickly bash into a live docker-container without any of the extra installations run `docker-compose run main bash`
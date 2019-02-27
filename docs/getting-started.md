# Getting started 

## Installing python and dependencies

The easiest way to install the Python dependencies is using Pipenv. 
Ensure that you have
[Pipenv installed](https://pipenv.readthedocs.io/en/latest/install/),
then, with the repo as your working directory, run:

```bash
pipenv install
```

To add a new Python dependency, run:

```bash
pipenv install antigravity  # Replace `antigravity` with desired package name
```

Be sure to commit `Pipfile` and `Pipfile.lock` to the repo.

### Running the notebooks

To run the notebooks, run:

```bash
pipenv run jupyter notebook jupyter_notebooks
```

## Installing R and dependencies

Install [RStudio](https://www.rstudio.com/) and install the following packages:

```R
install.packages(c("tidyverse", "noncensus",
                   "ggplot2", "choroplethr",
                   "choroplethrMaps", "lubridate"))
```

Make sure the symlink in the R directory points to the data directory.
You should unpack a copy of the scraped CSVs
(see [additional links](/additional-links)).

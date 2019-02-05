# Safe Water

This is a Code for Boston project that is trying to predict health-based drinking water violations using the Environmental Protection Agency's [Safe Drinking Water Information System](https://www.epa.gov/enviro/sdwis-model). 

We will explore other datasets from the EPA, including the [Toxic Release Inventory database](https://www.epa.gov/enviro/tri-search), the [Superfund Enterprise Management System](https://www.epa.gov/enviro/sems-search), the [Environmental Radiation Monitoring database](https://www.epa.gov/radnet), and the [Enforcement and Compliance History Outline](https://echo.epa.gov/). 

We are using Python for the analysis and are in the early stages.

Find us on our [Slack channel](https://cfb-public.slack.com) #water

## Getting started

The easiest way to install the Python dependencies is using Pipenv. Ensure that you have [Pipenv installed](https://pipenv.readthedocs.io/en/latest/install/), then, with the repo as your working directory, run:

```bash
pipenv install
```

To add a new Python dependency, run:

```bash
pipenv install antigravity  # Replace `antigravity` with desired package name
```

Be sure to commit `Pipfile` and `Pipfile.lock` to the repo.

## Running the notebooks

To run the notebooks, run:

```bash
pipenv run jupyter notebook jupyter_notebooks
```

## Running the scraper

To run the scraper, run:

```bash
pipenv run python -i swid-db-scraper.py
```

This will load the file and put you into a command prompt. From that prompt, run the following:

```python
pull_envirofacts_data()
```

**⚠️ Note:** The scraper can take _hours_ to run.

## data aggregation TODO:
- Log files should note tables which where not collected at all for one reason or another so they can be explored further
- there should be one log file for all tables OR one log file for each table, the current state is sub optimal
- we will have alot of tables now, can we make sure that the raw data is somehow being grouped into useful subsets
- how can we join and aggreate data so that we dont always have to navigate  
- parallel-ize scripts so that general users could potentially pull scritps
- additional print out info to better understand were we are in the scripts

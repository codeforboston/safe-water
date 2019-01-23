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

To run the notebooks, run:

```bash
pipenv run jupyter notebook jupyter_notebooks
```

To add a new Python dependency, run:

```bash
pipenv install antigravity  # Replace `antigravity` with desired package name
```

Be sure to commit `Pipfile` and `Pipfile.lock` to the repo.


## data aggregation TODO:
- Log files should note tables which where not collected at all for one reason or another so they can be explored further
- there should be one log file for all tables OR one log file for each table, the current state is sub optimal
- we will have alot of tables now, can we make sure that the raw data is somehow being grouped into useful subsets
- how can we join and aggreate data so that we dont always have to navigate  
- parallel-ize scripts so that general users could potentially pull scritps
- additional print out info to better understand were we are in the scripts

## running scripts on your machine
(instructions only tested on solus linux but should hold on other os')
in the command line cd to the safe water directory
run the command 'python3.6 -i swid-db-scraper.py'
this will load the file and put you into a command prompt
now run the following command: 'pull_envirofacts_data()'

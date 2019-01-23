# Safe Water
This is a Code for Boston project that is trying to predict health-based drinking water violations using the Environmental Protection Agency's [Safe Drinking Water Information System](https://www.epa.gov/enviro/sdwis-model).

We will explore other datasets from the EPA, including the [Toxic Release Inventory database](https://www.epa.gov/enviro/tri-search), the [Superfund Enterprise Management System](https://www.epa.gov/enviro/sems-search), the [Environmental Radiation Monitoring database](https://www.epa.gov/radnet), and the [Enforcement and Compliance History Outline](https://echo.epa.gov/). 

We are using Python for the analysis and are in the early stages. 

## data aggregation:
The web-scraper functions as a command-line program with a flag based interface. The --help and -h flag is supported to get futher information however flags covered are listed here
* -p takes a number of process that the script can use to process all of the different data sets
* -l takes a pathname to a logfile which the script will write too
* -rs takes a number which maps to the number of records to be included in any one request
* -mq takes a number which maps to the number of times a url should be attemped before giving up

## Webscraping TODO
* test parallel implementation of web scraper
* adjust webscraper to reference file name
* update list of databases we want beyond SWDIS databases


## running scripts on your machine
(instructions only tested on solus linux but should hold on other os')
in the command line cd to the safe water directory
run the command 'python3.6 -i swid-db-scraper.py'
this will load the file and put you into a command prompt
now run the following command: 'pull_envirofacts_data()'

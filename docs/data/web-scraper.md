## Running the scraper

To run the scraper, run:

```bash
pipenv run python -i swid-db-scraper.py
```

This will load the file and put you into a command prompt. From that prompt, run the following:

```python
pull_envirofacts_data()
```

!!! warning
    The scraper can take _hours_ to run.

## Data aggregation

The web-scraper functions as a command-line program with a flag based interface. The --help and -h flag is supported to get futher information however flags covered are listed here
* -p takes a number of process that the script can use to process all of the different data sets
* -l takes a pathname to a logfile which the script will write too
* -rs takes a number which maps to the number of records to be included in any one request
* -mq takes a number which maps to the number of times a url should be attemped before giving up

## Webscraping TODO

* test parallel implementation of web scraper
* adjust webscraper to reference file name
* update list of databases we want beyond SWDIS databases
* test that data read in
* how can we join and aggreate data so that we dont always have to navigate
* additional print out info to better understand were we are in the scripts
* additional error handlings

## Running scripts on your machine

(instructions only tested on solus linux but should hold on other os')

* in the command line cd to the safe water directory
* run the command 'python3.6 -i swid-db-scraper.py'
* this will load the file and put you into a command prompt
* now run the following command: 'pull_envirofacts_data()'

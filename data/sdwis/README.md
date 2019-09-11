# Safe Drinking Water Information System (SDWIS)

## Summary

This is a database of clean water violations collected by the EPA in compliance with the Safe Drinking Water Act.

## Collection Date

2019-02-26

## Source

This data was collected from running a file named `code/python/scraper/scraper.py`, which scrapes the EPA's API for this data set.

## Description

The SDWIS data contains the following tables, each contained in CSV files:

- __ENFORCEMENT\_ACTION__: Documents actions taken against a Public Water System (PWS), laboratory, or operator.
- __GEOGRAPHIC\_AREA__: Information on political units established by geographic boundaries, such as state, town, or county served by a Water System.
- __LCR\_SAMPLE\_RESULT__: 90th percentile sample summary results data for lead or copper. 
- __LCR\_SAMPLE__: 90th percentile sample summaries data for lead or copper.
- __SERVICE\_AREA__: A service area defines the sensitive populations that receive water from the water system. 
- __TREATMENT__: Treatment objectives and process for treating water from a water system facility.
- __WATER\_SYSTEM__: Inventory information on public water systems. 
- __WATER\_SYSTEM\_FACILITY__: Inventory information on public water system facilities.
- __VIOLATION__: Documents a breach of a requirement. Violations are detected by assessment of sample results or reviews (including on site visits).
- __VIOLATION\_ENF\_ACTION__: Association between a violation and an enforcement action.

Additionally, there are two more files, `contaminant-codes.csv` and `contaminant-group-codes.csv`, which describe what contaminant codes mean.

How these files relate is described [here](https://www.epa.gov/enviro/sdwis-model) on the EPA's website.

There are additional notes on this data in the Background file in the documentation.

## Use

This database is our primary source for safe drinking water violations.


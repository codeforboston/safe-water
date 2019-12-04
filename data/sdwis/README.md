# Safe Drinking Water Information System (SDWIS)

## Summary

This is a database of clean water violations collected by the EPA in compliance with the Safe Drinking Water Act.

## Collection Date

2019-02-26

## Source

This data was collected from running a file named `code/python/scraper/scraper.py`, which scrapes the EPA's API for this data set.

## Description

The SDWIS data contains the following tables, each contained in CSV files. Below is a list of those files and some fields that we identified as being useful.

#### __ENFORCEMENT\_ACTION__.csv

Documents actions taken against a Public Water System (PWS), laboratory, or operator.
- pwsid
- enforcement_id
- originator_code
- enforcement_date
- enforcement_action_type_code
- enforcement_comment_text

#### __GEOGRAPHIC\_AREA__
Information on political units established by geographic boundaries, such as state, town, or county served by a Water
 System
- geo_id
- pwsid
- tribal code
- state_served
- ansi_entity_code
- zip_code_served
- city_served
- area_type_code
- county_served


#### LCR\_SAMPLE\_RESULT.csv

90th percentile sample summary results data for lead or copper.

- sar_id
- pwsid
- sample_id
- contaminant_code
- result_sign_code
- sample_measure
- unit_of_measure

#### LCR\_SAMPLE.csv

90th percentile sample summaries data for lead or copper.

- pwsid
- sample_id
- sampling_start_date
- sampling_end_date

#### SERVICE\_AREA.csv

A service area defines the sensitive populations that receive water from the water system. 

- pwsid
- service_area_type_code
- is_primary_service_area_code

#### TREATMENT.csv

Treatment objectives and process for treating water from a water system facility.

- pwsid
- facility_id
- treatment_id
- comments_text
- treatment_objective_code
- treatment_process_code

#### WATER\_SYSTEM.csv

Inventory information on public water systems.

- pswid
- pws_activity_code
- population_served_count
- zip_code
- gw_sw_code
- city_name
- primacy_agency_code
- pws_type_code
- service_connections_count
- counties_served
- cities_served
- epa_region

#### WATER\_SYSTEM\_FACILITY

Inventory information on public water system facilities.

- pwsid
- facility_id
- facility_name
- facility_activity_code
- facility_type_code
- is_source_ind
- is_source_treated_ind

#### VIOLATION.csv

Documents a breach of a requirement. Violations are detected by assessment of sample results or reviews (including on site visits).

- pwsid
- violation_id
- facility_id
- violation_code
- violation_category_code
- is_health_based_ind
- contaminant_code
- compliance_status_code
- viol_measure
- unit_of_measure
- state_mcl
- compl_per_begin_date
- rtc_enforcement_id
- rtc_date
- sample_result_id
- corrective_action_id
- rule_code
- rule_group_code

#### VIOLATION\_ENF\_ACTION.csv

Association between a violation and an enforcement action.

- enforcement_id
- pwsid
- violation_id

Additionally, there are two more files, `contaminant-codes.csv` and `contaminant-group-codes.csv`, which describe what contaminant codes mean.

How these files relate is described [here](https://www.epa.gov/enviro/sdwis-model) on the EPA's website.

There are additional notes on this data in the Background file in the documentation.

## Use

This database is our primary source for safe drinking water violations.

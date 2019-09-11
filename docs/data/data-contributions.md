# Data Contributions

## Overview

Contributing data is an especially valuable way to contribute to this project.

Useful data for this project generally falls into two categories:

- __Features.__ Otherwise known as explanatory variables, predictors, or independent varaibles. These are data points that go into the **X** matrix parameter used to estimate violations. Features can be almost any data: as long as you believe the data may help predict violations, and it can be merged to water samples, then it can be a feature.
- __Water samples.__ These are the observations or data points that we fit the data onto. SDWIS is the main source of water samples, although there are other sources of interest such as water samples from private wells.

## Steps for Contributing Features

1. **Find a feature.** There are a few ways you can do this: (a.) Pick a feature from some documents on our Google Drive. (b.) Discuss what you think might be useful with others. (c.) Do some research.
2. **Collect and document the data.** The data collection should be reproducible. You should document this data in the ``Data contributions`` folder on the Google Drive. Ideally, you can record the collection of this data in whatever ``.py`` file or Jupyter notebook you use to also clean the data. (I.e. the file downloads the data and makes the whole process automated. If you're struggling with this, that's fine, just add a note in Python file on how to download the data.) **Please see the section below titled _Data Documentation_ for more information on how to document data that you have collected.**
3. **Clean the data.** Cleaning data is a broad and amorphous task, but the goal is to transform the data into something that can be used seamlessly with the rest of the data. This means transforming types (e.g. strings to floats), removing unnecessary columns, fixing bugs in the import process, addressing missing values, testing that calculated fields were calculated correctly, checking that things generally make sense with cross-tabulations. In some cases, data may be seemingly unusable because it is in a PDF file, but there are ways to import this data with a little bit of elbow grease.
4. **Merge the data.** Once you think your feature data is cleaned, try merging it onto water samples. Generally, the data we are working with will be merged on state, city, zip code, or latitude-longitude. Temporal data can also merge to both geography and time.
5. **Test the data, and record any issues.** Make sure the merge makes sense on an intuitive level. Did only 90% of the values merge, and not sure how to fix the rest? Did you merge some geospatial data to their nearest neighbors in the SDWIS data, but found out that some of the SDWIS data doesn't have nearest neighbors for hundreds of miles so you think this might be a gap? Keep notes of these things in your Python file. **You don't need to fix issues like this by yourself;** that's why we are working in a team. 😃 Do your best to document anything you see for either your future self or for others on the team to help fix.

## Data Documentation

In addition to the above steps for contributions, data contributions should be documented. Without documentation and the ability to replicate the data collection process, we cannot safely and reliably utilize your contributions.

The documentation file should have the following:

- **Summary:** Brief, 1-2 sentence description of your data near the top of the document.
- **Collected date:** The date(s) you collected the data. (In ISO 8601 date format, i.e. 2019-09-15)
- **Source:** Where you found this data. This should contain enough information for someone to be able to reasonably replicate the process if they want to. Note here which file you used to process the data, if you did process it.
- **Description:** Details on what this data contains, e.g. point to the columns you believe will be useful, and/or describe what each row represents.
- **Use:** Brief explanation of why you believe this data will be useful. It doesn't have to be long, a couple sentences will often suffice, it just enough so that people understand how they can make use of it.
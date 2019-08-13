# Contributing

We appreciate that you want to contribute to the Safe Drinking Water Project! There are various ways to contribute to the project, outlined in this document.

If you want to contribute, check out our [Trello project board](https://trello.com/b/qP7oYyWn/safe-water) to see what we need. If you have some ideas on what to contribute not covered the Trello board, we'd love to hear your ideas on our Slack and on Tuesday nights.

## Code Contributions

### Code Contributions Overview
Our project follows a standard Git workflow. If this is your first time working on a collaborative project with Git, check out this handy [First Contributions guide](https://github.com/firstcontributions/first-contributions). Additionally, the [Getting Started guide](getting-started.md) in this project's `/docs` folder outlines steps 1-4.

The basic outline for making contributions is:

1. Fork the project. (https://github.com/codeforboston/safe-water/fork)
2. Clone your fork. (`git clone https://github.com/<YOUR-USERNAME>/safe-water.git`)
3. Add a remote. (`git remote add upstream
https://github.com/codeforboston/safe-water.git`)
4. Checkout the master branch. (`git checkout master`)
5. Make your changes! 😃
6. Add the relative path(s) of the document(s) you added/changed. (`git add <MY/DOC/PATH/HERE>`)
6. Commit those changes. (`git commit -m "<DESCRIBE WHAT YOU DID>"`)
7. On your forked repo, submit a Pull Request to the Code for Boston's `master` branch.
8. Ask someone on the Slack channel to review your Pull Request.

We usually merge branches on Tuesday nights at the Code for Boston meetup.

All code goes into the `code/` subdirectory, into the language-specific directories.

### Modeling and Exploratory Contributions

Contributions to data modeling and exploratory data analysis are mainly being performed in Jupyter notebooks, located in the `code/python/notebooks/`. If you are working in R, you can add your contributions to `code/R/`.

If you want to contribute some analysis not covered on the Trello board, you may find it helpful to look through some recent notebooks to get a good idea of what work has already been done.

When providing code contributions for analyses, code should be documented and replicable. Notebooks should have easy instructions to reproduce the steps performed.

### Data Collection and Cleaning Contributions

Contributing data is an especially valuable way to contribute to this project.

Useful data for this project generally falls into two categories:

- __Features.__ Otherwise known as explanatory variables, predictors, or independent varaibles. These are data points that go into the **X** matrix parameter used to estimate violations. Features can be almost any data: as long as you believe the data may help predict violations, and it can be merged to water samples, then it can be a feature.
- __Water samples.__ These are the observations or data points that we fit the data onto. SDWIS is the main source of water samples, although there are other sources of interest such as water samples from private wells.

Here are the steps that we suggest you take to contribute features:

1. **Find a feature.** There are a few ways you can do this:
  a. Pick a feature from some documents on our Google Drive.
  b. Discuss what you think might be useful with others.
  c. Do some research.
2. **Collect the data.** The data collection should be reproducible. You should document this data somewhere on the Google Drive in a place you think is appropriate. Ideally, you can record the collection of this data in whatever ``.py`` file or Jupyter notebook you use to also clean the data. (I.e. the file downloads the data and makes the whole process automated. If you're struggling with this, that's fine, just add a note in Python file on how to download the data.)
3. **Clean the data.** Cleaning data is a broad and amorphous task, but the goal is to transform the data into something that can be used seamlessly with the rest of the data. This means transforming types (e.g. strings to floats), removing unnecessary columns, fixing bugs in the import process, addressing missing values, testing that calculated fields were calculated correctly, checking that things generally make sense with cross-tabulations. In some cases, data may be seemingly unusable because it is in a PDF file, but there are ways to import this data with a little bit of elbow grease.
4. **Merge the data.** Once you think your feature data is cleaned, try merging it onto water samples. Generally, the data we are working with will be merged on state, city, zip code, or latitude-longitude. Temporal data can also merge to both geography and time.
5. **Test the data, and record any issues.** Make sure the merge makes sense on an intuitive level. Did only 90% of the values merge, and not sure how to fix the rest? Did you merge some geospatial data to their nearest neighbors in the SDWIS data, but found out that some of the SDWIS data doesn't have nearest neighbors for hundreds of miles so you think this might be a gap? Keep notes of these things in your Python file. **You don't need to fix issues like this by yourself;** that's why we are working in a team. 😃 Do your best to document anything you see for either your future self or for others on the team to help fix.

## Research and Documentation Contributions

Our project is more than just what you see in the `code/` folder. Research and documentation are incredibly important parts of the process. Without good research, we'd have no idea what to analyze, what data should be used in the models, and what our models should even look like. Without good documentation, nobody can follow what's going on.

Research is stored on our [Google Drive](https://drive.google.com/drive/folders/1FbQE9_NP664lkz4d-Xu4omijLl-HNklz) and discussed in the Slack as well. Some of this research may be summarized in the Docs as well.
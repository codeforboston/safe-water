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

At the moment, our code to collect large data is contained in `code/python/scraper`; a lot of smaller data collection tasks are located across various notebooks in `code/python/notebook`.

## Research and Documentation Contributions

Our project is more than just what you see in the `code/` folder. Research and documentation are incredibly important parts of the process. Without good research, we'd have no idea what to analyze, what data should be used in the models, and what our models should even look like. Without good documentation, nobody can follow what's going on.

Research is stored on our [Google Drive](https://drive.google.com/drive/folders/1FbQE9_NP664lkz4d-Xu4omijLl-HNklz) and discussed in the Slack as well. Some of this research may be summarized in the Docs as well.
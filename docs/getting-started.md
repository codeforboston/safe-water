# Getting Started

The Safe Water Project is currently being developed in Python. Some project contributors have utilized MySQL to import data into pandas in their Jupyter notebooks, and historically we have had contributions done in R.

In addition to technology requirements, there are some data requirements. If you already have all the technology requirements and know how to fork a repo, you can skip down to the __Data__ section.

## Technology

#### Python

Download the latest version of Python [here](https://www.python.org/downloads/). Alternatively, you may be interested in downloading [Anaconda](https://www.anaconda.com/distribution/), which is a distribution of Python that comes with tons of data science tools pre-installed. You can read more about different Python distributions and their pros and cons [here](https://www.infoworld.com/article/3267976/anaconda-cpython-pypy-and-more-know-your-python-distributions.html). If you need additional help getting started in Python, check out [this guide](https://wiki.python.org/moin/BeginnersGuide).

#### Git and Github

Download Git [here](https://git-scm.com/downloads). If you're new to GitHub, after you create an account, go through [GitHub's Hello World tutorial](https://guides.github.com/activities/hello-world/). After that, you will need to learn how to fork the safe-water repo; you can learn how to do that by following GitHub's [Fork a repo](https://help.github.com/articles/fork-a-repo/) tutorial.

#### MySQL Server

MySQL Server is not a prerequisite for making contributions to this project, but it will be easier to run many of the contributions by others in this project if you have it installed. You can download it [here](https://dev.mysql.com/downloads/mysql/).

#### R and Dependencies

R is not a prerequisite for making contributions to this project, although some users in the past have used R, and we do not discourage volunteers from making contributions in R if they are more comfortable working in R. You can download R [here](https://cran.r-project.org/), and RStudio (an IDE for R) [here](https://www.rstudio.com/products/rstudio/download/).

## Forking the Project

1. On GitHub, navigate to the [repository](https://github.com/codeforboston/safe-water/). In the top-right corner of the page, click Fork.

2. On GitHub, navigate to your fork of the safe-water repository. In the Clone with HTTPs section, click to copy the clone URL for the repository.

3. Clone your fork. Navigate to a folder you would like to place this project, then type:

```bash
git clone
https://github.com/YOUR-USERNAME/safe-water.git
cd safe-water
```

4. Add the safe-water repository as a remote to your fork:

```bash
git remote add upstream
https://github.com/codeforboston/safe-water.git
```

4. Checkout the master branch:

```bash
git checkout master
```

## Dependencies

#### Python Dependencies

The easiest way to install the Python dependencies is using Pipenv. Ensure that you have [Pipenv installed](https://pipenv.readthedocs.io/en/latest/install/), then, with the repo as your working directory, run:

```bash
pipenv install
```

To add a new Python dependency, run:

```bash
pipenv install antigravity  # Replace `antigravity` with desired package name
```

Be sure to commit `Pipfile` and `Pipfile.lock` to the repo.

#### R Dependencies

Install the following packages:

```R
install.packages(c("tidyverse", "noncensus",
                   "ggplot2", "choroplethr",
                   "choroplethrMaps", "lubridate"))
```

Make sure the `symlink` in the R directory points to the data directory.

## Data

In order to run most of the Jupyter notebooks in this project, you will need to download the SDWIS data and place it into the `data/` folder. (We do not have enough space in our Github repository to store this data). You can find this data pinned in our Slack channel #water in a file called `SDWIS.zip`. Extract these csv files into `data/sdwis`.

Alternatively, you can run the scraper in `code/python/scraper` to obtain this information, although this would take some time to run.
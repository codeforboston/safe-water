# Contributing

We follow a basic git worklfow.
Some command line instructions are provided to help.

## Github repository

1. Fork our github repository at [codeforboston/safe-water](http://github.com/codeforboston/safe-water).

2. Clone your local repository.
    ```
    git clone git@github.com:<your-github-username>/safe-water.git
    ```
   Don't forget to replace `your-github-username`

3. Create a new branch related to the feature you are working on.
    ```
    git checkout -b add-new-source-data
    ```
    And replace `add-new-source-data` with your branch name.

4. Work on on your brand new branch and commit your features on this branch.
    ```bash
    # Add files
    git add myFile
    
    # Commit with a short description
    git commit -m "describe what I've done"
    ```
    
5. Push your changes on your remote branch.
    ```bash
    # On your new branch 
    git push origin 
    ```
    
6. Then, create a pull request from your branch on your own fork and target code for boston Safe water `master` branch and ask on the channel for people to review it.


We usually merge branches on tuesdays at the Hack Night.

All code goes into the `code/` subdirectory, into the language-specific directories.

All documentation is written in [mkdocs markdown](https://www.mkdocs.org) 
using the [mkdocs material](https://squidfunk.github.io/mkdocs-material/)
theme. Contribute to it by expanding and writing new files in the `docs/` 
directory.

### Python notebooks

All notebooks currently go into `code/python/notebooks`.
Try to use local links inside the repository to refer to data,
and try to give easy instructions to reproduce your steps.


# Welcome to {{cookiecutter.project_name}}!

Add your project description here


### Project structure

```
.
├── datasets                  <- Module for paths. In sources write:   from datasets import path_needed
│   ├── dataset_paths.py      <- Paths to datasets are stored as constants here. This file is excluded from source control
│   └── __init__.py           <- from .dataset_paths import <list your available paths> This file is under source control
├── docker_containers
├── .dockerignore
├── extra                     <- extra helper utilities that are not project-specific, ex. cookiecutter template updater
│   └── update_cookiecutter_template.sh <- run this script to merge recent changes in cookiecutter template into your project
├── .github
│   └── workflows
│       └── status.yml
├── .gitattributes
├── .gitignore
├── notebooks                 <- Development notebooks
├── pylintrc
├── readme.md                 <- The top-level README for developers using this project.
├── overview                  <- Notebooks with project overview
├── requirements.txt
├── Library submodule         <- SeismicPro, SeismiQB or PetroFlow as a git submodule
├── src                       <- Project-specific models and utilities
└── tests
```

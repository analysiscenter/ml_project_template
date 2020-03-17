# TaskCookieCutter
cookiecutter template for DS projects

Inspired by [this repo](https://github.com/drivendata/cookiecutter-data-science)

### Requirements to use the cookiecutter template:
 - Python 2.7 or 3.5
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with pip by or conda depending on how you manage your Python packages:

``` bash
$ pip install cookiecutter
```

or

``` bash
$ conda config --add channels conda-forge
$ conda install cookiecutter
```


### To start a new project, run:
```
cookiecutter https://github.com/analysiscenter/TaskCookieCutter
```

GitHub repositories should be created manually, but automatic GitHub repository creation can be added in future


### The resulting directory structure

The directory structure of your new project looks like this:

```
.
├── dataset_paths             <- Keep your datasets here
├── docker_containers
│   └── readme.md
├── extra                     <- extra helper utilities that are not project-specific, ex. cookiecutter template updater
│   ├── update_cookiecutter_template.sh <- run this script to merge recent changes in cookiecutter template into your project
│   └── .cookiecutter.json
├── .dockerignore
├── .github
│   └── workflows
│       └── status.yml
├── .gitattributes
├── .gitignore
├── notebooks                 <- Development notebooks
│   └── readme.md
├── pylintrc
├── readme.md                 <- The top-level README for developers using this project.
├── reports                   <- Notebooks with final reports
│   └── readme.md
├── requirements.txt
├── Library submodule         <- SeismicPro, SeismiQB or PetroFlow as a git submodule
├── src                       <- Project-specific models and utilities
│   ├── __init__.py
│   └── readme.md
└── tests
    └── readme.md
```

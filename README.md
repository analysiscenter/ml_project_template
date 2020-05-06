# TaskCookieCutter
cookiecutter template for DS projects

Inspired by [this repo](https://github.com/drivendata/cookiecutter-data-science)

### Requirements to use the cookiecutter template:
 - Python >= 3.5
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
├── Library submodule         <- SeismicPro, SeismiQB or PetroFlow as a git submodule
├── datasets                  <- Keep your datasets here
├── docker_containers
├── .dockerignore
├── extra                     <- extra helper utilities that are not project-specific, ex. cookiecutter template updater
│   ├── .cookiecutter.json
│   ├── src
│   └── update_cookiecutter_template.sh   <- run this script to merge recent changes in cookiecutter template into your project
├── .git
├── .gitattributes
├── .github
│   └── workflows
│       └── status.yml
├── .gitignore
├── notebooks                 <- Development notebooks
├── overview                  <- Notebooks with overview of main results
├── pylintrc
├── readme.md                 <- The top-level README for developers using this project.
├── requirements.txt
├── src                       <- Project-specific models and utilities
└── tests

```

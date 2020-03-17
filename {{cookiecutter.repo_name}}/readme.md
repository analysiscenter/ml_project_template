# Welcome to {{cookiecutter.project_name}}!

Add your project description here


### Project structure

```
.
├── datasets                  <- Keep your datasets here
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

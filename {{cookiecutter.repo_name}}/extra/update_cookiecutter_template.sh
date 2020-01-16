#!/usr/bin/env bash
BASEDIR=$(dirname "$0")
echo "$BASEDIR"
python $BASEDIR/src/cupper.py $BASEDIR/.cookiecutter.json template
git merge template

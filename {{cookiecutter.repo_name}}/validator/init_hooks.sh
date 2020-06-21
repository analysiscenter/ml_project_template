#!/bin/sh

git config core.hooksPath .githooks

chmod +x .githooks/prepare-commit-msg
chmod +x .githooks/pre-commit
chmod +x .githooks/post-commit
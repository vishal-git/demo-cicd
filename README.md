# Demo Makefile and github actions

This repository shows some examples of how to use a `Makefile` to run tests, linter, and bandit on your code.

Please note that one of the test fails; this is on purpose. Also, the linter will display some issues when you run it.

To run, clone the repository and run `make test`, `make linter`, or `make bandit` from the root folder of the repository.

All three steps (test, lint, and bandit) are also included as github actions in the `.github/workflows/image_clustering.yml` file, which run on _github push_.

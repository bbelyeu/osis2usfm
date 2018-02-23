# osis2usfm

[![Build Status](https://travis-ci.org/bbelyeu/osis2usfm.svg?branch=master)](https://travis-ci.org/bbelyeu/osis2usfm)
[![Coverage Status](https://coveralls.io/repos/github/bbelyeu/osis2usfm/badge.svg?branch=master)](https://coveralls.io/github/bbelyeu/osis2usfm?branch=master)

## Requirements

This project requires Python 3 (tested with 3.3-3.6)

## Installation

To install it, simply run

    pip install osis2usfm

## Usage

Import it and wrap app

    from osis2usfm import convert

    osis = ['Gen.1.1', '2Pet.1.1', 'John.1.1']
    usfms = convert(osis)
    print(usfms)
    >>> ['GEN.1.1', '2PE.1.1', 'JHN.1.1']

## Development

This project was written and tested with Python 3. Our builds currently support Python 3.3 to 3.6.

The easiest way to install Python 3 on a mac is via Homebrew(https://brew.sh/).

Once Homebrew is installed, you can use the following command if you haven't previously installed
python3.
``` bash
brew install python3
```
otherwise run
``` bash
brew upgrade python3
```
to make sure you have an up to date version.

This project uses [pipenv](https://docs.pipenv.org) for dependency management. Install pipenv
``` bash
pip3 install pipenv
```
Or you can install it with Homebrew.
```bash
brew install pipenv
```

Setup the project env
``` base
pipenv install --three --dev
```

Create a .env file using this sample
``` bash
export PYTHONPATH=`pwd`
```

Now load virtualenv and any .env file
```bash
pipenv shell
```

### Running tests

``` bash
./linters.sh && coverage run setup.py test
```

### Before committing any code

We have a pre-commit hook each dev needs to setup.
You can symlink it to run before each commit by changing directory to the repo and running

``` bash
cd .git/hooks
ln -s ../../pre-commit pre-commit
```

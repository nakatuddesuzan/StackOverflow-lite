[![Build Status](https://travis-ci.org/nakatuddesuzan/StackOverflow-lite.svg?branch=challenge-two)](https://travis-ci.org/nakatuddesuzan/StackOverflow-lite)
[![Coverage Status](https://coveralls.io/repos/github/nakatuddesuzan/StackOverflow-lite/badge.svg?branch=challenge-two)](https://coveralls.io/github/nakatuddesuzan/StackOverflow-lite?branch=challenge-two)
[![Maintainability](https://api.codeclimate.com/v1/badges/25f454357f5fbc72f92f/maintainability)](https://codeclimate.com/github/nakatuddesuzan/StackOverflow-lite/maintainability)

# StackOverflow-lite
StackOverflow-lite is a platform where people can ask questions and provide answers.

- This branch contains API endpoints for the above application

## Built-with
- `Python3.6` - Programming language that lets you work more quickly
- `Flask` - Python based web framework
- `Virtualenv` - A tool to create isolated virtual environment

## Running the tests
To run tests run this command below in your terminal

```
nosetests -v --with-coverage
```

## Installation
**Clone this _Repository_**
```
$ https://github.com/nakatuddesuzan/StackOverflow-lite.gite
$ cd StackOverflow-lite
```
**Create virtual environment and install it**
```
$ virtualenv --python=python3 venv
$ source /venv/bin/activate
```
**Install all the necessary _dependencies_ by**
```
$ pip install -r requirements.txt
```
**Run _app_ by**
```
$ Python run.py
$ Run the server At the terminal or console type
```
## Versioning
```
This API is versioned using url versioning starting, with the letter 'v'
This is version one"v1" of the API
```
## End Points
|           End Point                      |            Functionality                   |
|   -------------------------------------- | -----------------------------------------  |
|     POST   api/v1/users/signup           |             Registers a new user           |
|     POST api/v1/question/user_id         |             Post User Questions            |
|     GET  api/v1/question/user_id/qtn_id  |             Get one user Question          |
|     GET  api/v1/question/user_id         |             Get one user Question          |
|     PUT api/v1/question/user_id/qtn_id   |             Edit user Question             |
|    DELETE api/v1/question/user_id/qtn_id |             Delete user Question           |

## Contributors
- [Sue](https://github.com/nakatuddesuzan)

## Acknowledgements
- [Sue](https://github.com/nakatuddesuzan)

> *If you don't make it through the first time call it v1*

> *Don't stop because you are tired, Stop because you are done*

> *Learning is a continous process*

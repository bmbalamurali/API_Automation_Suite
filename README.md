# Purpose

The task is to write a test suite that tests each of these end-points for positive & negative scenarios and asserts based on the response.

# SetUp

Python 3.9.6

Pycharm 2020.1

# Required packages:

pytest

html reporter

requests

# How to run


To run each method test cases seperate pytest markers has been used
The flags and markers initiated in .ini file

To run Get Method test cases

```
pytest -m Get

```

# To run Post Method test cases

```
pytest -m Post

```

# To run Put and Patch Method test cases

```
pytest -m PutPatch

```

# To run Delete Method test cases

```
pytest -m Delete

```

Note: Html reporter is initiated in ini file, so html file will get generated and updated on each run

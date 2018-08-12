[![Build Status](https://travis-ci.org/simonporter007/codewars-python-solutions.svg?branch=master)](https://travis-ci.org/simonporter007/codewars-python-solutions)
[![Coverage Status](https://coveralls.io/repos/github/simonporter007/codewars-python-solutions/badge.svg?branch=master)](https://coveralls.io/github/simonporter007/codewars-python-solutions?branch=master)
[![Python Version](https://img.shields.io/badge/python-2.7-blue.svg)]()

# Codewars - Python Solutions

Project structure and README copied from the great [the-zebulan/CodeWars](https://github.com/the-zebulan/CodeWars).
My solutions for Codewars problems are written using `Python 2.7` and unittests are run using pytest.

- Codewars supports `Python 2.7.6` and `Python 3.4.3`.
- Since `Python 3` support is relatively new to Codewars, a lot of the `Python` katas are only available for `Python 2`.

### [Profile](http://www.codewars.com/users/simonporter007)

![Codewars Rank](https://www.codewars.com/users/simonporter007/badges/large)

### [Ranking](http://www.codewars.com/about)

```
8 - 7 kyu │ Beginner
6 - 5 kyu │ Novice
4 - 3 kyu │ Competent
2 - 1 kyu │ Proficient
1 - 5 dan │ Expert
5 - 8 dan │ Master
```

### Repo Structure

There are two main directories in this repository, `katas` and `tests`.

```
├── katas
│   ├── incomplete
│   ├── kyu_3
│   ├── kyu_4
│   ├── kyu_5
│   ├── kyu_6
│   ├── kyu_7
│   └── kyu_8
└── tests
    ├── kyu_3_tests
    ├── kyu_4_tests
    ├── kyu_5_tests
    ├── kyu_6_tests
    ├── kyu_7_tests
    └── kyu_8_tests
```

For each completed kata, there is a corresponding unittest file.

```
├── katas
│   ├── kyu_8
│   │   ├── add_length.py
└── tests
    ├── kyu_8_tests
    │   ├── test_add_length.py
```

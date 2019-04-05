## 0.0.5 (2019-04-05)

* bug fix: removed redundant `REQUIRES` var from `setup.py`, preventing a
  FileNotFound error during install from PyPI.


## 0.0.4 (2019-03-28)

* bug fix: `install_requires` in setup.py is now manually specified to avoid
  issues when trying to install from PyPI.


## 0.0.3 (2019-03-26)

* added `mux` operator: yields a single item from a set of generators by choosing and using a generator at random.
* added `factory` operator: constructs an object or calls a given method using randomly generated positional and keyword arguments.
* added `randint` operator.
* added basic examples to README.
* syntactic sugar: allow constant to be passed as `size` argument of `list` method.

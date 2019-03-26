.. -*-restructuredtext-*-

fluffycow
=========

.. image:: https://travis-ci.org/ChrisTimperley/fluffycow.svg?branch=master
    :target: https://travis-ci.org/ChrisTimperley/fluffycow

.. image:: https://badge.fury.io/py/fluffycow.svg
    :target: https://badge.fury.io/py/fluffycow

.. image:: https://img.shields.io/pypi/pyversions/fluffycow.svg
    :target: https://pypi.org/project/fluffycow


A simple and elegant library for generating complex random objects in Python.


.. image:: https://static.boredpanda.com/blog/wp-content/uploads/2014/03/cute-fluffy-animals-33.jpg

(image credit: `Matt Lautner <http://www.lautnerfarms.com/sires/texas-tornado/>`_.)


Installation
------------

To install the latest release from `PyPI <https://pypi.python.org/pypi/fluffycow/>`_:

.. code::

   $ pip install fluffycow

To install the latest development release:

.. code::

   $ git clone https://github.com/ChrisTimperley/fluffycow
   $ cd fluffycow
   $ python setup.py install


Examples
--------

To generate 10 lists containing 5 random numbers:

.. code:: python

   import fluffycow as g

   gen = g.list(g.random(), 5)
   lists = [next(g) for i in range(10)]


To generate 5 random cows 🐄:

.. code:: python

   import fluffycow as g
   import attr

   @attr.s
   class Cow:
      age = attr.ib(type=int)
      fluffiness = attr.ib(type=float)

   gen = g.object(Cow,
                  age=g.randint(0, 50),
                  fluffiness=g.gauss(5.0, 1.5))
   for i in range(5):
      cow = next(gen)
      print(cow)

   """
   ->
   Cow(age=16, fluffiness=6.737730437364233)
   Cow(age=30, fluffiness=3.6106200949734806)
   Cow(age=4, fluffiness=5.856278892241928)
   Cow(age=40, fluffiness=4.274460173984223)
   Cow(age=8, fluffiness=4.26886806010291)
   """

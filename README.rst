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
   for i in range(10):
       l = next(gen)
       print(l)

   """
   [0.8620918485892981, 0.4794836848262348, 0.262162063050416, 0.01909426938513137, 0.36506899628784006]
   [0.9397902843125912, 0.9883123343094299, 0.5728170848781718, 0.2430986751635641, 0.6504376531611539]
   [0.6530962809522628, 0.629805285301596, 0.7484217313556808, 0.4781887755635098, 0.7702516815623411]
   [0.6049464336804768, 0.6857354552123759, 0.4401119070721792, 0.16269631684472152, 0.4501522526776762]
   [0.6754685790929789, 0.14883325162091654, 0.7543575544723128, 0.7400186451945051, 0.7872586706933858]
   [0.6093352430215464, 0.601878065077082, 0.9864251783225236, 0.5652106608585465, 0.2000072917817054]
   [0.5288773016226057, 0.3473820645776373, 0.5181819860433858, 0.9795605815396756, 0.0941069188895195]
   [0.577403816680611, 0.6006088487133505, 0.7401053882982396, 0.9243339819764703, 0.8737058738019327]
   [0.15168246955860343, 0.9826794936881696, 0.8700116634339362, 0.23066589924280112, 0.6455718073363804]
   [0.4953407037944514, 0.4235910957127196, 0.9817109582233142, 0.19140229868504488, 0.4238482591507997]
   """


To generate 5 random cows 🐄:

.. code:: python

   import fluffycow as g
   import attr

   @attr.s
   class Cow:
      age = attr.ib(type=int)
      fluffiness = attr.ib(type=float)

   # provide generators for each keyword argument,
   gen = g.factory(Cow,
                   age=g.randint(0, 50),
                   fluffiness=g.gauss(5.0, 1.5))

   # or for each positional argument,
   gen = g.factory(Cow, g.randint(0, 50), g.gauss(5.0, 1.5))

   # or mix positional and keyword arguments
   gen = g.factory(Cow,
                   g.randint(0, 50),
                   fluffiness=g.gauss(5.0, 1.5))

   # generate some fluffy cows
   for i in range(5):
      cow = next(gen)
      print(cow)

   """
   Cow(age=16, fluffiness=6.737730437364233)
   Cow(age=30, fluffiness=3.6106200949734806)
   Cow(age=4, fluffiness=5.856278892241928)
   Cow(age=40, fluffiness=4.274460173984223)
   Cow(age=8, fluffiness=4.26886806010291)
   """


To generate a farm containing a random mixture of 10 animals:

.. code:: python

   @attr.s
   class Cow:
      age = attr.ib(type=int)
      fluffiness = attr.ib(type=float)

   @attr.s
   class Chicken:
       sass = attr.ib(type=int)

   @attr.s
   class Sheep:
      fluffiness = attr.ib(type=float)

   def farm():
       cows = g.factory(Cow,
                age=g.randint(0, 30),
                fluffiness=g.gauss(5.0, 1.5))
       chickens = g.object(Chicken, g.randint(0, 10))
       sheep = g.object(Sheep, g.gauss(4.5, 1.0))

       animals = g.mux(cows, chickens, sheep)
       for i in range(10):
           animal = next(animals)
           print(animal)

   """
   Cow(age=15, fluffiness=4.13522619329628)
   Cow(age=6, fluffiness=6.132266751335851)
   Sheep(fluffiness=4.996947740687185)
   Cow(age=25, fluffiness=4.268442712380023)
   Sheep(fluffiness=4.92952572321737)
   Chicken(sass=5)
   Cow(age=28, fluffiness=5.155204522890905)
   Sheep(fluffiness=3.9241924681246094)
   Sheep(fluffiness=3.676097181435127)
   Sheep(fluffiness=2.713429568549102)
   """

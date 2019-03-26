# -*- coding: utf-8 -*-
__all__ = (
    'call',
    'constant',
    'choice',
    'list',
    'random',
    'uniform',
    'gauss')

from typing import Iterator, TypeVar, Callable, Collection, List
import functools
import random as _random

T = TypeVar('T')


def call(f: Callable[[], T]) -> Iterator[T]:
    """Calls a function at each iteration to generate a value."""
    while True:
        yield f()


def constant(v: T) -> Iterator[T]:
    """Always returns a constant value."""
    while True:
        yield v


def choice(opts: Collection[T]) -> Iterator[T]:
    """Selects an item from a set of options."""
    assert opts, "at least one option must be provided."
    return call(functools.partial(_random.choice, opts))


def list(g: Iterator[T], size: Iterator[int]) -> Iterator[List[T]]:
    """Generates a list of a sampled size using an item generator."""
    while True:
        sz = next(size)
        yield [next(g) for i in range(sz)]


def random() -> Iterator[float]:
    """Samples a random floating point number in the range [0.0, 1.0)."""
    return call(_random.random)


def uniform(a: float, b: float) -> Iterator[float]:
    return call(functools.partial(_random.uniform, a, b))


def gauss(mu: float, sigma: float) -> Iterator[float]:
    return call(functools.partial(_random.gauss, mu, sigma))

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


K = TypeVar('K')
def call(f: Callable[[], K]) -> Iterator[K]:
    """Calls a function at each iteration to generate a value."""
    while True:
        yield f()


K = TypeVar('K')
def constant(v: K) -> K:
    """Always returns a constant value."""
    while True:
        yield v


K = TypeVar('K')
def choice(opts: Collection[K]) -> Iterator[K]:
    """Selects an item from a set of options."""
    assert opts, "at least one option must be provided."
    return call(functools.partial(_random.choice, opts))


K = TypeVar('K')
def list(g: Iterator[K], size: Iterator[int]) -> Iterator[List[K]]:
    """Generates a list of a sampled size using an item generator."""
    while True:
        sz = next(size)
        yield [next(g) for i in range(sz)]


random: Callable[[], Iterator[float]] = call(_random.random)


def uniform(a: float, b: float) -> Iterator[float]:
    return call(functools.partial(_random.uniform, a, b))


def gauss(mu: float, sigma: float) -> Iterator[float]:
    return call(functools.partial(_random.gauss, mu, sigma))

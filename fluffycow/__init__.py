# -*- coding: utf-8 -*-
__all__ = (
    'call',
    'constant',
    'choice',
    'list',
    'mux',
    'random',
    'randint',
    'object',
    'uniform',
    'gauss')

from typing import (Iterator, TypeVar, Callable, Collection, List, Union,
                    Type, Any)
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


def mux(*generators: Iterator[Any]) -> Iterator[Any]:
    """Generates an input using a randomly selected generator."""
    assert generators, "must be provided at least one generator"
    while True:
        gen = _random.choice(generators)
        yield next(gen)


def list(g: Iterator[T], size: Union[int, Iterator[int]]) -> Iterator[List[T]]:
    """Generates a list of a sampled size using an item generator."""
    if isinstance(size, int):
        size = constant(size)
    while True:
        sz = next(size)
        yield [next(g) for i in range(sz)]


def random() -> Iterator[float]:
    """Samples a random floating point number in the range [0.0, 1.0)."""
    return call(_random.random)


def randint(a: int, b: int) -> Iterator[int]:
    """Returns a random integer N such that a <= N <= b."""
    return call(functools.partial(_random.randint, a, b))


def uniform(a: float, b: float) -> Iterator[float]:
    return call(functools.partial(_random.uniform, a, b))


def gauss(mu: float, sigma: float) -> Iterator[float]:
    return call(functools.partial(_random.gauss, mu, sigma))


def factory(cls: Type[T],
            *args_generators: Iterator[Any],
            **kwargs_generators: Iterator[Any]
            ) -> Iterator[T]:
    """Generates random objects belonging to a given class."""
    while True:
        args = [next(g) for g in args_generators]
        kwargs = {n: next(g) for (n, g) in kwargs_generators.items()}
        yield cls(*args, **kwargs)  # type: ignore

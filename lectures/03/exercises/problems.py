"""Lecture 03 practice problems.

Implement each class/function below so tests pass.
Rules:
- Do not change names/signatures.
- Use only the Python standard library.

Problems:
1. Countdown iterator
2. Step iterator
3. Unique consecutive iterator
4. Circular iterator
6. File word reader generator
7. Batch generator
8. Recursive flatten generator (optional)
9. log_calls decorator
10. measure_time decorator
11. count_calls decorator
12. ensure_non_negative decorator
13. retry decorator (optional)
14. lru_cache decorator (optional)
"""

from __future__ import annotations

from collections.abc import Callable, Iterable, Iterator, Sequence
from typing import Any


class Countdown:
    def __init__(self, n: int) -> None:
        self.start = n

    def __iter__(self) -> Iterator[int]:
        current = self.start
        while current >= 0:
            yield current
            current -= 1
     
     
class StepIterator:
    """Problem 2. Step iterator.

    Iterate through a list by taking every `step`-th element.
    Default step is 2.
    Raise ValueError when step <= 0.

    Example:
    >>> list(StepIterator([10, 20, 30, 40, 50, 60]))
    [10, 30, 50]
    >>> list(StepIterator([1, 2, 3, 4, 5, 6, 7], step=3))
    [1, 4, 7]
    """

    def __init__(self, values: list[Any], step: int = 2) -> None:
        if step <= 0:
            raise ValueError()
        self.values = values
        self.step = step
        self.index = 0

    def __iter__(self) -> Iterator[Any]:
        return self

    def __next__(self) -> Any:
        if self.index >= len(self.values):
            raise StopIteration
        value = self.values[self.index]
        self.index += self.step
        return value


class UniqueConsecutiveIterator:
    """Problem 3. Unique consecutive iterator.

    Yield values while removing only *consecutive* duplicates.

    Example:
    >>> list(UniqueConsecutiveIterator([1, 1, 2, 2, 2, 3, 1, 1]))
    [1, 2, 3, 1]
    """

    def __init__(self, values: list[Any]) -> None:
       self.values = values
       self.index = 0
       
    def __iter__(self) -> Iterator[Any]:
        return self

    def __next__(self) -> Any:
        if self.index >= len(self.values):
            raise StopIteration
        value = self.values[self.index]
        while self.index + 1 < len(self.values) and self.values[self.index + 1] ==  value:
            self.index += 1
        self.index += 1
        return value    
      
class CircularIterator:
    """Problem 4. Circular iterator.

    Return exactly k values by cycling through sequence.
    Raise ValueError when sequence is empty or when k < 0.

    Example:
    >>> list(CircularIterator(["A", "B", "C"], 8))
    ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B']
    """

    def __init__(self, sequence: Sequence[Any], k: int) -> None:
        self.k = k
        self.sequence = sequence
        self.count = 0
        self.index = 0
        if self.k < 0 or len(self.sequence) == 0:
            raise ValueError
        
        
    def __iter__(self) -> Iterator[Any]:
        return self

    def __next__(self) -> Any:
        if self.count == self.k:
            raise StopIteration
        value = self.sequence[self.index]
        self.index = (self.index + 1) % len(self.sequence)
        self.count += 1
        return value
               


class FlattenIterator:
    """Problem 5 (optional). Flatten iterator.

    Build an iterator class that yields scalar values from nested lists
    of arbitrary depth.

    Example:
    >>> list(FlattenIterator([1, [2, 3], [4, [5, 6]], 7]))
    [1, 2, 3, 4, 5, 6, 7]
    """

    def __init__(self, data: list[Any]) -> None:
        raise NotImplementedError

    def __iter__(self) -> Iterator[Any]:
        raise NotImplementedError

    def __next__(self) -> Any:
        
        raise NotImplementedError
            
            
    """Problem 6. File word reader generator.

    Yield one word at a time from a text file without loading the whole
    file into memory.

    Example:
    >>> list(read_words("sample.txt"))
    ['one', 'two', 'three']
    """
def read_words(filename: str):
    with open(filename, "r") as f:
        for line in f:
            for word in line.split():
                yield word
            
"""Problem 7. Batch generator.

    Yield lists containing at most size items from iterable.
    Raise ValueError when size <= 0.
    

    Example:
    >>> list(batch([1, 2, 3, 4, 5, 6, 7], 3))
    [[1, 2, 3], [4, 5, 6], [7]]
    """
def batch(something: list, size: int):
    if size <= 0:
        raise ValueError
    l = []
    for s in something:
        l.append(s)
        if len(l) == size:
            yield l
            l = []
    if l != []:
        yield l    
    
    
    


def flatten(data: list[Any]) -> Iterator[Any]:
    """Problem 8 (optional). Recursive flatten generator.

    Recursively yield all scalar values from a nested list.

    Example:
    >>> list(flatten([1, [2, 3], [4, [5, 6]], 7]))
    [1, 2, 3, 4, 5, 6, 7]
    """
    raise NotImplementedError

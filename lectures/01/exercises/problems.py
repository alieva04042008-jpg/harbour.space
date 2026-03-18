"""Lecture 01 practice problems.

Implement each function below so tests pass.
Rules:
- Do not change function names/signatures.
- Keep implementations pure unless the function explicitly needs I/O.
- Use only the Python standard library.
"""

from __future__ import annotations


def normalize_username(name: str) -> str:
    norm_name = "_".join(name.strip().lower().split())
    return norm_name
    """Return a normalized username.

    Rules:
    - Trim outer whitespace
    - Lowercase everything
    - Replace internal whitespace runs with a single underscore
    """
    raise NotImplementedError


def is_valid_age(age: int) -> bool:
    return True if 18 <= age <= 120 else False
    """Return True if age is in [18, 120], otherwise False."""
    raise NotImplementedError


def truthy_values(values: list[object]) -> list[object]:
    result = []
    for v in values:
        if v:
            result.append(v)
    return result
    """Return a new list containing only truthy values from input."""
    raise NotImplementedError


def sum_until_negative(numbers: list[int]) -> int:
    result = 0
    for i in range(len(numbers)):
        if numbers[i] >= 0:
            result += numbers[i]
        else:
            break
    return result
    """Return sum of numbers until the first negative value (exclusive)."""
    raise NotImplementedError


def skip_multiples_of_three(numbers: list[int]) -> list[int]:
    numbers = [n for n in numbers if n % 3 != 0]
    return numbers
    """Return numbers excluding values divisible by 3."""
    raise NotImplementedError


def first_even_or_none(numbers: list[int]) -> int | None:
    for n in numbers:
        if n % 2 == 0:
            return n
    return None
    """Return the first even number, or None if no even number exists."""
    raise NotImplementedError


def squares_of_even(numbers: list[int]) -> list[int]:
    numbers = [n ** 2 for n in numbers if n % 2 == 0]
    return numbers
    """Return squares of all even numbers in input order."""
    raise NotImplementedError


def word_lengths(words: list[str]) -> dict[str, int]:
    result = {w: len(w) for w in words}
    return result
    """Return dict mapping each word to its length."""
    raise NotImplementedError


def zip_to_pairs(keys: list[str], values: list[int]) -> list[tuple[str, int]]:
    l = []
    for k, v in zip(keys, values):
        l.append((k, v))
    return l
    """Zip keys and values into list of pairs. Ignore extras in longer list."""
    raise NotImplementedError


def build_user(name: str, role: str = "student", active: bool = True) -> dict[str, object]:
    return {"name": name, "role": role, "active": active}
    """Build and return {'name': name, 'role': role, 'active': active}."""
    raise NotImplementedError


def append_tag_safe(tag: str, tags: list[str] | None = None) -> list[str]:
    if tags is None:
        tags = []
    tags.append(tag)
    return tags
    """Append tag to tags safely (no shared mutable default across calls)."""
    raise NotImplementedError


def invert_dict(mapping: dict[str, int]) -> dict[int, str]:
    mapping_new = dict([(value, key) for key, value in  mapping.items()])
    return mapping_new
    """Invert mapping. Assume values are unique."""
    raise NotImplementedError


def unique_sorted_tags(tags: list[str]) -> list[str]:
    return sorted(set(tags))
    """Return unique tags sorted ascending."""
    raise NotImplementedError

from collections import Counter
def count_words(words: list[str]) -> dict[str, int]:
    return Counter(words)

# with no counter
def count_words_hardcore(words: list[str]) -> dict[str, int]:
    dic = {}
    for w in words:
        if w in dic:
            dic[w] += 1
        else:
            dic[w] = 1
    return dic

    """Count occurrences of each word using collections.Counter."""
    raise NotImplementedError

from collections import defaultdict
def group_scores(records: list[tuple[str, int]]) -> dict[str, list[int]]:
    d = defaultdict(list)
    for g, s in  records:
        d[g].append(s)
    return d
    """Group scores by student name using collections.defaultdict(list)."""
    raise NotImplementedError

from collections import deque
def rotate_queue(items: list[str], steps: int) -> list[str]:
    dq = deque(items)
    dq.rotate(steps)
    return list(dq)
    """Rotate queue to the right by `steps` using collections.deque and return as list."""
    raise NotImplementedError


def safe_int(value: str) -> int | None:
    try:
        value = int(value)
    except:
        return None
    return value
    """Convert string to int, returning None if conversion fails."""
    raise NotImplementedError


def read_lines(path: str) -> list[str]:
    with open(path, 'r') as f:
        result = []
        for line in f:
            cl_l = line.strip()
            if cl_l:
                result.append(cl_l)
        return result
    """Read a text file with a context manager and return non-empty stripped lines."""
    raise NotImplementedError


def top_n_scores(scores: list[int], n: int = 3) -> list[int]:
    scores.sort()
    return scores[-1:-n-1:-1]
    """Return top `n` scores in descending order."""
    raise NotImplementedError


def all_passed(scores: list[int], threshold: int = 50) -> bool:
    passed = all(s >= threshold for s in scores)
    return passed
    """Return True if every score is >= threshold."""
    raise NotImplementedError

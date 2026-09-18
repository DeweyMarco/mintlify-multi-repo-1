"""Stable merge sort implementation."""

from collections.abc import Callable, Sequence
from typing import TypeVar

T = TypeVar("T")
K = TypeVar("K")


def merge_sort(values: Sequence[T], *, key: Callable[[T], K] | None = None) -> list[T]:
    """Return a stably sorted copy of *values* in O(n log n) time."""
    items = list(values)
    if len(items) < 2:
        return items

    key_fn: Callable[[T], object] = key if key is not None else lambda item: item

    def sort(partition: list[T]) -> list[T]:
        if len(partition) < 2:
            return partition

        middle = len(partition) // 2
        left = sort(partition[:middle])
        right = sort(partition[middle:])
        return merge(left, right)

    def merge(left: list[T], right: list[T]) -> list[T]:
        merged: list[T] = []
        left_index = right_index = 0

        while left_index < len(left) and right_index < len(right):
            if key_fn(left[left_index]) <= key_fn(right[right_index]):
                merged.append(left[left_index])
                left_index += 1
            else:
                merged.append(right[right_index])
                right_index += 1

        merged.extend(left[left_index:])
        merged.extend(right[right_index:])
        return merged

    return sort(items)

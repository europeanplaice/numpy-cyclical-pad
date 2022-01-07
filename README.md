# numpy-cyclical-pad
NumPy implementation of cyclical padding

## Features

It provides a function of NumPy array that pads cyclically.
It is a variation of `numpy.pad` (https://numpy.org/doc/stable/reference/generated/numpy.pad.html). You can easily extend an array that has patterns (e.g. seasonal time series). However, currently this function can only accept a one-dimensional array.

## Definition
```python
cyclical_pad(
    array, pad_width, pattern_start_idx, pattern_end_idx, edge_idxes
)
```

## Args
    array: One-dimentional array
    pad_width: A 2-tuple. Number of values padded to the edges of each axis.
    pattern_start_idx: A start index of a pattern
    pattern_end_idx: An end index of a pattern
    edge_idxes: A 2-tuple. Indexes where sequences that are padded start.


## Examples
```python
arr = np.array([0, 1, 2, 3, 0, 1])
padded = cyclical_pad(
    arr, pad_width=(0, 2), pattern_start_idx=0,
    pattern_end_idx=3, edge_idxes=(0, 4))
np.testing.assert_array_equal(padded, np.array([0, 1, 2, 3, 0, 1, 2, 3]))
```

```python
arr = np.array([2, 3, 0, 1, 2, 3, 0, 1])
padded = cyclical_pad(arr, pad_width=(2, 1), pattern_start_idx=2,
                        pattern_end_idx=5, edge_idxes=(1, 6))
np.testing.assert_array_equal(
    padded, np.array([0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2]))

```

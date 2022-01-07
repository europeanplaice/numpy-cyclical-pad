# numpy-cyclical-pad
NumPy implementation of cyclical padding

## Features

It provides a function of NumPy array that pads cyclically. You can easily extend an array that has patterns (e.g. seasonal time series).
```python
arr = np.array([0, 1, 2, 3, 0, 1])
padded = cyclical_pad(
    arr, pad_width=(0, 2), pattern_start_idx=0,
    pattern_end_idx=3, edge_idx=(0, 4))

b = np.array([0, 1, 2, 3, 0, 1, 2, 3])
np.testing.assert_array_equal(padded, b)
```

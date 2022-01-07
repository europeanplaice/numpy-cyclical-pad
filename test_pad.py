import pytest
import numpy as np
from pad import cyclical_pad


def test_repeat_pad_forward():
    arr = np.array([0, 1, 2, 3, 0, 1])
    padded = cyclical_pad(arr, pad_width=(0, 2), pattern_start_idx=0,
                          pattern_end_idx=3, edge_idx=(0, 4))
    b = np.array([0, 1, 2, 3, 0, 1, 2, 3])
    np.testing.assert_array_equal(padded, b)


def test_repeat_pad_forward_v2():
    arr = np.array([0, 1, 2, 3, 0, 1])
    padded = cyclical_pad(arr, pad_width=(0, 3), pattern_start_idx=0,
                          pattern_end_idx=3, edge_idx=(0, 4))
    np.testing.assert_array_equal(
        padded, np.array([0, 1, 2, 3, 0, 1, 2, 3, 0]))


def test_repeat_pad_forward_v3():
    arr = np.array([0, 1, 2, 3, 0, 1])
    padded = cyclical_pad(arr, pad_width=(0, 5), pattern_start_idx=0,
                          pattern_end_idx=3, edge_idx=(0, 4))
    np.testing.assert_array_equal(
        padded, np.array([0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2]))


def test_repeat_pad_forward_reversed_index():
    arr = np.array([0, 1, 2, 3, 0, 1, 2, 3, 0, 1])
    padded = cyclical_pad(arr, pad_width=(0, 1), pattern_start_idx=0,
                          pattern_end_idx=3, edge_idx=(0, -2))
    np.testing.assert_array_equal(
        padded, np.array([0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2]))


def test_repeat_pad_backward():
    arr = np.array([3, 0, 1, 2, 3, 0, 1])
    padded = cyclical_pad(arr, pad_width=(2, 0), pattern_start_idx=1,
                          pattern_end_idx=4, edge_idx=(0, 5))
    np.testing.assert_array_equal(
        padded, np.array([1, 2, 3, 0, 1, 2, 3, 0, 1]))


def test_repeat_pad_both_direction():
    arr = np.array([2, 3, 0, 1, 2, 3, 0, 1])
    padded = cyclical_pad(arr, pad_width=(2, 1), pattern_start_idx=2,
                          pattern_end_idx=5, edge_idx=(1, 6))
    np.testing.assert_array_equal(
        padded, np.array([0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2]))


def test_dimension_error():
    arr = np.array([[0, 1]])
    with pytest.raises(ValueError) as e:
        cyclical_pad(arr, pad_width=(2, 1), pattern_start_idx=2,
                     pattern_end_idx=5, edge_idx=(1, 6))
    str(e.value) == "The array must be one-dimensional."

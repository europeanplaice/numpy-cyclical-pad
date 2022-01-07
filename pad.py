import numpy as np


def cyclical_pad(array, pad_width, pattern_start_idx,
                 pattern_end_idx, edge_idxes):
    """
    Args:
        array: One-dimentional array
        pad_width: A 2-tuple. Number of values padded to the edges of each axis.
        pattern_start_idx: A start index of a pattern
        pattern_end_idx: An end index of a pattern
        edge_idxes: A 2-tuple. Indexes where sequences that are padded start.
    Returns:
        A NumPy array
    """
    if array.ndim > 1:
        raise ValueError("The array must be one-dimensional.")
    pattern = array[pattern_start_idx:pattern_end_idx + 1]
    _pattern_repeat = np.concatenate(
        [pattern] * (((pad_width[0] + pad_width[1]) // len(pattern)) + 2))

    _target_part_right = array[edge_idxes[1]:]
    _added_right = _pattern_repeat[
        len(_target_part_right):len(_target_part_right) + pad_width[1]]

    _target_part_left = array[:edge_idxes[0] + 1]
    _added_left = _pattern_repeat[
        -pad_width[0] - len(_target_part_left):-len(_target_part_left)]

    return np.concatenate([_added_left, array, _added_right])

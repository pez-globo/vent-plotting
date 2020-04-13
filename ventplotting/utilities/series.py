"""Support for pandas Series."""


def slice_interval(series, start_index=None, end_index=None):
    """Slice into a timeseries using start and end indices."""
    if start_index is not None and end_index is not None:
        series = series[start_index:end_index]
    elif start_index is not None:
        series = series[start_index:]
    elif end_index is not None:
        series = series[:end_index]

    return series

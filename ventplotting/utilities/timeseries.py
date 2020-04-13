"""Support for timeseries using pandas Series indexed with TimedeltaIndexes."""
import pandas as pd

from ventplotting.utilities import series


def slice_interval(
        timeseries, start_time=None, end_time=None,
        start_time_units='s', end_time_units='s'
):
    """Slice into a timeseries using start and end times."""
    if start_time is not None:
        start_time = pd.Timedelta(start_time, start_time_units)
    if end_time is not None:
        end_time = pd.Timedelta(end_time, end_time_units)

    return series.slice_interval(
        timeseries, start_index=start_time, end_index=end_time
    )

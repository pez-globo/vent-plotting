"""Support for signals in input files."""
import pandas as pd


SIGNAL_START_ROW = 0  # zero-indexed


def rename_column(column_name):
    """Rename a raw column name into a nicer one."""
    if column_name == 'Time (s)':
        return 'Time'
    if column_name == 'Paw (cmH2O)':
        return 'Paw'
    if column_name == 'Flow (l/min)':
        return 'Flow'
    if column_name == 'Volume (ml)':
        return 'Volume'
    if column_name == 'Vt (ml)':
        return 'Vt'
    if column_name == 'Ti (s)':
        return 'Ti'
    if column_name == 'RR (/min)':
        return 'RR'
    if column_name == 'PEEP (cmH2O)':
        return 'PEEP'
    return column_name


class RawSignalSet(object):
    """Raw signal set loading/access."""

    def __init__(self):
        """Make an empty signal set object."""
        self.df = None  # a Pandas dataframe of the signals

    def load_csv(self, path):
        """Load signal set from a file path."""
        self.df = pd.read_csv(path, header=SIGNAL_START_ROW)
        self.df.rename(rename_column, axis='columns', inplace=True)
        self.df['Time'] -= self.df.Time.min()
        self.df.index = pd.to_timedelta(self.df.Time, unit='s')

    @property
    def times(self):
        """Get the relative times of the signal set."""
        return self.df.Time

    @property
    def time_index(self):
        """Get the time deltas index of the signal set."""
        return self.df.index

    @property
    def num_samples(self):
        """Get the number of samples."""
        return len(self.df)

    def get_signal(self, column_name):
        """Get a signal by its name number.

        Note that channel numbers are one-indexed.
        """
        return self.df[column_name]

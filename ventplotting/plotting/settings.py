"""Functionality for plotting of settings."""
from ventplotting.plotting import plot
from ventplotting.utilities import timeseries


def make_fig(num_rows=3, **kwargs):
    """Make a figure with three vertically stacked axes for control settings."""
    kwargs = {**kwargs, 'num_rows': num_rows}
    return plot.make_fig(**kwargs)


def make_fig_with_legends(num_rows=3, **kwargs):
    """Make a figure with three vertically stacked axes for control settings."""
    kwargs = {**kwargs, 'num_rows': num_rows}
    return plot.make_fig_with_legends(**kwargs)


def plot_settings(
        raw_signal_set, ax_volume, ax_time, ax_rate,
        start_time=None, end_time=None
):
    """Plot all control settings from a RawSignalSet.

    Plot each setting on its own axis.
    """
    sliced = timeseries.slice_interval(
        raw_signal_set.df, start_time=start_time, end_time=end_time
    )
    sliced.plot(x='Time', y='Vt', ax=ax_volume, legend=False)
    plot.fill_timeseries(sliced.Time, sliced.Vt, ax_volume)
    sliced.plot(x='Time', y='Ti', ax=ax_time, legend=False)
    plot.fill_timeseries(sliced.Time, sliced.Ti, ax_time)
    sliced.plot(x='Time', y='RR', ax=ax_rate, legend=False)
    plot.fill_timeseries(sliced.Time, sliced.RR, ax_rate)

    plot.set_y_axis_label(ax_volume, 'Volume', units='mL')
    plot.limit_y_axes([ax_volume], min=0, max=500)
    plot.set_y_axis_label(ax_time, 'Time', units='s')
    plot.limit_y_axes([ax_time], min=0, max=1.5)
    plot.set_y_axis_label(ax_rate, 'Rate', units='/min')
    plot.limit_y_axes([ax_rate], min=0, max=35)


# STANDARD FIGURES

def make_settings_fig(
        analysis, fig_title, column_title='Control Settings',
        fig_maker=make_fig_with_legends,
        kwargs_make_fig={'num_cols': 1}, kwargs_plot_settings={},
        kwargs_polish_axes={}
):
    """Make a figure with settings from an analysis."""
    kwargs_make_fig = {**kwargs_make_fig, 'num_cols': 1}
    (fig, plot_axes, legend_axes) = fig_maker(**kwargs_make_fig)
    plot.add_fig_title(fig, fig_title)
    plot.add_axes_title(plot_axes, column_title)
    plot_settings(analysis.raw_signals, *plot_axes, **kwargs_plot_settings)
    plot.polish_axes(plot_axes, legend_axes, **kwargs_polish_axes)
    return (fig, plot_axes, legend_axes)

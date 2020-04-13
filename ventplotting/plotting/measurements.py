"""Functionality for plotting of raw measurements."""
from ventplotting.plotting import plot
from ventplotting.utilities import timeseries


def make_fig(num_rows=3, **kwargs):
    """Make a figure with three vertically stacked axes for measurements."""
    kwargs = {**kwargs, 'num_rows': num_rows}
    return plot.make_fig(**kwargs)


def make_fig_with_legends(num_rows=3, **kwargs):
    """Make a figure with three vertically stacked axes for measurements."""
    kwargs = {**kwargs, 'num_rows': num_rows}
    return plot.make_fig_with_legends(**kwargs)


def plot_measurements(
        raw_signal_set, ax_pressure, ax_flow, ax_volume,
        start_time=None, end_time=None
):
    """Plot all measurements from a RawSignalSet.

    Plot each measurement on its own axis.
    """
    df = raw_signal_set.df
    sliced = timeseries.slice_interval(
        raw_signal_set.df, start_time=start_time, end_time=end_time
    )
    sliced.plot(x='Time', y=df[['Paw']].columns, ax=ax_pressure, legend=False)
    sliced.plot(x='Time', y=df[['Flow']].columns, ax=ax_flow, legend=False)
    sliced.plot(x='Time', y=df[['Volume']].columns, ax=ax_volume, legend=False)

    plot.set_y_axis_label(ax_pressure, 'Pressure', units='cmH2O')
    plot.set_y_axis_label(ax_flow, 'Flow', units='L/min')
    plot.set_y_axis_label(ax_volume, 'Volume', units='mL')

    plot.limit_y_axes([ax_pressure], min=0, max=45)
    flow_y_lim = max(abs(df.Flow.min()), abs(df.Flow.max()))
    plot.limit_y_axes([ax_flow], min=-flow_y_lim, max=flow_y_lim)
    plot.limit_y_axes([ax_volume], min=0, max=500)


# STANDARD FIGURES

def make_measurements_fig(
        analysis, fig_title, column_title='Raw Measurements',
        fig_maker=make_fig_with_legends,
        kwargs_make_fig={'num_cols': 1}, kwargs_plot_measurements={},
        kwargs_polish_axes={}
):
    """Make a figure with measurements from an analysis."""
    kwargs_make_fig = {**kwargs_make_fig, 'num_cols': 1}
    (fig, plot_axes, legend_axes) = fig_maker(**kwargs_make_fig)
    plot.add_fig_title(fig, fig_title)
    plot.add_axes_title(plot_axes, column_title)
    plot_measurements(analysis.raw_signals, *plot_axes, **kwargs_plot_measurements)
    plot.polish_axes(plot_axes, legend_axes, **kwargs_polish_axes)
    return (fig, plot_axes, legend_axes)

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
    start_time=None, end_time=None,
    pressure_min=0, pressure_max=45,
    pressure_major_spacing=20, pressure_minor_spacing=10,
    flow_min=-80, flow_max=80,
    flow_major_spacing=60, flow_minor_spacing=30,
    volume_min=0, volume_max=550,
    volume_major_spacing=200, volume_minor_spacing=100
):
    """Plot all measurements from a RawSignalSet.

    Plot each measurement on its own axis.
    """
    sliced = timeseries.slice_interval(
        raw_signal_set.df, start_time=start_time, end_time=end_time
    )

    sliced.plot(x='Time', y='Paw', ax=ax_pressure, legend=False, color='#66c2a5')
    plot.fill_timeseries(sliced.Time, sliced.Paw, ax_pressure, color='#66c2a5')
    sliced.plot(x='Time', y='Flow', ax=ax_flow, legend=False, color='#fc8d62')
    plot.fill_timeseries(sliced.Time, sliced.Flow, ax_flow, color='#fc8d62')
    sliced.plot(x='Time', y='Volume', ax=ax_volume, legend=False, color='#8da0cb')
    plot.fill_timeseries(sliced.Time, sliced.Volume, ax_volume, color='#8da0cb')

    plot.set_y_axis_label(ax_pressure, 'Pressure', units='cmH2O')
    plot.set_y_axis_label(ax_flow, 'Flow', units='L/min')
    plot.set_y_axis_label(ax_volume, 'Volume', units='mL')

    plot.limit_y_axes([ax_pressure], min=pressure_min, max=pressure_max)
    if flow_min is not None and flow_max is not None:
        plot.limit_y_axes([ax_flow], min=flow_min, max=flow_max)
    else:  # make flow limits symmetric
        df = raw_signal_set.df
        flow_y_lim = max(abs(df.Flow.min()), abs(df.Flow.max()))
        plot.limit_y_axes([ax_flow], min=-flow_y_lim, max=flow_y_lim)
    plot.limit_y_axes([ax_volume], min=volume_min, max=volume_max)

    plot.set_y_axis(
        ax_pressure, major_tick_spacing=pressure_major_spacing,
        minor_tick_spacing=pressure_minor_spacing
    )
    plot.set_y_axis(
        ax_flow, major_tick_spacing=flow_major_spacing,
        minor_tick_spacing=flow_minor_spacing
    )
    plot.set_y_axis(
        ax_volume, major_tick_spacing=volume_major_spacing,
        minor_tick_spacing=volume_minor_spacing
    )


# STANDARD FIGURES

def make_measurements_fig(
        analysis, fig_title, column_title='Raw Measurements',
        fig_maker=make_fig_with_legends,
        kwargs_make_fig={'num_cols': 1}, kwargs_plot_measurements={},
        kwargs_polish_axes={
            'kwargs_set_x_axes': {'kwargs_grid': {'alpha': 0.5}},
            'kwargs_set_y_axes': {'kwargs_grid': {'alpha': 0.5}}
        }
):
    """Make a figure with measurements from an analysis."""
    kwargs_make_fig = {**kwargs_make_fig, 'num_cols': 1}
    (fig, plot_axes, legend_axes) = fig_maker(**kwargs_make_fig)
    plot.add_fig_title(fig, fig_title)
    plot.add_axes_title(plot_axes, column_title)
    plot_measurements(analysis.raw_signals, *plot_axes, **kwargs_plot_measurements)
    plot.polish_axes(plot_axes, legend_axes, **kwargs_polish_axes)
    return (fig, plot_axes, legend_axes)

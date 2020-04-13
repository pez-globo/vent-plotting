"""Utilities to support nice plotting."""
import itertools

import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib import ticker

import numpy as np

from ventplotting.utilities import timeseries


# FIGURES


def make_fig(num_rows=1, num_cols=1, figsize=None, sharex='all', sharey='row'):
    """Make a figure, optionally with vertically stacked axes.

    Returns a tuple with a variable number of parts. The first tuple element is
    always the figure object; each remaining tuple element is an array of axes
    objects for each column.
    """
    (fig, axes) = plt.subplots(
        nrows=num_rows, ncols=num_cols, squeeze=False, figsize=figsize,
        sharex=sharex, sharey=sharey
    )
    axes = axes.T
    if len(axes) == 1:
        return axes[0]
    if num_cols == 1:
        return (fig, axes)
    else:
        return (fig, *axes)


def add_axes_title(axes, title):
    """Add a title for a column of axes."""
    axes[0].set_title(title)


def add_fig_title(fig, title, left_padding=0.05, top_padding=0):
    """Add a left-aligned figure title."""
    fig.suptitle(
        title, x=left_padding, y=1 + top_padding, horizontalalignment='left'
    )


#  DATA

def plot_timeseries(
        times, series, ax, start_time=None, end_time=None,
        legend_label_template='{}', legend_label_components=[],
        ylabel=None, units=None, **kwargs
):
    """Plot a timeseries."""
    times = timeseries.slice_interval(times, start_time=start_time, end_time=end_time)
    series = timeseries.slice_interval(series, start_time=start_time, end_time=end_time)
    ax.plot(
        times, series, label=legend_label_template.format(*legend_label_components),
        **kwargs
    )
    if ylabel is not None:
        set_y_axis_label(ax, ylabel, units=units)


# LEGENDS


def make_fig_with_legends(
        num_rows=1, num_cols=1, figsize=None, width_ratio=(9, 1),
        sharex='all', sharey='row'
):
    """Make a figure, optionally with vertically stacked axes, and legend axes.

    For each subplot axis, a legend axis (a blank space for placing a legend)
    is also made.
    The width ratio should be the ratio of plot axis width to legend axis width.
    Returns a tuple with a variable number of parts. The first tuple element is
    always the figure object; each remaining tuple element is an array of plot axes
    objects for each column or an array of legend axes objects for each column;
    the plot axes and legend axes tuple elements alternate in order.
    """
    (fig, axes) = plt.subplots(
        nrows=num_rows, ncols=2 * num_cols, squeeze=False, figsize=figsize,
        sharex=sharex, sharey=sharey,
        gridspec_kw={'width_ratios': np.tile(width_ratio, num_cols)}
    )
    plot_axes = axes[:, 0::2].T
    legend_axes = axes[:, 1::2].T
    for ax in legend_axes.flatten():
        ax.axis('off')
    plots_legends = itertools.chain(*zip(plot_axes, legend_axes))
    return (fig, *plots_legends)


def add_legend(
        plot_ax, legend_ax=None,
        legend_position='upper right', remove_duplicates=True
):
    """Add a legend for a plot axis.

    If a legend axis is given, the legend is placed there in the center left;
    otherwise, it's placed in the plot axis in the specified position.
    """
    if legend_ax is None:
        plot_ax.legend(loc=legend_position)
        return

    (handles, labels) = plot_ax.get_legend_handles_labels()
    if not handles and not labels:
        return

    if remove_duplicates:
        added_labels = set()
        handles_labels = [
            (handle, label)
            for (handle, label) in zip(handles, labels)
            if not (label in added_labels or added_labels.add(label))
        ]
        (handles, labels) = zip(*handles_labels)

    legend_ax.legend(
        handles, labels, bbox_to_anchor=(-0.8, 1), loc='upper left', borderaxespad=0
    )


def add_legends(plot_axes, legend_axes, **kwargs):
    """Add legends for plot axes."""
    for (plot_ax, legend_ax) in zip(plot_axes, legend_axes):
        add_legend(plot_ax, legend_ax=legend_ax, **kwargs)


# AXES


def align_labels(plot_axes, position=-0.09):
    """Align axis labels between plot axes of a figure."""
    for ax in plot_axes:
        ax.yaxis.set_label_coords(position, 0.5)


def set_y_axis_label(ax, name, units=None):
    """Set a label for the y axis."""
    if units is None:
        ax.set_ylabel(name)
    else:
        ax.set_ylabel('{} ({})'.format(name, units))


def set_x_axis(ax, xlabel='Time (s)', tick_spacing=1.0, tight=True, log=False):
    """Configure the time axis."""
    if log:
        major = ticker.LogLocator(base=10, subs=range(tick_spacing))
        ax.xaxis.set_major_locator(major)
    else:
        major = ticker.MultipleLocator(base=tick_spacing)
        ax.xaxis.set_major_locator(major)
    ax.set_xlabel(xlabel)
    ax.autoscale(enable=True, axis='x', tight=tight)


def set_x_axes(plot_axes, **kwargs):
    """Configure the time axes."""
    set_x_axis(plot_axes[-1], **kwargs)


def limit_x_axes(plot_axes, min=None, max=None):
    """Limit the time axes to the specified interval."""
    for ax in plot_axes:
        ax.set_xlim(left=min, right=max)


def set_loglog(plot_axes):
    """Set axes to be loglog scale."""
    for ax in plot_axes:
        ax.loglog()


# LAYOUT

def polish_axes(
        plot_axes, legend_axes,
        kwargs_align_labels={}, kwargs_set_x_axes={}, kwargs_add_legends={}
):
    """Improve layout and display of axes."""
    align_labels(plot_axes, **kwargs_align_labels)
    set_x_axes(plot_axes, **kwargs_set_x_axes)
    add_legends(plot_axes, legend_axes, **kwargs_add_legends)


# STYLING

def use_helvetica():
    """Set plot fonts to Helvetica."""
    mpl.rc(
        'font',
        family=['Helvetica', 'Helvetica Neue', 'Helvetica Neue LT Std'],
        weight=500
    )
    mpl.rc(
        'axes',
        titleweight='medium',
        labelweight='medium',
        titlepad=12
    )
    mpl.rc(
        'figure',
        titleweight='medium',
        titlesize='xx-large',
        facecolor='white'
    )


def reset_prop_cycle(plot_axes):
    """Reset properties cycle of axes."""
    for ax in plot_axes:
        ax.set_prop_cycle(None)

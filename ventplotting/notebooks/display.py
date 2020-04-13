"""Utilities for Jupyter Notebook display."""
import IPython.display as ipd

import ipywidgets as ipw


def print_md(string):
    """Render a string as Markdown to the notebook's output cell."""
    ipd.display(ipd.Markdown(string))


def gdrive_progress(display=True):
    """Return a GDrive download progress bar."""
    progress =  ipw.FloatProgress(
        value=0.0, min=0.0, max=1.0, description='Download'
    )
    if display:
        ipd.display(progress)
    return progress

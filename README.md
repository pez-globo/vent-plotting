# vent-plotting
Ventilator data processing.
This repository maintains the `ventplotting` Python package.

## Installation

Install the Python packages listed in `ventplotting/requirements.txt`:
```
pip3 install -r ventplotting/requirements.txt
```

## Notebooks

Jupyter notebooks are found in `notebooks/`. To run them properly, start Jupyter
(or even better, JupyterLab) from the repository directory:
```
jupyter-lab
```
Notebooks are designed to be run from start to finish via the
"Restart and Run All Cells..." menu command from within Jupyter.

For optimal development experience, first install the Python packages listed in
`notebooks/requirements.txt`:
```
pip3 install -r notebooks/requirements.txt
```
and also install each extension listed in `notebooks/labextensions.txt` with the
following command format for each extension listed (where `@jupyterlab/celltags`
should be replaced with the extension as listed in `notebooks/labextensions.txt`):
```
jupyter labextension install @jupyterlab/celltags
```

Some notebooks are to be manually run, while other notebooks are automatically
and parametrically generated (using [Papermill](https://github.com/nteract/papermill))
by manual execution of other notebooks. Specifically:

- `notebooks/example_plotting.ipynb`: manually run, demonstrates plotting of raw measurements and control settings.
- `notebooks/plotting_template.ipynb`: a template for automatic notebook generation and execution, plots a single file specified by its parameters.
- `notebooks/solenoid pinch valve only.ipynb`: a notebook which automatically generates and runs notebooks for the `solenoid pinch valve only` dataset collection. The resulting notebooks are found at `notebooks/solenoid pinch valve only/`.

## Dataset Auto-Downloading

By default, notebooks will look for data in the `../vent-data` directory
(relative to the repository directory).
For example, if the repository directory is
`/home/lietk12/Projects/mp/vent4us/vent-plotting/`, then the notebooks will
look for datasets in `/home/lietk12/Projects/mp/vent4us/vent-data/`.

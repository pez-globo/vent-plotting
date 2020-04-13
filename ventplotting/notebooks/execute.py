"""Support for easy execution of notebooks using Papermill."""
import pathlib

import IPython.display as ipd

import ipywidgets as ipw

import joblib as jl

import papermill as pm

from ventplotting.notebooks.display import print_md


def execute(
    template_path, output_name, cwd=None, output_dir=None, parameters={}, engine_kwargs={}
):
    """Run a parameterized notebook template using papermill."""
    if output_dir is None:
        output_dir = ''
    output_path = pathlib.Path(output_dir) / output_name
    pm.execute_notebook(
        str(template_path), str(output_path), cwd=str(cwd), parameters=parameters,
        **engine_kwargs
    )


def batch_serial(
    template_path, output_dir, output_names_cwds, output_names_parameters,
    template_type='template', input_summarizer=lambda parameters: 'inputs',
    printer=print_md, progress=None, nest_asyncio=True, engine_kwargs={}
):
    """Run a parameterized notebook template each of multiple parameters and outputs.

    A progress bar is automatically generated if progress is None. If progress is
    False, no progress bar is generated or updated.
    """
    printer('Running {} using template `{}`...'.format(template_type, template_path))
    if progress is None:
        progress = ipw.IntProgress(
            min=0, max=len(output_names_parameters), description='Notebooks'
        )
        ipd.display(progress)
    elif progress is False:
        progress = None

    if nest_asyncio:
        engine_kwargs['nest_asyncio'] = True

    try:
        for (output_name, parameters) in output_names_parameters.items():
            printer(
                'Running {} on {} and saving to `{}`...'.format(
                    template_type, input_summarizer(parameters),
                    pathlib.Path(output_dir) / output_name
                )
            )
            execute(
                template_path, output_name, output_dir=output_dir,
                cwd=output_names_cwds[output_name], parameters=parameters,
                engine_kwargs=engine_kwargs
            )
            if progress is not None:
                progress.value += 1
        if progress is not None:
            progress.bar_style = 'success'
    except Exception:
        if progress is not None:
            progress.bar_style = 'danger'
        raise


def batch_parallel(
    template_path, output_dir, output_names_cwds, output_names_parameters,
    template_type='template', printer=print_md, verbosity=20,
    num_jobs=-1, method='processes', engine_kwargs={}
):
    """Run a parameterized notebook template on parameters/inputs in parallel."""
    printer('Running {} using template `{}`...'.format(template_type, template_path))
    jl.Parallel(n_jobs=num_jobs, prefer=method, verbose=verbosity)(
        jl.delayed(execute)(
            template_path, output_name, output_dir=output_dir,
            cwd=output_names_cwds[output_name], parameters=parameters,
            engine_kwargs=engine_kwargs
        )
        for (output_name, parameters) in output_names_parameters.items()
    )

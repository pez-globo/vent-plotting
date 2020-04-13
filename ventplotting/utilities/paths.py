"""Support for nicer paths."""
import os
import pathlib


PACKAGE_PATH = pathlib.Path(os.path.abspath(__file__)).parent.parent
REPO_PATH = PACKAGE_PATH.parent
EXAMPLES_PATH = REPO_PATH / 'examples'
TESTS_PATH = PACKAGE_PATH / 'tests'
UNIT_TESTS_PATH = TESTS_PATH / 'unit'

EXAMPLE_NAMES = [
    'impactor_training_01',
    'impactor_training_02',
    'impactor_training_03'
]


def name_to_path(name, file_ext='', suffix='', dir=None):
    """Get the file path from the name of a file."""
    filename = name
    if suffix != '':
        filename += '_' + suffix
    if file_ext != '':
        filename += '.' + file_ext

    if dir is None or dir == '':
        return pathlib.Path(filename)
    return pathlib.Path(dir) / filename


def csv_name_to_path(name, suffix='', dir=EXAMPLES_PATH):
    """Get the file path from the name of an input csv file."""
    return name_to_path(name, file_ext='csv', dir=dir, suffix=suffix)


def json_name_to_path(name, suffix='', dir=EXAMPLES_PATH):
    """Get the file path from the name of a generic json file."""
    return name_to_path(name, file_ext='json', dir=dir, suffix=suffix)


def mat_name_to_path(name, suffix='', dir=EXAMPLES_PATH):
    """Get the file path from the name of an input mat file."""
    return name_to_path(name, file_ext='mat', dir=dir, suffix=suffix)


def metadata_json_name_to_path(name, dir=EXAMPLES_PATH):
    """Get the file path from the name of a metadata json file."""
    return json_name_to_path(name, dir=dir, suffix='metadata')


def raw_kinematics_json_name_to_path(name, dir=EXAMPLES_PATH):
    """Get the file path from the name of a raw kinematics config json file."""
    return json_name_to_path(name, dir=dir, suffix='raw_kinematics')


def filters_json_name_to_path(name, dir=EXAMPLES_PATH):
    """Get the file path from the name of a kinematics filters config json file."""
    return json_name_to_path(name, dir=dir, suffix='filters')


def sixdof_json_name_to_path(name, dir=EXAMPLES_PATH):
    """Get the file path from the name of a 6-DOF kinematics config json file."""
    return json_name_to_path(name, dir=dir, suffix='sixdof')


def proj_json_name_to_path(name, dir=EXAMPLES_PATH):
    """Get the file path from the name of a projection config json file."""
    return json_name_to_path(name, dir=dir, suffix='projection')

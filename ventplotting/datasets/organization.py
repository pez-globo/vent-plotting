"""Dataset organization and path management."""
import pathlib


from ventplotting.utilities.paths import PACKAGE_PATH


DATASET_COLLECTIONS_PATH = PACKAGE_PATH.parent  # Default parent for dataset collections


def collection_path(dataset_collection_name, dir=DATASET_COLLECTIONS_PATH):
    """Return the path of the named dataset collection."""
    return pathlib.Path(dir) / dataset_collection_name


def dataset_path(
        dataset_name, collection_name,
        collections_dir=DATASET_COLLECTIONS_PATH
):
    """Return the path of the named dataset."""
    return collection_path(collection_name, dir=collections_dir) / dataset_name


def data_path(
        data_name, dataset_name, collection_name,
        collections_dir=DATASET_COLLECTIONS_PATH
):
    """Return the path of the named dataset data."""
    return dataset_path(
        dataset_name, collection_name, collections_dir=collections_dir
    ) / data_name

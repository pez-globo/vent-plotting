"""Support for manipulation of data collections."""


def transpose(list_of_lists):
    """Flip a list of lists so that the outer list becomes the inner list.

    Assumes that each inner list is of equal length.
    """
    return list(map(list, zip(*list_of_lists)))

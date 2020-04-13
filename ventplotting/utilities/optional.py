"""Handling of optional values."""


def with_default(value, default_value):
    """Return either value if it's not None or else default_value."""
    if value is not None:
        return value
    return default_value

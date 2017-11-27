"""Configuration module."""
import logging
import sys

import yaml

log = logging.getLogger()


def load_config(filename=None):
    """Load a configuration from a file or stdin.

    If `filename` is `None`, then configuration gets read from stdin.

    Returns: A configuration dict.
    """
    if filename is None or filename == '-':
        log.info('Reading config from stdin')
        return yaml.safe_load(sys.stdin)

    with open(filename, mode='rt') as handle:
        log.info('Reading config from %r', filename)
        return yaml.safe_load(handle)


def serialize_config(config):
    """Convert a configuration dict into a string.

    This is complementary with `load_config`.
    """
    return yaml.dump(config)


def get_db_name(session_name):
    """Determines the filename for a session.

    Basically, if `session_name` ends in ".json" this return `session_name`
    unchanged. Otherwise it return `session_name` with ".json" added to the
    end.
    """
    if session_name.endswith('.json'):
        return session_name
    return '{}.json'.format(session_name)


class ConfigError(Exception):
    """An error occurred while creating configuration."""
    pass

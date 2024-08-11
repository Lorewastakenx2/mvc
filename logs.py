

import logging

event_logger = logging.getLogger(name='event')
mvc_logger = logging.getLogger(name='mvc')

def tcn(cls: object) -> str:
    """
    truncate class name
    """
    return str(cls).split(' object at ')[0] + '>'
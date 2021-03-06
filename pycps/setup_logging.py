import os
import json
import logging
import logging.config

_logger = logging.getLogger(__name__)

def setup_logging(path_=None):
    if path_ is None:
        path_ = os.path.dirname(__file__) + '/logging.json'
    with open (path_) as f:
        config = json.load(f)
    logging.config.dictConfig(config)

setup_logging()

#!/usr/bin/env python

import os
import pathlib
from configparser import ConfigParser


def get_api_key():
    config = ConfigParser()
    config_file_path = os.path.join(
        pathlib.Path(__file__).parent.resolve(), "..", "config.ini"
    )
    config.read(config_file_path)
    return config["keys"]["api_key"], config["keys"]["api_secret"]

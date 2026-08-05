import os
import sys

import numpy as np
import dill
import yaml
from pandas import DataFrame

from src.exception import MyException
from src.logger import logging

def read_yaml_files(file_path: str) -> dict:
    try:
        with open(file_path, 'r') as yaml_file:
            return yaml.safe_load(yaml_file)

    except Exception as e:
        raise MyException(e, sys) from e

def write_yaml_files(file_path: str, content: object, replace: bool=False) -> None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        with open(file_path, 'w') as yaml_file:
            yaml.dump(content, yaml_file)

    except Exception as e:
        raise MyException(e, sys) from e




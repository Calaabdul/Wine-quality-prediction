import pickle
import json
from mlProject import logger
import os
import yaml
from box import ConfigBox
from ensure import ensure_annotations
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError


@ensure_annotations
def read_yaml(yaml_path: Path) -> ConfigBox:
    try:
        with open(yaml_path) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f'yaml file: {yaml_path} loaded successfully')
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError('yaml file is empty')
        
    except Exception as e:
        raise e



@ensure_annotations
def create_directories(path_to_dir: list, verbose =True):
    for path in path_to_dir:
        os.makedirs(path, exist_ok = True)
        if verbose:
            logger.info(f"created directory at: {path}")



@ensure_annotations
def save_json(path: Path, data: dict):
    with open(path, 'w') as f:
        json.dump(data, f, indent = 4)

    logger.info(f"json file saved at: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    with open(path) as f:
       content =  json.load(f)
    
    logger.info(f"json file loaded successfully from: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_object(data: Any, path: Path):
    with open(path, "wb") as f:
        pickle.dump(f)

    logger.info(f"binary file saved at: {path}")


@ensure_annotations
def load_object(path: Path) -> Any:
    try:
        with open(path, 'rb') as f:
            data = pickle.load(f)
        logger.info(f"binary file loaded from: {path}")
        return data
        
    except Exception as e:
        logger.info(f"Error loading from: {path}")

   
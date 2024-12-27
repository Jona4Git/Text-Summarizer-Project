import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns
    
    Args:
    path_to_yaml (str): path like input

    Raises:
    ValueError: if yaml file is empty
    e: empty file

    Returns:
    ConfigBox: loaded yaml file
    """
    try:
        # with open(path_to_yaml, 'r') as file:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
            raise e
    #         data = yaml.safe_load(file)
    #         if data is None:
    #             raise ValueError(f"The provided yaml file is empty: {path_to_yaml}")
    #         return ConfigBox(data)
    # except FileNotFoundError:
    #     logger.error(f"The provided yaml file was not found: {path_to_yaml}")
    #     raise
    # except BoxValueError as e:
    #     logger.error(f"The provided yaml file is not valid: {path_to_yaml}")
    #     raise e

    # method responsible for creating directories

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
        """create list of directories

        Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool,  optional): ignore if multiple dirs is to be created. Defaults to False.
        """
        for path in path_to_directories:
             os.makedirs(path, exist_ok=True)
             if verbose:
                  logger.info(f"Directory created at: {path}")

    # another method to get the size of the file
@ensure_annotations
def get_size(path: Path) -> str:
         """get size in KB

         Args:
         path (Path): path to the file
         
         Returns:
         str:size in KB
         """
         size_in_kb = round(os.path.getsize(path)/1024)
         return f"~ {size_in_kb}"
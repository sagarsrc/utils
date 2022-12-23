"""
common utils
"""

import os

import yaml
from glob import glob


class CommonUtils:
    def __init__(self, config_path=f"""{os.environ.get("PROJECT_ROOT")}/config"""):
        self.config_path = config_path
        # print("setting config path", self.config_path)

    def get_yml_config(self, keyname: str):
        """
        get yaml file config utility

        Args:
            keyname (str): file basename

        Returns:
            dict: dictionary of configs
        """
        files = glob(f"{self.config_path}/*.yml")
        files_dict = {os.path.basename(i).replace(".yml", ""): i for i in files}
        fpath = files_dict.get(keyname, "DEFAULT_PATH")

        # print(f"loading config from {fpath}")

        with open(fpath, "r") as stream:
            try:
                config = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)

        return config

    def get_data_root(self):
        DATA_ROOT = os.environ.get("DATA_ROOT")
        return DATA_ROOT

    def get_global_data_root(self):
        GLOBAL_DATA_ROOT = os.environ.get("GLOBAL_DATA_ROOT")
        return GLOBAL_DATA_ROOT

    def get_project_root(self):
        PROJECT_ROOT = os.environ.get("PROJECT_ROOT")
        return PROJECT_ROOT

    @staticmethod
    def path_exists(path):
        return os.path.exists(path)

    @staticmethod
    def fil_nan_with_list(df, col, list_fill):
        series = df[col]
        idx = series.isna()
        series[idx] = series[idx].apply(lambda x: list_fill)
        return series

    @staticmethod
    def make_directory_structure(local_paths:list=None, global_paths:list=None):

        if local_paths is not None:
            for p in local_paths:
                os.makedirs(f"{os.environ.get('DATA_ROOT')}/{p}", exist_ok=True)

        if global_paths is not None:
            for p in global_paths:
                os.makedirs(f"{os.environ.get('GLOBAL_DATA_ROOT')}/{p}", exist_ok=True)


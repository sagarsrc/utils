"""
common utils
"""

import os

import yaml
from glob import glob


class CommonUtils:
    def __init__(self, project_root=os.path.abspath(os.curdir), verbose=False):
        self.project_root = project_root

        self.config_path = f"""{project_root}/config"""
        self.data_root = f"""{project_root}/data_root"""
        self.config_files = glob(f"{self.config_path}/*")

        if verbose:
            print("~" * 30)
            print(f"setting paths")
            print(f"project_root {self.project_root}")
            print(f"config_path {self.config_path}")
            print(f"config_path {self.data_root}\n")
            print(f"config files {self.config_files}")
            print("~" * 30)

    def get_yml_config(self, keyname: str):
        """
        get yaml file config utility

        Args:
            keyname (str): file basename

        Returns:
            dict: dictionary of configs
        """

        files_dict = {
            os.path.basename(i).replace(".yml", ""): i for i in self.config_files
        }
        fpath = files_dict.get(keyname, "__DEFAULT__")

        with open(fpath, "r") as stream:
            try:
                config = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)

        return config

    def get_data_root(self):
        return self.data_root

    def get_project_root(self):
        return self.project_root

    def make_directory_structure(self, local_paths: list = None):
        if local_paths is not None:
            for p in local_paths:
                os.makedirs(f"{self.data_root}/{p}", exist_ok=True)

    @staticmethod
    def does_path_exist(path):
        return os.path.exists(path)

    @staticmethod
    def fil_nan_with_list(df, col, list_fill):
        series = df[col]
        idx = series.isna()
        series[idx] = series[idx].apply(lambda x: list_fill)
        return series

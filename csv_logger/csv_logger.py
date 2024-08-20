import pandas as pd
from typing import List, Dict
import csv
import os
import glob


class CSVLoader:
    def __init__(self, path: str):
        self.path = path

    def get_dfs(self):
        return {
            os.path.splitext(os.path.basename(file))[0]: pd.read_csv(file)  # { Module name : Dataframe }
            for file in glob.glob(os.path.join(self.path, "*.csv"))
        }
    
    def get_combined_df(self):
        dfs = self.get_dfs()
        combined = dfs[0]
        for df in dfs[1:]:
            combined = combined.merge(df, on='time')
        return combined


class LoggingModule:
    def __init__(self, path: str, keys: List[str]) -> None:
        self.file = open(path, 'w', newline='')
        self.keys = keys

        self.writer = csv.DictWriter(self.file, fieldnames=keys)
        self.writer.writeheader()

    def log(self, time, data):
        if diff := set(data.keys()) - set(self.keys):
            raise ValueError(f"module {self.path}: missing keys {diff}")
        data["time"] = time
        self.writer.writerow(data)

    def __del__(self):
        self.file.close()


class CSVLogger:
    def __init__(self, log_dir: str):
        if not os.path.exists(log_dir):
            os.mkdir(log_dir)
        self.log_dir = log_dir
        self.modules = {}

    def log(self, time, data: Dict[str, Dict]):
        for module_name, module_data in data.items():
            if module_name not in self.modules:
                self.modules[module_name] = LoggingModule(
                    os.path.join(self.log_dir, module_name, ".csv"), 
                    list(module_data.keys())
                )

            self.modules[module_name].log(time, module_data)

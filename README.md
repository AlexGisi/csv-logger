# csv-logger
Log data into different csv files with a common index.

# Installation
Install locally by cloning the repo and running `pip install .` in the root directory.

# Use
Save data into multiple files with a common index.
```
from csv_logger import CSVLogger

logger = CSVLogger(log_dir='logs')

# Log data into the temperature_sensor and motion_sensor files.
logger.log(time=1, data={
    'temperature_sensor': {'temperature': 22.5, 'humidity': 45},
    'motion_sensor': {'motion_detected': False, 'motion_intensity': 0}
})

logger.log(time=2, data={
    'temperature_sensor': {'temperature': 23.0, 'humidity': 50},
    'motion_sensor': {'motion_detected': True, 'motion_intensity': 5}
})
```
Easily load them.
```
from csv_logger import CSVLoader

loader = CSVLoader(path='path/to/csv_files')

# Load all CSV files as pandas DataFrames in a dictionary
dataframes = loader.get_dfs()

for name, df in dataframes.items():
    print(f"{name} DataFrame:")
    print(df)

# Combine all DataFrames based on the 'time' column
combined_df = loader.get_combined_df()
print("Combined DataFrame:")
print(combined_df)
```

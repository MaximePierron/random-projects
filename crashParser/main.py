import os
import pandas as pd
from pathlib import Path
from datetime import datetime
import re
# this should be a requirement I think it is not used per se but needs to be installed to create an xlsx
import openpyxl

crash_logs = 'crash_logs'
crash_logs_list = []

for crash_log in os.listdir(crash_logs):
    match = re.search(r'\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}', crash_log)
    if match:
        timestamp = match.group(0)
        datetime_obj = datetime.strptime(timestamp, "%Y-%m-%d_%H-%M-%S")
    else:
        timestamp = crash_log

    df = pd.read_json(Path(crash_logs) / Path(crash_log))
    df_normalized = pd.json_normalize(df.to_dict(orient='records'))[['apps.state', 'apps.restart counter']]
    df_normalized.columns = [f"{timestamp}", f"restart counter"]
    df_normalized = df_normalized.set_index(df.index)
    crash_logs_list.append(df_normalized)

result = pd.concat(crash_logs_list, axis=1)

# Keep only the last "restart counter" column
result = result.iloc[:, [i for i in range(result.shape[1]) if i % 2 == 0 or i == result.shape[1] - 1]]

result.to_excel('output.xlsx')

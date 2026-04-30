import pandas as pd

def parse_log(file_path):
    logs = []
    with open(file_path, "r") as f:
        for line in f:
            parts = line.strip().split(" ", 3)
            if len(parts) < 4:
                continue
            timestamp = parts[0] + " " + parts[1]
            level = parts[2]
            message = parts[3]

            logs.append({
                "timestamp": timestamp,
                "level": level,
                "message": message
            })

    return pd.DataFrame(logs)

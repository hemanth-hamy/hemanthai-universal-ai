
import pandas as pd

def load_logs():
    # Dummy logs for prototype
    return pd.DataFrame([
        {"timestamp": "2025-07-25 12:00", "user": "hemanth", "event": "Diagnosed GL error"},
        {"timestamp": "2025-07-25 12:15", "user": "hemanth", "event": "Viewed Logs"}
    ])

def export_logs(df):
    df.to_csv("diagnostic_logs.csv", index=False)

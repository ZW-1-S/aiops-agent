def detect_anomalies(df):
    anomalies = df[df['level'].isin(['ERROR', 'WARN'])]
    anomaly_ratio = len(anomalies) / len(df)
    return anomalies, anomaly_ratio

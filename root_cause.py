def analyze_root_cause(anomalies):
    causes = []

    for msg in anomalies['message']:
        if "Database" in msg:
            causes.append("数据库连接异常")
        elif "Timeout" in msg:
            causes.append("接口调用超时")
        elif "memory" in msg.lower():
            causes.append("内存不足")
        else:
            causes.append("未知问题")

    return causes

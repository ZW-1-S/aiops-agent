def suggest_fix(causes):
    solutions = []

    for c in causes:
        if c == "数据库连接异常":
            solutions.append("检查数据库服务是否启动，网络是否通畅")
        elif c == "接口调用超时":
            solutions.append("检查API服务负载或增加超时配置")
        elif c == "内存不足":
            solutions.append("增加内存或优化程序")
        else:
            solutions.append("建议进一步排查日志")

    return solutions

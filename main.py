from log_parser import parse_log
from anomaly_detector import detect_anomalies
from root_cause import analyze_root_cause
from fixer import suggest_fix

def main():
    print("🚀 AIOps Agent 启动...\n")

    df = parse_log("sample.log")
    print("📄 日志解析完成")
    print(df, "\n")

    anomalies, ratio = detect_anomalies(df)
    print(f"⚠️ 异常比例: {ratio*100:.2f}%")
    print(anomalies, "\n")

    causes = analyze_root_cause(anomalies)
    print("🔍 根因分析结果:")
    for c in causes:
        print("-", c)

    fixes = suggest_fix(causes)
    print("\n🛠 修复建议:")
    for f in fixes:
        print("-", f)

if __name__ == "__main__":
    main()

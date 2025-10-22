from datetime import datetime

# 実行ログファイル
log_file = "execution_log.txt"

# 現在時刻を取得
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# ファイルに追記
with open(log_file, "a") as f:
    f.write(f"Script executed at {now}\n")

print(f"Execution logged at {now}")

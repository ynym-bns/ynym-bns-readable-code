# 実行方法: $python print_better.py
# 出力: 上手

with open("dictionary-data.txt", "r", encoding="utf-8") as f:
    for row in f: # 行ごとにファイルを読み込む
        print(row, end="")
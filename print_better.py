# 実行方法: $python print_better.py
# 出力: 上手

with open("dictionary-data.txt", "r", encoding="utf-8") as f:
    for row in f: # 後に行ごとに読み込む可能性を考慮し、for文でファイルの中身を行ごとに分割
        print(row)
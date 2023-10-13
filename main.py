# 実行方法: $python print_better.py
# 出力: 上手

def main():
    with open("dictionary-data.txt", "r", encoding="utf-8") as f:
        for row in f: # 行ごとにファイルを読み込む
            print(row, end="")

if __name__ == "__main__":
    main()
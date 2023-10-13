# 実行方法: $python print_better.py
"""
出力例:
1: 上手
2: 一時
3: 市場
"""

def main():
    with open("dictionary-data.txt", "r", encoding="utf-8") as f:
        for i, row in enumerate(f): # 行ごとにファイルを読み込む
            row_num = i + 1 # i = 0, 1, 2 ...より現在の行には i + 1 が必要
            print(f'{row_num}: {row}', end="") # 行数: 内容 で出力

if __name__ == "__main__":
    main()
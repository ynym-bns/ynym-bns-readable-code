# 実行方法: $python print_better.py
"""
出力例:
1: 上手
2: 一時
3: 市場
"""


import argparse


def main(args):
    _id = args.id
    with open("dictionary-data.txt", "r", encoding="utf-8") as f:
        for i, row in enumerate(f): # 行ごとにファイルを読み込む
            row_num = i + 1 # i = 0, 1, 2 ...より現在の行には i + 1 が必要
            if _id is None: # idが未指定
                print(f'{row_num}: {row}', end="")
            elif row_num == int(args.id): # 指定したIDの単語
                print(f'{row_num}: {row}', end="") # 行数: 内容 で出力
            else: # 指定したID以外の単語は表示しない
                continue            
            

if __name__ == "__main__":
    parser = argparse.ArgumentParser() # descriptionは必要に応じて書くこと

    parser.add_argument("--id", help="単語IDの指定")

    args = parser.parse_args()
    main(args)
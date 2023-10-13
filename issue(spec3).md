<h1>将来的に変更されると思われるコード部分の実装に関する説明<h1>

# コード

```
# 実行方法: $python print_better.py
# 出力: 上手

with open("dictionary-data.txt", "r", encoding="utf-8") as f:
    for row in f: # 後に行ごとに読み込む可能性を考慮し、for文でファイルの中身を行ごとに分割
        print(row)
```

# 理由
今回では"上手"と書かれた1行読むだけでよいのでfor文を用いる必要はないが、
将来的に複数読むことを考慮し、for row in f: とした。<br>
またこの実装に関する意図をコメントで説明している。
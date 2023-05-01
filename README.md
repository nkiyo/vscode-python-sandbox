# ptvsd によるリモートデバッグで attach させるためのアプリ起動コマンド

```
python -m ptvsd --host 0.0.0.0 --port 5678 --wait -m sample.py
python -m ptvsd --host 0.0.0.0 --port 5678 --wait -m flask --app sample run
```

参考 => https://qiita.com/kenma/items/c46804a30f83bbfc18c8
ptvsd というのを使うのがポイント

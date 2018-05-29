# katate-lr2ir
片手LR2IR

## Environment
- 管理ツール
    - Django 2.0.5
    - Python 3.6.2
    - postgreSQL
- みるやつ
    - 未定
    - postgreSQL

### Django
`DATABASES` は `local_settings.py` に書く。

## Commands
発狂難易度表のBMSを抽出（完成？）
```
python manage.py insane_bms
```

LR2IRからスコアデータを収集、データベースに登録（作成中）
```
python manage.py lr2ir
```

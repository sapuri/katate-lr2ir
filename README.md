# katate-lr2ir
片手LR2IR

## Environment
- Django 2.0.5
- Python 3.6.2
- postgreSQL
- jQuery 3.3.1
- bootstrap 4.1.1

### Django
`DATABASES` は `local_settings.py` に書く。

## Commands
発狂難易度表のBMSを抽出、データベースに登録（できた）
```
python manage.py insane_bms
```

LR2IRからスコアデータを収集、データベースに登録（できた）
```
python manage.py lr2ir
```

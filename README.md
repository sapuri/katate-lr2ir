# katate-lr2ir
片手LR2IR

LR2IR - `http://www.dream-pro.info/~lavalse/LR2IR/search.cgi`

から、片手プレイヤーのスコアデータを抽出します。

## Environment
- 管理サイト・ランキングページ
  - Django 2.0.5
  - Python 3.6.2
  - postgreSQL, MariaDB
  - jQuery 3.3.1
  - bootstrap 4.1.1

### Django
`DATABASES` は `local_settings.py` に書く

## Commands
発狂難易度表のBMSを抽出、データベースに登録
```
python manage.py insane_bms
```

LR2IRからスコアデータを収集、データベースに登録
```
python manage.py lr2ir
```

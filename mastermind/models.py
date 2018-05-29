from django.db import models

class Bms(models.Model):
    level = models.CharField('レベル', max_length=8)
    genre = models.CharField('ジャンル', max_length=128)
    title = models.CharField('タイトル', max_length=128)
    bms_id = models.CharField('BMSID', max_length=8)
    artist = models.CharField('アーティスト', max_length=128)
    players = models.CharField('プレイ人数', max_length=8)

    def __str__(self):
        return self.bms_id

    class Meta:
        verbose_name = 'BMSデータ'
        verbose_name_plural = 'BMSデータ'

class Score(models.Model):
    bms_id = models.CharField('BMSID', max_length=8)
    player_name = models.CharField('プレイヤー名', max_length=16)
    clear_type = models.CharField('クリア状況', max_length=16)
    score_lank = models.CharField('スコアランク', max_length=8)
    score = models.CharField('スコアレート', max_length=32)
    combo = models.CharField('コンボ', max_length=16)
    bp = models.CharField('BP', max_length=8)
    pg = models.CharField('PG', max_length=8)
    gr = models.CharField('GR', max_length=8)
    gd = models.CharField('GD', max_length=8)
    bd = models.CharField('BD', max_length=8)
    pr = models.CharField('PR', max_length=8)

    def __str__(self):
        return self.bms_id

    class Meta:
        verbose_name = 'スコア'
        verbose_name_plural = 'スコア'

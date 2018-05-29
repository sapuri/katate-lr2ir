from django.db import models

class Score(models.Model):
    bms_id = models.CharField('BMSID', max_length=8)
    player_name = models.CharField('プレイヤー名', max_length=16)
    clear_type = models.CharField('クリア状況', max_length=8)
    score_lank = models.CharField('スコアランク', max_length=8)
    score = models.CharField('スコアレート', max_length=32)
    combo = models.CharField('コンボ', max_length=16)
    BP = models.CharField('BP', max_length=8)
    PG = models.CharField('PG', max_length=8)
    GR = models.CharField('GR', max_length=8)
    GD = models.CharField('GD', max_length=8)
    BD = models.CharField('BD', max_length=8)
    PR = models.CharField('PR', max_length=8)

    def __str__(self):
        return self.player_name

    class Meta:
        verbose_name = 'スコア'
        verbose_name_plural = 'スコア'

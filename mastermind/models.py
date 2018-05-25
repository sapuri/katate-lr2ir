from django.db import models

class Score(models.Model):
    bms_id = models.CharField('BMSID', max_length=255)
    player_name = models.CharField('プレイヤー名', max_length=255)
    clear_type = models.CharField('クリア状況', max_length=255)
    score_lank = models.CharField('スコアランク', max_length=255)
    score = models.CharField('スコア', max_length=255)
    combo = models.CharField('コンボ', max_length=255)
    BP = models.CharField('BP', max_length=255)
    PG = models.CharField('PG', max_length=255)
    GR = models.CharField('GR', max_length=255)
    GD = models.CharField('GD', max_length=255)
    BD = models.CharField('BD', max_length=255)
    PR = models.CharField('PR', max_length=255)

    def __str__(self):
        return self.bms_id

    class Meta:
        verbose_name = 'スコア'
        verbose_name_plural = 'スコア'

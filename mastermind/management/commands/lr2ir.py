import codecs
import requests
import time

from bs4 import BeautifulSoup
from django.core.management import BaseCommand
from mastermind.models import Player
from mastermind.models import Bms
from mastermind.models import Score

class Command(BaseCommand):
    help = 'スコアデータを取得、データベース登録'

    def handle(self, *args, **options):
        self.init_database()

        #bms_list取得
        bms_list = []
        b = Bms.objects.all()
        for bms in b:
            bms_list.append([bms.bms_id, bms.players])

        #player_id_list取得
        player_id_list = []
        p = Player.objects.all()
        for player in p:
            player_id_list.append(player.player_id)

        #スコアデータの取得
        for bms_data in bms_list:
            bms_id = int(bms_data[0])
            players = int(bms_data[1])
            print(f'BMSID: {bms_id}')

            pages = (players // 100) + 1
            for i in range(1, pages + 1):
                print(f'Page: {i}')
                target_url = f'http://www.dream-pro.info/~lavalse/LR2IR/search.cgi?mode=ranking&page={i}&bmsid={bms_id}'
                score_list = self.scrape(target_url, player_id_list)
                self.update_database(bms_id, score_list)

    @staticmethod
    def scrape(url: str, player_id_list: list) -> list:
        """
        player_id_listに載っている人のスコアデータを取得
        :param url:
        :param player_id_list:
        :return: score list
        """
        time.sleep(1)
        resp = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        content_type_encoding = resp.encoding if resp.encoding != 'ISO-8859-1' else None
        soup = BeautifulSoup(resp.content, 'html.parser', from_encoding=content_type_encoding)

        table = soup.find_all('table')[3]
        rows = table.find_all('tr')

        #指定プレイヤーIDのスコアデータ抽出
        score_data = []
        for row in rows:
            id_cell = row.find(['a'])
            if id_cell:
                player_id = id_cell.get('href').replace('search.cgi?mode=mypage&playerid=', '')
                if player_id not in player_id_list:
                    continue
            for cell in row.find_all(['td', 'th'], attrs={'class': ''}):
                score_data.append(cell.get_text())

        #抽出したスコアデータを整形
        del score_data[0:17]
        score_list = [score_data[i:i+17] for i in range(0, len(score_data), 17)]

        return score_list

    @staticmethod
    def init_database():
        """
        database 初期化
        """
        s = Score.objects.all()
        s.delete()

    @staticmethod
    def update_database(bms_id: str, score_list: list):
        """
        database 登録
        :param score_list:
        """
        for score in score_list:
            s = Score(bms_id=bms_id, player_name=score[1], clear_type=score[3],
            score_rank=score[4], score=score[5], combo=score[6], bp=score[7],
            pg=score[8], gr=score[9], gd=score[10], bd=score[11], pr=score[12])
            s.save()

import csv

import requests
from bs4 import BeautifulSoup
from django.core.management import BaseCommand

class Command(BaseCommand):
    help = 'コマンド作成テスト'

    def handle(self, *args, **options):
        file_path = './csv/airgod.csv'
        #self.init_csv(file_path)

        player_id_list = ['9829']
        players = 195
        pages = (players // 100) + 1

        bms_id = 241245
        for i in range(1, pages + 1):
            print(f'Page: {i}')
            target_url = f'http://www.dream-pro.info/~lavalse/LR2IR/search.cgi?mode=ranking&page={i}&bmsid={bms_id}'
            score_list = self.scrape(target_url, player_id_list)
            print(score_list)

    @staticmethod
    def scrape(url: str, player_id_list: list) -> list:
        """
        player_id_listに載っている人のスコアデータを取得
        :param url:
        :param player_id_list:
        :return: score list
        """
        resp = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(resp.text, 'lxml')

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
                if cell.get_text():
                    score_data.append(cell.get_text())

        #抽出したスコアデータを分割、整形
        score_list = [score_data[i:i+19] for i in range(0, len(score_data), 19)]
        score_list.pop(0)

        return score_list

    @staticmethod
    def init_csv(file_path: str):
        """
        CSV を初期化
        :param file_path:
        """
        with open(file_path, 'w') as f:
            writer = csv.writer(f, lineterminator='\n')
            writer.writerow(['サイト名', 'URL'])

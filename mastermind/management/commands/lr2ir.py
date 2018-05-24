import csv
import codecs

import requests
from bs4 import BeautifulSoup
from django.core.management import BaseCommand

class Command(BaseCommand):
    help = '楽曲ごとのプレイデータを取得、CSV出力'

    def handle(self, *args, **options):
        bms_list_file_path = './csv/insane_bms_list.csv'
        bms_list = []
        with codecs.open(bms_list_file_path, 'r', 'cp932') as f:
            reader = csv.reader(f)
            header = next(reader)
            for row in reader:
                bms_list.append([row[3], row[5]])

        player_id_list = ['132784', '54253', '60153']
        for bms_data in bms_list:
            bms_id = int(bms_data[0])
            players = int(bms_data[1])
            print(f'BMSID: {bms_id}')

            file_path = f'./csv/{bms_id}.csv'
            self.init_csv(file_path)

            pages = (players // 100) + 1
            for i in range(1, pages + 1):
                print(f'Page: {i}')
                target_url = f'http://www.dream-pro.info/~lavalse/LR2IR/search.cgi?mode=ranking&page={i}&bmsid={bms_id}'
                score_list = self.scrape(target_url, player_id_list)
                self.export2csv(file_path, score_list)

    @staticmethod
    def scrape(url: str, player_id_list: list) -> list:
        """
        player_id_listに載っている人のスコアデータを取得
        :param url:
        :param player_id_list:
        :return: score list
        """
        resp = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(resp.content.decode('cp932'), 'lxml')

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
    def init_csv(file_path: str):
        """
        CSV を初期化
        :param file_path:
        """
        with open(file_path, 'w') as f:
            writer = csv.writer(f, lineterminator='\n')
            writer.writerow(['順位', 'プレイヤー名', '段位', 'クリア', 'ランク',
            'スコア', 'コンボ', 'B+P', 'PG', 'GR', 'GD', 'BD', 'PR', 'OP',
            'OP', 'INPUT', '本体'])

    @staticmethod
    def export2csv(file_path: str, score_list: list):
        """
        CSV エクスポート
        :param file_path:
        :param score_list:
        """
        with codecs.open(file_path, 'a', 'cp932') as f:
            writer = csv.writer(f, lineterminator='\n')
            for score in score_list:
                writer.writerow(score)

import csv
import codecs
import requests
import time

from bs4 import BeautifulSoup
from django.core.management import BaseCommand
from mastermind.models import Bms

class Command(BaseCommand):
    help = '発狂BMSのリストを取得、CSV出力'

    def handle(self, *args, **options):
        self.init_database()
        file_path = './csv/insane_bms_list.csv'
        # self.init_csv(file_path)

        for i in range(1, 26):
            print(f'Page: {i}')
            target_url = f'http://www.dream-pro.info/~lavalse/LR2IR/search.cgi?mode=search&type=insane&exlevel={i}&7keys=1'
            bms_list = self.scrape(target_url)
            # self.export2csv(file_path, bms_list)
            self.update_database(bms_list)

    @staticmethod
    def scrape(url: str) -> list:
        """
        指定URL上のBMSリストを取得
        :param url:
        :return: bms list
        """
        time.sleep(1)
        resp = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(resp.content.decode('cp932'), 'lxml')

        table = soup.find_all('table')[0]
        rows = table.find_all('tr')

        #BMSリストの抽出
        bms_list = []
        for row in rows:
            for cell in row.find_all(['a', 'td', 'th']):
                if cell.get('href'):
                    bms_list.append(cell.get('href').replace('search.cgi?mode=ranking&bmsid=', ''))
                else:
                    bms_list.append(cell.get_text())

        #抽出したBMSリストを整形
        del bms_list[0:8]
        bms_list = [data.replace('SP★', '') for data in bms_list]
        bms_list = [bms_list[i:i+9] for i in range(0, len(bms_list), 9)]

        return bms_list

    @staticmethod
    def init_csv(file_path: str):
        """
        CSV を初期化
        :param file_path:
        """
        with open(file_path, 'w') as f:
            writer = csv.writer(f, lineterminator='\n')
            writer.writerow(['レベル', 'ジャンル', 'タイトル', 'BMSID',  'アーティスト',
            'プレイ人数', 'クリア人数', 'プレイ回数', '平均プレイ回数'])

    @staticmethod
    def export2csv(file_path: str, bms_list: list):
        """
        CSV エクスポート
        :param file_path:
        :param bms_list:
        """
        with codecs.open(file_path, 'a', 'cp932') as f:
            writer = csv.writer(f, lineterminator='\n')
            for bms in bms_list:
                writer.writerow(bms)

    @staticmethod
    def init_database():
        """
        database 初期化
        """
        b = Bms.objects.all()
        b.delete()

    @staticmethod
    def update_database(bms_list: list):
        """
        database 登録
        :param bms_list:
        """
        for bms in bms_list:
            b = Bms(level=bms[0], genre=bms[1], title=bms[2],
            bms_id=bms[3], artist=bms[4], players=bms[5])
            b.save()

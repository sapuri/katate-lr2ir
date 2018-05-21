import csv

import requests
from bs4 import BeautifulSoup
from django.core.management import BaseCommand

class Command(BaseCommand):
    help = 'コマンド作成テスト'

    def handle(self, *args, **options):
        print('test')

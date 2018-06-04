from django.shortcuts import render
from django.http import HttpResponse

from mastermind.models import Player
from mastermind.models import Bms
from mastermind.models import Score

def bms_list(request, level='1'):
    b = Bms.objects.filter(level=level)
    return render(request, 'ranking/bms_list.html', {'bms_list': b})

def bms_ranking(request, bms_id):
    b = Bms.objects.filter(bms_id=bms_id).first()
    s = Score.objects.filter(bms_id=bms_id)
    return render(request, 'ranking/bms_ranking.html', {'bms_data': b, 'score_list': s})

def players(request):
    p = Player.objects.all()
    return render(request, 'ranking/players.html', {'player_list': p})

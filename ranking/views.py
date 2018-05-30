from django.shortcuts import render
from django.http import HttpResponse

from mastermind.models import Player
from mastermind.models import Bms
from mastermind.models import Score

def bms_ranking(request, bms_id):
    b = Bms.objects.filter(bms_id__contains=bms_id)
    s = Score.objects.filter(bms_id__contains=bms_id)
    return render(request, 'ranking/bms_ranking.html', {'bms_data': b, 'score_list': s})

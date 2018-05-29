from django.shortcuts import render

from mastermind.models import Score

def index(request):
    score_list = Score.objects.order_by('bms_id')[:5]
    context = {
        'score_list': score_list,
    }
    return render(request, 'mastermind/index.html', context)

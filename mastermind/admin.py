from django.contrib import admin

from .models import Player
from .models import Bms
from .models import Score

admin.site.register(Player)
admin.site.register(Bms)
admin.site.register(Score)

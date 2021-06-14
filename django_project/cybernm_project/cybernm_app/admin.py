from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(discipline)
admin.site.register(tournament)
admin.site.register(tournament_participation)
admin.site.register(news)





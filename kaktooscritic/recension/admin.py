from django.contrib import admin

from recension.models import User, Film, Recension, Genre, Grade

admin.register(User)
admin.register(Film)
admin.register(Recension)
admin.register(Genre)
admin.register(Grade)

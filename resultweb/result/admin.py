# myapp/admin.py

from django.contrib import admin
from .models import Quiz,YoungDS,Sql,It_manager,Datashark,Ciphertrail,Mobilelegends

@admin.register(Quiz)
class TeamAdmin1(admin.ModelAdmin):
    list_display = ('name', 'college', 'team_leader', 'points')

@admin.register(YoungDS)
class TeamAdmin2(admin.ModelAdmin):
    list_display = ('name', 'college', 'participant1', 'participant2')

@admin.register(Sql)
class TeamAdmin3(admin.ModelAdmin):
    list_display = ('name', 'college', 'points')

@admin.register(It_manager)
class TeamAdmin4(admin.ModelAdmin):
    list_display = ('name', 'college', 'team_leader', 'points')

@admin.register(Datashark)
class TeamAdmin5(admin.ModelAdmin):
    list_display = ('name', 'college', 'team_leader', 'points')

@admin.register(Ciphertrail)
class TeamAdmin6(admin.ModelAdmin):
    list_display = ('name', 'college', 'team_leader')

@admin.register(Mobilelegends)
class TeamAdmin7(admin.ModelAdmin):
    list_display = ('name', 'college', 'team_leader', 'points')

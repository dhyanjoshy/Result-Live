from django.db import models

# Create your models here.
class Quiz(models.Model):
    name = models.CharField(max_length=255)
    college = models.CharField(max_length=255)
    team_leader = models.CharField(max_length=255)
    final = models.BooleanField(default=False)
    points = models.IntegerField()

    def __str__(self):
        return self.name
    
class YoungDS(models.Model):
    name = models.CharField(max_length=255)
    college = models.CharField(max_length=255)
    participant1 = models.CharField(max_length=255)
    participant2 = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Sql(models.Model):
    name = models.CharField(max_length=255)
    college = models.CharField(max_length=255)
    points = models.IntegerField()

    def __str__(self):
        return self.name
    
class It_manager(models.Model):
    name = models.CharField(max_length=255)
    college = models.CharField(max_length=255)
    team_leader = models.CharField(max_length=255)
    final = models.BooleanField(default=False)
    points = models.IntegerField()

    def __str__(self):
        return self.name
    
class Datashark(models.Model):
    name = models.CharField(max_length=255)
    college = models.CharField(max_length=255)
    team_leader = models.CharField(max_length=255)
    points = models.IntegerField()

    def __str__(self):
        return self.name
    
class Ciphertrail(models.Model):
    name = models.CharField(max_length=255)
    college = models.CharField(max_length=255)
    team_leader = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Mobilelegends(models.Model):
    name = models.CharField(max_length=255)
    college = models.CharField(max_length=255)
    team_leader = models.CharField(max_length=255)
    points = models.IntegerField()

    def __str__(self):
        return self.name
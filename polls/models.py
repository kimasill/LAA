from django.db import models

class Character(models.Model):
    #Caracter_name = models.CharField(max_length=12)
    def __str__(self):
        return self.character_text

class Amories(models.Model):
    #Character = models.ForeignKey(Character, on_delete=models.CASCADE)
    def __str__(self):
        return self.amories_text

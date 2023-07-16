from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#ganadores
class Winner(models.Model):
    client_id = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    draw = models.CharField(max_length=30)
    prize = models.CharField(max_length=30)
    def __str__(self):
        return f"id_cliente: {self.client_id} - nombre: {self.name} - apellido: {self.last_name} - draw: {self.draw} -prize: {self.prize}"
    #pwd = models.CharField(max_length=30)
    #pwd_question = models.CharField(max_length=30)

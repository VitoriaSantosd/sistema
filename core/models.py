from django.db import models
from django.contrib.auth.models import User

class Feriado(models.Model):
    data = models.DateField()
    descricao = models.CharField(max_length=255)
    nacional = models.BooleanField(default=True)

class Professor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1) 
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    nome = models.CharField(max_length=100)
    disponibilidade = models.BooleanField(default=False)

class Aula(models.Model):
    data = models.DateField()
    curso = models.CharField(max_length=100)
    descricao = models.CharField(max_length=255)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    sala = models.CharField(max_length=10)
    turno = models.CharField(max_length=10, choices=[('Manhã', 'Manhã'), ('Tarde', 'Tarde'), ('Noite', 'Noite')])
    periodo = models.CharField(max_length=50)

class Curso(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Periodo(models.Model):
    numero = models.PositiveIntegerField()  # Representa o semestre (1-10)

    def __str__(self):
        return f"{self.numero}º semestre"

class Turno(models.Model):
    nome = models.CharField(max_length=50)  # Manhã, Tarde ou Noite

    def __str__(self):
        return self.nome

class Sala(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
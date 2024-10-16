from django.db import models

# Create your models here.
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

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    disponibilidade = models.BooleanField(default=True)  # Presente ou ausente

    def __str__(self):
        return self.nome

class Sala(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Feriado(models.Model):
    data = models.DateField()
    descricao = models.CharField(max_length=100)
    nacional = models.BooleanField(default=True)  # Nacional ou Regional

    def __str__(self):
        return self.descricao

class Aula(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    turno = models.ForeignKey(Turno, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    data = models.DateField()
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.curso} - {self.descricao} - {self.data}"
    
class CalendarioFiltrado(models.Model):
    nome = models.CharField(max_length=100)
    data = models.DateField()

class CalendarioGeral(models.Model):
    nome = models.CharField(max_length=100)
    data = models.DateField()
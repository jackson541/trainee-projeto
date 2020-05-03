from django.db import models

# Create your models here.

class Especialidade (models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    descricao = models.TextField(verbose_name='Descrição')
    imagem = models.ImageField(upload_to='especialidades')

    def __str__ (self):
        return self.nome

    class Meta:
        ordering = ['nome']


class Consulta (models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=100)
    especialidade = models.ForeignKey('Especialidade', on_delete=models.PROTECT)
    data = models.CharField(max_length=10)

    turnos = [
        ('manha', 'Manhã'),
        ('tarde', 'Tarde')
    ]

    turno = models.CharField(max_length=10, choices=turnos, default='manha')
    info_adicionais = models.TextField(blank=True)
    respondida = models.BooleanField()

    def __str__ (self):
        valor = "[Respondida] " if self.respondida else "[Em espera] "
        return valor + self.email

    class Meta:
        ordering = ['respondida', 'id']


class QuemSomos (models.Model):
    missao = models.TextField(verbose_name='Missão')
    visao = models.TextField(verbose_name='Visão')
    valores = models.TextField()

    class Meta:
        verbose_name = 'Quem Somos'
        verbose_name_plural = 'Quem Somos'
from django.db import models

def __str__(self):
    return self.nome

class TD_categorias(models.Model):
    nome_categoria = models.CharField(max_length=20)
    def __str__(self):
        return(self.nome_categoria)

class TB_psicologos(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.IntegerField(primary_key=True)
    registro_crp = models.IntegerField()
    email = models.EmailField()
    senha = models.CharField(max_length=18)
    telefone = models.IntegerField()
    def __str__(self):
        return(self.nome)

class TB_salas(models.Model):
    cod_sala = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    admin = models.ForeignKey(TB_psicologos, on_delete=models.CASCADE)
    descricao = models.TextField()
    categoria = models.ForeignKey(TD_categorias, on_delete=models.CASCADE)

class TB_participantes(models.Model):
    email = models.EmailField()
    senha = models.CharField(max_length=18)
    nome = models.CharField(max_length=100)
    cpf = models.IntegerField(primary_key=True)
    telefone = models.IntegerField()
    disturbio = models.TextField(null=True, blank=True)
    sala_inserido = models.ForeignKey(TB_salas, on_delete=models.CASCADE, null=True)


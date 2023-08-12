from django.db import models

class Sabor(models.Model):
    sabor= models.CharField(max_length=50)

    class Meta:
        verbose_name_plural= 'Sabores'

class Doces(models.Model):
    nome= models.CharField(max_length=40)
    descricao= models.CharField(max_length=40, verbose_name='Descrição')
    tamanho = models.FloatField(max_length=10)

    sabor= models.ForeignKey(Sabor, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome, self.descricao, self.sabor
    
    class Meta:
        verbose_name_plural= 'Doces'
    
class Bolos(models.Model):
    nome= models.CharField(max_length=40)
    descricao= models.CharField(max_length=40, verbose_name='Descrição')
    tamanho = models.FloatField(max_length=10)
    observacao= models.TextField(max_length=50, verbose_name='Observações', blank=True)

    sabor= models.ForeignKey(Sabor, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome, self.descricao,self.sabor, format(self.tamanho)
    
    class Meta:
        verbose_name_plural= 'Bolos'

class Macarons(models.Model):
    nome= models.CharField(max_length=40)
    descricao= models.CharField(max_length=40, verbose_name='Descrição')
    tamanho = models.FloatField(max_length=10)

    sabor= models.ForeignKey(Sabor, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome, self.descricao,self.sabor
    
    class Meta:
        verbose_name_plural= 'Macarons'
    











    

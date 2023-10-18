from django.db import models

# Create your models here./Entidades
class Pessoa(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    
#USIPAV/Entidades
#Moegas
#Secador de Agregados
#Sistema de Pesagem
#Misturador
#Silo de Armazenamento de Mistura Pronta
#Sistema de Alimentação de Asfalto
#Sistema de Abastecimento de Combustível
#Sistema de Aditivos
#Elevador
#Esteira
#Sensor de Nível
#Sensor de Peso
#Sensor de Temperatura
#Célula de Carga
#Sensor de Fluxo
#Sensor de Velocidade

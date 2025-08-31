from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Estudiante(models.Model):
    CARRERAS = [
        ("Sistemas", "Sistemas"),
        ("Industrial", "Industrial"),
        ("Contabilidad", "Contabilidad"),
        ("Otro", "Otro"),
    ]

    nombre = models.CharField(max_length=100)
    carrera = models.CharField(max_length=30, choices=CARRERAS)
    ciclo = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])
    correo = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombre} ({self.carrera})"
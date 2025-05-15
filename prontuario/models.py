from distutils.command.clean import clean
from random import choices

from django.core.exceptions import ValidationError
from django.utils import timezone

from django.db import models

class Medico(models.Model):

    nome = models.CharField(
        max_length=200,
        help_text="Nome do medico",
        verbose_name="Nome Completo",
    )

    crm = models.CharField(
        max_length=12,
        unique=True,
        help_text="N° do conselho",
        verbose_name="CRM",
    )

    especialidades = models.CharField(
        choices=[('Cardiologista', 'Cardiologista'),
                 ('Neurologista', 'Neurologista'),
                 ('Pediatra', 'Pediatra')]
    )

    data_nascimento = models.DateField(
        help_text="ex: 01/01/2000",
        verbose_name="Data de Nascimento",
    )

    criado_em = models.DateTimeField(
        auto_now_add=True,
        auto_created=True,
        help_text="Criado em",
    )

    atualizado_em = models.DateField(auto_now=True)

    def clean(self):
        super().clean()

        if (timezone.now().year - self.data_nascimento.year) < 18:
            raise ValidationError("Muito novo para ser médico!")

        if len(self.nome) < 4:
            raise ValidationError("Nome precisa ter mas de 4 caracteres!")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Médico"
        verbose_name_plural = "Médicos"
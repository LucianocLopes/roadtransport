from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from core.models import TimeStampBase


USER = get_user_model()


class Record(TimeStampBase):
    TYPE_CHOICES = [
        ('P', _('Pessoa Física')),
        ('B', _('Pessoa Jurídica')),
    ]
    """Model definition for Record."""
    record_type = models.CharField(_("Tipo de Registro"), max_length=1, choices=TYPE_CHOICES)
    
    class Meta:
        """Meta definition for Record."""

        verbose_name = 'Registro'
        verbose_name_plural = 'Registros'

    def __str__(self):
        """Unicode representation of Record."""
        return self.id


class Business(Record):
    """Model definition for Business."""
    name = models.CharField(_("Razão Social"), max_length=254)
    fantasy_name = models.CharField(_("Fantasia"), max_length=150)
    cnpj_number = models.CharField(_("CNPJ"), max_length=14, unique=True)
        
    class Meta:
        """Meta definition for Business."""

        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        """Unicode representation of Business."""
        return f'{self.id} {self.name}'


class Person(Record):
    """Model definition for People."""

    first_name = models.CharField(_("Primeiro Nome"), max_length=50)
    last_name = models.CharField(_("Sobrenome"), max_length=70)
    cpf_number = models.CharField(_("CPF"), max_length=11, unique=True)
    
    class Meta:
        """Meta definition for People."""

        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'

    @property
    def full_name(self):
        return f'{self.first_name.title()} {self.last_name.title()}'
    
    def __str__(self):
        """Unicode representation of People."""
        return f'{self.id} - {self.full_name}'

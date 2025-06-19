from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from core.models import TimeStampBase


USER = get_user_model()


class Country(TimeStampBase):
    """Model definition for Country."""
    name = models.CharField(_("Nome"), max_length=50)

    class Meta:
        """Meta definition for Country."""

        verbose_name = _('País')
        verbose_name_plural = ('Países')

    def __str__(self):
        """Unicode representation of Country."""
        return self.name.upper()


class State(TimeStampBase):
    """Model definition for State."""
    name = models.CharField(_("Nome"), max_length=50)
    country = models.ForeignKey(
        Country, 
        verbose_name=_("País"), 
        on_delete=models.CASCADE,
    )
    
    class Meta:
        """Meta definition for State."""

        verbose_name = _('Estado')
        verbose_name_plural = _('Estados')

    def __str__(self):
        """Unicode representation of State."""
        return self.name.title()


class City(TimeStampBase):
    """Model definition for City."""
    name = models.CharField(_("Nome"), max_length=50)
    state = models.ForeignKey(
        State, 
        verbose_name=_("Estado"), 
        on_delete=models.CASCADE,
    )    
    class Meta:
        """Meta definition for City."""

        verbose_name = _('Cidade')
        verbose_name_plural = _('Cidades')

    def __str__(self):
        """Unicode representation of City."""
        return self.name.title()


class Address(TimeStampBase):
    """Model definition for Address."""
    address = models.CharField(_("Endereço"), max_length=100)
    district = models.CharField(_("Bairro"), max_length=50)
    zip_code = models.CharField(_("CEP"), max_length=8)
    city = models.ForeignKey(
        City, 
        verbose_name=_("Cidade"), 
        on_delete=models.CASCADE,
    )

    class Meta:
        """Meta definition for Address."""

        verbose_name = _('Endereço')
        verbose_name_plural = _('Endereços')

    def __str__(self):
        """Unicode representation of Address."""
        return f'{self.zip_code} - {self.address.title()} - {self.district.title()}'

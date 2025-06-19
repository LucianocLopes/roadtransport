from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

USER = get_user_model()


class TimeStampBase(models.Model):
    create_by = models.ForeignKey(
        USER, 
        verbose_name=_("Criado por"), 
        on_delete=models.DO_NOTHING,
    )
    create = models.DateTimeField(_("Criado em"), auto_now=False, auto_now_add=True)
    modified = models.DateTimeField(_("Modificado em"), auto_now=True, auto_now_add=False)
    class Meta:
        abstract = True
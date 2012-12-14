# -*- coding: utf-8 -*-
#from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Server(models.Model):
    description = models.TextField(_('description'))
    ip = models.IPAddressField(_('ip address'))
    fqdn = models.CharField(_('name'), max_length=128, blank=True)

    class Meta:
        verbose_name = _("server")
        verbose_name_plural = _("servers")



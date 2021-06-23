from django.db import models
from django.utils.translation import gettext_lazy as _


class Math(models.Model):
    operation_name = models.CharField(_("Operation name"), max_length=50)
    func = models.TextField(
        _("Pass the python function with proper indentation"), max_length=50)

    class Meta:
        db_table = 'api_math_ops'
        ordering = ['-id']

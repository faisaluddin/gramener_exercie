from django.db import models
from django.utils.translation import gettext_lazy as _


class Math(models.Model):
    operation_name = models.CharField(_("Operation name"), max_length=50)
    description = models.TextField(
        _("Add description of the function"), blank=True, null=True)
    func = models.TextField(
        _("Pass the python function with proper indentation, make sure function name is same as operation name"), max_length=50)

    class Meta:
        db_table = 'api_math_ops'
        ordering = ['-id']

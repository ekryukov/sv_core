from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ReportConfig(AppConfig):
    name = 'core.rpt'
    verbose_name = _("Report")

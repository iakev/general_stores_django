from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "general_stores.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import general_stores.users.signals  # noqa F401
        except ImportError:
            pass

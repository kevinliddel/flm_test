import re

from django.core import validators
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


@deconstructible
class ASCIIUsernameValidator(validators.RegexValidator):
    regex = r'^[a-zA-Z]+\/(...)\/(....)'
    message = _(
        'Veuillez entrer un nom d\'utilisateur valide, ne contenant que des lettres, '
    )
    flags = re.ASCII

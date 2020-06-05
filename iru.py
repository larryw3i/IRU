
import locale
import gettext
from interfaces import mainui

default_locale  = locale.getdefaultlocale()[0]
default_locale = default_locale if len( default_locale ) > 0 else 'en_US'

_ = gettext.translation('iru', 'locale', [ default_locale ] )\
    .gettext

if __name__ == "__main__":
    mainui.main_ui()
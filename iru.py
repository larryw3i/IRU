
import os
import locale
import gettext
from ui import main_ui

default_locale  = locale.getdefaultlocale()[0]

if default_locale not in  os.listdir('locale'): default_locale = 'en_US'

_ = gettext.translation('iru', 'locale', [ default_locale ] )\
    .gettext

if __name__ == "__main__":
    main_ui.main_ui()
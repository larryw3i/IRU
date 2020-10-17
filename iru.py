
import os
import locale
import gettext
import sys
from ui.main_ui import main_ui
from pony import orm
import platform


if __name__ == "__main__":
    sys_argv = sys.argv
    if len( sys_argv ) == 1:
        main_ui()

    elif sys_argv[1] == 'msgfmt':
        if platform_system == "Linux":
            os.system('for i in $en_locale ;do msgfmt locale/$i/LC_MESSAGES/'+\
            'iru.po -o locale/$i/LC_MESSAGES/iru.mo ; done;')
            print('Compile .po files finish!')

        else:
            print( _('Add your command to compile .po files') )
    else: 
        print('(^_^)')
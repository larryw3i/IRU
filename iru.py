
import os
import locale
import gettext
import sys
from ui import main_ui
from pony import orm
import platform

default_locale  = locale.getdefaultlocale()[0]
platform_system = platform.system()

if default_locale not in  os.listdir('locale'): default_locale = 'en_US'

_ = gettext.translation('iru', 'locale', [ default_locale ] )\
    .gettext

root_path = os.getcwd()

db  = orm.Database()
db.bind(
    provider='sqlite', 
    filename= os.path.join( root_path, 'data', 'iru.db' ) , 
    create_db=True)

if __name__ == "__main__":
    sys_argv = sys.argv
    if len( sys_argv ) == 0:
        main_ui.main_ui()
    elif sys_argv[0] == 'msgfmt':
        if platform_system == "Linux":
            os.system('for i in $en_locale ;do msgfmt locale/$i/LC_MESSAGES/'+\
            'iru.po -o locale/$i/LC_MESSAGES/iru.mo ; done;')
        else:
            print( _('Add your command to compile .po files') )
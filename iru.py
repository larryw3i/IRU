
import os
import locale
import gettext
from ui import main_ui
from pony import orm

default_locale  = locale.getdefaultlocale()[0]

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
    main_ui.main_ui()
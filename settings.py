
import os
import locale
import gettext
import sys
from ui.main_ui import main_ui
from pony import orm
import platform

default_locale  = locale.getdefaultlocale()[0]

if default_locale not in  os.listdir('locale'): default_locale = 'en_US'

_ = gettext.translation('iru', 'locale', [ default_locale ] )\
    .gettext

platform_system = platform.system()

root_path = os.getcwd()
db_path =  os.path.join( root_path, 'data', 'iru.db' )

if not os.path.exists( db_path ):
    os.mkdir( root_path+'/data' )
    with open( db_path, 'w' ) as f: pass

db  = orm.Database()

db.bind(
    provider='sqlite', 
    filename= db_path , 
    create_db=True)
#!d:\homework\djangoapp1\life0\env\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'static3==0.7.0','console_scripts','static'
__requires__ = 'static3==0.7.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('static3==0.7.0', 'console_scripts', 'static')()
    )

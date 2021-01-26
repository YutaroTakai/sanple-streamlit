#!Z:\Programming\YOUTUBE_SEARCH\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'chromedriver-binary==88.0.4324.96.0','console_scripts','chromedriver-path'
__requires__ = 'chromedriver-binary==88.0.4324.96.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('chromedriver-binary==88.0.4324.96.0', 'console_scripts', 'chromedriver-path')()
    )

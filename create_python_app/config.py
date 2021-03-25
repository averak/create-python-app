import os
import sys
import datetime

TEMPLATE_ROOT_PATH: str = os.path.join(os.path.dirname(__file__), 'template')
PYTHON_VERSION: str = '%s.%s' % (sys.version_info.major, sys.version_info.minor)
CURRENT_YEAR: str = datetime.date.today().year

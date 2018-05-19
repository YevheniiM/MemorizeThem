#!C:\Users\moroz.y\Study\Programing\CS_UCU\CourseWork\tests\MemorizeThemCourseWork\course_wor_env\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'setuptools==28.8.0','console_scripts','easy_install-3.7'
__requires__ = 'setuptools==28.8.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('setuptools==28.8.0', 'console_scripts', 'easy_install-3.7')()
    )

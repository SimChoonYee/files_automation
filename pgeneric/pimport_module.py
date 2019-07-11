import os
import re
import sys
import logging
import send2trash
import zipfile
import shutil
import subprocess
import patoolib
import lzma #https://stackoverflow.com/questions/22016178/how-pip-install-pylzma-on-windows-7-x64-python-2-7
import py7zlib

from pgeneric.pfilemethod import FileMethodClass
from pgeneric.pzipmethod import ZipMethodClass
from pgeneric.plogger import *

from pmod.pcusfw import FwClass




# Seems import has sequence too, this sequence causing send2trash unable to work
# import os
# import re
# import sys
# import logging
# from pgeneric.pfilemethod import FileMethodClass
# from pgeneric.pzipmethod import ZipMethodClass
# from pgeneric.plogger import *
#
# from pmod.pcusfw import FwClass
#
# import send2trash
# import zipfile
# import shutil
# import subprocess
# import patoolib
# import lzma #https://stackoverflow.com/questions/22016178/how-pip-install-pylzma-on-windows-7-x64-python-2-7
# import py7zlib
#
#




import re


# from pgeneric.pfilemethod import FileMethodClass
from pgeneric.pimport_module import *

class SoClass:
    def __init__(self, *args, so_path=None, **kwargs):
        self.so_path = so_path
        self.fm = FileMethodClass(*args, **kwargs)
        pass

    def find_version(self):
        '''
        *****version_start_2.09.00.71572ENG_version_end*****
        ^\*\*\*\*\*(version_start_)([0-9]{1})(\.)([0-9]{2})(\.)([0-9]{2})(\.)([0-9a-zA-Z]{1,})(_version_end)\*\*\*\*\*$
        '''
        pat = '^' \
              '\*\*\*\*\*' \
              '(version_start_)' \
              '([0-9]{1})(\.)' \
              '([0-9]{2})(\.)' \
              '([0-9]{2})(\.)' \
              '([0-9a-zA-Z]{1,})' \
              '(_version_end)' \
              '\*\*\*\*\*' \
              '$'

    def set_sofile(self,so_path=None):
        if so_path is not None:
            self.so_path = so_path
            logging.info('Reading self.so_path: %s', self.so_path)
        else:
            self.so_path = self.fm.file_path
            logging.info('Reading self.fm.file_path %s', self.fm.file_path)

        if self.so_path:
            pass
        else:
            logging.warning('self.so_path is empty. Please set a path')


if __name__ == "__main__":
    so = SoClass()
    so.fm.check_file_exists_in_dir('.so')
    so.set_sofile()
    print('End of program')


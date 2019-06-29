import re


from pgeneric.pfilemethod import FileMethodClass

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
            try:
                with open(so)
        else:
            print('so_path:',so_path)


if __name__ == "__main__":
    so = SoClass()
    so.fm.update()
    so.fm.check_file_exists_in_dir('.so')
    so.set_sofile(so.fm.file_path)
    print('end of program')


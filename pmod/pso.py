import re


from pgeneric.pfilemethod import FileMethodClass

class SoClass:
    def __init__(self, sofile):
        self.so_file = sofile

        self.fm = FileMethodClass()

        pass

    def find_version(self):
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





so_obj = SoClass()
so_obj.fm.update()


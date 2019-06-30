import re


# from pgeneric.pfilemethod import FileMethodClass
from pgeneric.pimport_module import *

class SoClass:
    def __init__(self, *args, so_path=None, **kwargs):
        self.so_path = so_path
        self.so_version = None
        self.fm = FileMethodClass(*args, **kwargs)
        pass

    def find_so_version(self):
        '''
        *****version_start_2.09.00.71572ENG_version_end*****
        ^\*\*\*\*\*(version_start_)([0-9]{1})(\.)([0-9]{2})(\.)([0-9]{2})(\.)([0-9a-zA-Z]{1,})(_version_end)\*\*\*\*\*$
        '''
        pat = b'\*\*\*\*\*' \
              b'(version_start_)' \
              b'([0-9]{1})(\.)' \
              b'([0-9]{2})(\.)' \
              b'([0-9]{2})(\.)' \
              b'([0-9a-zA-Z]{1,})' \
              b'(_version_end)' \
              b'\*\*\*\*\*'

        if self.so_path is not None:
            try:
                with open(self.so_path, 'rb') as so_file:
                    # TODO: Continue here
                    # https://stackoverflow.com/questions/5618988/regular-expression-parsing-a-binary-file/5620074
                    # https://stackoverflow.com/questions/8710456/reading-a-binary-file-with-python/8711061
                    text = so_file.read()
                    res = re.search(pat, text)

                    if res is None:
                        # error: it shouldnt be happening
                        # warning: cant find, user needs to change input
                        logging.warning('Cant find the pat:%s @%s', pat, self.so_path)
                        return res
                    else:
                        '''
                        .span() returns a tuple containing the start-, and end positions of the match.
                        .string returns the string passed into the function
                        .group() returns the part of the string where there was a match
                        '''
                        self.so_version = res.group().decode('utf-8')
                        logging.info('SET self.so_version: %s', self.so_version)
                        return res
            except Exception as e:
                logging.exception('Missing so_file')
                raise NotImplementedError

    def set_sofile(self,so_path=None):
        if so_path is not None:
            self.so_path = self.fm.set_file_path(so_path)
            logging.info('SET self.so_path: %s', self.so_path)
        else:
            self.so_path = self.fm.file_path
            logging.info('SET self.so_path: %s from self.fm.file_path', self.fm.file_path)

        if self.so_path:
            pass
        else:
            logging.warning('self.so_path is empty. Please set a path')


if __name__ == "__main__":
    so = SoClass()
    so.fm.check_file_exists_in_dir('.so')
    so.set_sofile()
    so.find_so_version()
    print('End of program')


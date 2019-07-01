import re
# from pgeneric.pfilemethod import FileMethodClass
from pgeneric.pimport_module import *


class SoClass:
    def __init__(self):
        logging.debug('Creating instance of SoClass, call instance.init to initializate')
        pass

    def init(self, *args, so_path=None, **kwargs):
        logging.info('INIT:%s', self.__class__.__name__)

        self.so_name = None
        self.so_version = None
        self.fm = FileMethodClass()

        self.fm.init(*args, **kwargs)
        # FileMethodClass attributes
        self.so_path = so_path
        self.so_dir = None
        self.so_search_dir = None

    def set_so_path(self, so_path=None):
        if so_path is not None:
            self.so_path = self.fm.chk_file_path(so_path)
            logging.info('SET self.so_path: %s', self.so_path)
            return self.so_path
        else:
            logging.warning('so_path missing %s', self.so_path)
            return None

    def set_so_dir(self, so_dir=None):

        if so_dir is not None:
            self.so_dir = self.fm.chk_file_dir(so_dir)
            logging.info('SET self.so_dir: %s', self.so_dir)
            return self.so_dir
        else:
            if self.so_path:
                self.so_dir = self.fm.return_dir_from_path(so_path=self.so_path)
                logging.info('SET self.so_dir: %s', self.so_dir)
                return self.so_dir
            else:
                logging.warning('so_dir missing %s', self.so_dir)
                return None

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





if __name__ == "__main__":
    # Find so version
    soObj = SoClass()
    soObj.init()
    soObj.so_search_dir = r'C:\automation_testfiles'

    if soObj.fm.chk_file_dir(filedir=soObj.so_search_dir):
        soObj.so_path = soObj.fm.search_file_in_dir(filedir=soObj.so_search_dir, pat_start='.so')

        # Normally we set both paths together
        soObj.set_so_path(so_path=soObj.so_path)
        soObj.set_so_dir(so_dir=soObj.so_dir)
        soObj.find_so_version()
        print('End of program')


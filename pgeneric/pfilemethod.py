# import os
# import re
from pgeneric.pimport_module import *

class FileMethodClass:
    def __init__(self, *args, filedir=r'C:\automation_testfiles', **kwargs):
        self.file_name = None
        self.file_path = None
        self.filedir = filedir

    def update(self):
        print("hi, found me:", self.__class__.__name__)

    def str_if_None(self, *args):
        '''
        Turn to "" if None
        '''
        for arg in args:
            if arg:
                return arg
            else:
                return ""

    def set_file_dir(self, filedir):
        if os.path.isdir(filedir):
            logging.info('SET file_dir @ %s', filedir)
            self.filedir = filedir
            return self.filedir
        else:
            logging.error('Dir not exists')
            raise FileNotFoundError('self.filedir is:', filedir)

    def set_file_path(self, file_path):
        if os.path.exists(file_path):
            logging.info('SET file_path @ %s', file_path)
            self.file_path = file_path
            return self.file_path
        else:
            logging.error('file_path not exists')
            raise FileNotFoundError('self.file_path is:', file_path)

    def check_file_exists_in_dir(self, pat_start=None, pat_end=None):
        '''
        It prints a dir tree list
        find start ext and end ext (if has)
        evaluates to true if only one file found in filedir

        TODO: I still need to make this as general func
        None cant concatenate: https://stackoverflow.com/questions/21095654/what-is-a-nonetype-object
        soln: https://stackoverflow.com/questions/3752240/join-string-and-none-string-using-optional-delimiter
        '''
        if self.filedir is None:
            # https://stackoverflow.com/questions/28799353/python-giving-filenotfounderror-for-file-name-returned-by-os-listdir
            raise FileNotFoundError('self.filedir is:', self.filedir)

        if pat_start is None and pat_end is None:
            # https://stackoverflow.com/questions/8297526/proper-exception-to-raise-if-none-encountered-as-argument
            raise TypeError('Search pattern cannot be None')
        pat_start, pat_end = self.str_if_None(pat_start), self.str_if_None(pat_end)
        pat = pat_start + pat_end

        file_found = None
        logging.info('Searching %s @ %s', pat, self.filedir)
        for dirpath, dirnames, filenames in os.walk(self.filedir):
            for filename in filenames:
                search_res = re.search(pat, filename)
                if search_res and file_found is None:
                    logging.debug('Found so @ %s, %s, %s:', dirpath, dirnames, filenames)
                    file_found = 1
                    self.file_path = dirpath + "\\" + filename
                elif search_res and file_found == 1:
                    raise ValueError('More than 1 of ', pat, 'only 1 allowed')

        if file_found == 1:
            logging.info('Found %s @ %s', pat, self.file_path)
            return self.file_path
        elif file_found == 0:
            logging.info('$s not found @ %s', pat, self.file_path)
            return None
        else:
            raise ValueError('file_found:',file_found)



    def read_so_ver(self):
        try:
            with open(self.file_path, 'rb') as f:
                f.read(self.so.path)

        except Exception as e:
            print(e)
        pass


if __name__ == "__main__":
    fmobj = FileMethodClass()
    fmobj.check_file_exists_in_dir('.so')
    print(fmobj.file_path)

# import os
# import re
from pgeneric.pimport_module import *


class FileMethodClass:
    def __init__(self):
        logging.debug('Creating instance of FileMethodClass, call instance.init to initializate')

    def init(self, *args, **kwargs):
        logging.info('INIT:%s', self.__class__.__name__)
        # self.file_name = None
        # self.file_path = None
        # self.filedir = None

    def str_if_none(self, *args):
        '''
        Turn to "" if None
        '''
        for arg in args:
            if arg:
                return arg
            else:
                return ""

    def chk_file_dir(self, filedir):
        if os.path.isdir(filedir):
            logging.debug('File_dir exists @ %s', filedir)
            # self.filedir = filedir
            # return self.filedir
            return filedir
        else:
            logging.error('Dir not exists')
            raise FileNotFoundError('self.filedir is:', filedir)

    def chk_file_path(self, file_path):
        if os.path.exists(file_path):
            logging.info('File_path exists @ %s', file_path)
            # self.file_path = file_path
            # return self.file_path
            return file_path
        else:
            logging.error('File_path not exists')
            raise FileNotFoundError('File_path @:', file_path)

    def return_dir_from_path(self, so_path=None):
        if so_path is not None:
            backslash_index = so_path.rfind("\\")
            so_dir = so_path[:backslash_index]
            return so_dir
        else:
            logging.warning('Cant get so_path as it is %s', so_path)
            return None

    def search_file_in_dir(self, filedir=None, pat_start=None, pat_end=None):
        '''
        It prints a dir tree list
        find start ext and end ext (if has)
        evaluates to true if only one file found in filedir

        TODO: I still need to make this as general func
        None cant concatenate: https://stackoverflow.com/questions/21095654/what-is-a-nonetype-object
        soln: https://stackoverflow.com/questions/3752240/join-string-and-none-string-using-optional-delimiter
        '''
        # if self.filedir is None:
        if filedir is None:
            # https://stackoverflow.com/questions/28799353/python-giving-filenotfounderror-for-file-name-returned-by-os-listdir
            raise FileNotFoundError('filedir is:', filedir)

        if pat_start is None and pat_end is None:
            # https://stackoverflow.com/questions/8297526/proper-exception-to-raise-if-none-encountered-as-argument
            raise TypeError('Search pattern cannot be None')
        pat_start, pat_end = self.str_if_none(pat_start), self.str_if_none(pat_end)
        pat = pat_start + pat_end

        file_found = None
        logging.info('Searching %s @ %s', pat, filedir)
        # for dirpath, dirnames, filenames in os.walk(self.filedir):
        for dirpath, dirnames, filenames in os.walk(filedir):
            for filename in filenames:
                search_res = re.search(pat, filename)
                if search_res and file_found is None:
                    logging.debug('Found so @ %s, %s, %s:', dirpath, dirnames, filenames)
                    file_found = 1
                    # self.file_path = dirpath + "\\" + filename
                    file_path = dirpath + "\\" + filename
                elif search_res and file_found == 1:
                    raise ValueError('More than 1 of ', pat, 'only 1 allowed')

        if file_found == 1:
            logging.info('Found %s @ %s', pat, file_path)
            # return self.file_path
            return file_path
        elif file_found == 0:
            logging.info('$s not found @ %s', pat, file_path)
            return None
        else:
            raise ValueError('file_found:', file_found)


if __name__ == "__main__":
    fmobj = FileMethodClass()
    fmobj.search_file_in_dir('.so')
    print(fmobj.file_path)

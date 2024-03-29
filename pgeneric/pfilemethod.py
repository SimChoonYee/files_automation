# import os
# import re
from pgeneric.pimport_module import *

class FileMethodClass:
    def __init__(self):

        pass

    def init(self, *args, **kwargs):
        logging.info('INIT:%s', self.__class__.__name__)
        # self.file_name = None
        # self.file_path = None
        # self.filedir = None

    def from_file_return_list_by_line(self, targetfile, pnumskipnewline=0):
        '''

        :param targetfile:
        :param pnumskipnewline: init:0, turns of continue reading if newline found
        :return: a list if file readable
        '''
        try:
            with open(targetfile, 'r') as f:
                filelist = []
                for line in f:
                    line = line.rstrip('\n')
                    if line == r'' and pnumskipnewline == 0:
                        logging.debug('Reached emptyquotes, STOP READ:%s', targetfile)
                        break
                    elif line == r'':
                        pnumskipnewline = pnumskipnewline - 1
                        logging.debug('Read emptyquotes, emptyquotes left to be skipped:%s', str(pnumskipnewline))
                        continue
                    filelist.append(line)
        except Exception as e:
            logging.debugging('Unable to read file:%s', e)
            return None
        return filelist

    def add_name_behind_filename(self, ptargetdir, prename=""):
        if not os.path.isdir(ptargetdir):
            logging.warning("Directory not exists")
            return None
        # else:
        #     # Delete all files in dir if directory exists
        #     if os.listdir(ptargetdir):
        #         for

        new_filepathlist = []
        for dirpath, dirnames, filenamelist in os.walk(ptargetdir):
            for filename in filenamelist:
                # https://stackoverflow.com/questions/45493022/rename-files-without-extension
                old_filepath, ext = os.path.splitext(os.path.join(dirpath, filename))
                if not ext:
                    logging.warning("This file %s has no ext, renaming it might be wrong", old_filepath)

                new_filepath = old_filepath + prename



                if os.rename(old_filepath+ext, new_filepath+ext):
                    new_filepathlist.append(new_filepath+ext)

        return new_filepathlist

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

    def delete_folder_if_exists(self, folder_dir=None):
        logging.info('DEL:%s', folder_dir)
        if os.path.isdir(folder_dir):
            send2trash.send2trash(folder_dir)
            return 1
        else:
            logging.info('Folder:%s does not exists for deletion', folder_dir)
            return None

    def create_folder(self, folder_dir):
        logging.debug('CHECK IF EXISTS: %s', folder_dir)
        # Check if folder do not exists? Create it: Do nothing
        if not os.path.isdir(folder_dir):
            os.makedirs(folder_dir)
            logging.info("Folder Missing, CREATE: %s \n", folder_dir)
            return folder_dir
        else:
            logging.info("EXISTS, NO-CREATE:%s \n", folder_dir)
            return None

    def create_folder_incrementally(self, folder_dir=None, init_name='output', num=0):
        logging.debug('CHECK: %s', folder_dir)
        if folder_dir is None:
            logging.debug('folder_dir is None? %s', folder_dir)
            num = 0
            folder_dir = init_name + str(num)
            logging.debug('SET folder_dir to: %s', folder_dir)

        # Check if folder exists? do nothing:create it
        if not os.path.isdir(folder_dir):
            os.makedirs(folder_dir)
            logging.info("Folder Missing, CREATE: %s", folder_dir)
            return folder_dir
        else:
            logging.info("Folder:%s exists", folder_dir)
            num = num + 1
            folder_dir = folder_dir + init_name + str(num)
            logging.info("SET folder_dir to: %s", folder_dir)
            return self.create_folder(folder_dir, init_name, num)

    # Write
    def write_bytes_to_folder(self):
        pass


if __name__ == "__main__":
    fmobj = FileMethodClass()
    testfile = r'C:\automation_testfiles_2\files_to_extract.txt'
    testlist = fmobj.from_file_return_list_by_line(targetfile=testfile, pnumskipnewline=1)
    print(testlist)
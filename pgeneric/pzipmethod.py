from pgeneric.pimport_module import *


class ZipMethodClass:
    def init(self):
        logging.info('INIT:%s', self.__class__.__name__)

    def extract_files_from_zipfile(self, files=None, zipfile=None):
        if files is None or zipfile is None:
            logging.warning('files is %s or zipfile is %s', files, zipfile)

        for file in files:
            
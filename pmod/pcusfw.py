
from pgeneric.pimport_module import *


class FwClass:
    def init(self, *args, **kwargs):
        logging.info('INIT:%s', self.__class__.__name__)

        self.fw_name = None
        self.fw_version = None

        self.fm = FileMethodClass()
        self.fm.init(*args, **kwargs)
        # FileMethodClass attributes
        self.fw_path = None
        self.fw_dir = None
        self.fw_search_dir = None
        self.fw_version = None


if __name__ == "__main__":
    cusfw = FwClass()




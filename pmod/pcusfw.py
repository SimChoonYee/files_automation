from pgeneric.pimport_module import *


class FwClass:
    def init(self, *args, **kwargs):
        logging.info('INIT:%s', self.__class__.__name__)

        # Results
        self.fw_name = None
        self.fw_version = None

        self.fm = FileMethodClass()
        self.fm.init(*args, **kwargs)
        # FileMethodClass attributes

        # Data
        self.fw = {'info': None, 'zip': None}

        data = {'fw_path': None,
                'fw_dir': None,
                'fw_search_dir': None}

        for key in self.fw:
            self.fw[key] = data

        logging.debug('STORE self.fw info & zip %s', self.fw)

    # def extract_file(self):
    #     pass

if __name__ == "__main__":
    cusfw = FwClass()
    cusfw.init()

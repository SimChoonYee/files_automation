from pgeneric.pimport_module import *


class FwClass:
    def init(self, *args, **kwargs):
        logging.info('INIT:%s', self.__class__.__name__)

        # Results not needed? as we have self.fw
        # self.fw_name = None
        # self.fw_version = None

        self.fm = FileMethodClass()
        self.fm.init(*args, **kwargs)
        # FileMethodClass attributes

        # Data
        # TODO Enhance: Retrieve data from config file
        # Underscore meaning protected and can be accessed.
        # C++CodeConcept: https://stackoverflow.com/questions/3247671/accessing-protected-members-in-a-derived-class
        self.fwdata = {'info': None, 'zip': None}

        data = {'fw_version': None,
                'fw_path': None,
                'fw_dir': None,
                'fw_search_dir': None}

        for key in self.fwdata:
            self.fwdata[key] = data




if __name__ == "__main__":
    cusfw = FwClass()
    cusfw.init()

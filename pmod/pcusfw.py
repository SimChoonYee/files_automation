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

    def add_name_behind_filename(self, ptargetdir, prename=""):
        if not os.path.isdir(ptargetdir):
            logging.warning("Directory not exists")
            return None

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


if __name__ == "__main__":
    cusfw = FwClass()
    cusfw.init()

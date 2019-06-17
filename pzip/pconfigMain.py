from configparser import ConfigParser
from pconfigMethods import ConfigMethodsClass
import os


# https://www.youtube.com/watch?v=HH9L9WFMfnE


class ConfigMainClass:
    def __init__(self, set_init):
        if set_init == 'default':
            # Set your default parameters
            self.filelists = ['cust_fw',
                              'mst_fw']
            self.fileattrs = {
                "filename": 'None',
                "path_replaced": 'None'
                "path_used"
            }

            self.method = ConfigMethodsClass()
            self.config = ConfigParser(allow_no_value=True)

    def config_create_default_section(self, section=None):
        config_flag = 0
        if section is None:
            config = self.config
            section = self.filelists
            config_flag = 1

        # create empty attributes for each sect
        # use config.add and set over here
        for sectionName in section:
            self.config.add_section(sectionName)
            for fileattr, fileattrV in self.fileattrs.items():
                print('fileattr:', fileattr, 'fileattrV:', fileattrV)
                self.config.set(sectionName, fileattr, fileattrV)

        if config_flag == 1:
            self.config = config
            return self.config
        else:
            return config

    def config_write_config(self, f, config=None):
        if config is None:
            config = self.config

        config.write(f)
        self.config = config
        return f

    def config_reset_config(self, config=None):
        config_flag = 0
        if config is None:
            # For returning the passed-in config instead
            config = self.config
            config_flag = 1

        try:
            for sectionName in config.sections():
                config.remove_section(sectionName)

        except Exception as e:
            print(e)

        if config_flag == 1:
            self.config = config
            return self.config
        else:
            return config


    def config_read_config(self, f):
        return self.config.read_file(f)


if __name__ == "__main__":
    # TODO: while file is open as write, config.write wont overite the file
    # thinking of moving it into function but worried if it is written twice

    with open("config.ini", 'w') as configfile, \
            open("config2.ini", 'r') as configfile2:
        configObj = ConfigMainClass('default')
        configObj.config_create_default_section()
        configObj.config_write_config(configfile)
        configObj.config_reset_config()
        configObj.config_write_config(configfile)
        configObj.config_read_config(configfile2)
        configObj.config_write_config(configfile)
        configObj.method.config_update()

    print("EOP")

from pgeneric.pimport_module import *


class ZipMethodClass:
    def init(self):
        logging.info('INIT:%s', self.__class__.__name__)

    def extract_files_from_zipfile_to(self, files=None, zipfile=None, output_folder=None):
        extract_list = ['test2.txt']
        if files is None or zipfile is None:
            logging.warning('files is %s or zipfile is %s', files, zipfile)
            return None
        for file in files:
            pass

        with ZipFile('output0/output0.zip', 'r') as z:
            for pathname in z.namelist():
                print('hey?', pathname.filename)
                print(pathname)
                fwdsl = pathname.rfind('/')
                print(fwdsl, len(pathname))
                index = fwdsl - len(pathname)
                index = index + 1
                if index < 0:
                    filename = pathname[index:]
                    print('filename:', filename)
                    if filename in extract_list:
                        print('extract:',pathname,'file:',filename)
                        if z.extract(pathname, r'C:\Users\Choon Yee Sim\PycharmProjects\files_automation\pgeneric\output0\outputdata'):
                            print('extraced success')

            z.close()


            print('found')


if __name__ == "__main__":
    testzip = ZipMethodClass()
    testzip.extract_files_from_zipfile_to(files='abc', zipfile='abc')

    print('Test')

            
from pgeneric.pimport_module import *






class ZipMethodClass:
    def init(self):
        logging.info('INIT:%s', self.__class__.__name__)


    def extract_files_from_zipfile_to(self, files_to_extract=None, zipdoc=None, targetdir=None):
        # https://stackoverflow.com/questions/4917284/extract-files-from-zip-without-keeping-the-structure-using-python-zipfile
        extract_list = ['abcdef.txt']
        if files_to_extract is None or zipdoc is None or targetdir is None:
            logging.warning('files is %s or zipfile is %s', files_to_extract, zipdoc)
            return None


        with zipfile.ZipFile('output1/output1.zip','r') as z:
            for zip_info in z.infolist():
                logging.debug('ALL:%s', zip_info)
                if zip_info.filename[-1] == '/':
                    continue

                zip_filename = os.path.basename(zip_info.filename)  # disable to remain structure in zip file
                print('zip_filename:', zip_info.filename)
                if zip_filename in extract_list:
                    zip_info.filename = 'ConfigFile/' + zip_filename + 'version'
                    logging.info('Found files:%s', zip_info.filename)
                    z.extract(zip_info, targetdir)

            z.close()

        with zipfile.ZipFile("version.zip", "w", zipfile.ZIP_DEFLATED) as z:
            for root, dirs, files in os.walk('output0\\target1'):
                for file in files:
                    z.write(os.path.join(root, file))







if __name__ == "__main__":
    testzip = ZipMethodClass()
    targetdir = 'C:\\Users\\41904\Box Sync\\Code_reference\\testpackage\\files_automation\pgeneric\output0\\target1'

    testzip.extract_files_from_zipfile_to(files_to_extract='abc', zipdoc='abc', targetdir=targetdir)

    print('EOP')



                # zfilename = os.path.basename(zpathname)
                # zsource = z.open(zpathname)
                # url = r'C:\Users\41904\Box Sync\Code_reference\testpackage\files_automation\pgeneric\output0\target'
                # ztarget = z(os.path.join(url, zfilename), 'wb')
                # with zsource, ztarget:
                #     shutil.copyfileobj(zsource,ztarget)

                # print(pathname)
                # fwdsl = pathname.rfind('/')
                # print(fwdsl, len(pathname))
                # index = fwdsl - len(pathname)
                # index = index + 1
                # if index < 0:
                #     filename = pathname[index:]
                #     print('filename:', filename)
                #     if filename in extract_list:
                #         print('extract:',pathname,'file:',filename)
                #         url = r'C:\Users\Choon Yee Sim\PycharmProjects\files_automation\pgeneric\output0\outputdata'
                #         with z.open(pathname):
                #             print('extraced success')

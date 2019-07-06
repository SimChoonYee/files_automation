from pgeneric.pimport_module import *


class ZipMethodClassLearn:
    def init(self):
        logging.info('INIT:%s', self.__class__.__name__)
        self.fm = FileMethodClass()
        self.fm.init()

        self.fw = FwClass()
        self.fw.init()


    def zip_files_to_folder(self, pfilelist, ptarget7z, ptargetfolder,):
        pass
    def _extract_files_to_folder(self, filelist, targetzip, targetfolder):
        # Read and create another folder
        with zipfile.ZipFile(targetzip, 'r') as z:
            for zip_info in z.infolist():
                logging.debug('ALL:%s', zip_info)
                if zip_info.filename[-1] == '/':
                    continue

                zip_filename = os.path.basename(zip_info.filename)  # disable to remain structure in zip file
                logging.debug('zip_filename:%s', zip_info.filename)
                if zip_filename in filelist:
                    zip_info.filename = 'ConfigFile/' + zip_filename + 'version'
                    zip_info.filename = zip_filename
                    logging.info('Found files:%s', zip_info.filename)
                    z.extract(zip_info, targetfolder)

            z.close()

    def extract_files_to_folder_n_zip(self, files_to_extract=None, zipdoc=None, targetdir=None):
        # https://stackoverflow.com/questions/4917284/extract-files-from-zip-without-keeping-the-structure-using-python-zipfile

        # Check for invalid input arguments
        if files_to_extract is None or zipdoc is None or targetdir is None:
            logging.warning('files is %s or zipfile is %s', files_to_extract, zipdoc)
            return None


class sevenZMethodClassLearn:
    def init(self):
        logging.info('INIT:%s', self.__class__.__name__)
        self.fm = FileMethodClass()
        self.fm.init()

        self.fw = FwClass()
        self.fw.init()
    def extract_files_to_folder(self, pfilelist, ptarget7z, ptargetfolder, puse_basename=True):
        # Read and create another folder

        try:
            with open(ptarget7z, 'rb') as ptarget7Zfp:
                if not self.fm.chk_file_dir(filedir=ptargetfolder):
                    self.fm.create_folder(folder_dir=ptargetfolder)

                ptarget7z_archive = py7zlib.Archive7z(ptarget7Zfp)
                pallnames = ptarget7z_archive.getnames()
                # getnames run in alphabetical order regardless of folder or files

                # return pfound_list for files that has been found
                pfound_list = []
                for pindex, pname in enumerate(pallnames):
                    psearchname = pname
                    if puse_basename:
                        pbasename = os.path.basename(pname)
                        psearchname = pbasename
                    if psearchname in pfilelist:

                        logging.debug('\npname[%s]:%s pbasename:%s psearchname:%s', pindex, pname, pbasename, psearchname)
                        logging.debug('pallnames[pindex]:%s', pallnames[pindex])
                        pmember = ptarget7z_archive.getmember(pallnames[pindex])
                        pdata = pmember.read()
                        pwrite_path = os.path.join(ptargetfolder, psearchname)

                        with open(pwrite_path, "wb") as filewrite:
                            logging.debug("Write data to:%s", pwrite_path)
                            pfound_list.append(pwrite_path)
                            filewrite.write(pdata)

                return pfound_list
        except IOError as e:
            logging.debug("Cannot open 7z file:%s", e)


if __name__ == "__main__":
    test7z = sevenZMethodClassLearn()
    test7z.init()

    target7z = r'C:\automation_testfiles_2\output0.7z'
    targetfolder = r'C:\automation_testfiles_2\targetfolder'

    filelist_to_extract = r'C:\automation_testfiles_2\files_to_extract.txt'
    filelist = test7z.fm.from_file_return_list_by_line(filelist_to_extract)

    test7z.extract_files_to_folder(pfilelist=filelist, ptarget7z=target7z, ptargetfolder=targetfolder)
    test7z.fw.fwdata['info']['fw_version'] = '_A0032Q3N'
    test7z.fw.add_name_behind_filename(ptargetdir=targetfolder, prename=test7z.fw.fwdata['info']['fw_version'])




    # testzip.extract_files_from_zipfile_to(files_to_extract='abc', zipdoc='abc', targetdir=targetdir)
    #
    # print('EOP')



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

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
        logging.debug('PRINT pfilelist:%s', pfilelist)
        pfilelist_basename = pfilelist.copy()
        #
        # try:
        with open(ptarget7z, 'rb') as ptarget7Zfp:
            if not self.fm.chk_file_dir(filedir=ptargetfolder):
                self.fm.create_folder(folder_dir=ptargetfolder)

            ptarget7z_archive = py7zlib.Archive7z(ptarget7Zfp)
            pgetnames = ptarget7z_archive.getnames()
            # getnames run in alphabetical order regardless of folder or files

            # return pfound for files that has been found
            pfound = []
            for pgetname_index, pgetname in enumerate(pgetnames):

                if puse_basename:
                    # As long as basename in pgetnames & pfilelist matches
                    pgetname_basename = os.path.basename(pgetname)
                    psearchname = pgetname_basename
                    psearchlist = pfilelist_basename
                else:
                    psearchname = pgetname
                    psearchlist = pfilelist

                if psearchname in psearchlist:
                    # Find the index out so we can write similar structure as pfilelist
                    logging.debug('psearchname:%s ', psearchname)
                    logging.debug('Getting member:%s', pgetnames[pgetname_index])
                    pmember = ptarget7z_archive.getmember(pgetnames[pgetname_index])
                    pdata = pmember.read()

                    pwrite_path = os.path.join(ptargetfolder, pfilelist[pfilelist.index(psearchname)])

                    # in case someone make mistake writing / at files_to_extract
                    pwrite_path = pwrite_path.replace('/', '\\')
                    logging.debug('pwrite_path dir name:%s', os.path.dirname(pwrite_path))
                    # if write to folder?
                    # puse_basenameuse use pfilelist as location:
                    #
                    # pfilelist_basename_index = psearchlist.index(psearchname)
                    # pwrite_path = os.path.join(ptargetfolder, pfilelist[pfilelist_basename_index])
                    # logging.debug('PRINT pfilelist[index]:%s path:%s', pfilelist[pfilelist_basename_index],
                    #               pwrite_path)
                    # pwrite_path = pwrite_path.replace(os.sep, '/')

                    self.fm.create_folder(folder_dir=os.path.dirname(pwrite_path))
                    with open(pwrite_path, "wb+") as filewrite:
                        logging.debug("Write data to:%s", pwrite_path)
                        pfound.append(pwrite_path)
                        filewrite.write(pdata)

            return pfound
        # except IOError as e:
        #     logging.debug("Cannot open 7z file:%s", e)


if __name__ == "__main__":
    test7z = sevenZMethodClassLearn()
    test7z.init()

    target7z = r'C:\automation_testfiles_2\output0.7z'
    targetfolder = r'C:\automation_testfiles_2\targetfolder'

    filelist_to_extract = r'C:\automation_testfiles_2\files_to_extract.txt'
    filelist = test7z.fm.from_file_return_list_by_line(filelist_to_extract)
    test7z.fm.delete_folder_if_exists(folder_dir=targetfolder)
    test7z.fm.create_folder(folder_dir=targetfolder)
    test7z.extract_files_to_folder(pfilelist=filelist, ptarget7z=target7z, ptargetfolder=targetfolder, puse_basename=False)
    test7z.fw.fwdata['info']['fw_version'] = '_A0032Q3N'
    test7z.fm.add_name_behind_filename(ptargetdir=targetfolder, prename=test7z.fw.fwdata['info']['fw_version'])




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

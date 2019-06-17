import os
import shutil
from zipfile import ZipFile
from pconfigMain import ConfigMainClass



# Pass is 0 https://stackoverflow.com/questions/9549342/should-i-return-0-or-1-for-successful-function
class ZipMainClass:
    def __init__(self, unzip_package):
        self.unzip_folder = "unzip_folder"
        self.unzip_package = unzip_package

        if __name__ != "__main__":
            self.main_run()

    def create_folder(self):
        # Check if folder exists? do nothing:create it
        if not os.path.isdir(self.unzip_folder):
            print("Creating:", self.unzip_folder)
            os.makedirs(self.unzip_folder)
            print("Created:", self.unzip_folder)
        else:
            print("Folder:", self.unzip_folder, "exists")

    def check_folder_unempty(self):
        if not os.listdir(self.unzip_folder):
            print("Directory:", self.unzip_folder, "is empty")
        else:
            print("Directory:", self.unzip_folder, "contains files")
            return 1

    def delete_folder(self):
        # Plan feature: Add bit flag for this setting
        print("Directory:", self.unzip_folder, "contains files, deleting whole folder named:", self.unzip_folder)
        try:
            print("Deleting:", self.unzip_folder)
            shutil.rmtree(self.unzip_folder)
            self.create_folder()
            print("Deleted and created new empty", self.unzip_folder)
        except:
            print("Unable to delete folder:", self.unzip_folder)
            return 1

    def unzip(self, sel='all', sel_list=None):
        try:
            with ZipFile(self.unzip_package, 'r') as obj:
                if sel == 'all':
                    print('sel:', sel)
                    obj.extractall(self.unzip_folder)
                    return obj
                if sel == 'some':
                    print('sel:', sel)
                    for files in sel_list:
                        try:
                            obj.extract(files, self.unzip_folder)
                        except Exception as e:
                            print("File:", files, "missing in", self.unzip_package, "e:", e)
                    return obj

        except Exception as e:
            print("unzip function has issue")
            print("e:",e)

    def main_run(self):
        print("Running main loop")
        self.create_folder()

        if self.check_folder_unempty():
            # TODO: Add a flag to check_folder_unempty for delete folder option
            print("Fail: Unzip folder not empty, performing delete->recreate folder action")
            if self.delete_folder():
                return 1
            return 1

        files_to_extract = ['file1.py', 'file2.py']
        # unzip process
        return self.unzip(sel='some', sel_list=files_to_extract)

        pass


if __name__ == "__main__":
    # 1Retrieve setiings data
    zipObj = ZipMainClass("test.zip")
    zipObj.main_run()
    # if zipObj.get_filelist():
    #     print("get_filelist fail")
    # TODO: Complete unzip functionality

    print("EOP")

import os


class FileMethodClass:
    def __init__(self):
        self.so_path = None

    def update(self):
        print("hi, found me")

    def check_dot_so_exists_in_dir(self, default=r'C:\automation_testfiles'):
        # It prints a list
        # I still need to make this as general func
        end_ext = '.so'
        so_found = 0
        for dirpath, dirnames, filenames in os.walk(default):
            # print(dirpath, dirnames, filenames)
            for filename in filenames:
                if filename.endswith(end_ext) and so_found == 0:
                    print('Found so @:', dirpath, dirnames, filenames)
                    so_found = 1
                    self.so_path = dirpath + "\\" + filename
                elif filename.endswith(end_ext) and so_found == 1:
                    raise ValueError('Two .so files are found, only 1 allowed')


    def read_so_ver(self):
        try:
            with open(self.so_path, 'rb') as f:
                f.read(self.so.path)

        except Exception as e:
            print(e)
        pass


if __name__ == "__main__":
    fmobj = FileMethodClass()
    fmobj.check_dot_so_exists_in_dir()
    print(fmobj.so_path)

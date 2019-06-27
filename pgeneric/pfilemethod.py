import os

class FileMethodClass:
    def update(self):
        print("hi, found me")

    def check_dot_so_exists_in_dir(self,default='C:\\automation_testfiles'):
        end_ext = '.so'
        for dirpath, dirnames, filenames in os.walk(default):
            print(dirpath, dirnames, filenames)
            for filename in filenames:
                if filename.endswith(end_ext):
                    print('Found so @:', dirpath, dirnames, filenames)



if __name__ == "__main__":
    fmobj = FileMethodClass()
    fmobj.check_dot_so_exists_in_dir()
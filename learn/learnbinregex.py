import re

def find_so_version():
    '''
    *****version_start_2.09.00.71572ENG_version_end*****
    ^\*\*\*\*\*(version_start_)([0-9]{1})(\.)([0-9]{2})(\.)([0-9]{2})(\.)([0-9a-zA-Z]{1,})(_version_end)\*\*\*\*\*$
    '''
    pat = b'\*\*\*\*\*' \
          b'(version_start_)' \
          b'([0-9]{1})(\.)' \
          b'([0-9]{2})(\.)' \
          b'([0-9]{2})(\.)' \
          b'([0-9a-zA-Z]{1,})' \
          b'(_version_end)' \
          b'\*\*\*\*\*'
    # pat = '^' \
    #       '\*\*\*\*\*' \
    #       '(version_start_)' \
    #       '([0-9]{1})(\.)' \
    #       '([0-9]{2})(\.)' \
    #       '([0-9]{2})(\.)' \
    #       '([0-9a-zA-Z]{1,})' \
    #       '(_version_end)' \
    #       '\*\*\*\*\*' \
    #       '$'
    # pat = b'^\*\*' \
    #     b'\*\*\*$'
    print('pat', pat)
    # so_path = r'C:\automation_testfiles\QUATTRO_ST20000_SO71572ENG_v01\5_9\tp_css_ess.so'
    so_path = r'C:\Users\Choon Yee Sim\PycharmProjects\files_automation\learn\test.so'
    try:
        with open(so_path, 'rb') as so_file:
            # TODO: Continue here
            # https://stackoverflow.com/questions/5618988/regular-expression-parsing-a-binary-file/5620074 regex bin
            # https://stackoverflow.com/questions/8710456/reading-a-binary-file-with-python/8711061 alter:unpack
            text = so_file.read()
            res = re.search(pat, text)
            print(res)
    except:
        print('fail')

find_so_version()
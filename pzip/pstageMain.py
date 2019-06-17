'''
Obj: To read out stage.txt file
pstageMethods will be the one for pstageMain implementation.
Avoid inheritance since it is not a variation of parent class, use composition instead
'''


import re


class StageMainClass:
    def __init__(self):
        self.stage_file = "stage.txt"
        self.setDict = {}
        self.setDict_stage = None
        self.setDict_data = None
        # stage are the regex pattern used
        self.stage_pattern = r'^\[.*\]$'
        self.stage_data = '='

    def get_filelist(self):
        rflag = 0

        with open(self.stage_file, "r") as f:
            print("Opened:", self.stage_file)
            # lines = f.readlines()
            # https://www.sololearn.com/Discuss/116640/difference-between-readline-and-readlines
            # https://www.ics.uci.edu/~brgallar/week2_1.html

            for line in f:
                if line == "\n":
                    print(r"\n")
                    continue
                else:
                    line = line.rstrip()
                    print(line)

                    if line[0] == "[":
                        print(" Stage:", line)
                        pattern = re.search(self.stage_pattern, line)
                        if pattern:

                            self.setDict_stage = line[(pattern.start() + 1):(pattern.end() - 1)]
                            self.setDict[line[(pattern.start() + 1):(pattern.end() - 1)]] = None
                            rflag = 1
                        else:
                            print("Fail find stage_pattern")
                    elif line[0] == "" or line[0] == " ":
                        print("Empty string, leaving stage_data mode")
                        rflag = 0
                        self.setDict_stage = None
                        self.setDict_data = None
                    elif line[0] is not "[" and rflag is 1:
                        pattern = re.search(self.stage_data, line)
                        if pattern:
                            self.setDict_data = line.split(self.stage_data, 1)
                            self.setDict[self.setDict_stage] = {self.setDict_data[0]: self.setDict_data[1]}
                    else:
                        print("Fail: Unexpected string reading occur:",line)
        print(self.setDict)
        # except:
        # print("Fail: ",self.stage_file)
        # return 1


if __name__ == "__main__":
    stageObj = StageMainClass()
    if stageObj.get_filelist():
        print("get_filelist fail")

    print("EOP")

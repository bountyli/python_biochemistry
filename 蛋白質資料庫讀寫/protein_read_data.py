from fileinput import filename
import os
import glob

#使用萬用字元*來獲取路徑為 data\PDB_files\ 下所有副檔名為pdb之檔案list
file_location = os.path.join('data','PDB_files', '*.pdb')
print(file_location)
filenames = glob.glob(file_location)
print(filenames)

#使用for迴圈讀取檔案list
for name in filenames:
    #依次讀取一行文字
    with open(name, 'r') as outfile:
        data = outfile.readlines()

    for line in data:
        #假設其中一行文字有包含'RESOLUTION.'
        if 'RESOLUTION.' in line:
            #將該行文字儲存下來
            res_line = line
            #以空格為分隔點，將該行文字回傳為字串列表
            words = res_line.split()
            #其中第4個字串以浮點數格式儲存，並列印出來
            resolution = float(words[3])
            print(resolution)
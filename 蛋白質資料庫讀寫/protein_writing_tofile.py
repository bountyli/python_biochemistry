import os
import glob

#使用萬用字元*來獲取路徑為 data\PDB_files\ 下所有副檔名為pdb之檔案list
file_location = os.path.join('data','PDB_files', '*.pdb')
filenames = glob.glob(file_location)

#"w+"模式 先讀取在寫入，若是無此名稱檔案，立即新建一個檔案
with open('resolutions.txt', 'w+') as outputfiles:
    #使用for迴圈讀取檔案list
    for name in filenames:
        #去除路徑，獲取PDB ID
        file_name = os.path.basename(name)
        #去除副檔名
        split_filename = file_name.split('.')
        molecule_name = split_filename[0]

        #依次讀取一行文字
        with open(name, 'r') as outfile:
            data = outfile.readlines()

        for line in data:
            if 'RESOLUTION.' in line:
                res_line = line
                words = res_line.split()
                resolution = float(words[3])
                #將獲取到的分子名稱、解析度依序寫入檔案
                outputfiles.write(F'{molecule_name} : {resolution} Angstorms \n')
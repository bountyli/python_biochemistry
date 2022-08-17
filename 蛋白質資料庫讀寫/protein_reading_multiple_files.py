import os
import glob

#使用萬用字元*來獲取路徑為 data\PDB_files\ 下所有副檔名為pdb之檔案list
file_location = os.path.join('data','PDB_files', '*.pdb')
filenames = glob.glob(file_location)


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
            print(molecule_name, ": ", resolution, " Angstorms", sep="")
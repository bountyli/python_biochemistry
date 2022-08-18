# 湘芸的蛋白質資料庫 (Protein Data Bank) 讀寫教學

使用RCSB Protein Data Bank中下載的蛋白質PDB檔案，練習以python作檔案讀寫。

RCSB Protein Data Bank 網站: https://www.rcsb.org/ 

參考資料: https://education.molssi.org/python-scripting-biochemistry/chapters/setup.html

PDB檔案中包含著蛋白質或是核酸的三維結構數據，大多數結構由X光繞射量測獲得。使用X光繞射獲得原子座標近似，NMR實驗得到原子對之間距離估計值。

## PDB數據庫原子座標格式
* 標題
  * HEADER (分子、公布日期、ID)
  * TITLE (實驗方法類型)
  * CAVEAT (可能得錯誤提示)
  * COMPND (化合物分子組成)
  * SOURCE (化合物來源)
  * KEYWDS (關鍵字)
  * EXPDTA (測定結構使用之實驗)
  * AUTHOR (結構測定者)
  * REVDAT (修訂日期)
  * JRNL (發表座標集之文獻)
  * REMARK
    * REMARK 1 (有關文獻)
    * REMARK 2 (最大分辨率)
    * REMARK 3 (使用程式和統計方法)
  * etc......


### 使用 python 處理多個檔案
假設目前有100個或是1000個檔案要分析數據，要單獨打開每個檔案 ctrl+c ctrl+v 超級無敵沒效率。使用 python 搭配迴圈讀取檔案，簡單幾行程式就可以一瞬間提取數據。以此為例，我們將讀取PDB資料庫中一系列酶結構的檔案，並提取分辨率數據和原子計數。所有的PDB檔案都保存在PDB_files的文件夾中，將該文件下載，並與執行程式表存在同一目錄。

首先，導入os模組，讓我們可以處裡資料夾中的檔案路徑

```python
 import os
 file_location = os.path.join('data','PDB_files','*.pdb')
 print(file_location)
```
輸出結果
```
data/PDB_files/*.pdb
```

.path.join()為os模組中重新組合路徑的函式，萬用字元*可以讓我們指定名為data\PDB_files下，所有副檔名為.pdb的檔案。

接下來，使用glob模組中的glob函式，由於函式名稱與模組相同，因此glob重複打了兩次，此函式可以輸出所有符合條件的檔案路徑，並以list格式回傳。

```python
import glob
filenames = glob.glob(file_location)
print(filenames)
```
輸出結果
```
['data\\PDB_files\\1ddo.pdb', 'data\\PDB_files\\2pkr.pdb', 'data\\PDB_files\\3iva.pdb', 'data\\PDB_files\\3vnd.pdb', 'data\\PDB_files\\4eyr.pdb', 'data\\PDB_files\\5eu9.pdb', 'data\\PDB_files\\5veu.pdb', 'data\\PDB_files\\6zt7.pdb', 'data\\PDB_files\\7tim.pdb']
```

### 使用迴圈循環讀取多個檔案
現在我們有PDB_files文件夾中所有.pdb檔案路徑的list，為了能夠讀取所有檔案，使用for迴圈來歷遍每個檔案路徑。

```python
for path in filenames:
    with open(path, 'r') as outfile:
        data = outfile.readlines()
    
    for line in data:
        if 'RESOLUTION.' in line:
            res_line = line
            words = res_line.split()
            resolution = float(words[3])
            print(resolution)
```
輸出結果
```
3.1
2.4
2.7
2.6
1.8
2.05
2.91
1.85
1.9
```
上述程式包含著兩個for迴圈，第一個for迴圈作用為，循環讀取filenames中的檔案路徑，每次循環path變數會取代為每個檔案路徑，並使用open()函式開啟檔案，參數'r'表示讀取，使用with open語法可以減短讀寫檔案的寫法，並在每次讀取後自動呼叫clase()關閉檔案。在開啟檔案後，使用readline()語法，逐一讀取所有行，直到結束符EOF並返回結束，所有的檔案內容會以行為單位除存在變數data內。

再者，第二個for迴圈作用為，將變數data內有包含RESOLUTION.之字串的行儲存下來。如果列印該行出來，會呈現以下內容
```
REMARK   2 RESOLUTION.    3.10 ANGSTROMS.        
```
由於我們希望單獨獲取解析度數值，使用split()語法將該行內容以空格為分隔點，拆解行內容並以變數words儲存，words變數格式為list，解析度為該list中的第4格元素，使用words[3]獲取該數值。以上為其中一個循環，當迴圈循環所有檔案路徑後，我們就可以得到所有蛋白酶的實驗解析度。

現在，除了蛋白酶的實驗解析度外，我們還希望可以將蛋白酶的名稱也同時提取。使用os.path.basename()函式我們可以去除檔案路徑，單獨得到檔案名稱與副檔名。稍微修改迴圈的內容，讀取檔案同時將名稱儲存下來。

```python
for path in filenames:
    file_name = os.path.basename(path)
    split_filename = file_name.split('.')
    molecule_name = split_filename[0]
    
    with open(path, 'r') as outfile:
        data = outfile.readlines()
    
    for line in data:
        if 'RESOLUTION.' in line:
            res_line = line
            words = res_line.split()
            resolution = float(words[3])
            print(molecule_name, ": ", resolution, " Angstroms", sep="")
```
輸出結果
```
1ddo: 3.1 Angstorms
2pkr: 2.4 Angstorms
3iva: 2.7 Angstorms
3vnd: 2.6 Angstorms
4eyr: 1.8 Angstorms
5eu9: 2.05 Angstorms
5veu: 2.91 Angstorms
6zt7: 1.85 Angstorms
7tim: 1.9 Angstorms
```
上面split('.')函式將檔案名稱與副檔名以.號為分隔點分開，我們只需要名稱即可以，所以已split_filename中的第一格元素提取，並儲存在變數molecule_name中。

### 將提取出的資料另存新檔
最後我們將提取的所有資料整理後儲存在txt檔案中，前面我們已經使用with open的語法讀取檔案，現在同樣可以來寫入檔案，只要將參數'r'改為'w+'即可，其中與'w'相同為寫入模式，但'w+'除了寫入同時可以讀取，要注意寫入模式若是檔案已存在，會覆蓋原先所有內容。同樣再次修改上面迴圈
```python
with open('resolution.txt','w+') as outputfile:
    for path in filenames:
        file_name = os.path.basename(path)
        split_filename = file_name.split('.')
        molecule_name = split_filename[0]

        with open(path, 'r') as outfile:
            data = outfile.readlines()

        for line in data:
            if 'RESOLUTION.' in line:
                res_line = line
                words = res_line.split()
                resolution = float(words[3])
                outputfiles.write(F'{molecule_name} : {resolution} Angstorms \n')
```
outputfiles.write()為寫入檔案之函式，其中F為格式化字串的方法，有可讀性且更簡潔不易出錯，使用方法為以單引號將要寫入之內容包住，變數部分以大括號包住即可。執行上述程式碼後，會在同路徑下生成resolutions.txt檔案內容為
```
1ddo : 3.1 Angstorms 
2pkr : 2.4 Angstorms 
3iva : 2.7 Angstorms 
3vnd : 2.6 Angstorms 
4eyr : 1.8 Angstorms 
5eu9 : 2.05 Angstorms 
5veu : 2.91 Angstorms 
6zt7 : 1.85 Angstorms 
7tim : 1.9 Angstorms 
```

教學結束!!

# 蛋白質資料庫 (Protein Data Bank) 讀寫教學

使用 RCSB Protein Data Bank 中下載的蛋白質 PDB 檔案，練習以 python 作檔案讀寫。

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

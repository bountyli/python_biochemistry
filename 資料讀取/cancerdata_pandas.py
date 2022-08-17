import os
import pandas as pd

#使用 Pandas DataFrame 來建立雙維度資料

cancer_file = os.path.join("data","cancer_tumor.csv")
print(cancer_file)

cancer_df = pd.read_csv(cancer_file)

print("取得前面10筆資料")
print(cancer_df.head(10))

print("取得後10筆資料")
print(cancer_df.tail(10))

#使用 .info() 可以看到該檔案資訊
print(cancer_df.info())

#使用中括號指定欄位名稱來得到所需資料集
print("取得單一欄位資料 (資料類型為 Series) ")
print(cancer_df["Gene name"])

print("取得單一欄位資料 (資料類型為 DataFrame) ")
print(cancer_df[["Gene name"]])

print("取得多欄位資料 (資料類型為 DataFrame) ")
print(cancer_df[["Gene name", "Total patients"]])

print("取得索引值0~2的資料")
print(cancer_df[0:3])


#指定索引值和欄位資料取得單一值 .at[索引值, "欄位名稱"]
print("使用at方法得到索引值10、Gene name欄位的資料")
print(cancer_df.at[10,"Gene name"])

#指定索引值和欄位順序取得單一值 .iat[索引值, 欄位順序]
print("使用iat方法得到索引值10、第2欄位的資料")
print(cancer_df.iat[10,1])

#指定索引值和欄位資料取得資料集 .loc[[索引值1,索引值2], ["欄位名稱1","欄位名稱2"]]
print("使用loc方法得到索引值1,2和Gene name,Tumor欄位的資料")
print(cancer_df.loc[[1,2],["Gene name", "Tumor"]])

#指定索引值和欄位資料取得資料集 .iloc[[索引值1,索引值2], ["欄位順序1","欄位順序2"]]
print("使用loc方法得到索引值1,2和2,3欄位的資料")
print(cancer_df.iloc[[1,2],[1,2]])


#依照索引值來排序，並且會回傳新的資料集
new_cancer_df_1 = cancer_df.sort_index(ascending=True)
print("遞增排序")
print(new_cancer_df_1)

new_cancer_df_2 = cancer_df.sort_index(ascending=False)
print("遞減排序")
print(new_cancer_df_2)

#指定欄位並依據內容來排序，回傳新的資料集
new_cancer_df_3 = cancer_df.sort_values(["Total patients"],ascending=True)
print("遞增排序")
print(new_cancer_df_3)

new_cancer_df_4 = cancer_df.sort_values(["Total patients"],ascending=False)
print("遞減排序")
print(new_cancer_df_4)

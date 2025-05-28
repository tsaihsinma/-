import re
import pandas as pd
import os
#批次匯入檔案
rt=r"C:/Users/ctbcm/OneDrive/桌面/CsvFileTest/"
dir_path=os.path.dirname((r"C:/Users/ctbcm/OneDrive/桌面/CsvFileTest/"))

all_file_name=os.listdir(dir_path)
all_file_name=pd.DataFrame(all_file_name)

for i in range(0,len(all_file_name)):
    all_file_name.loc[i,1]=".csv" in all_file_name.loc[i,0]
    
all_file_name=all_file_name[all_file_name[1]!=False]
all_file_name=all_file_name[[0]]
all_file_name=all_file_name.reset_index()
for i in range(0,len(all_file_name)):
    all_file_name.loc[i,1]=i+1

all_file_name=all_file_name[[0,1]]

for j in range(0,len(all_file_name)):
    input_da=all_file_name.loc[j,0]
    output_no=str(int(round(all_file_name.loc[j,1],0)))
    
    data=pd.read_csv(rt+input_da,header=None)
    data=data[[1,2,3,4]]
    
#     data.to_csv(rt+"範例"+output_no+'_測試題.csv',encoding="utf-8-sig",index=False,header=False)

    for i in range(0,len(data)):
            if data.loc[i,1]=="是非":
                data.loc[i,1]=1
                if data.loc[i,2]=="是":
                    data.loc[i,2]=1
                elif data.loc[i,2]=="否":
                    data.loc[i,2]=0
                elif data.loc[i,2]=="非":
                    data.loc[i,2]=0
            elif data.loc[i,1]=="單選":
                data.loc[i,1]=2
            elif data.loc[i,1]=="選擇":
                data.loc[i,1]=2
            elif data.loc[i,1]=="複選":
                data.loc[i,1]=3
                
    try1=data
    
    for i in range(0,len(try1)):
        
        if j ==2:
            try1.loc[i,5]=re.sub('nan','',str(try1.loc[i,4]))
            try1.loc[i,5]=re.sub('1.','',str(try1.loc[i,5]))
            try1.loc[i,6]=re.sub('\n2.',' || ',str(try1.loc[i,5]))
            try1.loc[i,6]=re.sub('\n3.',' || ',str(try1.loc[i,6]))
            try1.loc[i,6]=re.sub('\n4.',' || ',str(try1.loc[i,6]))
            try1.loc[i,6]=re.sub('\n5.',' || ',str(try1.loc[i,6]))
            try1.loc[i,6]=re.sub('\n6.',' || ',str(try1.loc[i,6]))
        elif j in (8,9):
            try1.loc[i,5]=re.sub('nan','',str(try1.loc[i,4]))
            try1.loc[i,5]=re.sub('\(無\)','',str(try1.loc[i,5]))
            try1.loc[i,5]=re.sub('1.','',str(try1.loc[i,5]))
            try1.loc[i,6]=re.sub('\n2.',' || ',str(try1.loc[i,5]))
            try1.loc[i,6]=re.sub('\n3.',' || ',str(try1.loc[i,6]))
            try1.loc[i,6]=re.sub('\n4.',' || ',str(try1.loc[i,6]))
            try1.loc[i,6]=re.sub('\n5.',' || ',str(try1.loc[i,6]))
            try1.loc[i,6]=re.sub('\n6.',' || ',str(try1.loc[i,6]))
            try1.loc[i,6]=re.sub('\n',' ||',str(try1.loc[i,6]))

        elif j ==14:
            try1.loc[i,4]=re.sub('\n\r\r','',str(try1.loc[i,4]))
            try1.loc[i,5]=re.sub('nan','',str(try1.loc[i,4]))
            try1.loc[i,5]=re.sub('1.','',str(try1.loc[i,5]))

            try1.loc[i,6]=re.sub('\n 2.',' || ',str(try1.loc[i,5]))
            try1.loc[i,6]=re.sub('\n 3.',' || ',str(try1.loc[i,6]))
            try1.loc[i,6]=re.sub('\n 4.',' || ',str(try1.loc[i,6]))
            try1.loc[i,6]=re.sub('\n 5.',' || ',str(try1.loc[i,6]))
            try1.loc[i,6]=re.sub('\n 6.',' || ',str(try1.loc[i,6]))

            try1.loc[i,6]=re.sub('\n  2.',' || ',str(try1.loc[i,6]))
            try1.loc[i,6]=re.sub('\n  3.',' || ',str(try1.loc[i,6]))
            try1.loc[i,6]=re.sub('\n  4.',' || ',str(try1.loc[i,6]))
            try1.loc[i,6]=re.sub('\n  5.',' || ',str(try1.loc[i,6]))
            try1.loc[i,6]=re.sub('\n  6.',' || ',str(try1.loc[i,6]))

            try1.loc[i,6]=re.sub('\n2.',' || ',str(try1.loc[i,6]))
            try1.loc[i,6]=re.sub('\n3.',' || ',str(try1.loc[i,6]))
            try1.loc[i,6]=re.sub('\n4.',' || ',str(try1.loc[i,6]))
            try1.loc[i,6]=re.sub('\n5.',' || ',str(try1.loc[i,6]))
            try1.loc[i,6]=re.sub('\n6.',' || ',str(try1.loc[i,6]))

        elif j ==7:
            try1.loc[i,5]=re.sub('nan','',str(try1.loc[i,4]))
            try1.loc[i,5]=re.sub('\(1\)','',str(try1.loc[i,5]))
            try1.loc[i,6]=re.sub('\n\(2\)',' || ',str(try1.loc[i,5]))
            try1.loc[i,6]=re.sub('\n\(3\)',' || ',str(try1.loc[i,6]))
            try1.loc[i,6]=re.sub('\n\(4\)',' || ',str(try1.loc[i,6]))
            try1.loc[i,6]=re.sub('\n\(5\)',' || ',str(try1.loc[i,6]))
            try1.loc[i,6]=re.sub('\n\(6\)',' || ',str(try1.loc[i,6]))
            try1.loc[i,2]=re.sub('1234','1,2,3,4',str(try1.loc[i,2]))
            try1.loc[i,2]=re.sub('234','2,3,4',str(try1.loc[i,2]))

        elif j ==4:
            try1.loc[i,5]=re.sub('nan','',str(try1.loc[i,4]))
            try1.loc[i,5]=re.sub('\(A\)','',str(try1.loc[i,5]))
            try1.loc[i,6]=re.sub('\n\(B\)',' || ',str(try1.loc[i,5]))
            try1.loc[i,6]=re.sub('\n\(C\)',' || ',str(try1.loc[i,6]))
            try1.loc[i,6]=re.sub('\n\(D\)',' || ',str(try1.loc[i,6]))
            try1.loc[i,6]=re.sub('\n\(E\)',' || ',str(try1.loc[i,6]))
            try1.loc[i,6]=re.sub('\n\(F\)',' || ',str(try1.loc[i,6]))
            try1.loc[i,6]=re.sub('\n',' ||',str(try1.loc[i,6]))
            try1.loc[i,2]=re.sub('\(A\)','1 ',str(try1.loc[i,2]))
            try1.loc[i,2]=re.sub('\(B\)','2 ',str(try1.loc[i,2]))
            try1.loc[i,2]=re.sub('\(C\)','3 ',str(try1.loc[i,2]))
            try1.loc[i,2]=re.sub('\(D\)','4 ',str(try1.loc[i,2]))
            try1.loc[i,2]=re.sub('\(E\)','5 ',str(try1.loc[i,2]))
            try1.loc[i,2]=re.sub('  \n',',',str(try1.loc[i,2]))
            try1.loc[i,2]=re.sub('  ',',',str(try1.loc[i,2]))
            try1.loc[i,2]=re.sub(' ','',str(try1.loc[i,2]))
            



        elif try1.loc[0,4]=='nan':
            try1.loc[i,5]=re.sub('nan','',str(try1.loc[i,4]))
            try1.loc[i,5]=re.sub('\n',' || ',str(try1.loc[i,5]))
            try1.loc[i,6]=re.sub('\(A\)','',str(try1.loc[i,5]))
            try1.loc[i,6]=re.sub('\(B\)','',str(try1.loc[i,6]))
            try1.loc[i,6]=re.sub('\(C\)','',str(try1.loc[i,6]))
            try1.loc[i,6]=re.sub('\(D\)','',str(try1.loc[i,6]))
            try1.loc[i,2]=re.sub('、',',',str(try1.loc[i,2]))
            

        elif try1.loc[0,4]=="(無)":
            try1.loc[i,5]=re.sub('\(無\)','',str(try1.loc[i,4]))
            try1.loc[i,6]=re.sub('\n',' || ',str(try1.loc[i,5]))
            try1.loc[i,5]=re.sub('1.','',str(try1.loc[i,5]))
            try1.loc[i,6]=re.sub('\n2.',' || ',str(try1.loc[i,5]))
            try1.loc[i,6]=re.sub('\n3.',' || ',str(try1.loc[i,6]))
            try1.loc[i,6]=re.sub('\n4.',' || ',str(try1.loc[i,6]))
            try1.loc[i,6]=re.sub('\n5.',' || ',str(try1.loc[i,6]))
            try1.loc[i,6]=re.sub('\n6.',' || ',str(try1.loc[i,6]))
            
   
        else:
            try1.loc[i,5]=re.sub('nan','',str(try1.loc[i,4]))
            try1.loc[i,5]=re.sub('1.','',str(try1.loc[i,5]))
            try1.loc[i,5]=re.sub('\n',' || ',str(try1.loc[i,5]))
            try1.loc[i,6]=re.sub('\r\n2.',' || ',str(try1.loc[i,5]))
            try1.loc[i,6]=re.sub('\r\n3.',' || ',str(try1.loc[i,6]))
            try1.loc[i,6]=re.sub('\r\n4.',' || ',str(try1.loc[i,6]))
            try1.loc[i,6]=re.sub('\r\n5.',' || ',str(try1.loc[i,6]))
            try1.loc[i,6]=re.sub('\r\n6.',' || ',str(try1.loc[i,6]))
            
            try1.loc[i,6]=re.sub('2.',' || ',str(try1.loc[i,6]))
            try1.loc[i,6]=re.sub('3.',' || ',str(try1.loc[i,6]))
            try1.loc[i,6]=re.sub('4.',' || ',str(try1.loc[i,6]))
            try1.loc[i,6]=re.sub('5.',' || ',str(try1.loc[i,6]))
            try1.loc[i,6]=re.sub('6.',' || ',str(try1.loc[i,6]))
            
            try1.loc[i,5]=re.sub('nan','',str(try1.loc[i,4]))
            try1.loc[i,5]=re.sub('\n',' || ',str(try1.loc[i,5]))
            try1.loc[i,6]=re.sub('\(A\)','',str(try1.loc[i,5]))
            try1.loc[i,6]=re.sub('\(B\)','',str(try1.loc[i,6]))
            try1.loc[i,6]=re.sub('\(C\)','',str(try1.loc[i,6]))
            try1.loc[i,6]=re.sub('\(D\)','',str(try1.loc[i,6]))  
            try1.loc[i,2]=re.sub('、',',',str(try1.loc[i,2]))
 
 
    
    try1=try1[[1,2,3,6]]
    new_filename = all_file_name.loc[j, 0].split('.')[0] + "_輸出完成.csv"
    try1.to_csv(rt + "output/" + new_filename, encoding="utf-8-sig", index=False, header=False)
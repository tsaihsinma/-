import os
import csv
from docx import Document

# 設定Word文件所在的文件夾路徑
input_folder = 'C:/Users/ctbcm/OneDrive/桌面/WordFileTest'

# 設定CSV文件的保存路徑
output_folder = 'C:/Users/ctbcm/OneDrive/桌面/CsvFileTest'

# 遍歷文件夾中的所有Word文件
for filename in os.listdir(input_folder):
    if filename.endswith(".docx"):
        # 讀取Word文件
        doc = Document(os.path.join(input_folder, filename))

        # 創建對應的CSV文件
        csv_filename = os.path.splitext(filename)[0] + ".csv"
        csv_path = os.path.join(output_folder, csv_filename)

        # 打開CSV文件並準備寫入數據
        with open(csv_path, 'w', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file)

            # 遍歷Word文件中的表格
            for table in doc.tables:
                # 遍歷表格中的每一行，從第三行開始處理
                for row_idx, row in enumerate(table.rows, start=1):
                    if row_idx >= 3:
                        # 每一行的數據將存儲在此列表中
                        row_data = []

                        # 遍歷每個儲存格，並將儲存格中的文本添加到列表中
                        for cell in row.cells:
                            cell_text = cell.text.strip()
                            row_data.append(cell_text)


                        # 寫入CSV文件中
                        csv_writer.writerow(row_data)

print("成功將表格數據轉換並寫入CSV文件。")

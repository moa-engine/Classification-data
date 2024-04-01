import csv
import os

def extract_first_column_from_csv(directory_path, output_file):
    with open(output_file, 'w') as outfile:
        for filename in os.listdir(directory_path):
            if filename.endswith('.csv'):
                csv_file = os.path.join(directory_path, filename)
                with open(csv_file, 'r') as infile:
                    csv_reader = csv.reader(infile)
                    for row in csv_reader:
                        if row:  # بررسی برای وجود ردیف خالی
                            first_column_value = row[0]
                            outfile.write(f"{first_column_value}\n")

# استفاده از تابع برای پیمایش دایرکتوری و استخراج ستون اول از فایل های CSV
extract_first_column_from_csv('/home/mehr32/بارگیری‌ها/داده موآ/csv/', 'ex2.txt')

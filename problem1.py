import glob
import os
import shutil
from datetime import datetime
import csv

# the folder that i want to copy the images from it
folder =  [os.path.normpath(i) for i in glob.glob('C:/Users/MAHMOUD/Desktop/drive-download-20230821T163354Z-001/problem1/dairies/dairies/**/*.jpg', recursive=True)]

image_names = []
image_size = []
image_modification_date = []

for file in folder:
    shutil.copy(file, 'E:/et3-project/images_dataset')
    image_names.append(os.path.basename(file).split('-')[-1])
    image_size.append(str(os.path.getsize(file)/(1024*1024))[:5] + ' MB')
    image_modification_date.append(datetime.fromtimestamp(os.path.getmtime(file)).strftime("%m/%d/%Y, %H:%M:%S"))
    
data = list(zip(image_names, image_size, image_modification_date))

# the Path of CSV file
csv_file_path = 'E:/et3-project/images_data.csv'

# put the data in the CSV file
with open(csv_file_path, mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Image Name', 'Image Size', 'Modification Date'])
    csv_writer.writerows(data)

print("CSV file created successfully.")
import json
import glob
import os

# path of the txt file
input_file_paths = [os.path.normpath(i) for i in glob.glob('C:/Users/MAHMOUD/Desktop/drive-download-20230821T163354Z-001/problem2/image1.txt', recursive=True)]

for input_file_path in input_file_paths:
    with open(input_file_path, 'r') as file:
        lines = file.readlines()

    # Initialize the JSON structure for each file
    data = {
        "annotations": [
            {
                "result": []
            }
        ],
        "data": {
            "image": "/data/upload/image1.jpg"
        }
    }

    # Process each line from the input text
    for line in lines:
        values = line.strip().split()
        if len(values) == 5:
            object_id, x, y, width, height = values
            annotation = {
                "image_rotation": 0,
                "value": {
                    "x": (float(x)-(float(width)/2))*100,
                    "y": (float(y)-(float(height)/2))*100,
                    "width": float(width)*100,
                    "height": float(height)*100,
                    "rotation": 0,
                    "rectanglelabels": ["object"]
                }
            }
            data["annotations"][0]["result"].append(annotation)

    output_file_path = os.path.join('E:/et3-project', os.path.basename(os.path.splitext(input_file_path)[0]) + '.json')

    with open(output_file_path, 'w') as outfile:
        json.dump(data, outfile, indent=4)

    print(f"Conversion complete for {input_file_path}. JSON data written to {output_file_path}")

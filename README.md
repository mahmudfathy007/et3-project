# eT3 TECHNICAL CHALLENGE

Welcome to the Et3 Technical Challenge repository! In this repository, you will find solutions to two problems that require using Python. Before you start, please make sure you have Python installed on your computer. If you don't have Python installed, you can download it from the Microsoft Store or the official Python website (https://www.python.org/).

## Problem 1: Organizing Images

### Instructions:

1. Open the file named `problem1.py` in your preferred Python code editor.
2. On line number 8, replace the existing path with the path to the folder containing sub-folders and images that you want to process.
3. Modify line number 15 to specify the destination path for the file that will contain all the processed images.
4. Also, on line number 23, adjust the file path to point to the desired location for the CSV file you intend to generate.
5. Run the `problem1.py` file.

### Output:

After running the script, you will find a CSV file generated with the processed image information. Here's an example of what the CSV file might look like:

# Example CSV Output

Here's an example of what the CSV output might look like when running the first problem's script:

| Image Name   | Image Size | Modification Date       |
|--------------|------------|-------------------------|
| Milk_001.jpg | 0.026 MB   | 08/21/2023, 20:35:01    |
| Milk_002.jpg | 0.020 MB   | 08/21/2023, 20:35:01    |
| Milk_003.jpg | 0.027 MB   | 08/21/2023, 20:35:01    |
| Milk_004.jpg | 0.022 MB   | 08/21/2023, 20:35:01    |
| Milk_005.jpg | 0.026 MB   | 08/21/2023, 20:35:01    |
| ...          | ...        | ...                     |

This table displays a snippet of the CSV file, presenting the image names, sizes, and modification dates. Your complete CSV file will include more rows based on the images and files you process.


## Problem 2: Text to JSON Conversion

### Instructions:

1. Open the file named `problem2.py` in your preferred Python code editor.
2. On line number 6, update the path to the text file you want to process.
3. Modify line number 42 to specify the destination path for the JSON file where the output will be saved.
4. Run the `problem2.py` file.

### Input Example (Text File):

An example of the expected input format in the text file:

```markdown
0 0.634286 0.175238 0.0914286 0.190476
0 0.632857 0.393333 0.0942857 0.180952
0 0.632857 0.282857 0.0942857 0.401905
0 0.142857 0.439048 0.0942857 0.127619
0 0.106429 0.797143 0.192857 0.379048
```

This excerpt showcases the format of the text input. Your actual input text file may contain more lines with similar data.

### Output Example (JSON File):

After running the script, a JSON file will be generated with the processed text. Here's an example of what the JSON file might contain:

# Example JSON Output

Here's an example of the expected output format for a JSON entry in Problem 2:

```json
{
    "annotations": [
        {
            "result": [
                {
                    "image_rotation": 0,
                    "value": {
                        "x": 58.85717,
                        "y": 8.0,
                        "width": 9.14286,
                        "height": 19.0476,
                        "rotation": 0,
                        "rectanglelabels": [
                            "object"
                        ]
                    }
                },
                {
                    "image_rotation": 0,
                    "value": {
                        "x": 58.571415,
                        "y": 30.2857,
                        "width": 9.42857,
                        "height": 18.0952,
                        "rotation": 0,
                        "rectanglelabels": [
                            "object"
                        ]
                    }
                },
            ]
        }
    ],
    "data": {
        "image": "/data/upload/image1.jpg"
    }
}
```

Feel free to explore, modify, and adapt these scripts to suit your needs. If you encounter any issues or have questions, please don't hesitate to reach out.

Please adjust the paths and descriptions as necessary to match your repository's structure and the specifics of your technical challenge.

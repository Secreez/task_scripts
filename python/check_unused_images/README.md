# Unused Images Checker

This script identifies unused images in a project by scanning `.rmd` and `.qmd` files and comparing the image references with the actual files in the `images` folder. Unused images are logged in a file for review.

## Folder Structure

The script expects a project folder to be structured as follows:

```
project_root/
│
├── images/                     # Folder containing all image files
│   ├── image1.png
│   ├── image2.jpg
│   └── ...
│
├── scripts/unused_images/      # Folder containing the script
│   └── check_unused_images.py  # The Python script
│
├── file1.Rmd                   # .Rmd or .qmd files in the root
├── file2.qmd
├── another_file.Rmd
├── ...
```

## How to Use

1. **Navigate to the `scripts/unused_images/` Folder:** Open a terminal and move to the script's directory:

```
cd project_root/scripts/unused_images
```

2. **Run the Script:** Execute the script using Python:


```
py check_unused_images.py
```

3. **Check the Output:**

- The script scans `.rmd` and `.qmd` files in the root directory and compares the image references with the files in the `images/` folder.
- A log file is created at `project_root/unused_images.log` with a list of unused images.

## Example Log File

The `unused_images.log` will look like this:

```
Unused Images Log
Generated on: 2024-11-15 12:00:00

Total images in folder: 50
Total unused images: 10

------------------------------------

unused_image1.png
unused_image2.jpg
extra_image3.svg
...
```
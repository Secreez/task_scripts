# Using the Broken Links Script for Quarto Markdown (QMD) Files

## Prerequisites

Before using the broken link checker script, ensure that Python is installed on your computer. You can download the latest version of Python from the official website: https://www.python.org/downloads/

During the installation, make sure to check the box **"Add Python to PATH"**, if available. This will allow you to run Python scripts from the command line more easily.

## Installation

The script requires the `requests` package. To install it, open a terminal or command prompt and run the following command:

  ```
  pip install requests
  ```
  
If you're using the given `requirements.txt` file for your project, you can install all dependencies by running:

  ```
  pip install -r requirements.txt
  ```

## Usage

1. **Folder structure**:
   - Place all your `.qmd` files directly in the root directory of your project (as shown in the screenshot).
   - Create a subfolder called `scripts` where the Python script will reside.

2. **Copy the script**:
   - Place the `main.py` file inside the `scripts` folder in your project directory.

3. **Ignore log files in Git** (optional):
   - If you are using Git for version control, create a `.gitignore` file in your project directory.
   - Add the following line to the `.gitignore` file to ignore log files generated by the script:
  
  ```
  logs/Result_*.log
  ```
  
4. **Run the script**:
   - Open a terminal or command prompt.
   - Navigate to the `scripts` folder using `cd`, for example:
  
  ```
  cd /path/to/project_folder/scripts
  ```
   
   - Run the Python script with:

  ```
  python3 main.py
  ```
  
The script will check all the links in the `.qmd` files in the root directory of your project and its subdirectories.

## Folder Structure

Make sure your folder structure looks like this:
  
  ```
  project_folder/
  │
  ├── 01-landschaft.qmd
  ├── 02-landschaftsstruktureller_ansatz.qmd
  ├── 03-lebensraeume.qmd
  ├── ...
  │
  ├── logs/  # logs will be saved here (optional, can be left in root if preferred)
  │   └── Result_*.log
  │
  ├── scripts/
  │   └── main.py (Python script here)
  │   └── requirements.txt (Python dependencies here)
  │
  ```


## Log File

The results will be logged in a file named `Result_YYYYMMDDTHHMM.log` (where `YYYYMMDDTHHMM` is the current date and time) inside the `logs` folder. 

The script will also generate an error log file (`errors_YYYYMMDDTHHMM.log`) for links that encountered problems (timeouts, blocked URLs, etc.). 

You can open the log files to review the status of the links in your `.qmd` files. Pay attention to any links marked as `ERROR`, `BLOCKED`, or `TIMEOUT`, as they may need manual checking.

## Disclaimer

Please note that this script is provided "as is" without warranty of any kind, express or implied. The authors of the script shall not be liable for any damages or losses resulting from the use of the script.
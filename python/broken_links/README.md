# Using the Broken Links Script for Bookdown

## Prerequisites

Before using the broken link checker script, you need to have Python installed on your computer. You can download the latest version of Python from the official website. Follow the installation instructions for your operating system. Make sure to check the box "Add Python to PATH" during installation (if available), as it will make it easier to run Python scripts from the command line.

## Installation

The link-checking script requires the requests package. Open a terminal or command prompt and run the following command to install the package:

```
pip install requests
```

## Usage

1. Create a new folder in your project directory called "auto_scripts".
2. Copy the broken_links.py file into the auto_scripts folder.
3. If you are using Git for version control, create a .gitignore file in your project directory to ignore the log files generated by the script. Add the following line to your .gitignore file:

   ```
   auto_scripts/Result_*.log
   ```

This line tells Git to ignore any log files in the auto*scripts folder that start with "Result*" and have a ".log" extension.

4. Open a terminal or command prompt, navigate to the auto_scripts folder with cd ..., and run the following command:

   ```
   py broken_links.py
   ```

The script will now check all the links in the RMD files within your project directory and its subdirectories.

## Folder Structure

For good measure, make sure your folder structure looks like this:

```
R_Project
│
├── auto_scripts
│   ├── broken_links.py
│   └── (log files will be generated here)
│
├── RMD_Files (or any other folder containing your RMD files)
```

## Log File

The results will be logged in a file named Result_YYYYMMDDTHHMM.log (where YYYYMMDDTHHMM is the current date and time) in the auto_scripts folder. Open the log file generated by the script to review the status of the links in your RMD files. Check any links marked as "ERROR" or with a status code other than 200 to ensure they are still valid.

## Disclaimer

Please note that this script is provided "as is" without warranty of any kind, express or implied. The authors of the script shall not be liable for any damages or losses resulting from the use of the script.

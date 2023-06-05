# Python-Email-Webpage
The Python program provided in this repository collects, summarizes, and emails all the programming assignments for for the course CSC 344 -Programming Languages.

Folder Structure
The assignments should be organized in the following folder structure:
```
csc344
├── a1
├── a2
├── a3
├── a4
└── a5
```
Each assignment folder (a1, a2, etc.) should contain the corresponding programming assignment.

## Program Functionality
The Python program performs the following tasks:

1. Creates a summary HTML file for each assignment, containing the following information:
    - Name of each source file, linked to the file itself
    - Number of lines in the file
    - Alphabetized list of all identifiers used in the program (class, function, rule, variable names), excluding duplicates and commented text
2. Creates a valid HTML web page called index.html in the csc344 directory, which provides links to each of the summary files.
3. Creates a tar.gz file that includes all the assignment source files (excluding non-sources such as executables and .class files) and the HTML files created in the previous step.
4. Prompts the user for an email address and sends the tar.gz file via email using the mutt command-line tool.

## Usage
1. Organize your assignments in the folder structure as described above.
2. Run the Python program and follow the instructions prompted by the program.
3. Enter the path of the directory where the assignments are stored.
4. The program will generate summary HTML files for each assignment and create an index.html file with links to the summaries.
5. The program will create a tar.gz file containing all the assignment sources and HTML files.
6. Enter the email address to which you want to send the tar.gz file.
7. The program will send the email with the tar.gz file attached.

## Requirements
- Python 3.x
- mutt command-line tool (used for sending emails)

## Notes
- Keywords and built-in functions are not filtered from the identifiers list.
- Punctuation that is not part of names will be excluded from the identifiers list.
- Commented text will be excluded from the identifiers list.

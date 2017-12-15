# Salesforce CustomLabels compare utility

This python 3 script can be used for automatic comparison of Custom Labels between two Salesforce sandboxes.

* **CustomLabels.labels** metadata files must exist locally on your computer. 
* You just need to set pathes to CustomLabels.labels metadata files for both Salesforce projects 
and custom names of Salesforce projects in configuration file **default.ini**. 

* Result of comparison is a CSV table with differences in values of some Custom Labels.
  CSV file will contain BOM utf-8 mark before first table header row.


## For using Salesforce CustomLabels compare utility you should verify (description and pathes for Windows):

1. Install Python 3 and set path to python.exe 
   Add path to python folder in Windows -> Advanced system settings -> Environmen Variables -> System varables -> Path
   
   If it is necessary run in command line (cmd) command:
   
   ```pip install ConfigParser```
2. Connect in IDE to two Salesforce orgs and Refresh from server (pull from Salesforce) these orgs
   with included in project Custom Labels **\src\labels\CustomLabels.labels**
   
   In **\src\package.xml** file next lines must exist:
   ```
    <types>
        <members>CustomLabels</members>
        <name>CustomLabels</name>
    </types>
   ```
3. Set path to Salesforce projects in configuration file **default.ini** in **project_path** and **project2_path** variables.
   
   If you want custom name for Labels values column you should set corresponding **project_name** and **project2_name** variables too.
4. Run **custom_labels_compare_csv.bat** from CustomLabels_Compare folder
5. Open resulting **custom_labels_compare.csv** in Excel and compare differences in Custom Labels in above Salesforce projects
6. (_Optional_) If there are some problems with _UTF-8 encoding_ in Excel, 
   just open custom_labels_compare.csv with Notepad, press Save and then reopen it again in Excel
   (thus Notepad will add BOM utf-8 mark in the begining of custom_labels_compare.csv)
7. (_Optional_) Resulting CSV file **custom_labels_compare.csv** may be renamed as you want. But don't change **csv** extension!
   For that purpouse just change **csv_result_file_name** variable in **default.ini**

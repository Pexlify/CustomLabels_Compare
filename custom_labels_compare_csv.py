#!/usr/bin/python
# -*- coding: utf-8 -*-

import inifile
import os
import codecs
import xml.dom.minidom as minidom

def getText(nodelist,tag):
    node_value = ""
    if nodelist.getElementsByTagName(tag) != None:
        for child_node in nodelist.getElementsByTagName(tag):
            node = child_node.childNodes[0]
            if node.nodeType == node.TEXT_NODE:
                node_value = node_value + node.data
    return node_value

# parsing of Custom Labels metadata file and returning dictionary {"Custom Label API name" : "Custom Label value"}
def parseXmlFromFile(file_path):
    label_dict = {}
    xmldoc = minidom.parse(file_path)
    labels_list = xmldoc.getElementsByTagName('labels')
    for label in labels_list:
        label_name = getText(label,'fullName')
        label_value = getText(label,'value')
        ldict = {label_name: label_value}
        label_dict.update(ldict)
    return label_dict

# comparing of values of Custom Labels values by API names
def getLabelsDifferencesDict(label_dict1={},label_dict2={}):
    label_diff_dict = {}
    for label_key in label_dict1.keys():
        label_temp_dict = {}
        if label_dict2.get(label_key) == None or (label_dict2.get(label_key) != None and label_dict1[label_key] != label_dict2[label_key]):
            label_temp_dict = {label_key:label_dict1[label_key]}
            label_diff_dict.update(label_temp_dict)
    return label_diff_dict

# quoting strings
def getEscapedCharsInString(strToEscape):
    return ("\""+strToEscape.replace('"','\"')+"\"")


# getting configuration settings from default.ini
csv_result_file = inifile.get_INI_Value("csv_result_file_name")
file1_path_init = inifile.get_INI_Value("project_path")+inifile.get_INI_Value("metadata_to_compare")
file2_path_init = inifile.get_INI_Value("project2_path")+inifile.get_INI_Value("metadata_to_compare")

file1_proj_init = inifile.get_INI_Value("project_path")
file2_proj_init = inifile.get_INI_Value("project2_path")
if inifile.get_INI_Value("project_name") != None: file1_proj_init = inifile.get_INI_Value("project_name")
if inifile.get_INI_Value("project2_name") != None: file2_proj_init = inifile.get_INI_Value("project2_name")

file1_path = file1_path_init
file2_path = file2_path_init
# fix Windows files path (by doubling escape character)
file1_path = file1_path.replace("\\", "\\\\")
file2_path = file2_path.replace("\\", "\\\\")

label_dict1 = {}
label_dict2 = {}

# parsing of Custom Labels metadata files
label_dict1 = parseXmlFromFile(file1_path)
label_dict2 = parseXmlFromFile(file2_path)

# comparing of keys (Custom Labels API names) and values (Custom Labels values)
label_diff_dict = {}
label_diff_dict.update( getLabelsDifferencesDict(label_dict1,label_dict2) )
label_diff_dict.update( getLabelsDifferencesDict(label_dict2,label_dict1) )

# if differences have been found then save results into CSV file
csv_result = open(csv_result_file, 'w', encoding='utf-8')
if len(label_diff_dict) > 0 :
    # BOM utf-8 signature and header
    csv_result.write( (codecs.BOM_UTF8).decode('utf-8')+('"Label",'+ getEscapedCharsInString(file1_proj_init) +','+ getEscapedCharsInString(file2_proj_init))+"\n" )

for label_key in sorted(label_diff_dict.keys(), key=lambda k: k.lower()):
    label_val1 = ""
    label_val2 = ""
    if label_dict1.get(label_key) != None: label_val1 = label_dict1.get(label_key)
    if label_dict2.get(label_key) != None: label_val2 = label_dict2.get(label_key)
    csv_result.write( (getEscapedCharsInString(label_key) +','+ getEscapedCharsInString(label_val1) +','+ getEscapedCharsInString(label_val2))+"\n" )

csv_result.close()
print( "Found differences",str(len(label_diff_dict)) )

#!/usr/bin/python
# -*- coding: utf-8 -*-

import configparser
import os


# Reading config file and get value by key
def get_INI_Value(value_key):
    value_str = None
    config = configparser.ConfigParser()
    config.read_file(open('default.ini'))
    try:
        if config['DEFAULT'] != None and config['DEFAULT'][value_key] != None:
            value_str = config['DEFAULT'][value_key]
    except:
        pass
    return value_str

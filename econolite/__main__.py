# AUTHOR: BENJAMIN BAESU
# DATE: Feb 5, 2020

# DESCRIPTION: Read all ini files in a given directory. Command line program. Enter __main__.py <path> <keyword in .INI file>
#                   Program will print each key word and the key, if found



# IMPORT FILES-------------------------------
import sys
import os.path
from os import path
from configparser import ConfigParser
#---------------------------------------------

config = ConfigParser()  # ConfigParser object for working with .INI files

# TESTING VALID ARUGMENTS------------------------------------------------------------------------
if len(sys.argv) != 3: # If invalid number of arguments given to program
    print('Invalid number of arguments. Use format: python __main__.py <path> <description>')
    sys.exit()
if not path.exists(str(sys.argv[1])):  # If the given file path is invalid
    print("That file path does not exist. Use format: Use format: python __main__.py <path> <description>")
    sys.exit()
#--------------------------------------------------------------------------------------------------

path = str(sys.argv[1])
description = str(sys.argv[2])


#GETTING INI FILES FROM A DIRECTORY-------------------------------------------------------
iniFiles = [] # List of file names to be appended
with os.scandir(path) as entries:
    for entry in entries:
        if str(entry.name).endswith('ini'): # Only .ini files will be added to the list
            iniFiles.append(path + '/' + str(entry.name))
#------------------------------------------------------------------------------------------

if len(iniFiles) == 0: # Checking if the .ini files exist
    print('That directory does not contain any <.ini> type files.')
    sys.exit()

count = 0 # To keep a count of if anything was printed to user


# READING INI FILES & SECTIONS-----------------------------------------
for i in iniFiles:
    config.read(i)
    for j in config.sections():
        if config.has_option(j, description):
            print(j + ':', config[j][description])
            count += 1
    config.clear()
#----------------------------------------------------------------------

if count == 0: # If nothing was printed, let the user know
    print('No keys in any sections matched provided description.')
    sys.exit()
#----------------------------------------------------------------------

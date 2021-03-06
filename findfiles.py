#!/usr/bin/python3
#Title: findfiles.py
#Author: ApexPredator
#License: MIT
#Github: https://github.com/ApexPredator-InfoSec/find_files
#Description: This script seraches for sensitive files that contain passwords, api keys, etc.
import argparse
import os
from colorama import init, Fore

parser = argparse.ArgumentParser(prog='findfiles.py', usage='python3 findfiles.py \npython3 findfiles.py -n <name of file to search for> \npython3 findfiles.py -f <file contianing list of files to serach for> \npython3 findfiles.py-s <string to search for in file>') #build argument list
parser.add_argument('-n', '--name', help='name of file to serach for', required=False)
parser.add_argument('-f', '--file', help='File Containing list of files to search for', required=False)
parser.add_argument('-s','--string', help='string to search for in file', required=False)
parser.add_argument('-p', '--path', help='path to start search from', required=False)
args = parser.parse_args()

init()
GREEN = Fore.GREEN
RESET = Fore.RESET
RED = Fore.RED

def find_file(path, file_name):

    for root, dir, files in os.walk(path): #walk directory path to build list of files
        if file_name in files: #check if file_name is in the list of files
            result = os.path.join(root, file_name) #build full file path to print
            print(f"[+]Found potential sensitve file: {GREEN}%s{RESET}" %result) #print the potential sensitive files that were found

def find_string(path, string):

    for root, dir, files in os.walk(path): #walk the directory path to build list of files
        for file in files: #iterate thru each file in the list
            file_to_search = os.path.join(root, file) #set full path of each file
            with open(file_to_search, 'r', encoding='latin-1', errors='ignore') as string_search: #open each file
                for line in string_search.readlines(): #iterate thru each line
                    if string in line: #check to if if the search string is present in the line
                        print(f'[+]Found {RED}%s{RESET} in {GREEN}%s{RESET}' %(string, os.path.join(root, file_to_search))) #print the full path to file containing the string
                        print(f'[+]Printing line containing string: {GREEN}%s{RESET}' %line) #print the line that contained the serach string

def main():

    if args.path:
        path = args.path #set path to path passed via arguments
        print("[+]Starting serach for sensitive files in: %s" %path)

    else:
        path = os.path.dirname(os.path.realpath(__file__)) #default to the current directory the script is ran from
        print("[+]Starting search for sensitive files in %s" %path)

    if args.name:
        file_name = args.name #set file name passed via arguments to search for
        find_file(path, file_name)

    elif args.file:
        file = args.file # set file to list containing file names to search for passed via arguments
        with open(file, 'r') as file_list: #parse file to get list of file names to search for
            for line in file_list.readlines(): #read in the lines of file names
                file_name = line.strip()
                find_file(path, file_name) #search for the filename
                find_string(path, file_name)

    if args.string:
        string = args.string #set string to search for passed via arguments
        find_string(path, string)

    if not args.string and not args.file and not args.name:
        find_file(path, 'id_rsa') #default files to serach for if no arguments passed
        find_file(path, '.env')
        find_file(path, 'manage.py')
        find_file(path, 'settings.py')
        find_file(path, 'web.config')
        find_file(path, 'SiteList.xml')
        find_file(path, 'passwords.txt')
        find_file(path, 'password')
        find_file(path, 'passwd')
        find_file(path, 'shadow')
        find_file(path, 'wp-config.php')
        find_file(path, 'config.php')
        find_string(path, 'password') #default strings to search for if no arguments passed
        find_string(path, 'username')
        find_string(path, 'api')
        find_string(path, 'apikey')
        find_string(path, '-----BEGIN RSA PRIVATE KEY-----')

    print('[+]Search complete')

if __name__ == '__main__':

    main()

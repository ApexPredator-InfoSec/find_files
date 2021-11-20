# find_files
Find potentially sensitive files

This script searchs for potentially sensitive files based off of file name or string contained in the file. If no arguments are passed the script will search thru a small list of default files and strings.

The script can search for a single file name, a list of file names, or a string. The script will serch recursivley thru the current directory or another directory path can be passed to start the recursive search from

Usage: 
python3 findfiles.py 
python3 findfiles.py -n <name of file to search for> 
python3 findfiles.py -f <file contianing list of files to serach for> 
python3 findfiles.py -s <string to search for in file>
python3 findfiles.py -p <path to search>
  python3 findfiles.py
 
  ![image](https://user-images.githubusercontent.com/84335647/142732541-bd20a325-9697-468b-b0d7-0bae2f3dfa7e.png)

  python3 findfiles.py -p / -n passwd
  
  ![image](https://user-images.githubusercontent.com/84335647/142732472-352eefa9-30e6-40e4-8009-aa68671089ad.png)

  python3 findfiles -f search.txt
  
  ![image](https://user-images.githubusercontent.com/84335647/142732485-2dd188c4-8d86-4e27-89b1-92665e606f47.png)

  python3 findfiles.py -s 'wp-config'
  
  ![image](https://user-images.githubusercontent.com/84335647/142732524-833009ce-c3ad-4409-82c3-4334e4dbf8c1.png)

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
  ![image](https://user-images.githubusercontent.com/84335647/142559198-e3b1868e-271a-48b2-b9d7-2bd41d946fb0.png)

  python3 findfiles.py -p / -n passwd
  ![image](https://user-images.githubusercontent.com/84335647/142559439-7776dc8b-7eaf-472e-80f8-3ebb471db2d9.png)

  python3 findfiles -f search.txt
  ![image](https://user-images.githubusercontent.com/84335647/142559522-2059c1f4-67df-4acc-a8a1-337c061b81bc.png)

  python3 findfiles.py -s 'wp-config'
  ![image](https://user-images.githubusercontent.com/84335647/142559630-bcdff7a0-ac03-4b20-89a0-1e97b3ff55f8.png)

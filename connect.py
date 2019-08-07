# -*- coding: utf-8 -*-
"""
Spyder Editor
Programmer: Eve Jimenez Sagastegui
Class: Independent Study
Date: 06/10/19
"""

import ftputil



import argparse, sys
ap = argparse.ArgumentParser(description='This script will connect to the FTP server, check if new files are available, and then download the updated files if that is the case. It specifically checks the files in the path indicated to see if those files have been modified since its been uploaded.')
ap.add_argument("path", type=str, help = "indicate the folder where current pubtator files are or where they wish to be placed")
ap.add_argument("email", help = "email must be provided")
if len(sys.argv)==1:
    ap.print_help(sys.stderr)
    sys.exit(1)

args = vars(ap.parse_args())

pathlocation = args['path'] 
email = args['email']

# connect to FTP server using name (anonymous) and password (email address)
host = ftputil.FTPHost('ftp.ncbi.nlm.nih.gov', 'anonymous', email)

# list all files/folders in current directory
host.listdir('pub')

#changes directory to pub
host.chdir('pub')
host.chdir('lu')
host.chdir('PubTator')



files = ['disease2pubtator.gz',
         'gene2pubtator.gz',
         'mutation2pubtator.gz',
         'chemical2pubtator.gz']


#for loop where files are being checked/updated
for i in files:
    if host.download_if_newer(i, pathlocation+i) == True:
        print("downloading: " + i)
    else:
        print(i + " is up to date")

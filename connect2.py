# -*- coding: utf-8 -*-
"""
Spyder Editor
Programmer: Eve Jimenez Sagastegui
Class: Independent Study
Date: 06/10/19
"""

import ftputil
import datetime



import argparse, sys
ap = argparse.ArgumentParser(description='This script will connect to the FTP server, check if new files are available, and then download the updated files if that is the case. Format: Month Date Year')
ap.add_argument("month",type=int, help = "Format: Month Date Year")
ap.add_argument("day",type=int, help = "Format: Month Date Year")
ap.add_argument("year",type=int, help = "Format: Month Date Year")
ap.add_argument("path", type=str, help = "directory")

if len(sys.argv)==1:
    ap.print_help(sys.stderr)
    sys.exit(1)

args = vars(ap.parse_args())

pathlocation = args['path']
month = args['month'] 
day = args['day'] 
year = args['year'] 


# connect to FTP server using name (anonymous) and password (email address)
host = ftputil.FTPHost('ftp.ncbi.nlm.nih.gov', 'anonymous', 'dancikg@easternct.edu')


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


disease = host.stat('disease2pubtator.gz')
gene = host.stat('gene2pubtator.gz')
mutation = host.stat('mutation2pubtator.gz')
chemical = host.stat('chemical2pubtator.gz')
lastModifiedDate = {'disease2pubtator.gz': disease[8],
                    'gene2pubtator.gz' : gene[8],
                    'mutation2pubtator.gz': mutation[8],
                    'chemical2pubtator.gz': chemical[8]}

userTime = datetime.datetime(year,month,day,0,0).timestamp()


updateFiles=[]
for i in files:
    if lastModifiedDate[i] < userTime:
        print(i + " is up to date")
    else:
        updateFiles.append(i)
        print(i + " is not up to date.")


for j in updateFiles:
    host.download(j, pathlocation + j)
    print("downloading: " + j)




#!/usr/bin/python

# Author: Carlo Torniai
# Creation Date: 11/20/2011
# Last revision: 06/12/2012
# This programs reads an ontofox_input file and saves the  response back from
# the Ontofox service in a file
# Example of usage: ontofoxCurl.py input_file output_file


# Notes:
# In order to run the script on MAcOS you need to have pycurl isntalled
# In order to install pycurl you need to have XTools installed: http://developer.apple.com/xcode/
# Once you've installed XTools in order to install pycurl you will need to run the following command
# sudo env ARCHFLAGS="-arch x86_64" easy_install setuptools pycurl==7.19.0


import pycurl
import sys
import StringIO
ontofoxCURL = 'http://ontofox.hegroup.org/service.php'

# Add parameter input file output file
if (len(sys.argv) < 2):
    print("Usage: ontofoxCurl.py input_file output_file")
    exit(0)
input_file = sys.argv[1]
output_file = sys.argv[2]

#Initialize pycurl and save the ontofox with input file and save the output
c = pycurl.Curl()
c.setopt(pycurl.URL, ontofoxCURL)
c.setopt(pycurl.HTTPHEADER, ["Accept:"])
c.setopt(pycurl.POST, 1)
c.setopt(pycurl.POSTFIELDS, 'file=@%s' %input_file)
c.setopt(pycurl.HTTPPOST, [(('file'), (pycurl.FORM_FILE, input_file)), ])
b = open(output_file, 'w')
c.setopt(pycurl.WRITEFUNCTION, b.write)
c.perform()
c.close()
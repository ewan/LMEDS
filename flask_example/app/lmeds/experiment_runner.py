'''
Created on Mar 2, 2014

@author: tmahrt

The only function of this code is to add LMEDS to the current path and 
execute the desired code.

-----
instructions
-----

COPY THIS FILE TO THE .cgi FOLDER
'''

import cgi
import cgitb
cgitb.enable()

import sys

# This should point to the directory /lmeds/
sys.path.append("/home/gail/Senior_Project/flask_example/app/")


from lmeds import rptMain


def runExperiment(leafFolder, sequenceFile, languageFile, disableRefresh):
    survey = rptMain.WebSurvey(leafFolder, sequenceFile, languageFile, disableRefresh)
    retval = survey.run()
    print 'exp_runner ' + str(retval) + '\n'
    return retval #added return
    
    

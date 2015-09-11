"""
========
helpers - functions of general use throughout test suite, i.e., no Selenium here!
========
"""
import os, subprocess, requests
import time
from datetime import datetime
import pdb


def generate_date_stamp():
    """ generates a unique datestamp of the form yyyymmdd-hhmmss """
    now = datetime.now()
    return(now.strftime("%Y%m%d-%H%M%S-%f"))

def generate_email(prefix="test",suffix="@getbetter.com"):
    """ given a unique date stamp, generates a unique email address for automated registering
        of Better accounts """
    return(prefix + "+" + generate_date_stamp() + suffix)

def get_default_password():
    return 'qwertyui'

def generate_password(date_stamp,str="clqa"):
    """ 
    given a date stamp of the form yyyymmdd-hhmmss-mmmmmm and a string,
    generates a password from interleaving characters from both 
    """
    return(str[0] + date_stamp[4] + str[1] + date_stamp[5] + str[2] + date_stamp[6])

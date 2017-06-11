#!/usr/local/bin/python

<<<<<<< HEAD
"""
Python script that allows you to SSH into a VM and sudo to a user to create .ssh/authorized_keys files with approriate permissions

ToDo : Time of execution is painfully slow due to prompt, investigate how to leverage expect() instead

"""



=======
>>>>>>> master
import os
import sys
import time
from pexpect import pxssh
import getpass
import re

try:
    import getpass, pexpect, re
except ImportError:
    print "You need to install certain modules, please review the README.MD"
    exit()



def prompt_user():
    hostname = raw_input('Please enter a host string : ')
    username = raw_input('Please enter a username : ')
    password = getpass.getpass('Please enter secure password : ' )
    password2 = getpass.getpass('Please enter password again : ' )
    if password == password2:
        print 'Passwords match, proceeding..'
    else:
        print 'passwords fail... exiting'
        exit()
    new_user = raw_input('Please enter the new user you want to sudo to : ')
    return (hostname, username, password, new_user)


def ssh_test(hostname, username, password, new_user):
    try:
        print 'Trying ssh connection... \n'
        prompt = r'\[sudo\] password for %s: ' % username
        print hostname
        s = pxssh.pxssh()
        s.login (hostname, username, password)
        s.sendline ('echo $HOSTNAME')   # run a command
        s.prompt()             # match the prompt
        local_hostname = s.before          # print everything before the prompt.
        #login_username = r'[%s@%s ~]$' % username, local_hostname
        #new_user = r'[%s@%s ~]$' % username, local_hostname
        print local_hostname
        s.sendline ('ps -ef')
        s.prompt()             # match the prompt
        print s.before          # print everything before the prompt.
        ####Start of the slow sudo stuff######
        s.sendline ('sudo su ebiz-jenkins')
        s.expect(prompt)
        s.sendline(password)
        s.prompt()
        #s.prompt()
        print s.before
        s.sendline ('mkdir $HOME/.ssh')
        s.prompt()
        print s.before
        s.sendline ('touch $HOME/.ssh/authorized_keys')
        s.prompt()
        print s.before
        s.sendline ('chmod 600 $HOME/.ssh/authorized_keys')
        s.prompt()
        print s.before
        s.sendline ('chmod 700 $HOME/.ssh')
        s.prompt()
        print s.before
<<<<<<< HEAD
=======

#ToDO allow sudo user to return a quick prompt via expect instead of prompt(). Use the login_username and new_user to act as harcoded prompts

>>>>>>> master
    except pxssh.ExceptionPxssh, e:
        print "pxssh failed on login."
        print str(e)

def main():
    hostname, username, password, new_user = prompt_user()
    ssh_test(hostname, username, password, new_user)




if __name__ == "__main__":
    main()

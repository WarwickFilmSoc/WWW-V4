'''
    Class for running git commands on the host machine. User on the 
    server_update page by Website Admins once they have made changes to the
    source code on GitHub

    methods:
        get_current_commit:
            returns a text string with the servers git commit ID and name
        get_current_commit_date:
            returns a string with the date of the last commit pulled to the 
            machine
        update:
            runs a git pull on the server which in turns updates files on the 
            server, then returns the raw output from the terminal which 
            normally contains the added/modified files since the last commit

    Depends on:
        subprocess

    Used by:
        pages/server_update

    Original Author: Joel Speed
    Originally Authored: Aug 10, 2015
    Update by: Joel Speed
    Last Updated: Aug 16, 2015
'''
from subprocess import call, check_output
    
def get_current_commit():
    ''' Returns the current commit ID and name from the web host '''
    return check_output(['git',
                         'log',
                         '-1',
                         '--pretty=oneline',
                         '--abbrev-commit'
                         ])
    
def get_current_commit_date():
    ''' Returns the date of the current commit in the form "Day MMM DD HH:MM:SS
    YYYY +HHMM"'''
    return check_output(['git', 'log', '-1', '--pretty=format:%cd'])
    
def update():
    '''Runs a git pull on the server and makes sure that the server directory 
    is exactly at that commit by using a git reset. It then returns the output
    from the git update, eg. insertions, deletions etc.'''
    pull = check_output(['git', 'pull', '-f'])
    call(['git', 'reset', '--hard', 'origin/master'])
    return pull
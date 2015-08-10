from subprocess import call, check_output
    
def get_current_commit():
    return check_output(['git', 'log', '-1', '--pretty=oneline', '--abbrev-commit'])
    
def get_current_commit_date():
    return check_output(['git', 'log', '-1', '--pretty=format:%cd'])
    
def update():
    call(['git', '-C /usr/share/www-v4/ pull -f'])
    call(['git', 'reset --hard origin/master'])
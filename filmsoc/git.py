from subprocess import call
    
def get_current_commit():
    return call(['git', '--git-dir="/usr/share/www-v4/.git" log -1 --pretty="oneline" --abbrev-commit'])
    
def get_current_commit_date():
    return call(['git', '--git-dir="/usr/share/www-v4/.git" log -1 --pretty="format:%cd"'])
    
def update():
    call(['git', '-C /usr/share/www-v4/ pull -f'])
    call(['git', 'reset --hard origin/master'])
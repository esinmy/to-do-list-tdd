import random
from fabric.contrib.files import append, exists
from fabric.api import cd, env, local, run

REPO_URL = 'https://github.com/esinmy/to-do-list-tdd'
env.hosts = ['ec2-18-222-232-158.us-east-2.compute.amazonaws.com']
env.user = 'ubuntu'
env.key_filename = r'D:\!MY_DOC\aws_key_pair.pem'

def local_uname():
    local('uname -a')

def remote_uname():
    run('uname -a')

def deploy():
    site_folder = f'/home/{env.user}/sites/{env.host}'
    run(f'mkdir -p {site_folder}')
    with cd(site_folder):
        _get_latest_source()
        _update_virtualenv()
        _create_or_update_dotenv()
        _update_static_files()
        _update_database()

def _get_latest_source():
    if exists(".git"):
        run("git fetch")
    else:
        run(f"git clone {REPO_URL} .")
    current_commit = local("git log -n 1 --format=%H", capture=True)
    run(f"git reset --hard {current_commit}")

def _update_virtualenv():
    if not exists("venv/bin/pip"):
        run(f"python3 -m venv venv")
    run("./venv/bin/pip install -r requirements.txt")

def _create_or_update_dotenv():
    append(".env", "DJANGO_DEBUG_FALSE=y")
    append(".env", "SITENAME={env.host}")
    current_contents = run("cat .env")
    if "DJANGO_SECRET_KEY" not in current_contents:
        new_secret = "".join(random.SystemRandom().choices("abcdefghijklmnopqrstuvwxyz0123456789"))
        append(".env", f"DJANGO_SECRET_KEY={new_secret}")

def _update_static_files():
    run("./venv/bin/python3 manage.py collectstatic --noinput")

def _update_database():
    run("./venv/bin/python3 manage.py migrate --noinput")



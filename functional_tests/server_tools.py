from fabric.api import run, prefix
from fabric.context_managers import settings, shell_env, prefix

# def _get_virtual_environment(host):
#     run(f'source ~/sites/{host}/virtualenv/bin/activate')

def _get_manage_dot_py(host):
    return f'~/sites/{host}/virtualenv/bin/python3.6 ~/sites/{host}/manage.py'


def reset_database(host):
#     run(f'source ~/sites/{host}/virtualenv/bin/activate')
    manage_dot_py = _get_manage_dot_py(host)
    with settings(host_string=f'elspeth@{host}'), prefix(workon virtualenv):
        run(f'{manage_dot_py} flush --noinput')


def _get_server_env_vars(host):
#     run(f'source ~/sites/{host}/virtualenv/bin/activate')
    env_lines = run(f'cat ~/sites/{host}/.env').splitlines()
    return dict(l.split('=') for l in env_lines if l)


def create_session_on_server(host, email):
    manage_dot_py = _get_manage_dot_py(host)
#     run(f'source ~/sites/{host}/virtualenv/bin/activate')
    with settings(host_string=f'elspeth@{host}'):
        env_vars = _get_server_env_vars(host)
        with shell_env(**env_vars):
            session_key = run(f'{manage_dot_py} create_session {email}')
            return session_key.strip()

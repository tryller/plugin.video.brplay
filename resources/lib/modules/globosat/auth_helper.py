from resources.lib.modules import control
from resources.lib.modules.globosat.auth import auth as authenticator


def get_credentials():
    username = control.setting('globoplay_username')
    password = control.setting('globoplay_password')

    if not username or not password or username == '' or password == '':
        return None

    credentials = authenticator().authenticate(username, password)

    return credentials


def get_globosat_token():
    return get_credentials()


def get_globosat_cookie(provider_id):
    return {'WMPTOKEN_%s' % provider_id: get_credentials()}
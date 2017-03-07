import json

from util.http_ import get_page, get_str_page
from util.kms import kms_decrypt_token

ENCRYPTED_APP_ID = 'AQECAHhGzpV8mQljdA8TKn6ES9Tut5So2p1aU1owbT61BvTSSgAAAH4wfAYJKoZIhvcNAQcGoG8wbQIBADBoBgkqhkiG9w0B' \
                   'BwEwHgYJYIZIAWUDBAEuMBEEDItA7huGm/2I1ll2/AIBEIA7PYu2OMlSDEGSPpkUf8eHrL6tFw36VZ5N9Pq/wMmkVT49QtwF' \
                   'MtdXSdtvQzsrNuI7alojg6TWqe46HOg='

APP_ID = kms_decrypt_token(ENCRYPTED_APP_ID)


def get_user_id_by_name(name, realm='eu'):
    url = "https://api.worldoftanks.{0}/wot/account/list/?application_id={2}&search={1}".format(realm, name, APP_ID)
    resp = json.loads(get_page(url).decode('utf-8'))
    if resp.get('status') == 'ok':
        return resp.get('data')[0].get('account_id')


def get_user_info(account_id, realm='eu'):
    url = 'https://api.worldoftanks.{0}/wot/account/info/?application_id={2}&account_id={1}'.format(realm, account_id,
                                                                                                    APP_ID)
    return json.loads(get_str_page(url))


def get_user_all_stats_by_id(account_id, **kwargs):
    return get_user_info(account_id, **kwargs) \
        .get('data') \
        .get('{0}'.format(account_id)) \
        .get('statistics').get('all')


id = get_user_id_by_name('Duselmanus')
print(get_user_all_stats_by_id(id))

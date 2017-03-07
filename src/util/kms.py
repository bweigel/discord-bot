from base64 import b64decode

import boto3


def kms_decrypt_token(token):
    kms = boto3.client('kms')
    return kms.decrypt(CiphertextBlob=b64decode(token))['Plaintext'].decode('utf-8')

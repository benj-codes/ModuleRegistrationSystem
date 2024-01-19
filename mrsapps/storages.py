from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'moduleregc0011865'
    account_key = 'GmrOHc09vXuCJLSK8spaTTAjknvlcaympWKeqeSheHqeFDibc4bVqvMz10XLQRWjRAnaLsvwjQle+AStBzfVMQ=='
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'moduleregc0011865'
    account_key = 'GmrOHc09vXuCJLSK8spaTTAjknvlcaympWKeqeSheHqeFDibc4bVqvMz10XLQRWjRAnaLsvwjQle+AStBzfVMQ=='
    azure_container = 'static'
    expiration_secs = None
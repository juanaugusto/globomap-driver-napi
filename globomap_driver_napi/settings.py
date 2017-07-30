import os

NETWORKAPI_ENDPOINT = os.getenv('NETWORKAPI_ENDPOINT')
NETWORKAPI_USER = os.getenv('NETWORKAPI_USER')
NETWORKAPI_PASSWORD = os.getenv('NETWORKAPI_PASSWORD')
NETWORKAPI_RMQ_USER = os.getenv('NETWORKAPI_RMQ_USER')
NETWORKAPI_RMQ_PASSWORD = os.getenv('NETWORKAPI_RMQ_PASSWORD')
NETWORKAPI_RMQ_HOST = os.getenv('NETWORKAPI_RMQ_HOST')
NETWORKAPI_RMQ_PORT = int(os.getenv('NETWORKAPI_RMQ_PORT', 5672))
NETWORKAPI_RMQ_VIRTUAL_HOST = os.getenv('NETWORKAPI_RMQ_VIRTUAL_HOST')
NETWORKAPI_RMQ_QUEUE = os.getenv('NETWORKAPI_RMQ_QUEUE')

MAP_FUNC = {
    'VipRequest': [
        {
            'name': 'vip',
            'package': 'globomap_driver_napi.kind',
            'class': 'Kind',
            'method': 'vip',
            'provider': 'napi'
        }
    ],
    'VipRequestPortPool': [
        {
            'name': 'port',
            'package': 'globomap_driver_napi.kind',
            'class': 'Kind',
            'method': 'port',
            'provider': 'napi'
        }
    ],
    'ServerPool': [
        {
            'name': 'pool',
            'package': 'globomap_driver_napi.kind',
            'class': 'Kind',
            'method': 'pool',
            'provider': 'napi'
        }
    ],
    'ServerPoolMember': [
        {
            'name': 'pool_comp_unit',
            'package': 'globomap_driver_napi.kind',
            'class': 'Kind',
            'method': 'pool_comp_unit',
            'provider': 'napi'
        },
        {
            'name': 'comp_unit',
            'package': 'globomap_driver_napi.kind',
            'class': 'Kind',
            'method': 'comp_unit',
            'provider': 'globomap'
        }
    ]
}
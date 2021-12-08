#!/usr/bin/python
# encoding=utf-8

import sys
if sys.version_info[0] == 2:
    # Python2
    import core.AepSdkRequestSend as AepSdkRequestSend
else:
    # Python3
    from apis.core import AepSdkRequestSend



#参数body: 类型json, 参数不可以为空
#  描述:body,具体参考平台api说明
def DeleteEdgeInstanceDevice(appKey, appSecret, body):
    path = '/aep_edge_gateway/instance/devices'
    head = {}
    param = {}
    version = '20201226000026'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, body, version, application, None, key, 'POST')
    if response is not None:
        return response.read()
    return None

#参数gatewayDeviceId: 类型String, 参数不可以为空
#  描述:
#参数pageNow: 类型long, 参数可以为空
#  描述:
#参数pageSize: 类型long, 参数可以为空
#  描述:
def QueryEdgeInstanceDevice(appKey, appSecret, gatewayDeviceId, pageNow, pageSize):
    path = '/aep_edge_gateway/instance/devices'
    head = {}
    param = {'gatewayDeviceId':gatewayDeviceId, 'pageNow':pageNow, 'pageSize':pageSize}
    version = '20201226000022'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, None, version, application, None, key, 'GET')
    if response is not None:
        return response.read()
    return None

#参数body: 类型json, 参数不可以为空
#  描述:body,具体参考平台api说明
def CreateEdgeInstance(appKey, appSecret, body):
    path = '/aep_edge_gateway/instance'
    head = {}
    param = {}
    version = '20201226000017'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, body, version, application, None, key, 'POST')
    if response is not None:
        return response.read()
    return None

#参数body: 类型json, 参数不可以为空
#  描述:body,具体参考平台api说明
def EdgeInstanceDeploy(appKey, appSecret, body):
    path = '/aep_edge_gateway/instance/settings'
    head = {}
    param = {}
    version = '20201226000010'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, body, version, application, None, key, 'POST')
    if response is not None:
        return response.read()
    return None

#参数id: 类型long, 参数不可以为空
#  描述:
def DeleteEdgeInstance(appKey, appSecret, id):
    path = '/aep_edge_gateway/instance'
    head = {}
    param = {'id':id}
    version = '20201225235957'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, None, version, application, None, key, 'DELETE')
    if response is not None:
        return response.read()
    return None

#参数body: 类型json, 参数不可以为空
#  描述:body,具体参考平台api说明
def AddEdgeInstanceDevice(appKey, appSecret, body):
    path = '/aep_edge_gateway/instance/device'
    head = {}
    param = {}
    version = '20201226000004'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, body, version, application, None, key, 'POST')
    if response is not None:
        return response.read()
    return None

#参数body: 类型json, 参数不可以为空
#  描述:body,具体参考平台api说明
def AddEdgeInstanceDrive(appKey, appSecret, body):
    path = '/aep_edge_gateway/instance/drive'
    head = {}
    param = {}
    version = '20201225235952'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, body, version, application, None, key, 'POST')
    if response is not None:
        return response.read()
    return None


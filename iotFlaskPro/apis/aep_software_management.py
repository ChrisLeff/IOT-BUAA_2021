#!/usr/bin/python
# encoding=utf-8

import sys
if sys.version_info[0] == 2:
    # Python2
    import core.AepSdkRequestSend as AepSdkRequestSend
else:
    # Python3
    from apis.core import AepSdkRequestSend



#参数id: 类型long, 参数不可以为空
#  描述:升级包id
#参数MasterKey: 类型String, 参数不可以为空
#  描述:MasterKey，在产品概况中可以查看
#参数body: 类型json, 参数不可以为空
#  描述:body,具体参考平台api说明
def UpdateSoftware(appKey, appSecret, id, MasterKey, body):
    path = '/aep_software_management/software'
    head = {}
    param = {'id':id}
    version = '20200529232851'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, body, version, application, MasterKey, key, 'PUT')
    if response is not None:
        return response.read()
    return None

#参数id: 类型long, 参数不可以为空
#  描述:升级包id
#参数productId: 类型long, 参数不可以为空
#  描述:产品id
#参数MasterKey: 类型String, 参数不可以为空
#  描述:MasterKey,在产品概况中可以查询
def DeleteSoftware(appKey, appSecret, id, productId, MasterKey):
    path = '/aep_software_management/software'
    head = {}
    param = {'id':id, 'productId':productId}
    version = '20200529232809'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, None, version, application, MasterKey, key, 'DELETE')
    if response is not None:
        return response.read()
    return None

#参数id: 类型long, 参数不可以为空
#  描述:升级包ID
#参数productId: 类型long, 参数不可以为空
#  描述:产品id
#参数MasterKey: 类型String, 参数不可以为空
#  描述:MasterKey，可在产品概况中查看
def QuerySoftware(appKey, appSecret, id, productId, MasterKey):
    path = '/aep_software_management/software'
    head = {}
    param = {'id':id, 'productId':productId}
    version = '20200529232806'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, None, version, application, MasterKey, key, 'GET')
    if response is not None:
        return response.read()
    return None

#参数productId: 类型long, 参数不可以为空
#  描述:产品id
#参数searchValue: 类型String, 参数可以为空
#  描述:查询条件，可以根据升级包名称模糊查询
#参数pageNow: 类型long, 参数可以为空
#  描述:当前页数
#参数pageSize: 类型long, 参数可以为空
#  描述:每页记录数
#参数MasterKey: 类型String, 参数不可以为空
#  描述:MasterKey，可以在产品概况中查看
def QuerySoftwareList(appKey, appSecret, productId, searchValue, pageNow, pageSize, MasterKey):
    path = '/aep_software_management/softwares'
    head = {}
    param = {'productId':productId, 'searchValue':searchValue, 'pageNow':pageNow, 'pageSize':pageSize}
    version = '20200529232801'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, None, version, application, MasterKey, key, 'GET')
    if response is not None:
        return response.read()
    return None


#!/usr/bin/python
# encoding=utf-8

import sys
if sys.version_info[0] == 2:
    # Python2
    import core.AepSdkRequestSend as AepSdkRequestSend
else:
    # Python3
    from apis.core import AepSdkRequestSend



#参数MasterKey: 类型String, 参数不可以为空
#  描述:MasterKey，在产品概况中查看
#参数body: 类型json, 参数不可以为空
#  描述:body,具体参考平台api说明
def OperationalSoftwareUpgradeTask(appKey, appSecret, MasterKey, body):
    path = '/aep_software_upgrade_management/operational'
    head = {}
    param = {}
    version = '20200529233236'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, body, version, application, MasterKey, key, 'POST')
    if response is not None:
        return response.read()
    return None

#参数id: 类型long, 参数不可以为空
#  描述:主任务id
#参数productId: 类型long, 参数不可以为空
#  描述:产品id
#参数taskStatus: 类型long, 参数可以为空
#  描述:子任务状态：
#       0.待升级，1.查询设备版本号，2.新版本通知，3.请求升级包，4.设备上报下载状态，5.执行升级，6.通知升级结果
#参数searchValue: 类型String, 参数可以为空
#  描述:查询值，设备ID或设备编号(IMEI)或设备名称模糊查询
#参数pageNow: 类型long, 参数可以为空
#  描述:当前页码
#参数pageSize: 类型long, 参数可以为空
#  描述:每页显示数
#参数MasterKey: 类型String, 参数不可以为空
#  描述:MasterKey，可在产品概况中查看
def QuerySoftwareUpgradeSubtasks(appKey, appSecret, id, productId, taskStatus, searchValue, pageNow, pageSize, MasterKey):
    path = '/aep_software_upgrade_management/details'
    head = {}
    param = {'id':id, 'productId':productId, 'taskStatus':taskStatus, 'searchValue':searchValue, 'pageNow':pageNow, 'pageSize':pageSize}
    version = '20200529233212'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, None, version, application, MasterKey, key, 'GET')
    if response is not None:
        return response.read()
    return None

#参数id: 类型long, 参数不可以为空
#  描述:主任务id
#参数productId: 类型long, 参数不可以为空
#  描述:产品id
#参数MasterKey: 类型String, 参数不可以为空
#  描述:MasterKey,产品概况中查看
def QuerySoftwareUpgradeTask(appKey, appSecret, id, productId, MasterKey):
    path = '/aep_software_upgrade_management/task'
    head = {}
    param = {'id':id, 'productId':productId}
    version = '20200529233136'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, None, version, application, MasterKey, key, 'GET')
    if response is not None:
        return response.read()
    return None

#参数MasterKey: 类型String, 参数不可以为空
#  描述:MasterKey，产品概况可以查看
#参数body: 类型json, 参数不可以为空
#  描述:body,具体参考平台api说明
def CreateSoftwareUpgradeTask(appKey, appSecret, MasterKey, body):
    path = '/aep_software_upgrade_management/task'
    head = {}
    param = {}
    version = '20200529233123'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, body, version, application, MasterKey, key, 'POST')
    if response is not None:
        return response.read()
    return None

#参数id: 类型long, 参数不可以为空
#  描述:主任务id
#参数MasterKey: 类型String, 参数不可以为空
#  描述:MasterKey，在产品概况中查看
#参数body: 类型json, 参数不可以为空
#  描述:body,具体参考平台api说明
def ModifySoftwareUpgradeTask(appKey, appSecret, id, MasterKey, body):
    path = '/aep_software_upgrade_management/task'
    head = {}
    param = {'id':id}
    version = '20200529233103'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, body, version, application, MasterKey, key, 'PUT')
    if response is not None:
        return response.read()
    return None

#参数id: 类型long, 参数不可以为空
#  描述:主任务id
#参数MasterKey: 类型String, 参数不可以为空
#  描述:MasterKey，在产品概况中查看
#参数body: 类型json, 参数不可以为空
#  描述:body,具体参考平台api说明
def ControlSoftwareUpgradeTask(appKey, appSecret, id, MasterKey, body):
    path = '/aep_software_upgrade_management/control'
    head = {}
    param = {'id':id}
    version = '20200529233046'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, body, version, application, MasterKey, key, 'PUT')
    if response is not None:
        return response.read()
    return None

#参数id: 类型long, 参数不可以为空
#  描述:主任务id
#参数productId: 类型long, 参数不可以为空
#  描述:产品id
#参数updateBy: 类型String, 参数可以为空
#  描述:修改人
#参数MasterKey: 类型String, 参数不可以为空
#  描述:MasterKey，在产品概况中查看
def DeleteSoftwareUpgradeTask(appKey, appSecret, id, productId, updateBy, MasterKey):
    path = '/aep_software_upgrade_management/task'
    head = {}
    param = {'id':id, 'productId':productId, 'updateBy':updateBy}
    version = '20200529233037'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, None, version, application, MasterKey, key, 'DELETE')
    if response is not None:
        return response.read()
    return None

#参数id: 类型long, 参数可以为空
#  描述:主任务id,isSelectDevice为1时必填，为2不必填
#参数productId: 类型long, 参数不可以为空
#  描述:产品id
#参数isSelectDevice: 类型String, 参数不可以为空
#  描述:查询类型（1.查询加入升级设备，2.查询可加入升级设备）
#参数pageNow: 类型long, 参数可以为空
#  描述:当前页，默认1
#参数pageSize: 类型long, 参数可以为空
#  描述:每页显示数，默认20
#参数MasterKey: 类型String, 参数不可以为空
#  描述:MasterKey，产品概况中查看
#参数deviceIdSearch: 类型String, 参数可以为空
#  描述:根据设备id精确查询
#参数deviceNameSearch: 类型String, 参数可以为空
#  描述:根据设备名称精确查询
#参数imeiSearch: 类型String, 参数可以为空
#  描述:根据imei号精确查询，仅支持LWM2M协议
#参数deviceGroupIdSearch: 类型String, 参数可以为空
#  描述:根据群组id精确查询
def QuerySoftwareUpradeDeviceList(appKey, appSecret, id, productId, isSelectDevice, pageNow, pageSize, MasterKey, deviceIdSearch, deviceNameSearch, imeiSearch, deviceGroupIdSearch):
    path = '/aep_software_upgrade_management/devices'
    head = {}
    param = {'id':id, 'productId':productId, 'isSelectDevice':isSelectDevice, 'pageNow':pageNow, 'pageSize':pageSize, 'deviceIdSearch':deviceIdSearch, 'deviceNameSearch':deviceNameSearch, 'imeiSearch':imeiSearch, 'deviceGroupIdSearch':deviceGroupIdSearch}
    version = '20200529233027'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, None, version, application, MasterKey, key, 'GET')
    if response is not None:
        return response.read()
    return None

#参数id: 类型long, 参数不可以为空
#  描述:
#参数productId: 类型long, 参数不可以为空
#  描述:
#参数MasterKey: 类型String, 参数不可以为空
#  描述:
def QuerySoftwareUpgradeDetail(appKey, appSecret, id, productId, MasterKey):
    path = '/aep_software_upgrade_management/detail'
    head = {}
    param = {'id':id, 'productId':productId}
    version = '20200529233010'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, None, version, application, MasterKey, key, 'GET')
    if response is not None:
        return response.read()
    return None

#参数productId: 类型long, 参数不可以为空
#  描述:产品id
#参数pageNow: 类型long, 参数可以为空
#  描述:当前页数，默认1
#参数pageSize: 类型long, 参数可以为空
#  描述:每页显示数，默认20
#参数MasterKey: 类型String, 参数不可以为空
#  描述:MasterKey，产品概况中查看
#参数searchValue: 类型String, 参数可以为空
#  描述:查询条件，支持主任务名称模糊查询
def QuerySoftwareUpgradeTaskList(appKey, appSecret, productId, pageNow, pageSize, MasterKey, searchValue):
    path = '/aep_software_upgrade_management/tasks'
    head = {}
    param = {'productId':productId, 'pageNow':pageNow, 'pageSize':pageSize, 'searchValue':searchValue}
    version = '20200529232940'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, None, version, application, MasterKey, key, 'GET')
    if response is not None:
        return response.read()
    return None


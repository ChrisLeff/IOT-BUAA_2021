#!/usr/bin/python
# encoding=utf-8

import sys
if sys.version_info[0] == 2:
    # Python2
    import core.AepSdkRequestSend as AepSdkRequestSend
else:
    # Python3
    from apis.core import AepSdkRequestSend



def QueryTenantDeviceCount(appKey, appSecret):
    path = '/tenant_device_statistics/queryTenantDeviceCount'
    head = {}
    param = {}
    version = '20201225122555'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, None, version, application, None, key, 'GET')
    if response is not None:
        return response.read()
    return None

#参数dateType: 类型String, 参数不可以为空
#  描述:时间类型：d:天；m:月
#参数type: 类型String, 参数不可以为空
#  描述:数据类型：1：设备总数量，激活数，活跃数；3：设备活跃数，活跃率
def QueryTenantDeviceTrend(appKey, appSecret, dateType, type):
    path = '/tenant_device_statistics/queryTenantDeviceTrend'
    head = {}
    param = {'dateType':dateType, 'type':type}
    version = '20201225122550'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, None, version, application, None, key, 'GET')
    if response is not None:
        return response.read()
    return None

def QueryTenantDeviceActiveCount(appKey, appSecret):
    path = '/tenant_device_statistics/queryTenantDeviceActiveCount'
    head = {}
    param = {}
    version = '20201225122558'
    application = appKey
    key = appSecret
    response = AepSdkRequestSend.sendSDKRequest(path, head, param, None, version, application, None, key, 'GET')
    if response is not None:
        return response.read()
    return None


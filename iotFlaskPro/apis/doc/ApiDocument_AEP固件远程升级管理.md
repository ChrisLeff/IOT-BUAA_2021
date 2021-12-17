# AEP固件远程升级管理
## API列表
|API名称 | 安全认证方式 | 签名认证方式 | 描述 |
|:-------|:------|:--------|:--------|
|QueryRemoteUpgradeDetail|none|hmac-sha1|查询主任务详情统计|
|QueryRemoteUpgradeTask|none|hmac-sha1|查询任务详情基本信息|
|ControlRemoteUpgradeTask|none|hmac-sha1|主任务执行控制(启动主任务开始升级)|
|QueryRemoteUpradeDeviceList|none|hmac-sha1|查询可升级设备列表|
|DeleteRemoteUpgradeTask|none|hmac-sha1|删除远程升级主任务|
|QueryRemoteUpgradeTaskList|none|hmac-sha1|查询升级主任务列表|
|ModifyRemoteUpgradeTask|none|hmac-sha1|修改远程升级主任务|
|CreateRemoteUpgradeTask|none|hmac-sha1|创建远程升级主任务|
|OperationalRemoteUpgradeTask|none|hmac-sha1|操作远程升级主任务（包括设备升级，取消升级，重试升级）|
|QueryRemoteUpgradeSubtasks|none|hmac-sha1|查询升级详情子任务列表|

## API调用
### 请求地址

|环境 | HTTP请求地址  | HTTPS请求地址 |
|:-------|:------|:--------|
|正式环境|ag-api.ctwing.cn/aep_upgrade_management|ag-api.ctwing.cn/aep_upgrade_management|

### 公共入参

公共请求参数是指每个接口都需要使用到的请求参数。

|参数名称 | 含义  | 位置 | 描述|
|:-------|:------|:--------|:--------|
|application|应用标识|HEAD|应用的App Key，如果需要进行签名认证则需要填写，例如：dAaFG7DiPt8|
|signature|签名数据|HEAD|将业务数据连同timestamp、application一起签名后的数据，如果需要进行签名认证则需要填写|
|timestamp|UNIX格式时间戳|HEAD|如果需要进行签名认证则需要填写，例如：1515752817580|
|version|API版本号|HEAD|可以指定API版本号访问历史版本|

## API 文档说明
### API名称：QueryRemoteUpgradeDetail   版本号: 20190615001517

#### 描述

查询主任务详情统计

#### 请求信息

请求路径：/detail

请求方法：GET

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|id|QUERY|Long|true|主任务id|
|productId|QUERY|Long|true|产品id|
|MasterKey|HEAD|String|false|MasterKey|


#### 返回信息

##### 返回参数类型
json

##### 返回结果示例
{
  "code": 0,
  "msg": "ok",
  "result": {
    "jobId": 3439,
    "productId": 10005986,
    "tenantId": "10007905",
    "jobName": "彩色电视",
    "jobStatus": 3,
    "firmwareName": "DVD发",
    "outTime": 24,
    "firmwareId": 3275,
    "firmwareUrl": "/webctdfs/file?tenantId=10007905&productId=10005986&fileName=1557995327619400.xlsx&fileType=package",
    "fileName": "工作簿1.xlsx",
    "firmwareVersion": "10.3",
    "jobDesc": "sss",
    "takeTime": "93时43分",
    "createTime": "2019-05-16 16:28:57",
    "retryTimes": 0,
    "allNum": 1
  }
}

##### 异常返回示例


#### 错误码

|错误码 | 错误信息| 描述|
|:-------|:------|:--------|
|200|OK|请求正常|
|400|Bad request|请求数据缺失或格式错误|
|401|Unauthorized|请求缺少权限|
|403|Forbidden|请求禁止|
|404|Not found|请求资源不存在|
|500|Internal Error|服务器异常|
|503|Service Unavailable|服务不可用|
|504|Async Service|异步通讯|

### API名称：QueryRemoteUpgradeTask   版本号: 20190615001509

#### 描述

查询任务详情基本信息

#### 请求信息

请求路径：/task

请求方法：GET

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|id|QUERY|Long|true|主任务id|
|productId|QUERY|Long|true|产品id|
|MasterKey|HEAD|String|false|MasterKey|


#### 返回信息

##### 返回参数类型
json

##### 返回结果示例
{
  "code": 0,
  "msg": "ok",
  "result": {
    "jobId": 3456,
    "productId": 10005977,
    "tenantId": "10007905",
    "jobName": "sdcsd",
    "jobStatus": 1,
    "deviceStatus": 1,
    "firmwareName": "测得所所所所所所所",
    "outTime": 0,
    "firmwareId": 3297,
    "firmwareUrl": "/upload?tenantId=10007905&productId=10005977&fileName=1558343157951402.xlsx&fileType=package",
    "fileName": "1558343157951402.xlsx",
    "firmwareVersion": "1.3251",
    "jobDesc": "cccc",
    "takeTime": "",
    "createTime": "2019-05-21 10:34:04",
    "upgradePlan": 1,
    "retryTimes": 2,
    "productName": "复用lw二进制 远程升级"
  }
}

##### 异常返回示例


#### 错误码

|错误码 | 错误信息| 描述|
|:-------|:------|:--------|
|200|OK|请求正常|
|400|Bad request|请求数据缺失或格式错误|
|401|Unauthorized|请求缺少权限|
|403|Forbidden|请求禁止|
|404|Not found|请求资源不存在|
|500|Internal Error|服务器异常|
|503|Service Unavailable|服务不可用|
|504|Async Service|异步通讯|

### API名称：ControlRemoteUpgradeTask   版本号: 20190615001456

#### 描述

主任务执行控制(启动主任务开始升级)

#### 请求信息

请求路径：/control

请求方法：PUT

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|id|QUERY|Long|true|主任务id|
|MasterKey|HEAD|String|false|MasterKey|

#### 请求BODY

##### 数据类型：
json

##### 内容描述：
{
  "productId": 10005977,
  "runStatus": 2
}
描述：
  "productId": 产品id 必填,Integer
  "runStatus": 执行方式：2.立即启动（目前仅支持立即启动）必填，Integer

#### 返回信息

##### 返回参数类型
default

##### 返回结果示例
{
  "code": 0,
  "msg": "ok",
  "result": "SUCCESS"
}

##### 异常返回示例


#### 错误码

|错误码 | 错误信息| 描述|
|:-------|:------|:--------|
|200|OK|请求正常|
|400|Bad request|请求数据缺失或格式错误|
|401|Unauthorized|请求缺少权限|
|403|Forbidden|请求禁止|
|404|Not found|请求资源不存在|
|500|Internal Error|服务器异常|
|503|Service Unavailable|服务不可用|
|504|Async Service|异步通讯|

### API名称：QueryRemoteUpradeDeviceList   版本号: 20190615001451

#### 描述

查询可升级设备列表

#### 请求信息

请求路径：/devices

请求方法：GET

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|id|QUERY|String|false|主任务id,isSelectDevice为1时必填，为2不必填|
|productId|QUERY|String|true|产品id|
|isSelectDevice|QUERY|String|true|查询类型（1.查询加入升级设备，2.查询可加入升级设备）|
|pageNow|QUERY|String|false|当前页，默认1|
|pageSize|QUERY|String|false|每页显示数，默认20|
|MasterKey|HEAD|String|false|MasterKey|
|deviceIdSearch|QUERY|String|false|根据设备id精确查询|
|deviceNameSearch|QUERY|String|false|根据设备名称精确查询|
|imeiSearch|QUERY|String|false|根据imei号精确查询，仅支持LWM2M协议|
|deviceNoSearch|QUERY|String|false|根据设备编号精确查询，仅支持T_Link协议|
|deviceGroupIdSearch|QUERY|String|false|根据群组id精确查询|


#### 返回信息

##### 返回参数类型
json

##### 返回结果示例
{
	"code": 0,
	"msg": "ok",
	"result": {
		"pageNum": 1,
		"pageSize": 20,
		"total": 2,
		"list": [{
			"deviceName": "十大城市打车",
			"deviceId": "1000598611113",
			"deviceSn": "11113",
			"imei": "",
			"taskId": "",
			"createTime": 1557995303000,
			"deviceStatus": 1,
			"firmwareVersion": "",
			"taskState": "",
			"resultCode": "",
			"flag": "",
			"netStatus": 2,
			"onlineAt": 1557995312831,
			"offlineAt": 1557995314321,
			"deviceGroupId": ""
		}]
	}
}

##### 异常返回示例


#### 错误码

|错误码 | 错误信息| 描述|
|:-------|:------|:--------|
|200|OK|请求正常|
|400|Bad request|请求数据缺失或格式错误|
|401|Unauthorized|请求缺少权限|
|403|Forbidden|请求禁止|
|404|Not found|请求资源不存在|
|500|Internal Error|服务器异常|
|503|Service Unavailable|服务不可用|
|504|Async Service|异步通讯|

### API名称：DeleteRemoteUpgradeTask   版本号: 20190615001444

#### 描述

删除远程升级主任务

#### 请求信息

请求路径：/task

请求方法：DELETE

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|id|QUERY|Long|true|主任务id|
|productId|QUERY|Long|true|产品id|
|updateBy|QUERY|String|false|修改人|
|MasterKey|HEAD|String|false|MasterKey|


#### 返回信息

##### 返回参数类型
default

##### 返回结果示例
{
  "code": 0,
  "msg": "ok",
  "result": "SUCCESS"
}

##### 异常返回示例


#### 错误码

|错误码 | 错误信息| 描述|
|:-------|:------|:--------|
|200|OK|请求正常|
|400|Bad request|请求数据缺失或格式错误|
|401|Unauthorized|请求缺少权限|
|403|Forbidden|请求禁止|
|404|Not found|请求资源不存在|
|500|Internal Error|服务器异常|
|503|Service Unavailable|服务不可用|
|504|Async Service|异步通讯|

### API名称：QueryRemoteUpgradeTaskList   版本号: 20190615001440

#### 描述

查询升级主任务列表

#### 请求信息

请求路径：/tasks

请求方法：GET

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|productId|QUERY|Long|true|产品id|
|pageNow|QUERY|Long|false|当前页数，默认1|
|pageSize|QUERY|Long|false|每页显示数，默认20|
|MasterKey|HEAD|String|false|MasterKey|
|searchValue|QUERY|String|false|查询条件，支持主任务名称模糊查询|


#### 返回信息

##### 返回参数类型
json

##### 返回结果示例
{
  "code": 0,
  "msg": "ok",
  "result": {
    "pageNum": 1,
    "pageSize": 20,
    "total": 1,
    "list": [
      {
        "jobId": 3456,
        "productId": 10005977,
        "tenantId": "10007905",
        "jobName": "sdcsd",
        "jobStatus": 1,
        "firmwareName": "测得所所所所所所所",
        "outTime": 0,
        "firmwareId": 3297,
        "firmwareUrl": "/upload?tenantId=10007905&productId=10005977&fileName=1558343157951402.xlsx&fileType=package",
        "fileName": "1558343157951402.xlsx",
        "firmwareVersion": "1.3251",
        "jobDesc": "测试测试",
        "takeTime": "",
        "createTime": "2019-05-21 10:34:04",
        "upgradePlan": 1,
        "retryTimes": 2,
        "productName": "复用lw二进制 远程升级"
      }
    ]
  }
}

##### 异常返回示例


#### 错误码

|错误码 | 错误信息| 描述|
|:-------|:------|:--------|
|200|OK|请求正常|
|400|Bad request|请求数据缺失或格式错误|
|401|Unauthorized|请求缺少权限|
|403|Forbidden|请求禁止|
|404|Not found|请求资源不存在|
|500|Internal Error|服务器异常|
|503|Service Unavailable|服务不可用|
|504|Async Service|异步通讯|

### API名称：ModifyRemoteUpgradeTask   版本号: 20190615001433

#### 描述

修改远程升级主任务

#### 请求信息

请求路径：/task

请求方法：PUT

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|id|QUERY|Long|true|主任务id|
|MasterKey|HEAD|String|false||

#### 请求BODY

##### 数据类型：
json

##### 内容描述：
{
  "updateBy": "huangliang",
  "jobDesc": "sddd",
  "jobName": "北向测试",
  "productId": 10005986,
  "retryTimes": 1,
  "outTime": "24"
}

  "updateBy": 修改人 选填，String,
  "jobDesc": 主任务描述 选填，String,
  "jobName": 主任务名称 选填，String,
  "productId": 产品id 必填，Integer,
  "retryTimes": 自动重试次数（范围0-3次）选填，仅支持LWM2M协议，Integer
  "outTime":超时时间（小时）范围1-168小时 选填，仅支持T_Link协议且不可为0

#### 返回信息

##### 返回参数类型
default

##### 返回结果示例
{
  "code": 0,
  "msg": "ok",
  "result": "SUCCESS"
}

##### 异常返回示例


#### 错误码

|错误码 | 错误信息| 描述|
|:-------|:------|:--------|
|200|OK|请求正常|
|400|Bad request|请求数据缺失或格式错误|
|401|Unauthorized|请求缺少权限|
|403|Forbidden|请求禁止|
|404|Not found|请求资源不存在|
|500|Internal Error|服务器异常|
|503|Service Unavailable|服务不可用|
|504|Async Service|异步通讯|

### API名称：CreateRemoteUpgradeTask   版本号: 20190615001416

#### 描述

创建远程升级主任务

#### 请求信息

请求路径：/task

请求方法：POST

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|MasterKey|HEAD|String|false|MasterKey|

#### 请求BODY

##### 数据类型：
json

##### 内容描述：
{
  "createBy": "huangliang",
  "firmwareId": 3167,
  "jobDesc": "sddd",
  "jobName": "北向测试",
  "productId": 10004516,
  "retryTimes": 1,
  "outTime": "129"
}
描述：
  "createBy": 创建人 选填，String,
  "firmwareId": 固件id 必填，Integer,
  "jobDesc": 主任务描述 选填，String,
  "jobName": 主任务名称 必填，String,
  "productId": 产品id 必填，Integer,
  "retryTimes": 自动重试次数（范围0-3次）选填，仅支持LWM2M协议且必填，Integer
  "outTime":超时时间（小时）范围1-168小时，仅支持T_Link协议且必填且不可为0

#### 返回信息

##### 返回参数类型
json

##### 返回结果示例
{
  "code": 0,
  "msg": "ok",
  "result": {
    "jobId": 3451,
    "productId": 10005978,
    "tenantId": "10007905",
    "jobName": "北向测试1",
    "jobDesc": "sddd",
    "firmwareId": 3278,
    "createBy": "huangliang",
    "productProtocol": 3,
    "upgradePlan": 1,
    "retryTimes": 1
  }
}

##### 异常返回示例


#### 错误码

|错误码 | 错误信息| 描述|
|:-------|:------|:--------|
|200|OK|请求正常|
|400|Bad request|请求数据缺失或格式错误|
|401|Unauthorized|请求缺少权限|
|403|Forbidden|请求禁止|
|404|Not found|请求资源不存在|
|500|Internal Error|服务器异常|
|503|Service Unavailable|服务不可用|
|504|Async Service|异步通讯|

### API名称：OperationalRemoteUpgradeTask   版本号: 20190615001412

#### 描述

操作远程升级主任务（包括设备升级，取消升级，重试升级）

#### 请求信息

请求路径：/operational

请求方法：POST

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|MasterKey|HEAD|String|false|MasterKey|

#### 请求BODY

##### 数据类型：
json

##### 内容描述：
T-Link协议：
T-Link加入升级
{
  "createBy": "string",
  "deviceIdList": "string",
  "jobId": 0,
  "operational": 0,
  "productId": 0
}
T_LINK取消升级	
{
  "createBy": "string",
  "jobId": 0,
  "operational": 0,
  "productId": 0,
  "taskIdList": "string"
}
描述：
  "createBy": 操作人 必填，String,
  "deviceIdList": 设备id集合[用,号隔开] 加入升级必填,String, 
  "jobId": 主任务id 必填，Integer,
  "productId":产品id 必填，Integer
  "operational":操作类型，1：加入升级，2：取消升级
  "taskIdList":要取消升级的子任务id[用,号隔开]，取消升级必填,String
LWM2M协议：
加入升级
{
  "createBy": "string",
  "deviceInfoList": [
    {
      "deviceId": "string"
    }
  ],
  "jobId": 0,
  "operational": 1,
  "productId": 0
}
LWM2M取消、重试升级
{
  "createBy": "String",
  "jobId": 0,
  "operational": 0,
  "productId": 0,
  "taskIdList": "String"
}
描述：
  "createBy": 操作人 必填，String,
  "deviceInfoList": [
    {
      "deviceId":设备id 必填 String
    }
  ]设备信息集合(设备id)必填,
  "jobId": 主任务id 必填，Integer,
  "operational":操作类型，1：加入升级，2：取消升级，3：重试升级,
  "productId":产品id 必填，Integer，
  "taskIdList":要取消、重试升级的子任务id[用,号隔开]，取消或重试升级必填,String

#### 返回信息

##### 返回参数类型
default

##### 返回结果示例
{
  "code": 0,
  "msg": "ok",
  "result": "SUCCESS"
}

##### 异常返回示例


#### 错误码

|错误码 | 错误信息| 描述|
|:-------|:------|:--------|
|200|OK|请求正常|
|400|Bad request|请求数据缺失或格式错误|
|401|Unauthorized|请求缺少权限|
|403|Forbidden|请求禁止|
|404|Not found|请求资源不存在|
|500|Internal Error|服务器异常|
|503|Service Unavailable|服务不可用|
|504|Async Service|异步通讯|

### API名称：QueryRemoteUpgradeSubtasks   版本号: 20190615001406

#### 描述

查询升级详情子任务列表

#### 请求信息

请求路径：/details

请求方法：GET

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|id|QUERY|Long|true|主任务id|
|productId|QUERY|Long|true|产品id|
|taskStatus|QUERY|Long|false|子任务状态\nT-Link协议必填（1.待升级，2.升级中，3.升级成功，4.升级失败）\nLWM2M协议选填（0:升级可行性判断,1:升级可行性判断失败,2:分派升级任务,3:分派升级任务失败,4:分派下载任务,5:分派下载任务失败,6:开始升级,7:升级失败,8:升级完成,9:取消当前设备的升级,10:取消当前设备升级成功,11:取消当前设备升级失败）|
|searchValue|QUERY|String|false|查询值，设备ID或设备编号(IMEI)或设备名称模糊查询|
|pageNow|QUERY|Long|false|当前页码|
|pageSize|QUERY|Long|false|每页显示数|
|MasterKey|HEAD|String|false|MasterKey|


#### 返回信息

##### 返回参数类型
json

##### 返回结果示例
{
	"code": 0,
	"msg": "ok",
	"result": {
		"pageNum": 1,
		"pageSize": 20,
		"total": 1,
		"list": [{
			"jobId": 3456,
			"taskId": 59,
			"productId": 10005977,
			"tenantId": "10007905",
			"deviceName": "sdcsd",
			"deviceId": "10339a95176c4bfbb029ef319318ee15",
			"deviceSn": "",
			"imei": "122344584512546",
			"productName": "复用lw二进制 远程升级",
			"updateTime": "",
			"taskState": "0",
			"resultCode": "-1",
			"finishTime": "",
			"preUpgradeVersion": "",
			"upgradedVersion": ""
		}]
	}
}

##### 异常返回示例


#### 错误码

|错误码 | 错误信息| 描述|
|:-------|:------|:--------|
|200|OK|请求正常|
|400|Bad request|请求数据缺失或格式错误|
|401|Unauthorized|请求缺少权限|
|403|Forbidden|请求禁止|
|404|Not found|请求资源不存在|
|500|Internal Error|服务器异常|
|503|Service Unavailable|服务不可用|
|504|Async Service|异步通讯|


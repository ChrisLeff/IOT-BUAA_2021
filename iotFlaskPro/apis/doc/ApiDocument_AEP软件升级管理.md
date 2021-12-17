# AEP软件升级管理
## API列表
|API名称 | 安全认证方式 | 签名认证方式 | 描述 |
|:-------|:------|:--------|:--------|
|OperationalSoftwareUpgradeTask|none|hmac-sha1|操作远程软件升级主任务（包括设备升级，取消升级，重试升级,删除子任务）|
|QuerySoftwareUpgradeSubtasks|none|hmac-sha1|查询软件升级详情子任务列表|
|QuerySoftwareUpgradeTask|none|hmac-sha1|查询任务详情基本信息|
|CreateSoftwareUpgradeTask|none|hmac-sha1|创建远程软件升级主任务|
|ModifySoftwareUpgradeTask|none|hmac-sha1|修改软件升级主任务信息|
|ControlSoftwareUpgradeTask|none|hmac-sha1|主任务执行控制(启动主任务开始升级)|
|DeleteSoftwareUpgradeTask|none|hmac-sha1|删除软件升级主任务|
|QuerySoftwareUpradeDeviceList|none|hmac-sha1|查询可升级设备列表|
|QuerySoftwareUpgradeDetail|none|hmac-sha1|查询主任务详情统计|
|QuerySoftwareUpgradeTaskList|none|hmac-sha1|查询升级主任务列表|

## API调用
### 请求地址

|环境 | HTTP请求地址  | HTTPS请求地址 |
|:-------|:------|:--------|
|正式环境|ag-api.ctwing.cn/aep_software_upgrade_management|ag-api.ctwing.cn/aep_software_upgrade_management|

### 公共入参

公共请求参数是指每个接口都需要使用到的请求参数。

|参数名称 | 含义  | 位置 | 描述|
|:-------|:------|:--------|:--------|
|application|应用标识|HEAD|应用的App Key，如果需要进行签名认证则需要填写，例如：dAaFG7DiPt8|
|signature|签名数据|HEAD|将业务数据连同timestamp、application一起签名后的数据，如果需要进行签名认证则需要填写|
|timestamp|UNIX格式时间戳|HEAD|如果需要进行签名认证则需要填写，例如：1515752817580|
|version|API版本号|HEAD|可以指定API版本号访问历史版本|

## API 文档说明
### API名称：OperationalSoftwareUpgradeTask   版本号: 20200529233236

#### 描述

操作远程软件升级主任务（包括设备升级，取消升级，重试升级,删除子任务）

#### 请求信息

请求路径：/operational

请求方法：POST

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|MasterKey|HEAD|String|true|MasterKey，在产品概况中查看|

#### 请求BODY

##### 数据类型：
json

##### 内容描述：
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
取消/重试升级,删除升级子任务
{
  "jobId": 0,
  "operational": 0,
  "productId": 0,
  "taskIdList": "String"
}
描述：
  "createBy": 操作人 选填，String,
  "deviceInfoList": [
    {
      "deviceId":设备id 必填 String
    }
  ]设备信息集合(设备id)必填,
  "jobId": 主任务id 必填，Integer,
  "operational":操作类型，1：加入升级，2：取消升级，3：重试升级,4删除升级子任务,
  "productId":产品id 必填，Integer，
  "taskIdList":要取消或重试升级的子任务id[用,号隔开]，取消、重试或删除升级必填,String

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

### API名称：QuerySoftwareUpgradeSubtasks   版本号: 20200529233212

#### 描述

查询软件升级详情子任务列表

#### 请求信息

请求路径：/details

请求方法：GET

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|id|QUERY|Long|true|主任务id|
|productId|QUERY|Long|true|产品id|
|taskStatus|QUERY|Long|false|子任务状态：\n0.待升级，1.查询设备版本号，2.新版本通知，3.请求升级包，4.设备上报下载状态，5.执行升级，6.通知升级结果|
|searchValue|QUERY|String|false|查询值，设备ID或设备编号(IMEI)或设备名称模糊查询|
|pageNow|QUERY|Long|false|当前页码|
|pageSize|QUERY|Long|false|每页显示数|
|MasterKey|HEAD|String|true|MasterKey，可在产品概况中查看|


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
        "jobId": 8340,
        "taskId": 7528,
        "productId": 10013604,
        "tenantId": "300",
        "deviceName": "测试设备",
        "deviceId": "119b7827919d401d8462149ad34ff396",
        "imei": "869060030003827",
        "productName": "升级测试",
        "updateTime": "2019-11-27 09:26:59",
        "taskState": "6",
        "resultCode": "5000",
        "finishTime": "2019-11-27",
        "preUpgradeVersion": "V1.6",
        "upgradedVersion": "V1.0"
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

### API名称：QuerySoftwareUpgradeTask   版本号: 20200529233136

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
|MasterKey|HEAD|String|true|MasterKey,产品概况中查看|


#### 返回信息

##### 返回参数类型
json

##### 返回结果示例
{
  "code": 0,
  "msg": "ok",
  "result": {
    "jobId": 11003,
    "productId": 10013604,
    "tenantId": "300",
    "jobName": "北向测试1111",
    "jobStatus": 2,
    "softwareVersion": "1.23",
    "fileName": "WaterV1.063000000000_signed.zip",
    "jobDesc": "2万222",
    "takeTime": "25时17分",
    "createTime": "2020-05-14 15:23:36"
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

### API名称：CreateSoftwareUpgradeTask   版本号: 20200529233123

#### 描述

创建远程软件升级主任务

#### 请求信息

请求路径：/task

请求方法：POST

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|MasterKey|HEAD|String|true|MasterKey，产品概况可以查看|

#### 请求BODY

##### 数据类型：
json

##### 内容描述：
{
  "createBy": "huangliang",
  "softwareId": 3167,
  "jobDesc": "sddd",
  "jobName": "北向测试",
  "productId": 10004516
}
描述：
  "createBy": 创建人 选填，String,
  "softwareId": 升级包版本id 必填，Integer,
  "jobDesc": 主任务描述 选填，String,
  "jobName": 主任务名称 必填，String,
  "productId": 产品id 必填，Integer

#### 返回信息

##### 返回参数类型
json

##### 返回结果示例
{
  "code": 0,
  "msg": "ok",
  "result": {
    "jobId": 11002,
    "productId": 10013604,
    "tenantId": "300",
    "jobName": "csdcds",
    "jobDesc": "ddddd",
    "softwareId": 7351
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

### API名称：ModifySoftwareUpgradeTask   版本号: 20200529233103

#### 描述

修改软件升级主任务信息

#### 请求信息

请求路径：/task

请求方法：PUT

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|id|QUERY|Long|true|主任务id|
|MasterKey|HEAD|String|true|MasterKey，在产品概况中查看|

#### 请求BODY

##### 数据类型：
json

##### 内容描述：
{
  "jobDesc": "sddd",
  "jobName": "北向测试",
  "productId": 10005986
}

  "jobDesc": 主任务描述 选填，String,
  "jobName": 主任务名称 选填，String,
  "productId": 产品id 必填，Integer

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

### API名称：ControlSoftwareUpgradeTask   版本号: 20200529233046

#### 描述

主任务执行控制(启动主任务开始升级)

#### 请求信息

请求路径：/control

请求方法：PUT

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|id|QUERY|Long|true|主任务id|
|MasterKey|HEAD|String|true|MasterKey，在产品概况中查看|

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

### API名称：DeleteSoftwareUpgradeTask   版本号: 20200529233037

#### 描述

删除软件升级主任务

#### 请求信息

请求路径：/task

请求方法：DELETE

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|id|QUERY|Long|true|主任务id|
|productId|QUERY|Long|true|产品id|
|updateBy|QUERY|String|false|修改人|
|MasterKey|HEAD|String|true|MasterKey，在产品概况中查看|


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

### API名称：QuerySoftwareUpradeDeviceList   版本号: 20200529233027

#### 描述

查询可升级设备列表

#### 请求信息

请求路径：/devices

请求方法：GET

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|id|QUERY|Long|false|主任务id,isSelectDevice为1时必填，为2不必填|
|productId|QUERY|Long|true|产品id|
|isSelectDevice|QUERY|String|true|查询类型（1.查询加入升级设备，2.查询可加入升级设备）|
|pageNow|QUERY|Long|false|当前页，默认1|
|pageSize|QUERY|Long|false|每页显示数，默认20|
|MasterKey|HEAD|String|true|MasterKey，产品概况中查看|
|deviceIdSearch|QUERY|String|false|根据设备id精确查询|
|deviceNameSearch|QUERY|String|false|根据设备名称精确查询|
|imeiSearch|QUERY|String|false|根据imei号精确查询，仅支持LWM2M协议|
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
		"total": 1,
		"list": [{
			"deviceName": "有方软件测试设备",
			"deviceId": "119b7827919d401d8462149ad34ff396",
			"imei": "869060030003827",
			"taskId": 11011,
			"createTime": 1574752564000,
			"deviceStatus": 1,
			"taskState": 1,
			"resultCode": 999,
			"flag": 1,
			"netStatus": 2,
			"onlineAt": 1574926211878,
			"offlineAt": 1574927698725,
			"deviceGroupId": 11
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

### API名称：QuerySoftwareUpgradeDetail   版本号: 20200529233010

#### 描述

查询主任务详情统计

#### 请求信息

请求路径：/detail

请求方法：GET

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|id|QUERY|Long|true||
|productId|QUERY|Long|true||
|MasterKey|HEAD|String|true||


#### 返回信息

##### 返回参数类型
json

##### 返回结果示例
{
  "code": 0,
  "msg": "ok",
  "result": {
    "jobId": 11003,
    "productId": 10013604,
    "tenantId": "300",
    "jobName": "北向测试1111",
    "jobStatus": 2,
    "softwareName": "测试22",
    "softwareId": 7351,
    "fileName": "WaterV1.063000000000_signed.zip",
    "softwareVersion": "1.23",
    "jobDesc": "2万222",
    "takeTime": "24时37分",
    "createTime": "2020-05-14 15:23:36",
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

### API名称：QuerySoftwareUpgradeTaskList   版本号: 20200529232940

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
|MasterKey|HEAD|String|true|MasterKey，产品概况中查看|
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
    "total": 39,
    "list": [
      {
        "jobId": 11003,
        "productId": 10013604,
        "tenantId": "300",
        "jobName": "北向测试1111",
        "jobStatus": 2,
        "softwareVersion": "1.23",
        "fileName": "WaterV1.063000000000_signed.zip",
        "jobDesc": "2万222",
        "takeTime": "23时23分",
        "createTime": "2020-05-14 15:23:36"
      },
      {
        "jobId": 8377,
        "productId": 10013604,
        "tenantId": "300",
        "jobName": "软件测试任务20",
        "jobStatus": 3,
        "softwareVersion": "V1.0",
        "fileName": "package_signed(2).zip",
        "jobDesc": null,
        "takeTime": "0时16分",
        "createTime": "2019-11-28 13:44:08"
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


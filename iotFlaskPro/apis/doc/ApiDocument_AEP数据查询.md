# AEP数据查询
## API列表
|API名称 | 安全认证方式 | 签名认证方式 | 描述 |
|:-------|:------|:--------|:--------|
|QueryDeviceStatus|none|hmac-sha1|终端单个最新状态查询接口|
|QueryDeviceStatusList|none|hmac-sha1|批量获取设备最新状态数据接口|
|getDeviceStatusHisInTotal|none|hmac-sha1|数据总数查询|
|getDeviceStatusHisInPage|none|hmac-sha1|设备状态历史数据分页查询|

## API调用
### 请求地址

|环境 | HTTP请求地址  | HTTPS请求地址 |
|:-------|:------|:--------|
|正式环境|ag-api.ctwing.cn/aep_device_status|ag-api.ctwing.cn/aep_device_status|

### 公共入参

公共请求参数是指每个接口都需要使用到的请求参数。

|参数名称 | 含义  | 位置 | 描述|
|:-------|:------|:--------|:--------|
|application|应用标识|HEAD|应用的App Key，如果需要进行签名认证则需要填写，例如：dAaFG7DiPt8|
|signature|签名数据|HEAD|将业务数据连同timestamp、application一起签名后的数据，如果需要进行签名认证则需要填写|
|timestamp|UNIX格式时间戳|HEAD|如果需要进行签名认证则需要填写，例如：1515752817580|
|version|API版本号|HEAD|可以指定API版本号访问历史版本|

## API 文档说明
### API名称：QueryDeviceStatus   版本号: 20181031202028

#### 描述

终端单个最新状态查询接口

#### 请求信息

请求路径：/deviceStatus

请求方法：POST

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|

#### 请求BODY

##### 数据类型：
json

##### 内容描述：
{"productId":"3238","deviceId":"1da54369fec54dfebce4accc69e9f338",
"datasetId":"temperature"} 其中datasetId为待查询的设备上报消息中某个属性标识,
透传数据datasetId为"APPdata"

#### 返回信息

##### 返回参数类型
json

##### 返回结果示例
{"code":0,"deviceStatus":{"value":"31","timestamp":1522724703130}}

##### 异常返回示例
{"code":1,"desc":"xxxx"}

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

### API名称：QueryDeviceStatusList   版本号: 20181031202403

#### 描述

批量获取设备最新状态数据接口

#### 请求信息

请求路径：/deviceStatusList

请求方法：POST

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|

#### 请求BODY

##### 数据类型：
json

##### 内容描述：
{"productId":"3238","deviceId":"1da54369fec54dfebce4accc69e9f338"}

#### 返回信息

##### 返回参数类型
json

##### 返回结果示例
{
	"code": 0,
	"deviceStatusList": [{
	     " datasetId" : "signalStrength",
		 "value" : "31",
		 "timestamp": 1535697526464
	},
	{
	    " datasetId" : "batteryLevel",
		"value" : "90",
		"timestamp": 1535697526464
	}]
}

##### 异常返回示例
{"code":1,"desc":"data fetch failed."}

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

### API名称：getDeviceStatusHisInTotal   版本号: 20190928013529

#### 描述

数据总数查询

#### 请求信息

请求路径：/api/v1/getDeviceStatusHisInTotal

请求方法：POST

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|

#### 请求BODY

##### 数据类型：
json

##### 内容描述：
{"productId":"10000088","deviceId":"10000088001",
"begin_timestamp":"1538981624878","end_timestamp":"1539575396505"}

#### 返回信息

##### 返回参数类型
json

##### 返回结果示例
{"code":0,"total":3}

##### 异常返回示例
{"code":1,"desc":"failed"}

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

### API名称：getDeviceStatusHisInPage   版本号: 20190928013337

#### 描述

设备状态历史数据分页查询

#### 请求信息

请求路径：/getDeviceStatusHisInPage

请求方法：POST

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|

#### 请求BODY

##### 数据类型：
json

##### 内容描述：
{"productId":"10000088","deviceId":"10000088001","begin_timestamp":"1538981624878",
"end_timestamp":"1539575396505","page_size":5,"page_timestamp":"1539575396505"}
请求中page_timestamp第一页查询时，可传空或end_timestamp，
第二页开始需使用返回值中的page_timestamp。
若返回值中page_timestamp为空，则说明无下一页数据

#### 返回信息

##### 返回参数类型
json

##### 返回结果示例
{"code":0,"page_timestamp":"1538981624878","deviceStatusList":[]}

##### 异常返回示例
{"code":1,"desc":"xxx"}

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


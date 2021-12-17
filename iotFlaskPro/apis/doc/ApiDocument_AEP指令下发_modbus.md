# AEP指令下发_modbus
## API列表
|API名称 | 安全认证方式 | 签名认证方式 | 描述 |
|:-------|:------|:--------|:--------|
|QueryCommandList|none|hmac-sha1|modbus批量查询指令详情|
|QueryCommand|none|hmac-sha1|modbus查询单个指令详情|
|CancelCommand|none|hmac-sha1|modbus取消指令|
|CreateCommand|none|hmac-sha1|modbus指令下发|

## API调用
### 请求地址

|环境 | HTTP请求地址  | HTTPS请求地址 |
|:-------|:------|:--------|
|正式环境|ag-api.ctwing.cn/aep_command_modbus|ag-api.ctwing.cn/aep_command_modbus|

### 公共入参

公共请求参数是指每个接口都需要使用到的请求参数。

|参数名称 | 含义  | 位置 | 描述|
|:-------|:------|:--------|:--------|
|application|应用标识|HEAD|应用的App Key，如果需要进行签名认证则需要填写，例如：dAaFG7DiPt8|
|signature|签名数据|HEAD|将业务数据连同timestamp、application一起签名后的数据，如果需要进行签名认证则需要填写|
|timestamp|UNIX格式时间戳|HEAD|如果需要进行签名认证则需要填写，例如：1515752817580|
|version|API版本号|HEAD|可以指定API版本号访问历史版本|

## API 文档说明
### API名称：QueryCommandList   版本号: 20200904171008

#### 描述

modbus批量查询指令详情

#### 请求信息

请求路径：/modbus/commands

请求方法：GET

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|MasterKey|HEAD|String|true|MasterKey在该设备所属产品的概况中可以查看|
|productId|QUERY|String|true|产品ID，必填|
|deviceId|QUERY|String|true|设备ID，必填|
|status|QUERY|String|false|状态可选填： 1：指令已保存 2：指令已发送 3：指令已送达 4：指令已完成 6：指令已取消 999：指令失败|
|startTime|QUERY|String|false||
|endTime|QUERY|String|false||
|pageNow|QUERY|String|false||
|pageSize|QUERY|String|false||


#### 返回信息

##### 返回参数类型
default

##### 返回结果示例
{
	"code": 0,
	"msg": "ok",
	"result": {
		"pageNum": 1,
		"pageSize": 10,
		"total": 98,
		"list": [{
				"commandId": "191533",
				"command": "{\"int\":1}",
				"commandStatus": "指令已发送",
				"deviceId": "10000271ABC23",
				"imei": null,
				"productId": 10000271,
				"createBy": "aep_test",
				"createTime": 1539565440000,
				"finishTime": null,
				"resultCode": null,
				"resultMessage": null
			},
			{
				"commandId": "191531",
				"command": "{\"int\":2}",
				"commandStatus": "指令发送失败",
				"deviceId": "10000271ABC24",
				"imei": null,
				"productId": 10000271,
				"createBy": "aep_test",
				"createTime": 1539565480000,
				"finishTime": 1539565980000,
				"resultCode": "100234",
				"resultMessage": "The host field of the callbackUrl is in conflict with existing callbackUrl."
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

### API名称：QueryCommand   版本号: 20200904172207

#### 描述

modbus查询单个指令详情

#### 请求信息

请求路径：/modbus/command

请求方法：GET

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|MasterKey|HEAD|String|true|MasterKey在该设备所属产品的概况中可以查看|
|productId|QUERY|Long|true|产品ID|
|deviceId|QUERY|String|true|设备ID|
|commandId|QUERY|String|true|指令ID|


#### 返回信息

##### 返回参数类型
default

##### 返回结果示例
{
  "code": 0,
  "msg": "ok",
  "result": {
    "commandId": "191533",
    "command": "{\"int\":1}",
    "commandStatus": "指令已发送",
    "deviceId": "10000271ABC23",
    "imei": null,
    "productId": 10000271,
    "createBy": "aep_test",	
    "createTime": 1539565440000,
    "finishTime": null,
    "resultCode": null,
    "resultMessage": null
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

### API名称：CancelCommand   版本号: 20200404012453

#### 描述

modbus取消指令

#### 请求信息

请求路径：/modbus/cancelCommand

请求方法：PUT

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|MasterKey|HEAD|String|true|MasterKey在该设备所属产品的概况中可以查看|

#### 请求BODY

##### 数据类型：
json

##### 内容描述：
{
  "commandId": "String",
  "deviceId": "String",
  "productId": 0
}
描述：
   "commandId": 指令ID，String,
   "deviceId": 设备ID，String,
   "productId": 产品Id，Integer

#### 返回信息

##### 返回参数类型
default

##### 返回结果示例
{
  "code": 0,
  "msg": "指令取消成功",
  "result": null
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

### API名称：CreateCommand   版本号: 20200404012449

#### 描述

modbus指令下发

#### 请求信息

请求路径：/modbus/command

请求方法：POST

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|MasterKey|HEAD|String|true|MasterKey在该设备所属产品的概况中可以查看|

#### 请求BODY

##### 数据类型：
json

##### 内容描述：
{
  "productId": 0,
  "deviceId": "12345",
  "platformType": 0,
  "content": "string",
  "modbusCommandReq": {
    "functionPoint": "01",
    "slaveAddr": "01",
    "forceAddr": "1111",
    "forceData": "2222"
  },
  "operator": "yangkun",
  "ttl": 0
}

描述：
productId: 产品ID，必填
deviceId: 设备ID，必填
platformType:下发指令类型，0平台编码，1自编码,必填
content:指令内容，当下发指令类型为1.自编码时必填,其他不填,格式为16进制字符串限制长度2048以内
functionPoint:功能点,当下发指令类型为0.平台编码时必填,其他不填,格式为两位16进制字符串，目前仅支持01至06
slaveAddr:从机地址,当下发指令类型为0.平台编码时必填,其他不填,格式为两位16进制字符串,范围01至F7
forceAddr:起始地址,当下发指令类型为0.平台编码时必填,其他不填,格式为四位16进制字符串
forceData:数据长度,当下发指令类型为0.平台编码时必填,其他不填,格式为四位16进制字符串
operator: 操作者，必填
ttl: 指令在缓存时长，单位：秒，NB网关选填。范围限制0-172800秒范围内,默认2小时。

#### 返回信息

##### 返回参数类型
default

##### 返回结果示例
{
	"code": 0,
	"msg": "ok",
	"result": {
		"commandId": "674",
		"command": "{\"functionPoint\":\"0x01\",\"slaveAddr\":\"0x01\",\"startedAddr\":\"0x1111\",\"dataLength\":\"0x2222\"}",
		"commandStatus": "指令已发送",
		"deviceId": "43c148896dcd43ef97826f3f539484f5",
		"productId": 10000577,
		"createBy": "test",
		"createTime": 1542877423798
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


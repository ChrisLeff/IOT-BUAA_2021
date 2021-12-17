# AEP物模型管理
## API列表
|API名称 | 安全认证方式 | 签名认证方式 | 描述 |
|:-------|:------|:--------|:--------|
|QueryPropertyList|none|hmac-sha1|查询属性列表信息|
|QueryServiceList|none|hmac-sha1|获取服务列表信息|

## API调用
### 请求地址

|环境 | HTTP请求地址  | HTTPS请求地址 |
|:-------|:------|:--------|
|正式环境|ag-api.ctwing.cn/aep_device_model|ag-api.ctwing.cn/aep_device_model|

### 公共入参

公共请求参数是指每个接口都需要使用到的请求参数。

|参数名称 | 含义  | 位置 | 描述|
|:-------|:------|:--------|:--------|
|application|应用标识|HEAD|应用的App Key，如果需要进行签名认证则需要填写，例如：dAaFG7DiPt8|
|signature|签名数据|HEAD|将业务数据连同timestamp、application一起签名后的数据，如果需要进行签名认证则需要填写|
|timestamp|UNIX格式时间戳|HEAD|如果需要进行签名认证则需要填写，例如：1515752817580|
|version|API版本号|HEAD|可以指定API版本号访问历史版本|

## API 文档说明
### API名称：QueryPropertyList   版本号: 20190712223330

#### 描述

查询属性列表信息

#### 请求信息

请求路径：/dm/app/model/properties

请求方法：GET

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|MasterKey|HEAD|String|true|MasterKey在该设备所属产品的概况中可以查看|
|productId|QUERY|Long|true||
|searchValue|QUERY|String|false|可填值：属性名称，属性标识符|
|pageNow|QUERY|Long|false|当前页数|
|pageSize|QUERY|Long|false|每页记录数|


#### 返回信息

##### 返回参数类型
json

##### 返回结果示例
{
	"code": 0,
	"msg": "ok",
	"result": {
		"pageNum": 1,
		"pageSize": 1,
		"total": 1,
		"list": [{
			"propertyId": 1,
			"propertyFlag": "asdggg",
			"propertyName": "属性1",
			"dataType": "fix-string",
			"unit": "g",
			"len": 1,
			"unitName": "克每毫升",
			"description": ""
		}, {
			"propertyId": 2,
			"propertyFlag": "a1",
			"propertyName": "a1",
			"dataType": "enum",
			"enumDetail": {
				"1": "2",
				"3": "4",
				"5": "6"
			},
			"len": 1,
			"description": "test"
		}, {
			"propertyId": 3,
			"propertyFlag": "a2",
			"propertyName": "a2",
			"dataType": "float",
			"unit": "ppm",
			"min": "1",
			"len": 4,
			"unitName": "百万分率",
			"max": "2",
			"step": "1",
			"description": "1"
		}, {
			"propertyId": 4,
			"propertyFlag": "a3",
			"propertyName": "a3",
			"dataType": "bool",
			"boolDetail": {
				"false": "关",
				"true": "开"
			},
			"len": 1,
			"description": "test"
		}]
	}
}

##### 异常返回示例
{
 "code":8800,
 "msg":"内部错误，请联系管理员",
 "result":null
}

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

### API名称：QueryServiceList   版本号: 20190712224233

#### 描述

获取服务列表信息

#### 请求信息

请求路径：/dm/app/model/services

请求方法：GET

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|MasterKey|HEAD|String|true|MasterKey在该设备所属产品的概况中可以查看|
|productId|QUERY|Long|true||
|searchValue|QUERY|String|false|可填： 服务Id, 服务名称,服务标识符|
|serviceType|QUERY|Long|false|服务类型\n1. 数据上报 \n2. 事件上报 \n3.数据获取 \n4.参数查询 \n5.参数配置\n6.指令下发 \n7.指令下发响应|
|pageNow|QUERY|Long|false|当前页数|
|pageSize|QUERY|Long|false|每页记录数|


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
			"serviceId": 1,
			"serviceFlag": "asdg",
			"serviceName": "阿萨德刚",
			"serviceType": 2,
			"eventType": 1,
			"description": "",
			"properties": [{
				"propertyId": 1,
				"propertyFlag": "asdggg",
				"propertyName": "属性1",
				"dataType": "fix-string",
				"unit": "g",
				"len": 1,
				"unitName": "克每毫升",
				"description": ""
			}, {
				"propertyId": 2,
				"propertyFlag": "a1",
				"propertyName": "a1",
				"dataType": "enum",
				"enumDetail": {
					"1": "2",
					"3": "4",
					"5": "6"
				},
				"len": 1,
				"description": "test"
			}, {
				"propertyId": 4,
				"propertyFlag": "a3",
				"propertyName": "a3",
				"dataType": "bool",
				"boolDetail": {
					"false": "关",
					"true": "开"
				},
				"len": 1,
				"description": "test"
			}],
			"parameters": [{
				"parameterId": 17,
				"parameterFlag": "cellId",
				"parameterName": "cellId",
				"dataType": "integer",
				"unit": "null",
				"min": -2147483648,
				"len": 4,
				"unitName": "",
				"max": 2147483647,
				"description": ""
			}]
		}]
	}
}

##### 异常返回示例
{"code":8800,"msg":"内部错误，请联系管理员","result":null}

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


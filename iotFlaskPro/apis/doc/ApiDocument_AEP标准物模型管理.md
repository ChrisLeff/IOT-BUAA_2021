# AEP标准物模型管理
## API列表
|API名称 | 安全认证方式 | 签名认证方式 | 描述 |
|:-------|:------|:--------|:--------|
|QueryStandardModel|none|hmac-sha1|标准物模型查询|

## API调用
### 请求地址

|环境 | HTTP请求地址  | HTTPS请求地址 |
|:-------|:------|:--------|
|正式环境|ag-api.ctwing.cn/aep_standard_management|ag-api.ctwing.cn/aep_standard_management|

### 公共入参

公共请求参数是指每个接口都需要使用到的请求参数。

|参数名称 | 含义  | 位置 | 描述|
|:-------|:------|:--------|:--------|
|application|应用标识|HEAD|应用的App Key，如果需要进行签名认证则需要填写，例如：dAaFG7DiPt8|
|signature|签名数据|HEAD|将业务数据连同timestamp、application一起签名后的数据，如果需要进行签名认证则需要填写|
|timestamp|UNIX格式时间戳|HEAD|如果需要进行签名认证则需要填写，例如：1515752817580|
|version|API版本号|HEAD|可以指定API版本号访问历史版本|

## API 文档说明
### API名称：QueryStandardModel   版本号: 20190713033424

#### 描述

标准物模型查询

#### 请求信息

请求路径：/standardModel

请求方法：GET

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|standardVersion|QUERY|String|false|标准物模型版本号|
|thirdType|QUERY|Long|true|三级分类Id|


#### 返回信息

##### 返回参数类型
json

##### 返回结果示例
{
	"code": 0,
	"msg": "ok",
	"result": {
		"properties": [{
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
			},
			{
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
			}
		],
		"services": [{
			"serviceId": 8001,
			"serviceFlag": "a3",
			"serviceName": "a3",
			"serviceType": 2,
			"eventType": 1,
			"description": "a",
			"properties": [{
				"propertyFlag": "a2",
				"serial": 2
			}],
			"parameters": [{
				"parameterFlag": "c1",
				"parameterName": "c1",
				"dataType": "Int32",
				"unit": "g",
				"min": "1",
				"len": 4,
				"unitName": "克每毫升",
				"max": "2",
				"step": "1",
				"description": "1",
				"serial": 1
			}]
		}]
	}
}

##### 异常返回示例
{
  "code": 2304,
  "msg": "查看标准物模型失败",
  "result": null
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


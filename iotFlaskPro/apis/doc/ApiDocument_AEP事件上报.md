# AEP事件上报
## API列表
|API名称 | 安全认证方式 | 签名认证方式 | 描述 |
|:-------|:------|:--------|:--------|
|QueryDeviceEventList|none|hmac-sha1|查询事件上报列表|
|QueryDeviceEventTotal|none|hmac-sha1|查询事件上报总数|

## API调用
### 请求地址

|环境 | HTTP请求地址  | HTTPS请求地址 |
|:-------|:------|:--------|
|正式环境|ag-api.ctwing.cn/aep_device_event|ag-api.ctwing.cn/aep_device_event|

### 公共入参

公共请求参数是指每个接口都需要使用到的请求参数。

|参数名称 | 含义  | 位置 | 描述|
|:-------|:------|:--------|:--------|
|application|应用标识|HEAD|应用的App Key，如果需要进行签名认证则需要填写，例如：dAaFG7DiPt8|
|signature|签名数据|HEAD|将业务数据连同timestamp、application一起签名后的数据，如果需要进行签名认证则需要填写|
|timestamp|UNIX格式时间戳|HEAD|如果需要进行签名认证则需要填写，例如：1515752817580|
|version|API版本号|HEAD|可以指定API版本号访问历史版本|

## API 文档说明
### API名称：QueryDeviceEventList   版本号: 20210327064751

#### 描述

查询事件上报列表

#### 请求信息

请求路径：/device/events

请求方法：POST

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|MasterKey|HEAD|String|true||

#### 请求BODY

##### 数据类型：
json

##### 内容描述：
{
"productId":"10000088",//必填
"deviceId":"10000088001",//必填
"eventType":1,//非必填
"startTime":"1538981624878",//必填
"endTime":"1539575396505",//必填
"pageSize":10,//必填
"pageTimestamp":"1539575396505"//非必填
}
//eventType:（int）LWM2M,MQTT,TUP协议可选填: 1：信息 2：警告 3：故障 T-link协议可选填: 1：告警事件(普通级) 2：告警事件(重大级) 3：告警事件(严重级)；匹配所有事件类型可不填写该参数。
//pageTimestamp:可传空或者等于endTime，表示倒序查询的下一页起始时间，每次查询返回pageTimestamp，表示下一页第一条数据的上报时间，为空则代表没有下一页数据。下次查询带上pageTimestamp参数，即查询startTime - pageTimestamp之间的数据，可实现分页查询。
//startTime与endTime之间的时间差最大为31天

#### 返回信息

##### 返回参数类型
json

##### 返回结果示例
{
	"code": 0,
	"msg": "ok",
	"result": {
		"pageSize": 10,
		"pageTimestamp": "",
		"list": [{
			"deviceSn": "",
			"imei": "861639682615400",
			"eventType": 0,
			"eventContent": "4007",
			"createTime": 1616396826154,
			"deviceId": "g601a829f0dc497bba19e9eaf98d4433"}]
	}
}

##### 异常返回示例
{
    "code": -1,
    "msg": "error",
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

### API名称：QueryDeviceEventTotal   版本号: 20210327064755

#### 描述

查询事件上报总数

#### 请求信息

请求路径：/device/events/total

请求方法：POST

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|MasterKey|HEAD|String|true||

#### 请求BODY

##### 数据类型：
json

##### 内容描述：
{
"productId":"10000088",//必填
"deviceId":"10000088001",//必填
"eventType":1,//非必填
"startTime":"1538981624878",//必填
"endTime":"1539575396505"//必填
}
//eventType:（int）LWM2M,MQTT,TUP协议可选填: 1：信息 2：警告 3：故障 T-link协议可选填: 1：告警事件(普通级) 2：告警事件(重大级) 3：告警事件(严重级)；匹配所有事件类型可不填写该参数。
//startTime与endTime之间最大的时间差为31天

#### 返回信息

##### 返回参数类型
json

##### 返回结果示例
{
    "code": 0,
    "msg": "ok",
    "result": 51
}

##### 异常返回示例
{
    "code": -1,
    "msg": "error",
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


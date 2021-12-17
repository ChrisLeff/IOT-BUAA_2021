# AEP指令下发
## API列表
|API名称 | 安全认证方式 | 签名认证方式 | 描述 |
|:-------|:------|:--------|:--------|
|CreateCommand|none|hmac-sha1|统一合并指令下发|
|QueryCommandList|none|hmac-sha1|批量查询指令详情|
|QueryCommand|none|hmac-sha1|查询单个指令详情|
|CancelCommand|none|hmac-sha1|取消指令|

## API调用
### 请求地址

|环境 | HTTP请求地址  | HTTPS请求地址 |
|:-------|:------|:--------|
|正式环境|ag-api.ctwing.cn/aep_device_command|ag-api.ctwing.cn/aep_device_command|

### 公共入参

公共请求参数是指每个接口都需要使用到的请求参数。

|参数名称 | 含义  | 位置 | 描述|
|:-------|:------|:--------|:--------|
|application|应用标识|HEAD|应用的App Key，如果需要进行签名认证则需要填写，例如：dAaFG7DiPt8|
|signature|签名数据|HEAD|将业务数据连同timestamp、application一起签名后的数据，如果需要进行签名认证则需要填写|
|timestamp|UNIX格式时间戳|HEAD|如果需要进行签名认证则需要填写，例如：1515752817580|
|version|API版本号|HEAD|可以指定API版本号访问历史版本|

## API 文档说明
### API名称：CreateCommand   版本号: 20190712225145

#### 描述

统一合并指令下发

#### 请求信息

请求路径：/command

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
  "content": {},
  "deviceId": "string",
  "operator": "string",
  "productId": 0,
  "ttl": 7200,
  "deviceGroupId": 100,
  "level": 1
}

deviceId: 设备ID，（当指令级别为设备级时必填，为设备组级时则不填）
operator: 操作者，必填
productId: 产品ID，必填
ttl: 设备指令缓存时长，选填。单位：秒，取值范围：0-864000。
     不携带则默认值：7200。如不需缓存请填0。
level:指令级别，1或2为设备级别,3为设备组级别，选填。不填默认设备级。
deviceGroupId：设备组ID，选填，当指令级别为设备级，
               deviceId不为空，deviceGroupId为空；
               当指令级别为设备组级，deviceId为空，deviceGroupId不为空。
content: 指令内容，必填，格式为Json。

content填写样例：
	 MQTT协议透传的content内容：
	     {
	      payload:指令内容 格式为Json传Json格式内容
	     }
	     样例：
		{
	          "payload": {
			"status": 1,
		        "temperature": 26
			}
		}	
	 TCP和LWM2M协议透传的content内容：
	     {
	      payload:指令内容,数据格式为十六进制时需要填十六进制字符串,
	      dataType:数据类型：1字符串，2十六进制
	     }
	     样例：
		{
		  "dataType":1,
	          "payload": "5365ab32d"
		}	
	 MQTT、LWM2M协议非透传和T-Link协议的content内容	
		{
		 params：指令参数
		 serviceIdentifier：服务定义时的服务标识
		}
		 样例：
		   {
		     "params": 
			    {
			 "status": 1,
			 "temperature": 26
			    },
		    "serviceIdentifier": "eeeeee"
		   }
	 JT/T808协议的content内容
	{
		jtMessageId:消息Id ,
		jtMessageType: 消息类型,
		dataType:数据类型：1字符串，2十六进制 ,
		payload:指令内容,数据格式为十六进制时需要填十六进制字符串 
	}
	注：jtMessageId字段为0x8900时，jtMessageType字段必填
            jtMessageType字段：
               0x00,GNSS模块详细定位数据;
               0x0B,道路运输证IC卡信息;
               0x41,串口1透传;
               0x42,串口2透传;
               0xF0-0xFF,用户自定义透传;
	样例：
	 {
		"jtMessageId": "0x8900",
		"jtMessageType": "0x00",
		"dataType": 1,
		"payload": "112233"
	}
        南向云的content内容：
       {
        payload:指令内容 格式为Json传Json格式内容
        }
       样例：
        {
           "payload": {
               "status": 1,
               "temperature": 26
            }
        }

#### 返回信息

##### 返回参数类型
json

##### 返回结果示例
{
  "code": 0,
  "msg": "ok",
  "result": {
    "commandId": "674",
    "command": "{\"double\":3}",
    "commandStatus": "指令已保存",
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

### API名称：QueryCommandList   版本号: 20200814163736

#### 描述

批量查询指令详情

#### 请求信息

请求路径：/commands

请求方法：GET

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|MasterKey|HEAD|String|true|MasterKey在该设备所属产品的概况中可以查看|
|productId|QUERY|Long|true|产品ID，必填|
|deviceId|QUERY|String|true|设备ID，必填|
|startTime|QUERY|String|false|日期格式，年月日时分秒，例如：20200801120130|
|endTime|QUERY|String|false|日期格式，年月日时分秒，例如：20200801120130|
|pageNow|QUERY|Long|false|当前页数|
|pageSize|QUERY|Long|false|每页记录数，最大40|


#### 返回信息

##### 返回参数类型
json

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

### API名称：QueryCommand   版本号: 20190712225241

#### 描述

查询单个指令详情

#### 请求信息

请求路径：/command

请求方法：GET

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|MasterKey|HEAD|String|true|MasterKey在该设备所属产品的概况中可以查看|
|commandId|QUERY|String|true|创建指令成功响应中返回的id，|
|productId|QUERY|Long|true||
|deviceId|QUERY|String|true|设备ID|


#### 返回信息

##### 返回参数类型
json

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

### API名称：CancelCommand   版本号: 20190615023142

#### 描述

取消指令

#### 请求信息

请求路径：/cancelCommand

请求方法：PUT

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|MasterKey|HEAD|String|true||

#### 请求BODY

##### 数据类型：
json

##### 内容描述：
{
  "commandId": "a5c71cfcc5074a2f846e26f2988b57b4",
  "deviceId": "c0cda6dd6c52446ba1a0d2a5d26d231a",
  "productId": 10004101
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
{
  "code": -1,
  "msg": "指令取消失败，服务端响应错误",
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


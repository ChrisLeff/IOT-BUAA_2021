# AEPNB设备管理
## API列表
|API名称 | 安全认证方式 | 签名认证方式 | 描述 |
|:-------|:------|:--------|:--------|
|BatchCreateNBDevice|none|hmac-sha1|批量增加NB设备|
|BatchCancelDevices|none|hmac-sha1|批量注销设备|

## API调用
### 请求地址

|环境 | HTTP请求地址  | HTTPS请求地址 |
|:-------|:------|:--------|
|正式环境|ag-api.ctwing.cn/aep_nb_device_management|ag-api.ctwing.cn/aep_nb_device_management|

### 公共入参

公共请求参数是指每个接口都需要使用到的请求参数。

|参数名称 | 含义  | 位置 | 描述|
|:-------|:------|:--------|:--------|
|application|应用标识|HEAD|应用的App Key，如果需要进行签名认证则需要填写，例如：dAaFG7DiPt8|
|signature|签名数据|HEAD|将业务数据连同timestamp、application一起签名后的数据，如果需要进行签名认证则需要填写|
|timestamp|UNIX格式时间戳|HEAD|如果需要进行签名认证则需要填写，例如：1515752817580|
|version|API版本号|HEAD|可以指定API版本号访问历史版本|

## API 文档说明
### API名称：BatchCreateNBDevice   版本号: 20200828140355

#### 描述

批量增加NB设备

#### 请求信息

请求路径：/batchNBDevice

请求方法：POST

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|

#### 请求BODY

##### 数据类型：
json

##### 内容描述：
{
	"productId": 0,   
	"operator": "admin",  
	"devices": [{
			"imei": "123456789012345",  
			"deviceName": "deviceName1", 
			"autoObserver": 0,  
			"imsi": "12545154878451",   
			"pskValue": "ADvNWlkcNq9AfKnk" ,  
			"pskType": 0 

		},
		{
			"imei": "123456789012345",
			"deviceName": "deviceName2",
			"autoObserver": 0,
			"imsi": "12545154878451",
			"pskValue": "ADvNWlkcNq9AfKnk",
			"pskType": 0  

		}
	]
}
描述：
productId: 产品ID，必填
operator: 操作者，必填
devices: 
      imei: imei号，必填；
      deviceName: 设备名称，必填;      	  
      autoObserver:0.自动订阅 1.取消自动订阅，选填;
      imsi:总长度不超过15位，使用0~9的数字，String类型,选填;
      pskValue:由大小写字母加0-9数字组成的16位字符串,选填;
      pskType:取值0或者1,0代表普通字符串，1代表16进制字符串,选填;
注意：最多一次可以添加100个设备。

#### 返回信息

##### 返回参数类型
json

##### 返回结果示例
{
    "code": 0,
    "msg": "ok",
    "result": [
        {
            "description": "IMEI号已存在",
            "imei": "113456789012349",
            "resultCode": 2010115
        },
        {
            "deviceId": "1d303b69cf7345c998380d577bda323e",
            "imei": "113456789013349",
            "resultCode": 0
        }
    ]
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

### API名称：BatchCancelDevices   版本号: 20211009093738

#### 描述

批量注销设备

#### 请求信息

请求路径：/cancelledDevices

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
  "deviceIdList": [
    "deviceId1","deviceId2","deviceId3"
  ],
  "productId": 12345678
}

#### 返回信息

##### 返回参数类型
default

##### 返回结果示例
{
  "code": 0,
  "msg": "ok",
  "result": {}
}

##### 异常返回示例
{
  "code": 0,
  "msg": "ok",
  "result": {
    "errorList": [
      {
        "deviceId": "821053af60fe4014bf1275ec9s43e8b9a",
        "errorCode": 1104,
        "errorMsg": "此设备不存在"
      }
    ]
  }
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


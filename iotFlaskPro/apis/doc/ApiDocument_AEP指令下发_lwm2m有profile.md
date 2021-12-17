# AEP指令下发_lwm2m有profile
## API列表
|API名称 | 安全认证方式 | 签名认证方式 | 描述 |
|:-------|:------|:--------|:--------|
|CreateCommandLwm2mProfile|none|hmac-sha1|lwm2m协议有profile指令下发接口|

## API调用
### 请求地址

|环境 | HTTP请求地址  | HTTPS请求地址 |
|:-------|:------|:--------|
|正式环境|ag-api.ctwing.cn/aep_device_command_lwm_profile|ag-api.ctwing.cn/aep_device_command_lwm_profile|

### 公共入参

公共请求参数是指每个接口都需要使用到的请求参数。

|参数名称 | 含义  | 位置 | 描述|
|:-------|:------|:--------|:--------|
|application|应用标识|HEAD|应用的App Key，如果需要进行签名认证则需要填写，例如：dAaFG7DiPt8|
|signature|签名数据|HEAD|将业务数据连同timestamp、application一起签名后的数据，如果需要进行签名认证则需要填写|
|timestamp|UNIX格式时间戳|HEAD|如果需要进行签名认证则需要填写，例如：1515752817580|
|version|API版本号|HEAD|可以指定API版本号访问历史版本|

## API 文档说明
### API名称：CreateCommandLwm2mProfile   版本号: 20191231141545

#### 描述

lwm2m协议有profile指令下发接口

#### 请求信息

请求路径：/commandLwm2mProfile

请求方法：POST

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|MasterKey|HEAD|String|false|MasterKey在该设备所属产品的概况中可以查看|

#### 请求BODY

##### 数据类型：
json

##### 内容描述：
{
	"command": {
                "serviceId": "Command",
		"method": "QueryDeviceData",
		"paras": {
			"a": 1
		}
	},
	"deviceId": "string",
	"operator": "string",
	"productId": 0,
	"ttl": 0,
	"deviceGroupId": 100,
	"level": 1
}

描述：
command: 指令内容，必填，格式为Json，参数如下：
         {
	  serviceId:命令对应的服务ID,
	  method:命令服务下具体的命令名称
          paras:指令参数，格式为json,  
         }

deviceId: 设备ID，选填
operator: 操作者，必填
productId: 产品ID，必填
ttl: 消息超时时长，单位：秒。范围限制0-864000秒范围内。
level:指令级别，1或2为设备级别,3为设备组级别，选填。不填默认设备级。
deviceGroupId：设备组ID，选填，当指令级别为设备级，deviceId不为空，deviceGroupId为空；
               当指令级别为设备组级，deviceId为空，deviceGroupId不为空。

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


# AEP边缘网关接入
## API列表
|API名称 | 安全认证方式 | 签名认证方式 | 描述 |
|:-------|:------|:--------|:--------|
|DeleteEdgeInstanceDevice|none|hmac-sha1|删除边缘实例子设备|
|QueryEdgeInstanceDevice|none|hmac-sha1|查询边缘实例子设备列表|
|CreateEdgeInstance|none|hmac-sha1|创建边缘实例|
|EdgeInstanceDeploy|none|hmac-sha1|边缘实例部署|
|DeleteEdgeInstance|none|hmac-sha1|删除边缘实例|
|AddEdgeInstanceDevice|none|hmac-sha1|边缘实例添加子设备|
|AddEdgeInstanceDrive|none|hmac-sha1|分配驱动|

## API调用
### 请求地址

|环境 | HTTP请求地址  | HTTPS请求地址 |
|:-------|:------|:--------|
|正式环境|ag-api.ctwing.cn/aep_edge_gateway|ag-api.ctwing.cn/aep_edge_gateway|

### 公共入参

公共请求参数是指每个接口都需要使用到的请求参数。

|参数名称 | 含义  | 位置 | 描述|
|:-------|:------|:--------|:--------|
|application|应用标识|HEAD|应用的App Key，如果需要进行签名认证则需要填写，例如：dAaFG7DiPt8|
|signature|签名数据|HEAD|将业务数据连同timestamp、application一起签名后的数据，如果需要进行签名认证则需要填写|
|timestamp|UNIX格式时间戳|HEAD|如果需要进行签名认证则需要填写，例如：1515752817580|
|version|API版本号|HEAD|可以指定API版本号访问历史版本|

## API 文档说明
### API名称：DeleteEdgeInstanceDevice   版本号: 20201226000026

#### 描述

删除边缘实例子设备

#### 请求信息

请求路径：/instance/devices

请求方法：POST

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|

#### 请求BODY

##### 数据类型：
json

##### 内容描述：
{
  "edgeDeviceInfos": [
    {
      "deviceId": "string"
    }
  ],
  "gatewayDeviceId": "string"
}

描述：
gatewayDeviceId：网关设备ID，必填
deviceId：子设备ID，必填

#### 返回信息

##### 返回参数类型
json

##### 返回结果示例
{
  "code": 0,
  "msg": "ok",
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

### API名称：QueryEdgeInstanceDevice   版本号: 20201226000022

#### 描述

查询边缘实例子设备列表

#### 请求信息

请求路径：/instance/devices

请求方法：GET

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|gatewayDeviceId|QUERY|String|true||
|pageNow|QUERY|Long|false||
|pageSize|QUERY|Long|false||


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
		"total": 1,
		"list": [{
			"deviceId": "test",//String,子设备ID
			"deviceSn": "test",//String,子设备编号
			"deviceName": "test",//String,子设备名称
			"productId": 10000000,//Integer,子设备产品ID
			"productName": "test",//String,子设备产品名称
			"productProtocol": 8,//Integer,子设备产品协议
			"tupIsThrough": 1,//Integer,子设备所属产品是否透传
			"tupIsProfile": 1,//Integer,子设备所属产品是否有Profile
			"deviceStatus": 1,//Integer,设备状态
			"firmwareVersion": "",//String,固件版本
			"createTime": 1605094547000,//Long,创建时间
			"netStatus": 2,//Integer,在线状态
			"onlineAt": 1608103857000,//Long,最后上线时间
			"offlineAt": 1608103892000,//Long,最后下线时间
			"driveName": ""//String,驱动名称
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

### API名称：CreateEdgeInstance   版本号: 20201226000017

#### 描述

创建边缘实例

#### 请求信息

请求路径：/instance

请求方法：POST

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|

#### 请求BODY

##### 数据类型：
json

##### 内容描述：
{
  "edgeName": "string",
  "gatewayDeviceId": "string",
  "gatewayProductId": 0,
  "operator": "string"
}

描述：
edgeName：边缘实例名称，必填
gatewayDeviceId：网关设备ID，必填
gatewayProductId：网关产品ID，必填
operator：操作者，必填

#### 返回信息

##### 返回参数类型
json

##### 返回结果示例
{
	"code": 0,
	"msg": "ok",
	"result": {
		"edgeId": 1051,//边缘实例ID
		"edgeName": "test",//边缘实例名称
		"gatewayProductId": 20002551,//网关产品名称
		"gatewayDeviceId": "20002551001"//网关设备ID
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

### API名称：EdgeInstanceDeploy   版本号: 20201226000010

#### 描述

边缘实例部署

#### 请求信息

请求路径：/instance/settings

请求方法：POST

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|

#### 请求BODY

##### 数据类型：
json

##### 内容描述：
{
  "edgeId": 0
}

描述：
edgeId：边缘实例ID，必填

#### 返回信息

##### 返回参数类型
json

##### 返回结果示例
{
  "code": 0,
  "msg": "ok",
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

### API名称：DeleteEdgeInstance   版本号: 20201225235957

#### 描述

删除边缘实例

#### 请求信息

请求路径：/instance

请求方法：DELETE

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|id|QUERY|Long|true||


#### 返回信息

##### 返回参数类型
json

##### 返回结果示例
{
  "code": 0,
  "msg": "ok",
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

### API名称：AddEdgeInstanceDevice   版本号: 20201226000004

#### 描述

边缘实例添加子设备

#### 请求信息

请求路径：/instance/device

请求方法：POST

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|

#### 请求BODY

##### 数据类型：
json

##### 内容描述：
{
  "devices": [
    {
      "deviceId": "string",
      "productId": 0
    }
  ],
  "gatewayDeviceId": "string"
}

描述：
deviceId：子设备ID，必填
productId：子设备产品ID，必填
gatewayDeviceId：网关设备ID，必填

#### 返回信息

##### 返回参数类型
json

##### 返回结果示例
{
  "code": 0,
  "msg": "ok",
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

### API名称：AddEdgeInstanceDrive   版本号: 20201225235952

#### 描述

分配驱动

#### 请求信息

请求路径：/instance/drive

请求方法：POST

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|

#### 请求BODY

##### 数据类型：
json

##### 内容描述：
{
  "drives": [
    {
      "driveId": 0,
      "port": 0,
      "productId": 0
    }
  ],
  "edgeId": 0
}
描述：
driveId：驱动ID
port：端口
productId：子设备所属产品Id，必填
edgeId：边缘实例ID，必填

#### 返回信息

##### 返回参数类型
json

##### 返回结果示例
{
  "code": 0,
  "msg": "ok",
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


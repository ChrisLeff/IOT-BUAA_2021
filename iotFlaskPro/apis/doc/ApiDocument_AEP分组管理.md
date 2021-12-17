# AEP分组管理
## API列表
|API名称 | 安全认证方式 | 签名认证方式 | 描述 |
|:-------|:------|:--------|:--------|
|CreateDeviceGroup|none|hmac-sha1|新增分组(单产品)|
|UpdateDeviceGroup|none|hmac-sha1|编辑分组信息(单产品)|
|DeleteDeviceGroup|none|hmac-sha1|删除分组(单产品)|
|QueryDeviceGroupList|none|hmac-sha1|查询分组列表信息(单产品)|
|QueryGroupDeviceList|none|hmac-sha1|查询分组下已关联或未关联的设备列表(单产品)|
|UpdateDeviceGroupRelation|none|hmac-sha1|编辑分组与设备关联关系(单产品)|
|getGroupDetailByDeviceId|none|hmac-sha1|查询设备所属分组信息|

## API调用
### 请求地址

|环境 | HTTP请求地址  | HTTPS请求地址 |
|:-------|:------|:--------|
|正式环境|ag-api.ctwing.cn/aep_device_group_management|ag-api.ctwing.cn/aep_device_group_management|

### 公共入参

公共请求参数是指每个接口都需要使用到的请求参数。

|参数名称 | 含义  | 位置 | 描述|
|:-------|:------|:--------|:--------|
|application|应用标识|HEAD|应用的App Key，如果需要进行签名认证则需要填写，例如：dAaFG7DiPt8|
|signature|签名数据|HEAD|将业务数据连同timestamp、application一起签名后的数据，如果需要进行签名认证则需要填写|
|timestamp|UNIX格式时间戳|HEAD|如果需要进行签名认证则需要填写，例如：1515752817580|
|version|API版本号|HEAD|可以指定API版本号访问历史版本|

## API 文档说明
### API名称：CreateDeviceGroup   版本号: 20190615001622

#### 描述

新增分组(单产品)

#### 请求信息

请求路径：/deviceGroup

请求方法：POST

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|MasterKey|HEAD|String|false||

#### 请求BODY

##### 数据类型：
json

##### 内容描述：
{
  "description": "groupDesc",
  "deviceGroupName": "groupName",
  "productId": 10006031
}
描述：
   "description": 分组描述，String,
   "deviceGroupName": 分组名称(只支持英文和数字)，String,
   "productId": 产品Id，Integer

#### 返回信息

##### 返回参数类型
json

##### 返回结果示例
{
  "code": 0,
  "msg": "ok",
  "result": {
    "deviceGroupId": 790,
    "tenantId": "300",
    "productId": 10000587,
    "deviceGroupName": "string",
    "description": "string"
  }
}

##### 异常返回示例
{
  "code": 2101,
  "msg": "创建群组失败",
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

### API名称：UpdateDeviceGroup   版本号: 20190615001615

#### 描述

编辑分组信息(单产品)

#### 请求信息

请求路径：/deviceGroup

请求方法：PUT

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|MasterKey|HEAD|String|false||

#### 请求BODY

##### 数据类型：
json

##### 内容描述：
{
  "description": "groupDesc",
  "deviceGroupId": 196,
  "deviceGroupName": "groupName",
  "productId": 10006031
}
描述：
   "description": 分组描述，String,
   "deviceGroupId": 分组Id，Integer,
   "deviceGroupName": 分组名称(只支持英文和数字)，String,
   "productId": 产品Id，Integer

#### 返回信息

##### 返回参数类型
default

##### 返回结果示例
{
  "code": 0,
  "msg": "ok",
  "result": null
}

##### 异常返回示例
{
  "code": 2102,
  "msg": "编辑群组失败",
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

### API名称：DeleteDeviceGroup   版本号: 20190615001601

#### 描述

删除分组(单产品)

#### 请求信息

请求路径：/deviceGroup

请求方法：DELETE

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|productId|QUERY|Long|true|产品Id|
|deviceGroupId|QUERY|Long|true|分组Id|
|MasterKey|HEAD|String|false||


#### 返回信息

##### 返回参数类型
default

##### 返回结果示例
{
  "code": 0,
  "msg": "ok",
  "result": null
}

##### 异常返回示例
{
  "code": 2104,
  "msg": "删除群组失败",
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

### API名称：QueryDeviceGroupList   版本号: 20190615001555

#### 描述

查询分组列表信息(单产品)

#### 请求信息

请求路径：/deviceGroups

请求方法：GET

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|productId|QUERY|Long|true||
|searchValue|QUERY|String|false|分组名称，分组ID|
|pageNow|QUERY|Long|true|当前页数|
|pageSize|QUERY|Long|true|每页记录数|
|MasterKey|HEAD|String|false||


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
    "total": 2,
    "list": [
      {
        "deviceGroupId": 196,
        "tenantId": "10007903",
        "productId": 10006031,
        "deviceGroupName": "estedsdf",
        "deviceCount": 0,
        "activeCount": 0,
        "description": "strfewfewing",
        "createTime": 1558423978000,
        "updateTime": 1558424035000
      },
      {
        "deviceGroupId": 193,
        "tenantId": "10007903",
        "productId": 10006031,
        "deviceGroupName": "fe",
        "deviceCount": 1,
        "activeCount": 1,
        "description": "",
        "createTime": 1558421733000,
        "updateTime": 1558421733000
      }
    ]
  }
}

##### 异常返回示例
{
  "code": 0,
  "msg": "ok",
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

### API名称：QueryGroupDeviceList   版本号: 20190615001540

#### 描述

查询分组下已关联或未关联的设备列表(单产品)

#### 请求信息

请求路径：/groupDeviceList

请求方法：GET

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|MasterKey|HEAD|String|false||
|productId|QUERY|Long|true||
|searchValue|QUERY|String|false|可查询：设备ID，设备名称，设备编号或者IMEI号|
|pageNow|QUERY|Long|true|当前页数|
|pageSize|QUERY|Long|true|每页条数|
|deviceGroupId|QUERY|Long|false|群组ID：1.有值则查询该群组已关联的设备信息列表。2.为空则查询该产品下未关联的设备信息列表|


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
    "list": [
      {
        "deviceName": "fe",
        "deviceId": "6d9ff188a6394e63b3760e76188e175a",
        "imei": "",
        "deviceSn": "",
        "deviceStatus": 1
      }
    ]
  }
}

##### 异常返回示例
{
  "code": 0,
  "msg": "ok",
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

### API名称：UpdateDeviceGroupRelation   版本号: 20190615001526

#### 描述

编辑分组与设备关联关系(单产品)

#### 请求信息

请求路径：/deviceGroupRelation

请求方法：PUT

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|MasterKey|HEAD|String|false||

#### 请求BODY

##### 数据类型：
json

##### 内容描述：
{
  "deviceGroupId": 196,
  "deviceList": [
    "6d9ff188a6394e63b3760e76188e175a"
  ],
  "flag": 0,
  "productId": 10006031
}
 描述：
   deviceGroupId:分组ID，Integer,
   deviceList:设备ID列表，List<String>,
   flag:关联操作标识:0：关联，1：去除关联, Integer,
   productId:产品Id ,Integer

#### 返回信息

##### 返回参数类型
default

##### 返回结果示例
{
  "code": 0,
  "msg": "ok",
  "result": null
}

##### 异常返回示例
{
  "code": 2106,
  "msg": "编辑群组关联失败",
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

### API名称：getGroupDetailByDeviceId   版本号: 20211014095939

#### 描述

查询设备所属分组信息

#### 请求信息

请求路径：/groupOfDeviceId

请求方法：GET

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|productId|QUERY|Long|true||
|deviceId|QUERY|String|true||


#### 返回信息

##### 返回参数类型
json

##### 返回结果示例
{
	"code": 0,
	"msg": "ok",
	"result": {
		"deviceGroupId": 15629,   //组ID
		"productId": 15067073,   //跨产品分组返回null
		"deviceGroupName": "组名称",
		"description": "",
		"groupLevel": 0,  //组级别，0:单产品,1:跨产品
		"maxDevNum": 0    //设备数量上限，0不做限制'
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


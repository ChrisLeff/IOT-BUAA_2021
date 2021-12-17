# AEP固件管理
## API列表
|API名称 | 安全认证方式 | 签名认证方式 | 描述 |
|:-------|:------|:--------|:--------|
|UpdateFirmware|none|hmac-sha1|修改固件信息|
|QueryFirmwareList|none|hmac-sha1|查询固件列表|
|QueryFirmware|none|hmac-sha1|查询固件详情|
|DeleteFirmware|none|hmac-sha1|删除固件|

## API调用
### 请求地址

|环境 | HTTP请求地址  | HTTPS请求地址 |
|:-------|:------|:--------|
|正式环境|ag-api.ctwing.cn/aep_firmware_management|ag-api.ctwing.cn/aep_firmware_management|

### 公共入参

公共请求参数是指每个接口都需要使用到的请求参数。

|参数名称 | 含义  | 位置 | 描述|
|:-------|:------|:--------|:--------|
|application|应用标识|HEAD|应用的App Key，如果需要进行签名认证则需要填写，例如：dAaFG7DiPt8|
|signature|签名数据|HEAD|将业务数据连同timestamp、application一起签名后的数据，如果需要进行签名认证则需要填写|
|timestamp|UNIX格式时间戳|HEAD|如果需要进行签名认证则需要填写，例如：1515752817580|
|version|API版本号|HEAD|可以指定API版本号访问历史版本|

## API 文档说明
### API名称：UpdateFirmware   版本号: 20190615001705

#### 描述

修改固件信息

#### 请求信息

请求路径：/firmware

请求方法：PUT

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|id|QUERY|Long|true|固件id|
|MasterKey|HEAD|String|false|MasterKey|

#### 请求BODY

##### 数据类型：
json

##### 内容描述：
{
  "firmwareDesc": "string",
  "firmwareName": "string",
  "firmwareVersion": "string",
  "productId": 0
}
描述：
  "firmwareDesc": 固件描述,选填
  "firmwareName": 固件名称,选填
  "firmwareVersion": 固件版本号,选填
  "productId": 产品id Integer,必填

#### 返回信息

##### 返回参数类型
default

##### 返回结果示例
{
  "code": 0,
  "msg": "ok",
  "result": "Success to update firmware."
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

### API名称：QueryFirmwareList   版本号: 20190615001608

#### 描述

查询固件列表

#### 请求信息

请求路径：/firmwares

请求方法：GET

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|productId|QUERY|Long|true|产品id|
|searchValue|QUERY|String|false|查询条件，可以根据固件名称模糊查询|
|pageNow|QUERY|Long|false|当前页数|
|pageSize|QUERY|Long|false|每页记录数|
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
    "pageSize": 20,
    "total": 13,
    "list": [
      {
        "firmwareId": 3120,
        "firmwareName": "测试固件1",
        "tenantId": "10007905",
        "productId": 10004017,
        "firmwareUrl": "/webctdfs/file?tenantId=10007905&productId=10004017&fileName=1551231667611501.xlsx&fileType=package",
        "firmwareVersion": "v1.0",
        "upgradeId": 1,
        "upgradeType": 0,
        "firmwareSignature": 1,
        "firmwareDesc": "",
        "createTime": 1551231667000,
        "createBy": "huangliang",
        "updateTime": 1551231667000,
        "updateBy": "yyyf",
        "fileName": "设备批量导入模板 (1).xlsx",
        "md5": "59a650b2a43c170e",
        "upgradeUploadType": 1,
        "moduleType": 1003,
        "moduleName": "电信定制模组",
        "upgradePlan": 2
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

### API名称：QueryFirmware   版本号: 20190618151645

#### 描述

查询固件详情

#### 请求信息

请求路径：/firmware

请求方法：GET

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|id|QUERY|Long|true|固件id|
|productId|QUERY|Long|true|产品id|
|MasterKey|HEAD|String|false|MasterKey|


#### 返回信息

##### 返回参数类型
json

##### 返回结果示例
{
  "code": 0,
  "msg": "ok",
  "result": {
    "firmwareId": 3144,
    "firmwareName": "csdcsd",
    "tenantId": "10007905",
    "productId": 10004017,
    "firmwareUrl": "/webctdfs/file?tenantId=10007905&productId=10004017&fileName=1551784639426519.xlsx&fileType=package",
    "firmwareVersion": "1.0454",
    "upgradeId": 1,
    "upgradeType": 0,
    "firmwareSignature": 1,
    "firmwareDesc": "",
    "createTime": 1551784639000,
    "createBy": "huangliang",
    "updateTime": 1551784631111,
    "updateBy": "yyy",
    "fileName": "设备批量导入模板 (1).xlsx",
    "md5": "AB4A7D9A59A650B2A43C170EA330F6BC",
    "upgradeUploadType": 1,
    "moduleType": 1001,
    "moduleName": "海思150",
    "upgradePlan": 1
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

### API名称：DeleteFirmware   版本号: 20190615001534

#### 描述

删除固件

#### 请求信息

请求路径：/firmware

请求方法：DELETE

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|id|QUERY|Long|true|固件id|
|productId|QUERY|Long|true|产品id|
|updateBy|QUERY|String|false|修改人|
|MasterKey|QUERY|String|false|MasterKey|


#### 返回信息

##### 返回参数类型
default

##### 返回结果示例
{
  "code": 0,
  "msg": "ok",
  "result": "Success to update firmware."
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


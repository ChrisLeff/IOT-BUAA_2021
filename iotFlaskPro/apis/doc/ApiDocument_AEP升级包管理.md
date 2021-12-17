# AEP升级包管理
## API列表
|API名称 | 安全认证方式 | 签名认证方式 | 描述 |
|:-------|:------|:--------|:--------|
|UpdateSoftware|none|hmac-sha1|修改升級包信息|
|DeleteSoftware|none|hmac-sha1|删除升级包|
|QuerySoftware|none|hmac-sha1|查询升级包详情|
|QuerySoftwareList|none|hmac-sha1|查询升级包列表|

## API调用
### 请求地址

|环境 | HTTP请求地址  | HTTPS请求地址 |
|:-------|:------|:--------|
|正式环境|ag-api.ctwing.cn/aep_software_management|ag-api.ctwing.cn/aep_software_management|

### 公共入参

公共请求参数是指每个接口都需要使用到的请求参数。

|参数名称 | 含义  | 位置 | 描述|
|:-------|:------|:--------|:--------|
|application|应用标识|HEAD|应用的App Key，如果需要进行签名认证则需要填写，例如：dAaFG7DiPt8|
|signature|签名数据|HEAD|将业务数据连同timestamp、application一起签名后的数据，如果需要进行签名认证则需要填写|
|timestamp|UNIX格式时间戳|HEAD|如果需要进行签名认证则需要填写，例如：1515752817580|
|version|API版本号|HEAD|可以指定API版本号访问历史版本|

## API 文档说明
### API名称：UpdateSoftware   版本号: 20200529232851

#### 描述

修改升級包信息

#### 请求信息

请求路径：/software

请求方法：PUT

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|id|QUERY|Long|true|升级包id|
|MasterKey|HEAD|String|true|MasterKey，在产品概况中可以查看|

#### 请求BODY

##### 数据类型：
json

##### 内容描述：
{
  "productId": 0,
  "softwareDesc": "string",
  "softwareName": "string",
  "softwareVersion": "string"
}
描述：
  "productId": 产品id,
  "softwareDesc": 升级包版本描述,
  "softwareName": 升级包版本名称,
  "softwareVersion": 升级包版本号

#### 返回信息

##### 返回参数类型
default

##### 返回结果示例
{
  "code": 0,
  "msg": "ok",
  "result": "Successfully modified."
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

### API名称：DeleteSoftware   版本号: 20200529232809

#### 描述

删除升级包

#### 请求信息

请求路径：/software

请求方法：DELETE

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|id|QUERY|Long|true|升级包id|
|productId|QUERY|Long|true|产品id|
|MasterKey|HEAD|String|true|MasterKey,在产品概况中可以查询|


#### 返回信息

##### 返回参数类型
default

##### 返回结果示例
{
  "code": 0,
  "msg": "ok",
  "result": "Successfully deleted."
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

### API名称：QuerySoftware   版本号: 20200529232806

#### 描述

查询升级包详情

#### 请求信息

请求路径：/software

请求方法：GET

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|id|QUERY|Long|true|升级包ID|
|productId|QUERY|Long|true|产品id|
|MasterKey|HEAD|String|true|MasterKey，可在产品概况中查看|


#### 返回信息

##### 返回参数类型
json

##### 返回结果示例
{
  "code": 0,
  "msg": "ok",
  "result": {
    "softwareId": 7434,
    "softwareName": "sdcsdc",
    "tenantId": "300",
    "productId": 10013604,
    "softwareVersion": "1232",
    "softwareDesc": "",
    "createTime": 1585813709000,
    "fileName": "SOTA_test11.zip",
    "fileSize": 39152,
    "checkCode": "3132"
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

### API名称：QuerySoftwareList   版本号: 20200529232801

#### 描述

查询升级包列表

#### 请求信息

请求路径：/softwares

请求方法：GET

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|productId|QUERY|Long|true|产品id|
|searchValue|QUERY|String|false|查询条件，可以根据升级包名称模糊查询|
|pageNow|QUERY|Long|false|当前页数|
|pageSize|QUERY|Long|false|每页记录数|
|MasterKey|HEAD|String|true|MasterKey，可以在产品概况中查看|


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
    "total": 21,
    "list": [
      {
        "softwareId": 7435,
        "softwareName": "sdcsdc",
        "tenantId": "300",
        "productId": 10013604,
        "softwareVersion": "13433",
        "softwareDesc": "",
        "createTime": 1585813748000,
        "fileName": "SOTA_test11.zip",
        "fileSize": 39152,
        "checkCode": "3132"
      },
      {
        "softwareId": 7296,
        "softwareName": "三生三世",
        "tenantId": "300",
        "productId": 10013604,
        "softwareVersion": "S01",
        "softwareDesc": "",
        "createTime": 1575970983000,
        "fileName": "S01.zip",
        "fileSize": 3904,
        "checkCode": "1207"
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


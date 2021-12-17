# User
## API列表
|API名称 | 安全认证方式 | 签名认证方式 | 描述 |
|:-------|:------|:--------|:--------|
|SdkDownload|none|hmac-sha1|SDK下载|

## API调用
### 请求地址

|环境 | HTTP请求地址  | HTTPS请求地址 |
|:-------|:------|:--------|
|正式环境|ag-api.ctwing.cn/usr|ag-api.ctwing.cn/usr|

### 公共入参

公共请求参数是指每个接口都需要使用到的请求参数。

|参数名称 | 含义  | 位置 | 描述|
|:-------|:------|:--------|:--------|
|application|应用标识|HEAD|应用的App Key，如果需要进行签名认证则需要填写，例如：dAaFG7DiPt8|
|signature|签名数据|HEAD|将业务数据连同timestamp、application一起签名后的数据，如果需要进行签名认证则需要填写|
|timestamp|UNIX格式时间戳|HEAD|如果需要进行签名认证则需要填写，例如：1515752817580|
|version|API版本号|HEAD|可以指定API版本号访问历史版本|

## API 文档说明
### API名称：SdkDownload   版本号: 20180000000000

#### 描述

SDK下载

#### 请求信息

请求路径：/sdk/download

请求方法：GET

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|sdk_type|QUERY|String|false|SDK语言类型，默认为Java(字典项: sdk_type)|
|file_name|QUERY|String|true|SDK描述，用以标识其中的biz包|
|application_id|QUERY|String|true|应用编码，下载的SDK会根据该编码收集所有有权限的API打包|
|api_version|QUERY|String|false|API版本信息 TODO|


#### 返回信息

##### 返回参数类型
default

##### 返回结果示例
[BINARY DATA]

##### 异常返回示例
Application not found: 10001

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


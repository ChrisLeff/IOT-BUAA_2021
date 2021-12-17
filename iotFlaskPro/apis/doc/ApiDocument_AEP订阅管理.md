# AEP订阅管理
## API列表
|API名称 | 安全认证方式 | 签名认证方式 | 描述 |
|:-------|:------|:--------|:--------|
|GetSubscription|none|hmac-sha1|根据subId查询设备北向订阅信息|
|GetSubscriptionsList|none|hmac-sha1|查询设备北向订阅信息列表|
|DeleteSubscription|none|hmac-sha1|删除设备北向订阅信息|
|CreateSubscription|none|hmac-sha1|创建设备北向订阅|

## API调用
### 请求地址

|环境 | HTTP请求地址  | HTTPS请求地址 |
|:-------|:------|:--------|
|正式环境|ag-api.ctwing.cn/aep_subscribe_north|ag-api.ctwing.cn/aep_subscribe_north|

### 公共入参

公共请求参数是指每个接口都需要使用到的请求参数。

|参数名称 | 含义  | 位置 | 描述|
|:-------|:------|:--------|:--------|
|application|应用标识|HEAD|应用的App Key，如果需要进行签名认证则需要填写，例如：dAaFG7DiPt8|
|signature|签名数据|HEAD|将业务数据连同timestamp、application一起签名后的数据，如果需要进行签名认证则需要填写|
|timestamp|UNIX格式时间戳|HEAD|如果需要进行签名认证则需要填写，例如：1515752817580|
|version|API版本号|HEAD|可以指定API版本号访问历史版本|

## API 文档说明
### API名称：GetSubscription   版本号: 20181031202033

#### 描述

根据subId查询设备北向订阅信息

#### 请求信息

请求路径：/subscription

请求方法：GET

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|subId|QUERY|Long|true|订阅记录id|
|productId|QUERY|Long|true|产品id|
|MasterKey|HEAD|String|true|产品MasterKey|


#### 返回信息

##### 返回参数类型
default

##### 返回结果示例
{
  "code": 0,
  "msg": "ok",
  "result": {
    "subId": 49,
    "tenantId": "10007905",
    "productId": 1531,
    "deviceId": "1",
    "subType": 1,
    "subLevel": 2,
    "subUrl": "http://baidu.com",
    "createTime": 1529055308000,
    "createBy": "ss",
    "updateTime": null,
    "updateBy": null,
    "isSub": 0,
    "isDel": 0
  }
}


    "code": 返回码(0成功),
    "msg": 返回描述(ok成功),
    "result": 返回内容
    "subId": 序号,
    "tenantId": 租户id,
    "productId": 产品id,
    "deviceId": 设备id,
    "subType":订阅消息类型，1.设备数据变化 2.设备指令响应 3.设备事件上报 4.设备上下线通知 9.TUP合并数据上报
    "subLevel": 1.产品级 2.设备级,
    "subUrl": 地址,
    "createTime": 创建时间,
    "createBy": 创建人,
    "updateTime": 更新时间,
    "updateBy": 更新人,
    "isSub": 是否订阅（0订阅,1取消订阅）
    "isDel": 是否删除（0未删除，1删除）

##### 异常返回示例
{
 "code":-1,
 "msg":"服务端错误", 
 "result":null
}
失败时code为-1,从msg中获取错误详情

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

### API名称：GetSubscriptionsList   版本号: 20181031202027

#### 描述

查询设备北向订阅信息列表

#### 请求信息

请求路径：/subscribes

请求方法：GET

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|productId|QUERY|Long|true|产品ID|
|pageNow|QUERY|Long|true|当前页|
|pageSize|QUERY|Long|true|每页条数|
|MasterKey|HEAD|String|true||
|subType|QUERY|Long|false|订阅类型|
|searchValue|QUERY|String|false|检索deviceId,模糊匹配|


#### 返回信息

##### 返回参数类型
default

##### 返回结果示例
{
  "code": 0,
  "msg": "ok",
  "result": {}
}
    "code": 返回码(0成功),
    "msg": 返回描述(ok成功),
    "result": 返回内容
    "subId": 序号,
    "tenantId": 租户id,
    "productId": 产品id,
    "deviceId": 设备id,
    "subType":订阅消息类型，1.设备数据变化 2.设备指令响应 3.设备事件上报 4.设备上下线通知 9.TUP合并数据上报
    "subLevel": 1.产品级 2.设备级,
    "subUrl": 地址,
    "createTime": 创建时间,
    "createBy": 创建人,
    "updateTime": 更新时间,
    "updateBy": 更新人,
    "isSub": 是否订阅（0订阅,1取消订阅）
    "isDel": 是否删除（0未删除,1已删除）

##### 异常返回示例
{
 "code":-1,
 "msg":"服务端错误", 
 "result":null
}
失败时code为-1,从msg中获取错误详情

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

### API名称：DeleteSubscription   版本号: 20181031202023

#### 描述

删除设备北向订阅信息

#### 请求信息

请求路径：/subscription

请求方法：DELETE

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|subId|QUERY|String|true|订阅记录id|
|deviceId|QUERY|String|false|设备id|
|productId|QUERY|Long|true|产品id|
|subLevel|QUERY|Long|true|订阅级别|
|MasterKey|HEAD|String|true|产品MasterKey|


#### 返回信息

##### 返回参数类型
default

##### 返回结果示例
{
  "code": 0,
  "msg": "ok",
  "result": null
}
  "code": 返回码(0成功),
  "msg": 返回描述(ok成功),
  "result": null

##### 异常返回示例
{
 "code":-1,
 "msg":"服务端错误", 
 "result":null
}
失败时code为-1,从msg中获取错误详情

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

### API名称：CreateSubscription   版本号: 20181031202018

#### 描述

创建设备北向订阅

#### 请求信息

请求路径：/subscription

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
  "deviceId": "String",
  "operator": "String",
  "productId": int,
  "subLevel": int,
  "subTypes":int[],
  "subUrl": "String"
}
描述：
subTypes:消息类型(必填),可填写1个或多个(1表示设备数据变化通知、2表示设备响应命令通知、
         3表示设备事件上报、4表示设备上下线通知、9表示TUP合并数据上报）
deviceId:设备id(产品级可以不填,设备级必填),
subLevel:订阅级别,必填(1:产品级 2：设备级)
subUrl:消息接收路径，接收消息的url(必填),
operator:操作人(必填),
productId:产品id(必填)

#### 返回信息

##### 返回参数类型
default

##### 返回结果示例
{
  "code": 0,
  "msg": "ok",
  "result": null
}

  "code": 返回码(0成功),
  "msg": 返回描述(ok成功),
  "result": null

##### 异常返回示例
{
 "code":-1,
 "msg":"服务端错误", 
 "result":null
}
失败时code为-1,从msg中获取错误详情

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


# AEP远程控制
## API列表
|API名称 | 安全认证方式 | 签名认证方式 | 描述 |
|:-------|:------|:--------|:--------|
|QueryRemoteControlList|none|hmac-sha1|批量查询远程控制指令详情|
|CreateRemoteControl|none|hmac-sha1|下发远程控制指令|

## API调用
### 请求地址

|环境 | HTTP请求地址  | HTTPS请求地址 |
|:-------|:------|:--------|
|正式环境|ag-api.ctwing.cn/aep_device_control|ag-api.ctwing.cn/aep_device_control|

### 公共入参

公共请求参数是指每个接口都需要使用到的请求参数。

|参数名称 | 含义  | 位置 | 描述|
|:-------|:------|:--------|:--------|
|application|应用标识|HEAD|应用的App Key，如果需要进行签名认证则需要填写，例如：dAaFG7DiPt8|
|signature|签名数据|HEAD|将业务数据连同timestamp、application一起签名后的数据，如果需要进行签名认证则需要填写|
|timestamp|UNIX格式时间戳|HEAD|如果需要进行签名认证则需要填写，例如：1515752817580|
|version|API版本号|HEAD|可以指定API版本号访问历史版本|

## API 文档说明
### API名称：QueryRemoteControlList   版本号: 20190507012630

#### 描述

批量查询远程控制指令详情

#### 请求信息

请求路径：/controls

请求方法：GET

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|MasterKey|HEAD|String|true|MasterKey在该设备所属产品的概况中可以查看|
|productId|QUERY|Long|true||
|searchValue|QUERY|String|false|可选填：设备Id|
|type|QUERY|Long|false|可选填枚举值：\n1：设备重启\n2：退出平台\n3：重新登录\n4：设备自检\n6：开始发送数据\n7：停止发送数据\n8：恢复出厂设置|
|status|QUERY|Long|false|可选填：1：指令已保存\n2：指令已发送\n3：指令已送达\n4：指令已完成\n999：指令发送失败|
|startTime|QUERY|String|false|精确到毫秒的时间戳|
|endTime|QUERY|String|false|精确到毫秒的时间戳|
|pageNow|QUERY|Long|false|当前页数|
|pageSize|QUERY|Long|false|每页记录数|


#### 返回信息

##### 返回参数类型
json

##### 返回结果示例
{
  "code": 0,
  "msg": "ok",
  "result": {
    "pageNum": 1,
    "pageSize": 1,
    "total": 3,
    "list": [
      {
        "tenantId": "10007905",
        "taskId": 191585,
        "deviceId": "10000365weq123",
        "deviceSn": "weq123",
        "productId": 10000365,
        "controlType": 1,
        "status": 2,
        "ttl": 7200,
        "createTime": 1539593279000,
        "finishTime": 1539593299000,
        "resultCode": "",
        "operator": "aepuser"
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

### API名称：CreateRemoteControl   版本号: 20181031202247

#### 描述

下发远程控制指令

#### 请求信息

请求路径：/control

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
  "controlType": 0,
  "deviceId": "string",
  "deviceSn": "string",
  "operator": "string",
  "productId": 0,
  "ttl": 0
}
controlType: 远程控制类型，必填
指令类型：1.设备重启，2.退出平台，3.重新登录，4.设备自检，5.通知设备软件升级，
          6.开始发送数据，7.停止发送数据，8.恢复出厂设置
deviceId: 设备ID，必填
deviceSn: 设备编号，必填
operator: 操作者，必填
productId: 产品ID，必填
ttl: 指令在缓存时长默认7200秒，单位秒，选填

#### 返回信息

##### 返回参数类型
default

##### 返回结果示例
{
  "code": 0,
  "msg": "string",
  "result": {}
}

##### 异常返回示例
{
  "code": 8803,
  "msg": "参数验证失败",
  "result": null
}
(8803, "参数验证失败")报错原因：可能是产品id为空或者小于等于0或者未能获取到租户id或者设备Sn为空，或者参数类型有误。
(1101, "设备编号已存在")报错原因：填写的设备编号已存在
(1105, "获取设备token失败")报错原因：未获取到设备token
(1102, "操作设备信息表失败")报错原因：操作数据库失败

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


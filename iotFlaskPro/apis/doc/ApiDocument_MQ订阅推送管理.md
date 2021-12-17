# MQ订阅推送管理
## API列表
|API名称 | 安全认证方式 | 签名认证方式 | 描述 |
|:-------|:------|:--------|:--------|
|QueryServiceState|none|hmac-sha1|根据tenantId查询开通状态、开通时间、token等信息|
|OpenMqService|none|hmac-sha1|开通租户MQ消息推送服务|
|CreateTopic|none|hmac-sha1|创建topic，同一租户最多能创建10个主题，不能出现同名topic|
|QueryTopicInfo|none|hmac-sha1|根据topicId查询topic基本信息|
|QueryTopicCacheInfo|none|hmac-sha1|根据topicId查询topic缓存空间使用信息|
|QueryTopics|none|hmac-sha1|查询某个租户的所有topic列表|
|ChangeTopicInfo|none|hmac-sha1|更新topic基本信息，可更新topic名称、描述、启用状态、数据源类型、删除状态|
|QuerySubRules|none|hmac-sha1|根据产品ID获取指定topic下的订阅规则列表，支持多产品ID|
|ChangeSubRules|none|hmac-sha1|增加或修改产品订阅规则|
|ClosePushService|none|hmac-sha1|关闭租户MQ消息提送服务|

## API调用
### 请求地址

|环境 | HTTP请求地址  | HTTPS请求地址 |
|:-------|:------|:--------|
|正式环境|ag-api.ctwing.cn/aep_mq_sub|ag-api.ctwing.cn/aep_mq_sub|

### 公共入参

公共请求参数是指每个接口都需要使用到的请求参数。

|参数名称 | 含义  | 位置 | 描述|
|:-------|:------|:--------|:--------|
|application|应用标识|HEAD|应用的App Key，如果需要进行签名认证则需要填写，例如：dAaFG7DiPt8|
|signature|签名数据|HEAD|将业务数据连同timestamp、application一起签名后的数据，如果需要进行签名认证则需要填写|
|timestamp|UNIX格式时间戳|HEAD|如果需要进行签名认证则需要填写，例如：1515752817580|
|version|API版本号|HEAD|可以指定API版本号访问历史版本|

## API 文档说明
### API名称：QueryServiceState   版本号: 20201218144210

#### 描述

根据tenantId查询开通状态、开通时间、token等信息

#### 请求信息

请求路径：/mqStat

请求方法：GET

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|


#### 返回信息

##### 返回参数类型
default

##### 返回结果示例
{
  "code":0,
  "msg":"ok",
  "result":{
"tenantId":"xx",
"isOpen":true,
"token":" xxxx",
"createTime":"2020-08-18 16:44:30",
"updateTime":"2020-08-18 16:44:30"
}
其中：
"tenantId": 租户id,
"isOpen": 开通状态，true(1):开通；false(0):未开通
"token": 认证JWT信息
"createTime": 创建时间,
"updateTime": 更新时间,
}

  "code": 返回码(0成功),
  "msg": 返回描述(ok成功)

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

### API名称：OpenMqService   版本号: 20201217094438

#### 描述

开通租户MQ消息推送服务

#### 请求信息

请求路径：/mqStat

请求方法：POST

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|


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

### API名称：CreateTopic   版本号: 20201218142343

#### 描述

创建topic，同一租户最多能创建10个主题，不能出现同名topic

#### 请求信息

请求路径：/topic

请求方法：POST

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|

#### 请求BODY

##### 数据类型：
json

##### 内容描述：
{
"topicName":"String",
"topicDesc":"String"
}
描述：
topicName：topic名称（必填），只能包含字母数字、中/下划线，30字符以内，
topicDesc ：topic描述（必填）， 255英文字符以内

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

### API名称：QueryTopicInfo   版本号: 20201218153403

#### 描述

根据topicId查询topic基本信息

#### 请求信息

请求路径：/topic

请求方法：GET

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|topicId|QUERY|Long|true||


#### 返回信息

##### 返回参数类型
default

##### 返回结果示例
{
  "code":0,
  "msg":"ok",
  "result":{
"topicId": xx,
"tenantId":"xx",
"topicName":"xx",
"topicDesc":"xx",
"isAllMsg":false,
"isEnable":true,
"isDel":false,
"createTime":"2020-08-18 16:53:17",
"updateTime":"2020-10-27 10:48:43",
"deptCode":"0"
}
其中：
"topicId":主题id,
"tenantId":租户id,
"topicName":主题名称,
"topicDesc":主题描述,
"isAllMsg":主题是否包含所有数据源。true(1):是；false(0):否,
"isEnable":该主题是否启用, true(1):是；false(0):否,
"isDel": 该主题是否已删除, true(1):是；false(0):否,
"createTime":创建时间,
"updateTime": 更新时间,
"deptCode": 机构id
}
  "code": 返回码(0成功),
  "msg": 返回描述(ok成功)

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

### API名称：QueryTopicCacheInfo   版本号: 20201218150354

#### 描述

根据topicId查询topic缓存空间使用信息

#### 请求信息

请求路径：/topic/cache

请求方法：GET

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|topicId|QUERY|Long|true||


#### 返回信息

##### 返回参数类型
default

##### 返回结果示例
{
  "code": 0,
  "msg": "ok",
  "result":{
"limit": xxx,
"used": xxx
}
其中：
"limit":限制大小，字节数，
"used":已用空间，字节数
}
  "code": 返回码(0成功),
  "msg": 返回描述(ok成功)

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

### API名称：QueryTopics   版本号: 20201218153456

#### 描述

查询某个租户的所有topic列表

#### 请求信息

请求路径：/topics

请求方法：GET

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|


#### 返回信息

##### 返回参数类型
default

##### 返回结果示例
{
  "code":0,
  "msg":"ok",
  "result":[{
"topicId":xxx,
"tenantId":"xxx",
"topicName":"xxx",
"topicDesc":"xxx",
"isAllMsg":false,
"isEnable":true,
"isDel":false,
"createTime":"2020-12-18 14:25:58",
"updateTime":"2020-12-18 14:25:58",
"deptCode":"0"
},
{
…
}
]
其中：
"topicId":主题id,
"tenantId":租户id,
"topicName":主题名称,
"topicDesc":主题描述,
"isAllMsg":主题是否包含所有数据源。true(1):是；false(0):否,
"isEnable":该主题是否启用, true(1):是；false(0):否,
"isDel": 该主题是否已删除, true(1):是；false(0):否,
"createTime":创建时间,
"updateTime": 更新时间,
"deptCode": 机构id
}
  "code": 返回码(0成功),
  "msg": 返回描述(ok成功)

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

### API名称：ChangeTopicInfo   版本号: 20201218153044

#### 描述

更新topic基本信息，可更新topic名称、描述、启用状态、数据源类型、删除状态

#### 请求信息

请求路径：/topic

请求方法：PUT

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|topicId|QUERY|Long|true||

#### 请求BODY

##### 数据类型：
json

##### 内容描述：
{
"topicName":"String",
"topicDesc":"String",
"isAllMsg":0,
"isEnable":1,
"isDel":0
}
描述：
topicName：topic名称，只能包含字母数字、中/下划线，30字符以内，
topicDesc ：topic描述， 255英文字符以内
isAllMsg:主题是否包含所有数据源。true(1):是；false(0):否,
isEnable:该主题是否启用, true(1):是；false(0):否,
isDel: 该主题是否已删除, true(1):是；false(0):否,
各字段都不是必填，按需填写

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

### API名称：QuerySubRules   版本号: 20201218160237

#### 描述

根据产品ID获取指定topic下的订阅规则列表，支持多产品ID

#### 请求信息

请求路径：/rule

请求方法：POST

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|

#### 请求BODY

##### 数据类型：
json

##### 内容描述：
{
"productIds":int[],
"topicId":"String"
}
描述：
productIds: 产品id（必填），为int数组，
topicId: 主题id（必填）

#### 返回信息

##### 返回参数类型
default

##### 返回结果示例
{
  "code":0,
  "msg":"ok",
  "result":[{
"topicId":xx,
"productId":xx,
"tenantId":"xx",
"subTypes":"1,2,3",
"subTypesArray":[1,2,3],
"isDel":false,
"createTime":"2020-12-17 15:33:27",
"updateTime":"2020-12-17 16:01:05"
},
{
…
}
]
其中：
"topicId":主题id,
"productId":产品id
"tenantId":租户id,
"subTypes":消息类型int数组，（1.设备数据变化2.下发指令响应3.设备事件上报4.设备上下线通知5.创建删除设备9.TUP合并数据上报）,
"isDel": 该主题是否已删除, true(1):是；false(0):否,
"createTime":创建时间,
"updateTime": 更新时间,
}
  "code": 返回码(0成功),
  "msg": 返回描述(ok成功)

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

### API名称：ChangeSubRules   版本号: 20201218161013

#### 描述

增加或修改产品订阅规则

#### 请求信息

请求路径：/rule

请求方法：PUT

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|

#### 请求BODY

##### 数据类型：
json

##### 内容描述：
{
"topicId":"String",
"productId":int,
"subTypes":int[]
}
描述：
topicId:主题id（必填），
productId:产品id（必填），
subTypes:消息类型int数组，为空则认为可删除

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

### API名称：ClosePushService   版本号: 20201217141937

#### 描述

关闭租户MQ消息提送服务

#### 请求信息

请求路径：/mqStat

请求方法：DELETE

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|


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


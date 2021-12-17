# AEP设备管理
## API列表
|API名称 | 安全认证方式 | 签名认证方式 | 描述 |
|:-------|:------|:--------|:--------|
|QueryDeviceList|none|hmac-sha1|批量获取设备信息|
|QueryDevice|none|hmac-sha1|获取单个设备详情|
|DeleteDevice|none|hmac-sha1|删除设备|
|UpdateDevice|none|hmac-sha1|更新设备|
|CreateDevice|none|hmac-sha1|增加设备|
|BindDevice|none|hmac-sha1|调用方使用IMEI绑定物联网平台中已注册的NB设备，平台更改设备绑定状态为”已绑定”并返回设备ID，设备状态等数据给调用方|
|UnbindDevice|none|hmac-sha1|调用方通过设备ID解绑物联网平台中已绑定的NB设备，平台更改设备绑定状态为”已解绑”并取消该设备的订阅|
|QueryProductInfoByImei|none|hmac-sha1|通过IMEI号查询产品名称产品ID(只支持LWM2M协议)|
|ListDeviceInfo|none|hmac-sha1|根据设备ID列表查询设备信息|
|DeleteDeviceByPost|none|hmac-sha1|批量删除设备Post方法|
|ListDeviceActiveStatus|none|hmac-sha1|批量查询设备激活状态|

## API调用
### 请求地址

|环境 | HTTP请求地址  | HTTPS请求地址 |
|:-------|:------|:--------|
|正式环境|ag-api.ctwing.cn/aep_device_management|ag-api.ctwing.cn/aep_device_management|

### 公共入参

公共请求参数是指每个接口都需要使用到的请求参数。

|参数名称 | 含义  | 位置 | 描述|
|:-------|:------|:--------|:--------|
|application|应用标识|HEAD|应用的App Key，如果需要进行签名认证则需要填写，例如：dAaFG7DiPt8|
|signature|签名数据|HEAD|将业务数据连同timestamp、application一起签名后的数据，如果需要进行签名认证则需要填写|
|timestamp|UNIX格式时间戳|HEAD|如果需要进行签名认证则需要填写，例如：1515752817580|
|version|API版本号|HEAD|可以指定API版本号访问历史版本|

## API 文档说明
### API名称：QueryDeviceList   版本号: 20190507012134

#### 描述

批量获取设备信息

#### 请求信息

请求路径：/devices

请求方法：GET

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|MasterKey|HEAD|String|true|MasterKey在该设备所属产品的概况中可以查看|
|productId|QUERY|Long|true||
|searchValue|QUERY|String|false|T-link协议可选填:设备名称，设备编号，设备Id\nMQTT协议可选填:设备名称，设备编号，设备Id\nLWM2M协议可选填:设备名称，设备Id ,IMEI号\nTUP协议可选填:设备名称，设备Id ,IMEI号\nTCP协议可选填:设备名称，设备编号，设备Id\nHTTP协议可选填:设备名称，设备编号，设备Id\nJT/T808协议可选填:设备名称，设备编号，设备Id|
|pageNow|QUERY|Long|false|当前页数|
|pageSize|QUERY|Long|false|每页记录数,最大100|


#### 返回信息

##### 返回参数类型
default

##### 返回结果示例
MQTT,T-Link,HTTP,TCP协议：
{
  "code": 0,
  "msg": "ok",
  "result": {
    "pageNum": 1,
    "pageSize": 1,
    "total": 3,
    "list": [
      {
       "deviceSn": "4444",//string，设备编号
       "deviceId": "100054604444",//string，设备id
       "deviceName": "4444",//string，终端名称
       "tenantId": "10007903",//string，租户id
       "productId": 10005460,//Integer，产品id
       "firmwareVersion": "",//string，版本信息
       "deviceStatus": 2,//Integer，设备状态 0:已注册，1：已激活，2：已注销
       "createTime": 1555557239000,//Timestamp，创建时间
       "updateTime": 1555557274000,//Timestamp，修改时间
       "activeTime": 1555557243000,//Timestamp，激活时间
       "logoutTime": 1555557274000,//Timestamp，注销时间
       "netStatus": 2,//设备在线状态
       "onlineAt": 1555557243483,//Long，设备最后上线时间
       "offlineAt": 1555557244923,//Long，设备最后下线时间
       "productProtocol": 1//设备所在产品协议：1.T-LINK协议  2.MQTT协议  3.LWM2M协议  4.TUP协议  5.HTTP协议  6.JT/T808  7.TCP协议  8.私有TCP(网关子设备协议)  9.私有UDP(网关子设备协议)  10.网关产品MQTT(网关产品协议)  11.南向云
      }
    ]
  }
}
LWM2M协议：
{
  "code": 0,
  "msg": "ok",
  "result": {
    "pageNum": 1,
    "pageSize": 1,
    "total": 22,
    "list": [
      {
       "deviceId": "094eb1dc586349338b4b68313134991b",//string，设备ID
       "deviceName": "de-43",//string，设备名称
       "tenantId": "10007903",//string，租户ID
       "productId": 10006024,//Integer，产品ID
       "imei": "435676567891031",//String，IMEI号,全局唯一，根据产品的Endpoint必填，创建时可相同，则删除原产品新建产品
       "imsi": null,//String，IMSI号,根据产品的Endpoint选填
       "firmwareVersion": null,,//String，固件版本
       "deviceStatus": 2,//Integer，设备状态0.已注册 1.已激活 2.已注销
       "autoObserver": 0,//Integer，是否订阅,0.订阅1.不订阅
       "createTime": 1558404977000,//Long，创建时间
       "createBy": "aepuser",//String，创建者
       "updateTime": 1558760482000,//Long，更新时间
       "updateBy": "wwww",//String，更新者
       "netStatus": 2,//Integer，设备在线状态，1在线2不在线
       "onlineAt": 1558760604611,//Long，设备最后上线时间
       "offlineAt": 1558761600432//Long，设备最后下线时间
      }
    ]
  }
}
NB网关：
{
  "code": 0,
  "msg": "ok",
  "result": {
    "pageNum": 1,
    "pageSize": 1,
    "total": 1,
    "list": [
      {
       "deviceId": "eef13b3ba8dc41cb8db86e68002b7b5f",//string，设备ID
       "deviceName": "test512",//string，设备名称
       "tenantId": "10007905",//string，租户ID
       "productId": 10000607,//Integer，产品ID
       "imei": "122222222233332",//String，IMEI号,全局唯一，根据产品的Endpoint必填，创建时可相同，则删除原产品新建产品
       "deviceStatus": 2,//Integer，设备状态:0.已注册 1.已激活 2.已注销
       "createTime": 1540540567000,//Long，创建时间
       "createBy": "aepuser",//String，创建者
       "updateTime": 1540546732000,//Long，更新时间
       "updateBy": "eeee",//String，更新者
       "netStatus": 2,//Integer，设备在线状态，1在线2不在线
       "onlineAt": 1558345352273,//Long 设备最后上线时间
       "offlineAt": 1558345755738//Long 设备最后下线时间
      }
    ]
  }
}
JT/T808协议：
{
  "code": 0,
  "msg": "ok",
  "result": {
    "pageNum": 1,
    "pageSize": 30,
    "total": 1,
    "list": [
      {
       "deviceId": "b0f62038087a4177ac45b7c4b09bed27",//String，设备ID
       "deviceName": "JTT808_透传_设备01",//String，设备名称
       "deviceSn": "JT04221",//String,设备编号
       "deviceModel": "JTT80804221611001",//String,设备型号
       "manufacturerId": "JT001",//String,制造商ID
       "tenantId": "10028069",//String,租户ID
       "productId": 10005606,//Integer,产品ID
       "deviceVersion": "",//String,设备版本号
       "deviceStatus": 2,//Integer,设备状态:-1.未注册 0.已注册 1.已激活 2.已注销
       "createTime": 1555920751000,//Long,创建时间
       "updateTime": 1555922101000,//Long,更新时间
       "activeTime": 1555921801000,//Long,激活时间
       "logoutTime": 1555922101000,//Long,注销时间
       "createBy": null,//String,创建者
       "updateBy": null,//String,更新者
       "netStatus": 2,//Integer,在线状态
       "onlineAt": 1555921801355,//Long,最后上线时间
       "offlineAt": 1555922101300//Long,最后下线时间
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

### API名称：QueryDevice   版本号: 20181031202139

#### 描述

获取单个设备详情

#### 请求信息

请求路径：/device

请求方法：GET

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|MasterKey|HEAD|String|true|MasterKey在该设备所属产品的概况中可以查看|
|deviceId|QUERY|String|true||
|productId|QUERY|Long|true||


#### 返回信息

##### 返回参数类型
default

##### 返回结果示例
MQTT、T-Link、HTTP、TCP:
{
  "code": 0,
  "msg": "ok",
  "result": {
    "deviceSn": "4444",//string，设备编号
    "deviceId": "100054604444",//string，设备id
    "deviceName": "4444",//string，终端名称
    "tenantId": "10007903",//string，租户id
    "productId": 10005460,//Integer，产品id
    "firmwareVersion": "",//string，版本信息
    "deviceStatus": 2,//Integer，设备状态 0:已注册，1：已激活，2：已注销
    "createTime": 1555557239000,//Timestamp，创建时间
    "updateTime": 1555557274000,//Timestamp，修改时间
    "activeTime": 1555557243000,//Timestamp，激活时间
    "logoutTime": 1555557274000,//Timestamp，注销时间
    "netStatus": 2,//设备在线状态
    "onlineAt": 1555557243483,//Long，设备最后上线时间
    "offlineAt": 1555557244923,//Long，设备最后下线时间
    "productProtocol": 1//设备所在产品协议：1.T-LINK协议  2.MQTT协议  3.LWM2M协议  4.TUP协议  5.HTTP协议  6.JT/T808  7.TCP协议  8.私有TCP(网关子设备协议)  9.私有UDP(网关子设备协议)  10.网关产品MQTT(网关产品协议)  11.南向云
  }
}

LWM2M：
{
  "code": 0,
  "msg": "ok",
  "result": {
    "deviceId": "094eb1dc586349338b4b68313134991b",//string，设备ID
    "deviceName": "de-43",//string，设备名称
    "tenantId": "10007903",//string，租户ID
    "productId": 10006024,//Integer，产品ID
    "imei": "435676567891031",//String，IMEI号,全局唯一，根据产品的Endpoint必填，创建时可相同，则删除原产品新建产品
    "imsi": null,//String，IMSI号,根据产品的Endpoint选填
    "firmwareVersion": null,,//String，固件版本
    "deviceStatus": 2,//Integer，设备状态0.已注册 1.已激活 2.已注销
    "autoObserver": 0,//Integer，是否订阅,0.自动订阅1.取消自动订阅
    "createTime": 1558404977000,//Long，创建时间
    "createBy": "aepuser",//String，创建者
    "updateTime": 1558760482000,//Long，更新时间
    "updateBy": "wwww",//String，更新者
    "netStatus": 2,//Integer，设备在线状态，1在线2不在线
    "onlineAt": 1558760604611,//Long，设备最后上线时间
    "offlineAt": 1558761600432//Long，设备最后下线时间
  }
}

NB网关：
{
  "code": 0,
  "msg": "ok",
  "result": {
    "deviceId": "eef13b3ba8dc41cb8db86e68002b7b5f",//string，设备ID
    "deviceName": "test512",//string，设备名称
    "tenantId": "10007905",//string，租户ID
    "productId": 10000607,//Integer，产品ID
    "imei": "122222222233332",//String，IMEI号,全局唯一，根据产品的Endpoint必填，创建时可相同，则删除原产品新建产品
    "deviceStatus": 2,//Integer，设备状态:0.已注册 1.已激活 2.已注销
    "createTime": 1540540567000,//Long，创建时间
    "createBy": "aepuser",//String，创建者
    "updateTime": 1540546732000,//Long，更新时间
    "updateBy": "eeee",//String，更新者
    "netStatus": 2,//Integer，设备在线状态，1在线2不在线
    "onlineAt": 1558345352273,//Long 设备最后上线时间
    "offlineAt": 1558345755738//Long 设备最后下线时间
  }
}
JT/T808协议：
{
  "code": 0,
  "msg": "ok",
  "result": {
    "deviceId": "b0f62038087a4177ac45b7c4b09bed27",//String，设备ID
    "deviceName": "JTT808_透传_设备01",//String，设备名称
    "deviceSn": "JT04221",//String,设备编号
    "deviceModel": "JTT80804221611001",//String,设备型号
    "manufacturerId": "JT001",//String,制造商ID
    "tenantId": "10028069",//String,租户ID
    "productId": 10005606,//Integer,产品ID
    "deviceVersion": "",//String,设备版本号
    "deviceStatus": 2,//Integer,设备状态:-1.未注册 0.已注册 1.已激活 2.已注销
    "createTime": 1555920751000,//Long,创建时间
    "updateTime": 1555922101000,//Long,更新时间
    "activeTime": 1555921801000,//Long,激活时间
    "logoutTime": 1555922101000,//Long,注销时间
    "createBy": null,//String,创建者
    "updateBy": null,//String,更新者
    "netStatus": 2,//Integer,在线状态
    "onlineAt": 1555921801355,//Long,最后上线时间
    "offlineAt": 1555922101300//Long,最后下线时间
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

### API名称：DeleteDevice   版本号: 20181031202131

#### 描述

删除设备

#### 请求信息

请求路径：/device

请求方法：DELETE

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|MasterKey|HEAD|String|true|MasterKey在该设备所属产品的概况中可以查看|
|productId|QUERY|Long|true||
|deviceIds|QUERY|String|true|可以删除多个设备（最多支持200个设备）。多个设备id，中间以逗号 \",\" 隔开 。样例：05979394b88a45b0842de729c03d99af,06106b8e1d5a458399326e003bcf05b4|


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

### API名称：UpdateDevice   版本号: 20181031202122

#### 描述

更新设备

#### 请求信息

请求路径：/device

请求方法：PUT

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|MasterKey|HEAD|String|true||
|deviceId|QUERY|String|true||

#### 请求BODY

##### 数据类型：
json

##### 内容描述：
{
  "deviceName": "string",
  "operator": "string",
  "other": {"autoObserver":0,
            "imsi":"12545154878451"},
  "productId": 0
}

描述：
deviceName: 设备名称，选填
operator: 操作者，必填
other: LWM2M协议必填参数,其他协议不填：{
      autoObserver:0.自动订阅 1.取消自动订阅，订阅指的是平台订阅设备能够上报的object数据  选填;
      imsi:总长度不超过15位，使用0~9的数字，String类型  选填;
}
productId: 产品ID，必填

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

### API名称：CreateDevice   版本号: 20181031202117

#### 描述

增加设备

#### 请求信息

请求路径：/device

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
  "deviceName": "string",
  "deviceSn": "string",
  "imei": "string",
  "operator": "string",
  "other": {"autoObserver":0,
            "imsi":"12545154878451",
            "pskValue":"ADvNWlkcNq9AfKnk"},
  "productId": 0
}

描述：
deviceName: 设备名称，必填
deviceSn: 设备编号，MQTT,T_Link,TCP,HTTP,JT/T808，南向云协议必填
imei: imei号，LWM2M,NB网关协议必填
operator: 操作者，必填
other: LWM2M协议必填参数,其他协议不填：{
      autoObserver:0.自动订阅 1.取消自动订阅，必填;
      imsi:总长度不超过15位，使用0~9的数字，String类型,选填;
      pskValue:由大小写字母加0-9数字组成的16位字符串,选填
}
productId: 产品ID，必填

#### 返回信息

##### 返回参数类型
json

##### 返回结果示例
{
	"code": 0,
	"msg": "ok",
	"result": {
		"deviceId": "89e920fa0eda47a89f04f52a88b17146",
		"deviceName": "test003",
		"tenantId": "300",
		"productId": 10003304,
		"imei": "125658789874565",
		"deviceSn": "",
		"token": "Tyhp7mYXm1k_upy44j32vw8GlKGH8gwvgdayOX27_2E"
	}
}

##### 异常返回示例
{
	"code": 8803,
	"msg": "参数验证失败",
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

### API名称：BindDevice   版本号: 20191024140057

#### 描述

调用方使用IMEI绑定物联网平台中已注册的NB设备，平台更改设备绑定状态为”已绑定”并返回设备ID，设备状态等数据给调用方

#### 请求信息

请求路径：/bindDevice

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
  "imei": "string",
  "productId": 0
}
imei：设备的imei号
productId ：产品id

#### 返回信息

##### 返回参数类型
default

##### 返回结果示例
{
  "code": 0,
  "msg": "ok",
  "result": {
    "imei": "123582465231358",
    "deviceId": "124a2880e8d04b59b89d1a73b48766e1",
    "deviceName": "测试十四师",
    "tenantId": "300",
    "productId": 10012979,
    "deviceStatus": 1,
    "netStatus": 2,
    "bindStatus": 1,
    "createTime": 1571722660000
  }
}

    "imei": 设备IMEI,
    "deviceId": 设备ID,
    "deviceName": 设备名称,
    "tenantId": 租户ID,
    "productId": 产品ID,
    "deviceStatus": 设备状态：0已注册(默认)1已激活 2已注销,
    "netStatus": 设备在线状态，1在线2不在线,
    "bindStatus": 设备绑定状态：0未绑定(初始状态)1已绑定2已解绑,
    "createTime": 设备在平台创建(注册)时间

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

### API名称：UnbindDevice   版本号: 20191024140103

#### 描述

调用方通过设备ID解绑物联网平台中已绑定的NB设备，平台更改设备绑定状态为”已解绑”并取消该设备的订阅

#### 请求信息

请求路径：/unbindDevice

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
  "deviceId":"124a2880e8d04b59b89d1a73b48766e1",
  "productId": 10012979
}
"deviceId":String 设备ID,
"productId":Integer 产品ID

#### 返回信息

##### 返回参数类型
default

##### 返回结果示例
{
  "code": 0,
  "msg": "ok",
  "result": {
    "deviceId": "124a2880e8d04b59b89d1a73b48766e1",
    "deviceStatus": 1,
    "netStatus": 2,
    "bindStatus": 2
  }
}

    "deviceId": 设备ID,
    "deviceStatus": 设备状态 0注册，1激活，2注销,
    "netStatus": 设备在线状态 1在线2不在线,
    "bindStatus": 设备绑定状态 0未绑定（默认）1已绑定2已解绑

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

### API名称：QueryProductInfoByImei   版本号: 20191213161859

#### 描述

通过IMEI号查询产品名称产品ID(只支持LWM2M协议)

#### 请求信息

请求路径：/device/getProductInfoFormApiByImei

请求方法：GET

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|imei|QUERY|String|true||


#### 返回信息

##### 返回参数类型
json

##### 返回结果示例
{
  "code": 0,
  "msg": "ok",
  "result": {
    "productId": 10013527,
    "productName": "lw"
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

### API名称：ListDeviceInfo   版本号: 20210828062945

#### 描述

根据设备ID列表查询设备信息

#### 请求信息

请求路径：/listByDeviceIds

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
    "productId":20002505,
    "deviceIdList":[
        "0001fa98029b4fc0b2ba8dd37c88100a",
        "00044dda3b4945f4ab3c6ca7a9c34f1f",
        "00057badf872490a87a255b183a4c63c",
        "0005a7a6bd1144a7814fd25dc136a6b5",
        "00063f88bdee4ddc8e776a0dfcc74341",
        "00093cb1ed31461b84cc7195e1ebb3e5"
    ]
}

#### 返回信息

##### 返回参数类型
default

##### 返回结果示例
{
    "code": 0,
    "msg": "ok",
    "result": [
        {
            "productId": 20002505,
            "tenantId": "300",
            "deviceId": "0001fa98029b4fc0b2ba8dd37c88100a",
            "deviceSn": null,
            "deviceName": "169999000012646",
            "imei": "169999000012646",
            "imsi": null,
            "firmwareVersion": null,
            "deviceStatus": 1,
            "createTime": 1607077076000,
            "createBy": null,
            "updateTime": null,
            "updateBy": null,
            "netStatus": 2,
            "onlineAt": 1614846046723,
            "offlineAt": 1614846132401,
            "activeTime": 1610014035000,
            "logoutTime": null
        },
        {
            "productId": 20002505,
            "tenantId": "300",
            "deviceId": "00044dda3b4945f4ab3c6ca7a9c34f1f",
            "deviceSn": null,
            "deviceName": "169999000017770",
            "imei": "169999000017770",
            "imsi": null,
            "firmwareVersion": null,
            "deviceStatus": 1,
            "createTime": 1607077076000,
            "createBy": null,
            "updateTime": null,
            "updateBy": null,
            "netStatus": 2,
            "onlineAt": 1610017220285,
            "offlineAt": 1610024319053,
            "activeTime": 1610017220000,
            "logoutTime": null
        },
        {
            "productId": 20002505,
            "tenantId": "300",
            "deviceId": "00057badf872490a87a255b183a4c63c",
            "deviceSn": null,
            "deviceName": "159999000006540",
            "imei": "159999000006540",
            "imsi": null,
            "firmwareVersion": null,
            "deviceStatus": 0,
            "createTime": 1607064272000,
            "createBy": null,
            "updateTime": null,
            "updateBy": null,
            "netStatus": null,
            "onlineAt": null,
            "offlineAt": null,
            "activeTime": null,
            "logoutTime": null
        },
        {
            "productId": 20002505,
            "tenantId": "300",
            "deviceId": "0005a7a6bd1144a7814fd25dc136a6b5",
            "deviceSn": null,
            "deviceName": "169999000001008",
            "imei": "169999000001008",
            "imsi": null,
            "firmwareVersion": null,
            "deviceStatus": 0,
            "createTime": 1607077075000,
            "createBy": null,
            "updateTime": null,
            "updateBy": null,
            "netStatus": null,
            "onlineAt": null,
            "offlineAt": null,
            "activeTime": null,
            "logoutTime": null
        },
        {
            "productId": 20002505,
            "tenantId": "300",
            "deviceId": "00063f88bdee4ddc8e776a0dfcc74341",
            "deviceSn": null,
            "deviceName": "169999000019090",
            "imei": "169999000019090",
            "imsi": null,
            "firmwareVersion": null,
            "deviceStatus": 1,
            "createTime": 1607077076000,
            "createBy": null,
            "updateTime": null,
            "updateBy": null,
            "netStatus": 2,
            "onlineAt": 1610018837905,
            "offlineAt": 1610018916775,
            "activeTime": 1610018837000,
            "logoutTime": null
        },
        {
            "productId": 20002505,
            "tenantId": "300",
            "deviceId": "00093cb1ed31461b84cc7195e1ebb3e5",
            "deviceSn": null,
            "deviceName": "159999000005889",
            "imei": "159999000005889",
            "imsi": null,
            "firmwareVersion": null,
            "deviceStatus": 0,
            "createTime": 1607064272000,
            "createBy": null,
            "updateTime": null,
            "updateBy": null,
            "netStatus": null,
            "onlineAt": null,
            "offlineAt": null,
            "activeTime": null,
            "logoutTime": null
        }
    ],
    "valid": true,
    "ok": true,
    "notOk": false
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

### API名称：DeleteDeviceByPost   版本号: 20211009132842

#### 描述

批量删除设备Post方法

#### 请求信息

请求路径：/deleteDevice

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
    "productId":20002505,
    "deviceIdList":[
        "0001fa98029b4fc0b2ba8dd37c88100a",
        "00044dda3b4945f4ab3c6ca7a9c34f1f",
        "00057badf872490a87a255b183a4c63c",
        "0005a7a6bd1144a7814fd25dc136a6b5",
        "00063f88bdee4ddc8e776a0dfcc74341",
        "00093cb1ed31461b84cc7195e1ebb3e5"
    ]
}

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

### API名称：ListDeviceActiveStatus   版本号: 20211010063104

#### 描述

批量查询设备激活状态

#### 请求信息

请求路径：/listActiveStatus

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
    "productId": 20008341,
    "deviceIdList": [
        "1234567890123456",
        "ABCDEABCDEABCDEF",
        "ABCDEFABCDEFAB11",
        "111111111111111A"
    ]
}

#### 返回信息

##### 返回参数类型
default

##### 返回结果示例
{
    "msg": "ok",
    "result": [
        {
            "deviceId": "1234567890123456",
            "deviceStatus": "已注册"
        },
        {
            "deviceId": "ABCDEABCDEABCDEF",
            "deviceStatus": "已注册"
        },
        {
            "deviceId": "ABCDEFABCDEFAB11",
            "deviceStatus": "已注册"
        },
        {
            "deviceId": "111111111111111A",
            "deviceStatus": "已注册"
        }
    ],
    "code": 0
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


# AEP公共产品管理
## API列表
|API名称 | 安全认证方式 | 签名认证方式 | 描述 |
|:-------|:------|:--------|:--------|
|QueryPublicByPublicProductId|none|hmac-sha1|根据公共产品ID查询公共产品信息|
|QueryPublicByProductId|none|hmac-sha1|根据私有产品ID查询公共产品信息|
|InstantiateProduct|none|hmac-sha1|根据公共产品实例化私有产品|
|QueryAllPublicProductList|none|hmac-sha1|北向api分页查询所有公共产品|
|QueryMyPublicProductList|none|hmac-sha1|北向api分页查询我的公共产品|

## API调用
### 请求地址

|环境 | HTTP请求地址  | HTTPS请求地址 |
|:-------|:------|:--------|
|正式环境|ag-api.ctwing.cn/aep_public_product_management|ag-api.ctwing.cn/aep_public_product_management|

### 公共入参

公共请求参数是指每个接口都需要使用到的请求参数。

|参数名称 | 含义  | 位置 | 描述|
|:-------|:------|:--------|:--------|
|application|应用标识|HEAD|应用的App Key，如果需要进行签名认证则需要填写，例如：dAaFG7DiPt8|
|signature|签名数据|HEAD|将业务数据连同timestamp、application一起签名后的数据，如果需要进行签名认证则需要填写|
|timestamp|UNIX格式时间戳|HEAD|如果需要进行签名认证则需要填写，例如：1515752817580|
|version|API版本号|HEAD|可以指定API版本号访问历史版本|

## API 文档说明
### API名称：QueryPublicByPublicProductId   版本号: 20190507003930

#### 描述

根据公共产品ID查询公共产品信息

#### 请求信息

请求路径：/publicProducts

请求方法：POST

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|

#### 请求BODY

##### 数据类型：
json

##### 内容描述：
{
  "publicProductIds": [
   99000056,99000057
  ]
}
描述：
publicProductIds:公共产品Id集合

#### 返回信息

##### 返回参数类型
json

##### 返回结果示例
{
  "code": 0,
  "msg": "ok",
  "result": [
    {
      "publicProductId": 99000009,
      "publicProductName": "MQTT_add_devicep",
      "vendorId": "10007903",
      "vendorName": "gs",
      "deviceType": "segh",
      "deviceModel": "gsdh",
      "productProtocol": "MQTT协议",
      "productType":10,
      "productTypeValue":"一级分类名称",
      "secondaryType":11,
      "secondaryTypeValue":"二级分类名称",
      "thirdType": 12,
      "thirdTypeValue": "三级分类名称",
      "publicProductImage":"",
      "standardVersion": "V0.1"
    }
  ]
}

##### 异常返回示例
{
 "code":1045,
 "msg":"公共产品查询失败",
 "result":null
}
(8802, "参数解析失败")报错原因：可能是参数格式不正确
(1045, "公共产品查询失败")报错原因：可能是必填参数没有填写

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

### API名称：QueryPublicByProductId   版本号: 20190507004139

#### 描述

根据私有产品ID查询公共产品信息

#### 请求信息

请求路径：/publicProductList

请求方法：POST

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|

#### 请求BODY

##### 数据类型：
json

##### 内容描述：
{
  "productIds": [
    10004101,10004311
  ]
}

描述：
productIds:私有产品Id集合
私有产品Id:
1.一个产品A申请为公共产品B后，该产品A相对公共产品B称为私有产品，产品A的Id为私有产品Id。
2.从公共产品C复用创建产品D，则产品D为公共产品C的私有产品，产品D的Id为私有产品Id。

#### 返回信息

##### 返回参数类型
json

##### 返回结果示例
{
  "code": 0,
  "msg": "ok",
  "result": [
    {
      "productId":10004101,
      "publicProductId": 99000009,
      "publicProductName": "MQTT_add_devicep",
      "vendorId": "10007903",
      "vendorName": "gs",
      "deviceType": "segh",
      "deviceModel": "gsdh",
      "productProtocol": "MQTT协议",
      "productType":10,
      "productTypeValue":"一级分类名称",
      "secondaryType":11,
      "secondaryTypeValue":"二级分类名称",
      "thirdType": 12,
      "thirdTypeValue": "三级分类名称",
      "publicProductImage":"",
      "standardVersion": "V0.1"
    }
  ]
}

##### 异常返回示例
{
 "code":1045,
 "msg":"公共产品查询失败",
 "result":null
}
(8802, "参数解析失败")报错原因：可能是参数格式不正确
(1045, "公共产品查询失败")报错原因：可能是必填参数没有填写

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

### API名称：InstantiateProduct   版本号: 20200801233037

#### 描述

根据公共产品实例化私有产品

#### 请求信息

请求路径：/instantiateProduct

请求方法：POST

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|

#### 请求BODY

##### 数据类型：
json

##### 内容描述：
{
  "publicProductId":10000001
}

描述：
publicProductId:公共产品Id

#### 返回信息

##### 返回参数类型
json

##### 返回结果示例
{
  "code": 0,
  "msg": "ok",
  "result": {
    "publicProductId": 9000000,
    "productId": 10000000,
    "masterKey": "361be7ebc05a46a58fae58ff0f368196"
  }
}

##### 异常返回示例
{
  "code": -1,
  "msg": "参数校验失败",
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

### API名称：QueryAllPublicProductList   版本号: 20200829005548

#### 描述

北向api分页查询所有公共产品

#### 请求信息

请求路径：/allPublicProductList

请求方法：GET

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|searchValue|QUERY|String|false|设备类型、厂商ID、厂商名称|
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
    "pageNum": 2,
    "pageSize": 10,
    "total": 378,
    "list": [
      {
        "publicProductID": 99000992,
        "vendorId": "990000000005038",
        "vendorName": "天翼物联测试",
        "deviceType": "测试",
        "deviceModel": "tywl",
        "productProtocol": "GB28181协议",
        "standardVersion": null
      },
      {
        "publicProductID": 99000990,
        "vendorId": "10049709",
        "vendorName": "superyuan",
        "deviceType": "YUAN",
        "deviceModel": "123456789098766",
        "productProtocol": "LWM2M协议",
        "standardVersion": null
      },
      {
        "publicProductID": 99000988,
        "vendorId": "10081160",
        "vendorName": "asdgsadg",
        "deviceType": "asdgasdg",
        "deviceModel": "sdagasdg",
        "productProtocol": "GB28181协议",
        "standardVersion": null
      },
      {
        "publicProductID": 99000984,
        "vendorId": "10129423",
        "vendorName": "223132",
        "deviceType": "12332",
        "deviceModel": "32322",
        "productProtocol": "MQTT协议",
        "standardVersion": "V0.1"
      },
      {
        "publicProductID": 99000981,
        "vendorId": "10081160",
        "vendorName": "123123",
        "deviceType": "12312",
        "deviceModel": "131232132",
        "productProtocol": "MQTT协议",
        "standardVersion": null
      },
      {
        "publicProductID": 99000980,
        "vendorId": "300",
        "vendorName": "123123",
        "deviceType": "123213",
        "deviceModel": "3232",
        "productProtocol": "LWM2M协议",
        "standardVersion": "V0.1"
      },
      {
        "publicProductID": 99000974,
        "vendorId": "ZNSW",
        "vendorName": "ZNSW",
        "deviceType": "WaterMeter",
        "deviceModel": "CAPDATA",
        "productProtocol": "LWM2M协议",
        "standardVersion": null
      },
      {
        "publicProductID": 99000973,
        "vendorId": "10129423",
        "vendorName": "3243245",
        "deviceType": "868654",
        "deviceModel": "23232",
        "productProtocol": "MQTT协议",
        "standardVersion": "V0.1"
      },
      {
        "publicProductID": 99000972,
        "vendorId": "10129423",
        "vendorName": "76776",
        "deviceType": "989898",
        "deviceModel": "232332",
        "productProtocol": "LWM2M协议",
        "standardVersion": "V0.1"
      },
      {
        "publicProductID": 99000954,
        "vendorId": "10081160",
        "vendorName": "gree",
        "deviceType": "air",
        "deviceModel": "123123",
        "productProtocol": "LWM2M协议",
        "standardVersion": null
      }
    ]
  }
}

##### 异常返回示例
{
  "code": 8800,
  "msg": "内部错误，请联系管理员",
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

### API名称：QueryMyPublicProductList   版本号: 20200829005359

#### 描述

北向api分页查询我的公共产品

#### 请求信息

请求路径：/myPublicProductList

请求方法：GET

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|searchValue|QUERY|String|false|产品名称|
|pageNow|QUERY|Long|false|当前页数|
|pageSize|QUERY|Long|false|每页记录数|
|productIds|QUERY|String|false|私有产品idList|


#### 返回信息

##### 返回参数类型
json

##### 返回结果示例
{
  "code": 0,
  "msg": "ok",
  "result": {
    "pageNum": 5,
    "pageSize": 10,
    "total": 187,
    "list": [
      {
        "productId": 10002042,
        "publicProductID": 304,
        "publicProductName": "lc_eDRX",
        "vendorId": "snowtest00006",
        "vendorName": "snowtest00006",
        "deviceType": "snowtest00006",
        "deviceModel": "snowtest00006",
        "productProtocol": "LWM2M协议",
        "productType": 36,
        "productTypeValue": "空调",
        "secondaryType": 40,
        "secondaryTypeValue": "好的",
        "thirdType": 41,
        "thirdTypeValue": "好的",
        "publicProductImage": null,
        "standardVersion": null
      },
      {
        "productId": 10002024,
        "publicProductID": 306,
        "publicProductName": "lc_lw_json",
        "vendorId": "sdf",
        "vendorName": "dfs",
        "deviceType": "dfs",
        "deviceModel": "sdf",
        "productProtocol": "LWM2M协议",
        "productType": 36,
        "productTypeValue": "空调",
        "secondaryType": 40,
        "secondaryTypeValue": "好的",
        "thirdType": 41,
        "thirdTypeValue": "好的",
        "publicProductImage": null,
        "standardVersion": null
      },
      {
        "productId": 10002060,
        "publicProductID": 307,
        "publicProductName": "lw-001",
        "vendorId": "new",
        "vendorName": "new",
        "deviceType": "new",
        "deviceModel": "new",
        "productProtocol": "LWM2M协议",
        "productType": 110,
        "productTypeValue": "一级分类名称测试5",
        "secondaryType": 112,
        "secondaryTypeValue": "二级分类名称测试3",
        "thirdType": 120,
        "thirdTypeValue": "三级分类测试内容5",
        "publicProductImage": null,
        "standardVersion": null
      },
      {
        "productId": 10000389,
        "publicProductID": 99000089,
        "publicProductName": "tup",
        "vendorId": "300",
        "vendorName": "test1",
        "deviceType": "test2",
        "deviceModel": "test3",
        "productProtocol": "NB网关",
        "productType": 1,
        "productTypeValue": "家电",
        "secondaryType": 2,
        "secondaryTypeValue": "测试",
        "thirdType": 13,
        "thirdTypeValue": "好测试",
        "publicProductImage": null,
        "standardVersion": null
      },
      {
        "productId": 10004507,
        "publicProductID": 99000097,
        "publicProductName": "tuptuptup",
        "vendorId": "300",
        "vendorName": "venderid",
        "deviceType": "verdertype",
        "deviceModel": "verderno",
        "productProtocol": "NB网关",
        "productType": 1,
        "productTypeValue": "家电",
        "secondaryType": 2,
        "secondaryTypeValue": "测试",
        "thirdType": 13,
        "thirdTypeValue": "好测试",
        "publicProductImage": null,
        "standardVersion": null
      },
      {
        "productId": 10004507,
        "publicProductID": 99000098,
        "publicProductName": "#@￥&%￥#&%￥#1",
        "vendorId": "300",
        "vendorName": "vendername",
        "deviceType": "vendertype",
        "deviceModel": "venderno",
        "productProtocol": "NB网关",
        "productType": 1,
        "productTypeValue": "家电",
        "secondaryType": 2,
        "secondaryTypeValue": "测试",
        "thirdType": 13,
        "thirdTypeValue": "好测试",
        "publicProductImage": "http://aep-dm-dmfileserver:8082/file/productPic//webctdfs/public_file?tenantId=300&fileName=1552643063017204.png&fileType=picture",
        "standardVersion": null
      },
      {
        "productId": 10004590,
        "publicProductID": 99000115,
        "publicProductName": "http",
        "vendorId": "300",
        "vendorName": "http申请公共产品",
        "deviceType": "test0001",
        "deviceModel": "test0001",
        "productProtocol": "HTTP协议",
        "productType": 133,
        "productTypeValue": "智能停车",
        "secondaryType": 134,
        "secondaryTypeValue": "我snowtestlevel2",
        "thirdType": 135,
        "thirdTypeValue": "我snowtestlevel3",
        "publicProductImage": "http://aep-dm-dmfileserver:8082/file/productPic//webctdfs/public_file?tenantId=300&fileName=1552878426197356.png&fileType=picture",
        "standardVersion": null
      },
      {
        "productId": 10004590,
        "publicProductID": 99000117,
        "publicProductName": "http snow",
        "vendorId": "300",
        "vendorName": "asdf",
        "deviceType": "asdgg",
        "deviceModel": "adsggd",
        "productProtocol": "HTTP协议",
        "productType": 133,
        "productTypeValue": "智能停车",
        "secondaryType": 134,
        "secondaryTypeValue": "我snowtestlevel2",
        "thirdType": 135,
        "thirdTypeValue": "我snowtestlevel3",
        "publicProductImage": "http://aep-dm-dmfileserver:8082/file/productPic//webctdfs/public_file?tenantId=300&fileName=1552879157998906.png&fileType=picture",
        "standardVersion": null
      },
      {
        "productId": 10001305,
        "publicProductID": 99000119,
        "publicProductName": "lq_nb_json",
        "vendorId": "300",
        "vendorName": "nb",
        "deviceType": "nb",
        "deviceModel": "nb",
        "productProtocol": "NB网关",
        "productType": 1,
        "productTypeValue": "家电",
        "secondaryType": 9,
        "secondaryTypeValue": "白色家电",
        "thirdType": 10,
        "thirdTypeValue": "空调",
        "publicProductImage": null,
        "standardVersion": null
      },
      {
        "productId": 10004574,
        "publicProductID": 99000120,
        "publicProductName": "tcp",
        "vendorId": "300",
        "vendorName": "tcp",
        "deviceType": "tcp",
        "deviceModel": "tcp",
        "productProtocol": "TCP协议",
        "productType": 130,
        "productTypeValue": "边缘计算",
        "secondaryType": 131,
        "secondaryTypeValue": "附近的萨科附近的斯卡拉附近的卡拉",
        "thirdType": 132,
        "thirdTypeValue": "附近的萨科附近的斯卡拉附近的卡拉",
        "publicProductImage": null,
        "standardVersion": null
      }
    ]
  }
}

##### 异常返回示例
{
  "code": 8800,
  "msg": "内部错误，请联系管理员",
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


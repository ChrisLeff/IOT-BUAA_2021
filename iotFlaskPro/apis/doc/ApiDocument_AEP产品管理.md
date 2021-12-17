# AEP产品管理
## API列表
|API名称 | 安全认证方式 | 签名认证方式 | 描述 |
|:-------|:------|:--------|:--------|
|QueryProduct|none|hmac-sha1|支持第三方应用根据产品ID查询产品数据，注意本接口只能查询单个产品数据|
|QueryProductList|none|hmac-sha1|批量查询产品信息|
|DeleteProduct|none|hmac-sha1|支持第三方应用删除产品数据，如果产品下有设备数据，则无法删除产品|
|CreateProduct|none|hmac-sha1|添加产品(产品为设备直连+非NB网关协议)|
|UpdateProduct|none|hmac-sha1|更新产品(产品为设备直连+非NB网关协议)|

## API调用
### 请求地址

|环境 | HTTP请求地址  | HTTPS请求地址 |
|:-------|:------|:--------|
|正式环境|ag-api.ctwing.cn/aep_product_management|ag-api.ctwing.cn/aep_product_management|

### 公共入参

公共请求参数是指每个接口都需要使用到的请求参数。

|参数名称 | 含义  | 位置 | 描述|
|:-------|:------|:--------|:--------|
|application|应用标识|HEAD|应用的App Key，如果需要进行签名认证则需要填写，例如：dAaFG7DiPt8|
|signature|签名数据|HEAD|将业务数据连同timestamp、application一起签名后的数据，如果需要进行签名认证则需要填写|
|timestamp|UNIX格式时间戳|HEAD|如果需要进行签名认证则需要填写，例如：1515752817580|
|version|API版本号|HEAD|可以指定API版本号访问历史版本|

## API 文档说明
### API名称：QueryProduct   版本号: 20181031202055

#### 描述

支持第三方应用根据产品ID查询产品数据，注意本接口只能查询单个产品数据

#### 请求信息

请求路径：/product

请求方法：GET

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|productId|QUERY|Long|true||


#### 返回信息

##### 返回参数类型
json

##### 返回结果示例
{
  "code": 0,
  "msg": "ok",
  "result": {
    "productId": 10012761,
    "productName": "测试创建产品",
    "tenantId": "300",
    "productDesc": "创建产品",
    "productType": 10024,
    "secondaryType": 10025,
    "thirdType": 10026,
    "productProtocol": 1,
    "authType": 1,
    "payloadFormat": 1,
    "createTime": 1571402267678,
    "updateTime": 1571402268678,
    "networkType": 4,
    "endpointFormat": 1,
    "powerModel": 1,
    "apiKey": "67141cddbf2e4f62a2ff458f1dd9ba8e",
    "onlineDeviceCount": 0,
    "deviceCount": 3,
    "productTypeValue": "家电",
    "secondaryTypeValue": "测试",
    "thirdTypeValue": "测试tanglv",
    "rootCert": 1,
    "createBy": "user",
    "updateBy": "user",
     "accessType": 2,
     "nodeType": 1,
     "tupIsThrough": 1,
     "dataEncryption": 5,
     "lwm2mEdrxTime": 25.2
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

### API名称：QueryProductList   版本号: 20190507004824

#### 描述

批量查询产品信息

#### 请求信息

请求路径：/products

请求方法：GET

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|searchValue|QUERY|String|false|产品id或者产品名称|
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
        "list": [
            {
                "accessType": 2,
                "apiKey": "b0910dc269db472fb45823292e706f3e",
                "authType": 1,
                "createBy": "user",
                "createTime": 1535942487000,
                "dataEncryption": 5,
                "deviceCount": 4,
                "endpointFormat": 1,
                "lwm2mEdrxTime": 25.2,
                "networkType": 3,
                "nodeType": 1,
                "onlineDeviceCount": 0,
                "payloadFormat": 2,
                "powerModel": 1,
                "productDesc": "",
                "productId": 307,
                "productName": "tup-test-zcj",
                "productProtocol": 4,
                "productType": 1,
                "productTypeValue": "家电",
                "rootCert": "",
                "secondaryType": 2,
                "secondaryTypeValue": "测试",
                "tenantId": "10007905",
                "thirdType": 13,
                "thirdTypeValue": "测试tanglv",
                "tupIsThrough": 1,
                "updateBy": "user",
                "updateTime": 1535943389000
            }
        ],
        "pageNum": 1,
        "pageSize": 30,
        "total": 8
    }
}

##### 异常返回示例
{
 "code":8800,
 "msg":"内部错误，请联系管理员",
 "result":null
}
(8803, "参数验证失败")报错原因：可能是产品id为空或者未能获取到租户id或者删除操作失败,
(8800, "内部错误，请联系管理员")报错原因：可能缺少必要参数,
(1002, "此产品不存在")报错原因：不存在此产品id对应的产品信息,

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

### API名称：DeleteProduct   版本号: 20181031202029

#### 描述

支持第三方应用删除产品数据，如果产品下有设备数据，则无法删除产品

#### 请求信息

请求路径：/product

请求方法：DELETE

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|MasterKey|HEAD|String|true|MasterKey在该设备所属产品的概况中可以查看|
|productId|QUERY|Long|true||


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
 "code":8800,
 "msg":"内部错误，请联系管理员",
 "result":null
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

### API名称：CreateProduct   版本号: 20191018204154

#### 描述

添加产品(产品为设备直连+非NB网关协议)

#### 请求信息

请求路径：/product

请求方法：POST

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|

#### 请求BODY

##### 数据类型：
json

##### 内容描述：
{
  "accessType": 1,
  "authType": 0,
  "dataEncryption": 0,
  "deviceModel": "string",
  "encryptionType": 0,
  "endpointFormat": 0,
  "lwm2mEdrxTime": null,
  "manufacturerId": "string",
  "networkType": 0,
  "nodeType": 1,
  "payloadFormat": 0,
  "powerModel": 0,
  "productDesc": "string",
  "productName": "string",
  "productProtocol": 0,
  "productType": "string",
  "secondaryType": "string",
  "thirdType": "string",
  "tupIsThrough": 0,
  "tupDeviceModel": "string"
}
描述：
productName：产品名称（必填）：产品名称最多 64 个字符，产品名称必须包含数字或字母或汉字
，产品名称租户内不能重复
productType：产品分类（必填）
secondaryType：二级分类（必填）
thirdType：三级分类（必填）
nodeType：节点类型（必填）：1.设备 ，2.网关
accessType：接入类型（必填）: 1.设备直连，2.网关接入，3.南向云接入（只支持1）
networkType：网络类型（必填）:1.WIFI,2.移动蜂窝数据3.NB-IoT,4.以太网,5.蓝牙,6.ZigBee（只支持1/2/3/4）
productProtocol：产品协议（必填）：只支持 1.T-LINK协议 2.MQTT协议 3.LWM2M协议 5.HTTP协议 6.JT/T808 7.TCP协议 10.网关MQTT协议
authType：认证方式 1:特征串认证,2:SM9认证,3:证书认证,4:IMEI认证，5:SIMID认证，6:SM2认证，7:IPV6标识认证
注：SM9认证、SIMID认证需要订购
    T-LINK协议支持：1:特征串认证,2:SM9认证,3:证书认证,5:SIMID认证
    MQTT协议支持：1:特征串认证,2:SM9认证,5:SIMID认证,6:SM2认证
    LWM2M协议支持：2:SM9认证,4:IMEI认证，5:SIMID认证，6:SM2认证，7:IPV6标识认证
    HTTP协议、TCP协议支持：1:特征串认证
    JT/T808支持：无
    网关MQTT协议支持：1:特征串认证
payloadFormat：消息格式 1:json，2:紧凑二进制
dataEncryption：数据加密方式 1:sm1,2:sm2,3:sm4,4:dtls,5:明文（只支持MQTT/LWM2M）
encryptionType：安全类型(只支持MQTT,TCP协议) 0:一机一密，1:一型一密
tupIsThrough：是否透传：0.透传，1不透传（JT/T808，tcp协议，只有透传，消息格式必须只能传null）
deviceModel：JT/T808协议 设备型号
manufacturerId：JT/T808协议 制造商ID
endpointFormat:Endpoint格式（LWM2M协议必填）:1.IMEI2.URN:IMEI:###############3.URN:IMEI-IMSI: ###############-############### 4.URN:IMEI+SM9
注：认证方式为SM9认证时，Endpoint格式只能为4
    认证方式为IMEI认证，SIMID认证，SM2认证时，Endpoint格式为1/2/3
    认证方式为IPV6标识认证时，Endpoint格式为3
powerModel：省电模式（LWM2M协议必填）：1.PSM 2.DRX 3.eDRX
lwm2mEdrxTime:eDRX模式时间窗(LWM2M协议,当省电模式为3时,必填):20 ～ 10485.76 间的值,精确到小数点后两位
productDesc：产品描述（选填）：产品描述最多100个字符
tupDeviceModel:设备型号，选填，设备直连并且非JT/T808协议产品必填

#### 返回信息

##### 返回参数类型
json

##### 返回结果示例
{
  "code": 0,
  "msg": "ok",
  "result": {
    "productId": 10012761,
    "productName": "测试创建产品",
    "tenantId": "300",
    "productDesc": "创建产品",
    "productType": 10024,
    "secondaryType": 10025,
    "thirdType": 10026,
    "productProtocol": 1,
    "authType": 1,
    "payloadFormat": 1,
    "createTime": 1571402267678,
    "updateTime": 1571402268678,
    "networkType": 4,
    "endpointFormat": 1,
    "powerModel": 1,
    "apiKey": "67141cddbf2e4f62a2ff458f1dd9ba8e",
    "onlineDeviceCount": 0,
    "deviceCount": 3,
    "productTypeValue": "家电",
    "secondaryTypeValue": "测试",
    "thirdTypeValue": "测试tanglv",
    "rootCert": 1,
    "createBy": "user",
    "updateBy": "user",
     "accessType": 2,
     "nodeType": 1,
     "tupIsThrough": 1,
     "dataEncryption": 5,
     "lwm2mEdrxTime": 15.2
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

### API名称：UpdateProduct   版本号: 20191018204806

#### 描述

更新产品(产品为设备直连+非NB网关协议)

#### 请求信息

请求路径：/product

请求方法：PUT

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|

#### 请求BODY

##### 数据类型：
json

##### 内容描述：
{
  "endpointFormat": null,
  "powerModel": null,
  "productDesc": "string",
  "productId": 0,
  "productName": "string",
  "lwm2mEdrxTime": null
}
描述：
productId: 产品ID，必填
productName：产品名称，产品名称租户内不能重复，必填
productDesc：产品描述，选填
endpointFormat：endpoint类型(Lwm2m协议必填) 1.IMEI 2.URN:IMEI:############### 3.URN:IMEI-IMSI: ###############-############### 4.URN:IMEI+SM9
注：认证方式为SM9认证时，endpoint类型为4
    认证方式为IMEI认证、sm2认证时，endpoint类型为1、2、3
powerModel：省电模式(Lwm2m协议必填) 1.PSM 2.DRX 3.eDRX
lwm2mEdrxTime：eDRX模式时间窗(LWM2M协议,当省电模式为3时,必填):20 ～ 10485.76 间的值,精确到小数点后两位

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


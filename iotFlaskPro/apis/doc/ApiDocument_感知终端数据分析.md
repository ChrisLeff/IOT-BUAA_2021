# 感知终端数据分析
## API列表
|API名称 | 安全认证方式 | 签名认证方式 | 描述 |
|:-------|:------|:--------|:--------|
|QueryTenantDeviceCount|none|hmac-sha1|查询租户下设备注册总数、设备激活总数|
|QueryTenantDeviceTrend|none|hmac-sha1|查询租户下设备历史趋势|
|QueryTenantDeviceActiveCount|none|hmac-sha1|查询租户下设备月活跃数|

## API调用
### 请求地址

|环境 | HTTP请求地址  | HTTPS请求地址 |
|:-------|:------|:--------|
|正式环境|ag-api.ctwing.cn/tenant_device_statistics|ag-api.ctwing.cn/tenant_device_statistics|

### 公共入参

公共请求参数是指每个接口都需要使用到的请求参数。

|参数名称 | 含义  | 位置 | 描述|
|:-------|:------|:--------|:--------|
|application|应用标识|HEAD|应用的App Key，如果需要进行签名认证则需要填写，例如：dAaFG7DiPt8|
|signature|签名数据|HEAD|将业务数据连同timestamp、application一起签名后的数据，如果需要进行签名认证则需要填写|
|timestamp|UNIX格式时间戳|HEAD|如果需要进行签名认证则需要填写，例如：1515752817580|
|version|API版本号|HEAD|可以指定API版本号访问历史版本|

## API 文档说明
### API名称：QueryTenantDeviceCount   版本号: 20201225122555

#### 描述

查询租户下设备注册总数、设备激活总数

#### 请求信息

请求路径：/queryTenantDeviceCount

请求方法：GET

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|


#### 返回信息

##### 返回参数类型
default

##### 返回结果示例
{"code":0,"msg":"ok","result":{"tenantId":null,"terCount":0,"activeCount":0,"onlineCount":0,"offlineCount":0,"onlineRate":0,"activeRate":0}}

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

### API名称：QueryTenantDeviceTrend   版本号: 20201225122550

#### 描述

查询租户下设备历史趋势

#### 请求信息

请求路径：/queryTenantDeviceTrend

请求方法：GET

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|dateType|QUERY|String|true|时间类型：d:天；m:月|
|type|QUERY|String|true|数据类型：1：设备总数量，激活数，活跃数；3：设备活跃数，活跃率|


#### 返回信息

##### 返回参数类型
default

##### 返回结果示例
{"code":0,"msg":"ok","result":[{"region":null,"id":0,"tenantId":null,"terCount":null,"activeCount":null,"activeRate":0.0,"activeDeviceCount":null,"activeDeviceRate":0.0,"monthlyIncreaseCount":null,"syncDate":"2020/01","dateType":null,"createTime":null,"updateTime":null},{"region":null,"id":0,"tenantId":null,"terCount":null,"activeCount":null,"activeRate":0.0,"activeDeviceCount":null,"activeDeviceRate":0.0,"monthlyIncreaseCount":null,"syncDate":"2020/02","dateType":null,"createTime":null,"updateTime":null},{"region":null,"id":0,"tenantId":null,"terCount":null,"activeCount":null,"activeRate":0.0,"activeDeviceCount":null,"activeDeviceRate":0.0,"monthlyIncreaseCount":null,"syncDate":"2020/03","dateType":null,"createTime":null,"updateTime":null},{"region":null,"id":0,"tenantId":null,"terCount":null,"activeCount":null,"activeRate":0.0,"activeDeviceCount":null,"activeDeviceRate":0.0,"monthlyIncreaseCount":null,"syncDate":"2020/04","dateType":null,"createTime":null,"updateTime":null},{"region":null,"id":0,"tenantId":null,"terCount":null,"activeCount":null,"activeRate":0.0,"activeDeviceCount":null,"activeDeviceRate":0.0,"monthlyIncreaseCount":null,"syncDate":"2020/05","dateType":null,"createTime":null,"updateTime":null},{"region":null,"id":0,"tenantId":null,"terCount":null,"activeCount":null,"activeRate":0.0,"activeDeviceCount":null,"activeDeviceRate":0.0,"monthlyIncreaseCount":null,"syncDate":"2020/06","dateType":null,"createTime":null,"updateTime":null},{"region":null,"id":0,"tenantId":null,"terCount":null,"activeCount":null,"activeRate":0.0,"activeDeviceCount":null,"activeDeviceRate":0.0,"monthlyIncreaseCount":null,"syncDate":"2020/07","dateType":null,"createTime":null,"updateTime":null},{"region":null,"id":0,"tenantId":null,"terCount":null,"activeCount":null,"activeRate":0.0,"activeDeviceCount":null,"activeDeviceRate":0.0,"monthlyIncreaseCount":null,"syncDate":"2020/08","dateType":null,"createTime":null,"updateTime":null},{"region":null,"id":0,"tenantId":null,"terCount":null,"activeCount":null,"activeRate":0.0,"activeDeviceCount":null,"activeDeviceRate":0.0,"monthlyIncreaseCount":null,"syncDate":"2020/09","dateType":null,"createTime":null,"updateTime":null},{"region":null,"id":0,"tenantId":null,"terCount":null,"activeCount":null,"activeRate":0.0,"activeDeviceCount":null,"activeDeviceRate":0.0,"monthlyIncreaseCount":null,"syncDate":"2020/10","dateType":null,"createTime":null,"updateTime":null},{"region":null,"id":0,"tenantId":null,"terCount":1023,"activeCount":192,"activeRate":0.0,"activeDeviceCount":0,"activeDeviceRate":0.0,"monthlyIncreaseCount":null,"syncDate":"2020/11","dateType":null,"createTime":null,"updateTime":null},{"region":null,"id":0,"tenantId":null,"terCount":null,"activeCount":null,"activeRate":0.0,"activeDeviceCount":null,"activeDeviceRate":0.0,"monthlyIncreaseCount":null,"syncDate":"2020/12","dateType":null,"createTime":null,"updateTime":null}]}

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

### API名称：QueryTenantDeviceActiveCount   版本号: 20201225122558

#### 描述

查询租户下设备月活跃数

#### 请求信息

请求路径：/queryTenantDeviceActiveCount

请求方法：GET

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|


#### 返回信息

##### 返回参数类型
default

##### 返回结果示例
{"code":0,"msg":"ok","result":{"monthlyActiveRate":0,"monthlyActiveCount":0,"issuedCount":0,"issuedGrowthRate":0,"monthlyIncrease":0,"reportGrowthRate":0,"reportCount":0}}

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


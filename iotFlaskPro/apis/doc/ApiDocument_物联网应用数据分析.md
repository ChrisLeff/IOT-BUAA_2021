# 物联网应用数据分析
## API列表
|API名称 | 安全认证方式 | 签名认证方式 | 描述 |
|:-------|:------|:--------|:--------|
|QueryTenantApiMonthlyCount|none|hmac-sha1|查询租户Api月调用数与消息月推送数|
|QueryTenantAppCount|none|hmac-sha1|查询租户下应用总数|
|QueryTenantApiTrend|none|hmac-sha1|查询租户Api历史趋势|

## API调用
### 请求地址

|环境 | HTTP请求地址  | HTTPS请求地址 |
|:-------|:------|:--------|
|正式环境|ag-api.ctwing.cn/tenant_app_statistics|ag-api.ctwing.cn/tenant_app_statistics|

### 公共入参

公共请求参数是指每个接口都需要使用到的请求参数。

|参数名称 | 含义  | 位置 | 描述|
|:-------|:------|:--------|:--------|
|application|应用标识|HEAD|应用的App Key，如果需要进行签名认证则需要填写，例如：dAaFG7DiPt8|
|signature|签名数据|HEAD|将业务数据连同timestamp、application一起签名后的数据，如果需要进行签名认证则需要填写|
|timestamp|UNIX格式时间戳|HEAD|如果需要进行签名认证则需要填写，例如：1515752817580|
|version|API版本号|HEAD|可以指定API版本号访问历史版本|

## API 文档说明
### API名称：QueryTenantApiMonthlyCount   版本号: 20201225122609

#### 描述

查询租户Api月调用数与消息月推送数

#### 请求信息

请求路径：/queryTenantApiMonthlyCount

请求方法：GET

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|


#### 返回信息

##### 返回参数类型
default

##### 返回结果示例
{"code":0,"msg":"ok","result":{"apiTotalCount":0,"apiGrowthRate":null,"msgPushTotalCount":2,"msgPushGrowthRate":-0.9904,"msgRuleTotalCount":0,"msgRuleGrowthRate":null}}

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

### API名称：QueryTenantAppCount   版本号: 20201225122611

#### 描述

查询租户下应用总数

#### 请求信息

请求路径：/queryTenantAppCount

请求方法：GET

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|


#### 返回信息

##### 返回参数类型
default

##### 返回结果示例
{"code":0,"msg":"ok","result":{"ruleEngineTotalCount":"0","appTotalCount":"0"}}

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

### API名称：QueryTenantApiTrend   版本号: 20201225122606

#### 描述

查询租户Api历史趋势

#### 请求信息

请求路径：/queryTenantApiTrend

请求方法：GET

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|dateType|QUERY|String|true|日期格式 m：月  d：日|
|dataType|QUERY|String|true|数据格式 1：api调用量分析|


#### 返回信息

##### 返回参数类型
default

##### 返回结果示例
{"code":0,"msg":"ok","result":[{"region":null,"id":null,"tenantId":null,"totalCount":null,"successCount":null,"failureCount":null,"successRate":null,"averageDelay":null,"growthRate":null,"syncDate":"2020/11/15","dateType":null},{"region":null,"id":null,"tenantId":null,"totalCount":null,"successCount":null,"failureCount":null,"successRate":null,"averageDelay":null,"growthRate":null,"syncDate":"2020/11/16","dateType":null},{"region":null,"id":null,"tenantId":null,"totalCount":9,"successCount":9,"failureCount":0,"successRate":null,"averageDelay":null,"growthRate":null,"syncDate":"2020/11/17","dateType":null},{"region":null,"id":null,"tenantId":null,"totalCount":null,"successCount":null,"failureCount":null,"successRate":null,"averageDelay":null,"growthRate":null,"syncDate":"2020/11/18","dateType":null},{"region":null,"id":null,"tenantId":null,"totalCount":2,"successCount":2,"failureCount":0,"successRate":null,"averageDelay":null,"growthRate":null,"syncDate":"2020/11/19","dateType":null},{"region":null,"id":null,"tenantId":null,"totalCount":null,"successCount":null,"failureCount":null,"successRate":null,"averageDelay":null,"growthRate":null,"syncDate":"2020/11/20","dateType":null},{"region":null,"id":null,"tenantId":null,"totalCount":null,"successCount":null,"failureCount":null,"successRate":null,"averageDelay":null,"growthRate":null,"syncDate":"2020/11/21","dateType":null},{"region":null,"id":null,"tenantId":null,"totalCount":null,"successCount":null,"failureCount":null,"successRate":null,"averageDelay":null,"growthRate":null,"syncDate":"2020/11/22","dateType":null},{"region":null,"id":null,"tenantId":null,"totalCount":null,"successCount":null,"failureCount":null,"successRate":null,"averageDelay":null,"growthRate":null,"syncDate":"2020/11/23","dateType":null},{"region":null,"id":null,"tenantId":null,"totalCount":null,"successCount":null,"failureCount":null,"successRate":null,"averageDelay":null,"growthRate":null,"syncDate":"2020/11/24","dateType":null},{"region":null,"id":null,"tenantId":null,"totalCount":null,"successCount":null,"failureCount":null,"successRate":null,"averageDelay":null,"growthRate":null,"syncDate":"2020/11/25","dateType":null},{"region":null,"id":null,"tenantId":null,"totalCount":null,"successCount":null,"failureCount":null,"successRate":null,"averageDelay":null,"growthRate":null,"syncDate":"2020/11/26","dateType":null},{"region":null,"id":null,"tenantId":null,"totalCount":null,"successCount":null,"failureCount":null,"successRate":null,"averageDelay":null,"growthRate":null,"syncDate":"2020/11/27","dateType":null},{"region":null,"id":null,"tenantId":null,"totalCount":null,"successCount":null,"failureCount":null,"successRate":null,"averageDelay":null,"growthRate":null,"syncDate":"2020/11/28","dateType":null},{"region":null,"id":null,"tenantId":null,"totalCount":null,"successCount":null,"failureCount":null,"successRate":null,"averageDelay":null,"growthRate":null,"syncDate":"2020/11/29","dateType":null},{"region":null,"id":null,"tenantId":null,"totalCount":null,"successCount":null,"failureCount":null,"successRate":null,"averageDelay":null,"growthRate":null,"syncDate":"2020/11/30","dateType":null},{"region":null,"id":null,"tenantId":null,"totalCount":null,"successCount":null,"failureCount":null,"successRate":null,"averageDelay":null,"growthRate":null,"syncDate":"2020/12/01","dateType":null},{"region":null,"id":null,"tenantId":null,"totalCount":null,"successCount":null,"failureCount":null,"successRate":null,"averageDelay":null,"growthRate":null,"syncDate":"2020/12/02","dateType":null},{"region":null,"id":null,"tenantId":null,"totalCount":null,"successCount":null,"failureCount":null,"successRate":null,"averageDelay":null,"growthRate":null,"syncDate":"2020/12/03","dateType":null},{"region":null,"id":null,"tenantId":null,"totalCount":null,"successCount":null,"failureCount":null,"successRate":null,"averageDelay":null,"growthRate":null,"syncDate":"2020/12/04","dateType":null},{"region":null,"id":null,"tenantId":null,"totalCount":null,"successCount":null,"failureCount":null,"successRate":null,"averageDelay":null,"growthRate":null,"syncDate":"2020/12/05","dateType":null},{"region":null,"id":null,"tenantId":null,"totalCount":null,"successCount":null,"failureCount":null,"successRate":null,"averageDelay":null,"growthRate":null,"syncDate":"2020/12/06","dateType":null},{"region":null,"id":null,"tenantId":null,"totalCount":null,"successCount":null,"failureCount":null,"successRate":null,"averageDelay":null,"growthRate":null,"syncDate":"2020/12/07","dateType":null},{"region":null,"id":null,"tenantId":null,"totalCount":null,"successCount":null,"failureCount":null,"successRate":null,"averageDelay":null,"growthRate":null,"syncDate":"2020/12/08","dateType":null},{"region":null,"id":null,"tenantId":null,"totalCount":null,"successCount":null,"failureCount":null,"successRate":null,"averageDelay":null,"growthRate":null,"syncDate":"2020/12/09","dateType":null},{"region":null,"id":null,"tenantId":null,"totalCount":null,"successCount":null,"failureCount":null,"successRate":null,"averageDelay":null,"growthRate":null,"syncDate":"2020/12/10","dateType":null},{"region":null,"id":null,"tenantId":null,"totalCount":null,"successCount":null,"failureCount":null,"successRate":null,"averageDelay":null,"growthRate":null,"syncDate":"2020/12/11","dateType":null},{"region":null,"id":null,"tenantId":null,"totalCount":null,"successCount":null,"failureCount":null,"successRate":null,"averageDelay":null,"growthRate":null,"syncDate":"2020/12/12","dateType":null},{"region":null,"id":null,"tenantId":null,"totalCount":null,"successCount":null,"failureCount":null,"successRate":null,"averageDelay":null,"growthRate":null,"syncDate":"2020/12/13","dateType":null},{"region":null,"id":null,"tenantId":null,"totalCount":null,"successCount":null,"failureCount":null,"successRate":null,"averageDelay":null,"growthRate":null,"syncDate":"2020/12/14","dateType":null}]}

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


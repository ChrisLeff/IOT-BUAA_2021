# AEP规则引擎
## API列表
|API名称 | 安全认证方式 | 签名认证方式 | 描述 |
|:-------|:------|:--------|:--------|
|saasCreateRule|none|hmac-sha1|SAAS规则引擎创建|
|saasQueryRule|none|hmac-sha1|SAAS规则查询|
|saasUpdateRule|none|hmac-sha1|更新SAAS规则引擎|
|saasDeleteRuleEngine|none|hmac-sha1|SAAS规则删除|
|CreateRule|none|hmac-sha1|创建规则|
|UpdateRule|none|hmac-sha1|更新规则，规则状态为停止时才可操作|
|DeleteRule|none|hmac-sha1|删除规则，只有规则状态为停止时才可操作|
|GetRules|none|hmac-sha1|获取规则|
|GetRuleRunStatus|none|hmac-sha1|获取规则运行状态|
|UpdateRuleRunStatus|none|hmac-sha1|修改规则运行状态|
|CreateForward|none|hmac-sha1|创建转发规则，只有规则状态为停止时才可操作|
|UpdateForward|none|hmac-sha1|更新转发规则，只有规则状态为停止时才可操作|
|DeleteForward|none|hmac-sha1|删除转发规则，只有规则状态为停止时才可操作|
|GetForwards|none|hmac-sha1|获取转发规则|
|GetWarns|none|hmac-sha1|分页获取告警规则|
|DeleteWarn|none|hmac-sha1|删除告警规则，只有规则状态为停止时才可操作|
|UpdateWarn|none|hmac-sha1|更新告警规则，只有规则状态为停止时才可操作|
|CreateWarn|none|hmac-sha1|创建告警规则，只有规则状态为停止时才可操作|
|CreateAction|none|hmac-sha1|创建动作规则，只有规则状态为停止时才可操作|
|UpdateAction|none|hmac-sha1|更新动作规则，只有规则状态为停止时才可操作|
|DeleteAction|none|hmac-sha1|删除动作规则，只有规则状态为停止时才可操作|
|GetActions|none|hmac-sha1|分页获取动作规则|
|GetWarnUsers|none|hmac-sha1|分页获取告警用户信息规则|

## API调用
### 请求地址

|环境 | HTTP请求地址  | HTTPS请求地址 |
|:-------|:------|:--------|
|正式环境|ag-api.ctwing.cn/aep_rule_engine|ag-api.ctwing.cn/aep_rule_engine|

### 公共入参

公共请求参数是指每个接口都需要使用到的请求参数。

|参数名称 | 含义  | 位置 | 描述|
|:-------|:------|:--------|:--------|
|application|应用标识|HEAD|应用的App Key，如果需要进行签名认证则需要填写，例如：dAaFG7DiPt8|
|signature|签名数据|HEAD|将业务数据连同timestamp、application一起签名后的数据，如果需要进行签名认证则需要填写|
|timestamp|UNIX格式时间戳|HEAD|如果需要进行签名认证则需要填写，例如：1515752817580|
|version|API版本号|HEAD|可以指定API版本号访问历史版本|

## API 文档说明
### API名称：saasCreateRule   版本号: 20200111000503

#### 描述

SAAS规则引擎创建

#### 请求信息

请求路径：/api/v2/rule/sass/createRule

请求方法：POST

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|

#### 请求BODY

##### 数据类型：
json

##### 内容描述：
{
  "dataLevel": 0,
  "description": "测试add",
  "ruleForwardInfos": [
    {
      "forwardConfig": {
        "content": "{\"test\":\"%a%\"}",
        "url": "http://127.0.0.1:9090/test"
      },
      "forwardType": "HTTP",
      "operatorType": "01"
    }
  ],
  "ruleStreams": [
    {
      "productId": "10003561",
	"deviceId":"",
	"deviceGroupId":null,
      	"ruleStr": "select aa,cc from ruleengine_10106316_10003561 where aa = 1",
	"dataLevel":0
    }
  ],
  "ruleType": "1000",
  "userId": "ljtest"
}
  ruleId:修改、删除时必填，新增规则时，此参数为空

描述:
dataLevel:规则数据类型:0-产品级别;1-设备级别；2-设备分组级别[*必填]；组合规则只支持设备级别。
ruleType:规则类型；1000：简单规则，2000：组合规则
userId：用户ID[*必填]
description:规则的描述信息, 长度不超过160位的字符串[*必填]
ruleStreams：规则信息[*必填][{   
     ruleStr:规则内容，即sql。不能包含特殊字符*，修改、新增时必填,
		具体详看下面SQL描述   
	 productId:产品ID[*必填]		
	 deviceId：设备ID,可选;当dataLevel为1时则必填。
	 deviceGroupId：设备分组ID,可选;当dataLevel为2时则必填,类型为Integer型;
	 dataLevel:子数据流规则类型:0-产品级别;1-设备级别；2-设备分组级别；可选；当dataLevel填写时规则按照此定义的规则类型进行规则处理，未填写时按照上一级配置的级别处理。	
     
}]
ruleForwardInfos：JSON数组，可选[
     {
         ruleForwardId:修改规则涉及推送修改时必填，新增推送时，此参数为空
         operatorType:操作类型：“01”：新增（配合新增规则使用），
		      “10”：修改（配合修改规则使用），“00”：删除（配合修改规则使用）
         forwardType:推送类型，目前仅支持HTTP，新增、修改推送时，必填；
		     删除推送时，此参数为空
         forwardConfig:JSON格式
	 {
            url:推送地址，必填，http的url路径,例如: http://rule.ctwind.cn/test/api
            content:推送内容，必填.
            参数格式: JSON
            参数模板：配置发送给应用的消息体的定义；所填的数据全部以body的方式传递。
                      参数模板是HTTP接口请求的参数部分，应当是合法的JSON格式字符串。
		      当不需要参数时，应当填”{}”。当参数需要注入规则执行的输出结果时，
		      可以使用字符%左右包裹变量名，变量名目前不区分大小写；组合规则时指定deviceId的某个属性，格式为%deviceId1.a%。
		      规则的执行结果包括规则语句SELECT和FROM之间的字段和自定义函数的
		      执行结果
            示例:
		    规则语句
		    SELECT COL1 AS AA,COL2 AS BB,COL3 AS CC FROM topic WHERE COL1 < 3
		     参数模板
		     {"COL1":"%AA%","const":"123"}
		     测试数据
		    {"COL1":1, "COL2":"B", "COL3":"Y", "COL4":"NO"}
		    输出接口参数
		    {"COL1":1,"const":"123"}

         }
      }
  ]
SQL描述:
	为了容易理解，把规则抽象成SQL表达式(类似Mysql语法)  
	注意，设备消息只有json格式才运行！
	1. SELECT
	select的属性来源于消息的payload，查询字段与payload字段对应，
	可以使用AS指定别名引用，也可以来源于函数比如deviceName()。
	若查询字段既不是来自于产品的属性字段(物模型)，也不在自定义函数列表中，
	则无法创建规则。
	如：select a, b, deviceId() as devId from ruleengine_100987211_10292321;
	其中a，b字段均为该产品的属性字段，devId 为deviceId()函数的别名。
	2. AS
	可以为表名称或列名称指定别名。 
	3. FROM
	FROM用来指定数据来源，表名拼接格式为ruleengine_tenantId_productId，
	如：ruleengine_10039191_10001079。
	当有符合规则的消息到达时，消息的payload数据以json形式被上下文环境使用
	(如果消息格式不合法,将忽略此消息)。 
	4. WHERE
	规则触发条件，条件表达式。当符合topic的消息到达时，这条消息触发规则的条件。
	在WHERE中使用到字段或者别名，需要在SELECT中明确获取，或者是该产品的属性。
	 如：select a, b from ruleengine_10039191_10001079 where a = ‘1’ and c = ‘2’;
	 其中where字段的a，c均为该产品的属性。
	5. Sql示例
	单条数据通过条件进行筛选。
	//查询字段掘payload字段对应，此处仅为示例
	SELECT 
	COL1 AS AA,
	COL2 AS BB,
	COL3 AS CC
	FROM ruleengine_100000_1000001
	WHERE AA< 3

#### 返回信息

##### 返回参数类型
json

##### 返回结果示例
{
    "code": "0",
    "msg": "ok",
    "result": {
        "ruleForwardInfos": [
            {
                "forwardConfig": {
                    "content": "{\"test\":\"%a%\"}",
                    "url": "http://127.0.0.1:9090/test"
                },
                "forwardType": "HTTP",
                "operatorType": "01",
                "ruleForwardId": "317a66be-a578-538a-b3ca-344fed801b19"
            }
        ],
        "ruleId": "c68c7769-3e3a-c2f9-383d-ab8e73122a0b"
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

### API名称：saasQueryRule   版本号: 20200111000633

#### 描述

SAAS规则查询

#### 请求信息

请求路径：/api/v2/rule/sass/queryRule

请求方法：GET

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|ruleId|QUERY|String|false||
|productId|QUERY|String|true||
|pageNow|QUERY|Long|false||
|pageSize|QUERY|Long|false||


#### 返回信息

##### 返回参数类型
json

##### 返回结果示例
{
    "code": "0",
    "msg": "ok",
    "result": {
        "endRow": 1,
        "firstPage": 0,
        "hasNextPage": false,
        "hasPreviousPage": false,
        "isFirstPage": false,
        "isLastPage": true,
        "lastPage": 0,
        "list": [
            {               
                "dataLevel": 0,
                "description": "修改规则，看转发是否存在",
                "productId": "10003561",
                "ruleForwardInfos": [],
                "ruleId": "be334616-d858-b382-9352-a50aaeb3fa1f",
                "ruleString": "select aa,cc from ruleengine_10106316_10003561 where aa = 1",
                "ruleType": "1000",
                "userId": "10107390"
            }
        ],
        "navigatePages": 8,
        "navigatepageNums": [],
        "nextPage": 0,
        "pageNum": 0,
        "pageSize": 0,
        "pages": 0,
        "prePage": 0,
        "size": 1,
        "startRow": 1,
        "total": 0
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

### API名称：saasUpdateRule   版本号: 20200111000540

#### 描述

更新SAAS规则引擎

#### 请求信息

请求路径：/api/v2/rule/sass/updateRule

请求方法：POST

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|

#### 请求BODY

##### 数据类型：
json

##### 内容描述：
{
  "ruleId": "c68c7769-3e3a-c2f9-383d-ab8e73122a0b",
   "dataLevel": 1,
  "description": "修改规则",
  "ruleType": "1000",
  "userId": "ljupdate",
  "ruleStreams": [
    {
	   "deviceId": "123",
       "productId": "10003561",
	   "deviceGroupId":null,
	   "dataLevel": 1,
       "ruleStr": "select aa,cc from ruleengine_10106316_10003561 where aa = 1 and deviceId()='123'"
    }
  ],
  "ruleForwardInfos": [
    {
        "forwardConfig": {
        "content": "{\"test\":\"%a%\"}",
        "url": "http://127.0.0.1:9090/test"
      },
      "forwardType": "HTTP",
      "operatorType": "01"
    }
    
  ]  

}

描述:
ruleId:修改、删除时必填，新增规则时，此参数为空
dataLevel:规则数据类型:0-产品级别;1-设备级别；2-设备分组级别[*必填];组合规则时只支持设备级别。
description:规则的描述信息, 长度不超过160位的字符串[*必填]
ruleType:规则类型;1000：简单规则，2000：组合规则
userId：用户ID[*必填]
ruleStreams：规则信息[*必填][{   
     ruleStr:规则内容，即sql。不能包含特殊字符*，修改、新增时必填,
		具体详看下面SQL描述   
	 productId:产品ID[*必填]		
	 deviceId：设备ID,可选;当dataLevel为1时则必填。
	 deviceGroupId：设备分组ID,可选;当dataLevel为2时则必填,类型为Integer型。
	 dataLevel:子数据流规则类型:0-产品级别;1-设备级别；2-设备分组级别；可选；当dataLevel填写时规则按照此定义的规则类型进行规则处理，未填写时按照上一级配置的级别处理。	
     
}]
ruleForwardInfos：JSON数组，可选[
     {
         ruleForwardId:修改规则涉及推送修改时必填，新增推送时，此参数为空
         operatorType:操作类型：“01”：新增（配合新增规则使用），
		      “10”：修改（配合修改规则使用），“00”：删除（配合修改规则使用）
         forwardType:推送类型，目前仅支持HTTP，新增、修改推送时，必填；
		     删除推送时，此参数为空
         forwardConfig:JSON格式
	 {
            url:推送地址，必填，http的url路径,例如: http://rule.ctwind.cn/test/api
            content:推送内容，必填.
            参数格式: JSON
            参数模板：配置发送给应用的消息体的定义；所填的数据全部以body的方式传递。
                      参数模板是HTTP接口请求的参数部分，应当是合法的JSON格式字符串。
		      当不需要参数时，应当填”{}”。当参数需要注入规则执行的输出结果时，
		      可以使用字符%左右包裹变量名，变量名目前不区分大小写；变量名目前不区分大小写；
                      组合规则时指定deviceId的某个属性，格式为%deviceId1.a%。
		      规则的执行结果包括规则语句SELECT和FROM之间的字段和自定义函数的
		      执行结果
            示例:
		    规则语句
		    SELECT COL1 AS AA,COL2 AS BB,COL3 AS CC FROM topic WHERE COL1 < 3
		     参数模板
		     {"COL1":"%AA%","const":"123"}
		     测试数据
		    {"COL1":1, "COL2":"B", "COL3":"Y", "COL4":"NO"}
		    输出接口参数
		    {"COL1":1,"const":"123"}

         }
      }
  ]
SQL描述:
	为了容易理解，把规则抽象成SQL表达式(类似Mysql语法)  
	注意，设备消息只有json格式才运行！
	1. SELECT
	select的属性来源于消息的payload，查询字段与payload字段对应，
	可以使用AS指定别名引用，也可以来源于函数比如deviceName()。
	若查询字段既不是来自于产品的属性字段(物模型)，也不在自定义函数列表中，
	则无法创建规则。
	如：select a, b, deviceId() as devId from ruleengine_100987211_10292321;
	其中a，b字段均为该产品的属性字段，devId 为deviceId()函数的别名。
	2. AS
	可以为表名称或列名称指定别名。 
	3. FROM
	FROM用来指定数据来源，表名拼接格式为ruleengine_tenantId_productId，
	如：ruleengine_10039191_10001079。
	当有符合规则的消息到达时，消息的payload数据以json形式被上下文环境使用
	(如果消息格式不合法,将忽略此消息)。 
	4. WHERE
	规则触发条件，条件表达式。当符合topic的消息到达时，这条消息触发规则的条件。
	在WHERE中使用到字段或者别名，需要在SELECT中明确获取，或者是该产品的属性。
	 如：select a, b from ruleengine_10039191_10001079 where a = ‘1’ and c = ‘2’;
	 其中where字段的a，c均为该产品的属性。
	5. Sql示例
	单条数据通过条件进行筛选。
	//查询字段掘payload字段对应，此处仅为示例
	SELECT 
	COL1 AS AA,
	COL2 AS BB,
	COL3 AS CC
	FROM ruleengine_100000_1000001
	WHERE AA< 3

#### 返回信息

##### 返回参数类型
json

##### 返回结果示例
{
    "code": "0",
    "msg": "ok",
    "result": {
        "ruleForwardInfos": [
            {
                "forwardConfig": {
                    "content": "{\"test\":\"%a%\"}",
                    "url": "http://127.0.0.1:9090/test1"
                },
                "forwardType": "HTTP",
                "operatorType": "01",
                "ruleForwardId": "3eba4769-c64c-6681-d8b6-c2eacac52ff3"
            }
        ],
        "ruleId": "c68c7769-3e3a-c2f9-383d-ab8e73122a0b"
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

### API名称：saasDeleteRuleEngine   版本号: 20200111000611

#### 描述

SAAS规则删除

#### 请求信息

请求路径：/api/v2/rule/sass/deleteRule

请求方法：POST

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|

#### 请求BODY

##### 数据类型：
json

##### 内容描述：
{ 
  "ruleId": "c68c7769-3e3a-c2f9-383d-ab8e73122a0b"
}
描述;
ruleId:规则Id[*必填]

#### 返回信息

##### 返回参数类型
json

##### 返回结果示例
{
    "code": "0",
    "msg": "ok"
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

### API名称：CreateRule   版本号: 20210327062633

#### 描述

创建规则

#### 请求信息

请求路径：/v3/rule/createRule

请求方法：POST

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|

#### 请求BODY

##### 数据类型：
json

##### 内容描述：
{  
  "dataLevel": 0,
  "description": "测试add",
  "ruleStreams": [
    {
      "productId": "10003561",
	"deviceId":"",
	"deviceGroupId":null,
    "ruleStr": "select aa,cc from ruleengine_10106316_10003561 where aa = 1",
	"dataLevel":0
    }
  ],
  "ruleType": "1000",
  "creator": "ljtest"
}
  ruleId:修改、删除时必填，新增规则时，此参数为空

描述:
dataLevel:规则数据类型:0-产品级别;1-设备级别；2-设备分组级别[*必填]；组合规则只支持设备级别。
ruleType:规则类型；1000：简单规则，2000：组合规则
creator：创建人[*必填]
description:规则的描述信息, 长度不超过160位的字符串[*必填]
ruleStreams：规则信息[*必填][{   
     ruleStr:规则内容，即sql。不能包含特殊字符*，修改、新增时必填,
		具体详看下面SQL描述   
	 productId:产品ID[*必填]		
	 deviceId：设备ID,可选;当dataLevel为1时则必填。
	 deviceGroupId：设备分组ID,可选;当dataLevel为2时则必填,类型为Integer型;
	 dataLevel:子数据流规则类型:0-产品级别;1-设备级别；2-设备分组级别；可选；当dataLevel填写时规则按照此定义的规则类型进行规则处理，未填写时按照上一级配置的级别处理。	
     
}]
SQL描述:
	为了容易理解，把规则抽象成SQL表达式(类似Mysql语法)  
	注意，设备消息只有json格式才运行！
	1. SELECT
	select的属性来源于消息的payload，查询字段与payload字段对应，
	可以使用AS指定别名引用，也可以来源于函数比如deviceName()。
	若查询字段既不是来自于产品的属性字段(物模型)，也不在自定义函数列表中，
	则无法创建规则。
	如：select a, b, deviceId() as devId from ruleengine_100987211_10292321;
	其中a，b字段均为该产品的属性字段，devId 为deviceId()函数的别名。
	2. AS
	可以为表名称或列名称指定别名。 
	3. FROM
	FROM用来指定数据来源，表名拼接格式为ruleengine_tenantId_productId，
	如：ruleengine_10039191_10001079。
	当有符合规则的消息到达时，消息的payload数据以json形式被上下文环境使用
	(如果消息格式不合法,将忽略此消息)。 
	4. WHERE
	规则触发条件，条件表达式。当符合topic的消息到达时，这条消息触发规则的条件。
	在WHERE中使用到字段或者别名，需要在SELECT中明确获取，或者是该产品的属性。
	 如：select a, b from ruleengine_10039191_10001079 where a = ‘1’ and c = ‘2’;
	 其中where字段的a，c均为该产品的属性。
	5. Sql示例
	单条数据通过条件进行筛选。
	//查询字段掘payload字段对应，此处仅为示例
	SELECT 
	COL1 AS AA,
	COL2 AS BB,
	COL3 AS CC
	FROM ruleengine_100000_1000001
	WHERE AA= 3

#### 返回信息

##### 返回参数类型
default

##### 返回结果示例
{
    "code": "0",
    "msg": "ok",
    "result": "ec7bcf7e-3e49-21be-2c34-9ee6018cb855"
}

描述：result为创建的规则ID。

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

### API名称：UpdateRule   版本号: 20210327062642

#### 描述

更新规则，规则状态为停止时才可操作

#### 请求信息

请求路径：/v3/rule/updateRule

请求方法：POST

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|

#### 请求BODY

##### 数据类型：
json

##### 内容描述：
{  
 "ruleId": "c68c7769-3e3a-c2f9-383d-ab8e73122a0b",  
  "dataLevel": 0,
  "description": "测试add",
  "ruleStreams": [
    {
      "productId": "10003561",
	"deviceId":"",
	"deviceGroupId":null,
    "ruleStr": "select aa,cc from ruleengine_10106316_10003561 where aa = 1",
	"dataLevel":0
    }
  ],
  "ruleType": "1000"
}
  ruleId:修改、删除时必填，新增规则时，此参数为空

描述:
ruleId:修改、删除时必填，新增规则时，此参数为空
dataLevel:规则数据类型:0-产品级别;1-设备级别；2-设备分组级别[*必填]；组合规则只支持设备级别。
ruleType:规则类型；1000：简单规则，2000：组合规则
description:规则的描述信息, 长度不超过160位的字符串[*必填]
ruleStreams：规则信息[*必填][{   
     ruleStr:规则内容，即sql。不能包含特殊字符*，修改、新增时必填,
		具体详看下面SQL描述   
	 productId:产品ID[*必填]		
	 deviceId：设备ID,可选;当dataLevel为1时则必填。
	 deviceGroupId：设备分组ID,可选;当dataLevel为2时则必填,类型为Integer型;
	 dataLevel:子数据流规则类型:0-产品级别;1-设备级别；2-设备分组级别；可选；当dataLevel填写时规则按照此定义的规则类型进行规则处理，未填写时按照上一级配置的级别处理。	
     
}]

SQL描述:
	为了容易理解，把规则抽象成SQL表达式(类似Mysql语法)  
	注意，设备消息只有json格式才运行！
	1. SELECT
	select的属性来源于消息的payload，查询字段与payload字段对应，
	可以使用AS指定别名引用，也可以来源于函数比如deviceName()。
	若查询字段既不是来自于产品的属性字段(物模型)，也不在自定义函数列表中，
	则无法创建规则。
	如：select a, b, deviceId() as devId from ruleengine_100987211_10292321;
	其中a，b字段均为该产品的属性字段，devId 为deviceId()函数的别名。
	2. AS
	可以为表名称或列名称指定别名。 
	3. FROM
	FROM用来指定数据来源，表名拼接格式为ruleengine_tenantId_productId，
	如：ruleengine_10039191_10001079。
	当有符合规则的消息到达时，消息的payload数据以json形式被上下文环境使用
	(如果消息格式不合法,将忽略此消息)。 
	4. WHERE
	规则触发条件，条件表达式。当符合topic的消息到达时，这条消息触发规则的条件。
	在WHERE中使用到字段或者别名，需要在SELECT中明确获取，或者是该产品的属性。
	 如：select a, b from ruleengine_10039191_10001079 where a = ‘1’ and c = ‘2’;
	 其中where字段的a，c均为该产品的属性。
	5. Sql示例
	单条数据通过条件进行筛选。
	//查询字段掘payload字段对应，此处仅为示例
	SELECT 
	COL1 AS AA,
	COL2 AS BB,
	COL3 AS CC
	FROM ruleengine_100000_1000001
	WHERE AA= 3

#### 返回信息

##### 返回参数类型
default

##### 返回结果示例
{
    "code": "0",
    "msg": "ok",
    "result":null
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

### API名称：DeleteRule   版本号: 20210327062626

#### 描述

删除规则，只有规则状态为停止时才可操作

#### 请求信息

请求路径：/v3/rule/deleteRule

请求方法：POST

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|

#### 请求BODY

##### 数据类型：
json

##### 内容描述：
{
    "ruleId": "073a07e1-8be6-5648-d01a-8e7693b1eab8"
}

ruleId：规则Id，当规则为停止状态时才可以删除。

#### 返回信息

##### 返回参数类型
json

##### 返回结果示例
{ "code": "0", "msg": "ok", "result": null }

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

### API名称：GetRules   版本号: 20210327062616

#### 描述

获取规则

#### 请求信息

请求路径：/v3/rule/getRules

请求方法：GET

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|ruleId|QUERY|String|true||
|productId|QUERY|String|false||
|pageNow|QUERY|Long|false||
|pageSize|QUERY|Long|false||


#### 返回信息

##### 返回参数类型
json

##### 返回结果示例
{
    "code": "0",
    "msg": "ok",
    "result": {
        "endRow": 2,
        "firstPage": 1,
        "hasNextPage": false,
        "hasPreviousPage": false,
        "isFirstPage": true,
        "isLastPage": true,
        "lastPage": 1,
        "list": [
            {
                "createTimeStamp": "2021-03-08 10:24:24.0",
                "dataLevel": 1,
                "description": "创建规则",
                "productId": "20002001",
                "ruleId": "ec7bcf7e-3e49-21be-2c34-9ee6018cb855",
                "ruleString": "SELECT aaa FROM ruleengine_300_20002001 WHERE deviceId() = '6552ad90c4094be692d17cb7b6d69452' AND bId = 1",
                "ruleType": "1000",
                "runningStatus": "1100",
                "creator": "ljtest"
            },
            {
                "createTimeStamp": "2021-03-08 10:08:28.0",
                "dataLevel": 0,
                "description": "更新规则",
                "productId": "20002023",
                "ruleId": "e901eef7-2e86-9811-a073-2b8c34d970f2",
                "ruleString": "SELECT ww FROM ruleengine_300_20002023 WHERE ww = 12",
                "ruleType": "1000",
                "runningStatus": "1100",
                "creator": "1234"
            }
        ],
        "navigatePages": 8,
        "navigatepageNums": [
            1
        ],
        "nextPage": 0,
        "pageNum": 1,
        "pageSize": 2,
        "pages": 1,
        "prePage": 0,
        "size": 2,
        "startRow": 1,
        "total": 2
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

### API名称：GetRuleRunStatus   版本号: 20210327062610

#### 描述

获取规则运行状态

#### 请求信息

请求路径：/v3/rule/getRuleRunningStatus

请求方法：POST

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|

#### 请求BODY

##### 数据类型：
json

##### 内容描述：
["e901eef7-2e86-9811-a073-2b8c34d970f2"] 
List类型，规则id。

#### 返回信息

##### 返回参数类型
json

##### 返回结果示例
{
    "code": "0",
    "msg": "ok",
    "result": [
        {
            "ruleId": "e901eef7-2e86-9811-a073-2b8c34d970f2",
            "runningStatus": "1100"
        }
    ]
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

### API名称：UpdateRuleRunStatus   版本号: 20210327062603

#### 描述

修改规则运行状态

#### 请求信息

请求路径：/v3/rule/modifyRuleRunningStatus

请求方法：POST

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|

#### 请求BODY

##### 数据类型：
json

##### 内容描述：
{
  "ruleId": "e901eef7-2e86-9811-a073-2b8c34d970f2",
  "runningStatus": "1000"
}

ruleId：规则id，必选。
runningStatus：运行状态，1000-启动/1100-停止；不选

#### 返回信息

##### 返回参数类型
json

##### 返回结果示例
{ "code": "0", "msg": "ok", "result": null }

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

### API名称：CreateForward   版本号: 20210327062556

#### 描述

创建转发规则，只有规则状态为停止时才可操作

#### 请求信息

请求路径：/v3/rule/addForward

请求方法：POST

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|

#### 请求BODY

##### 数据类型：
json

##### 内容描述：
{ 
  "content": "{\"a\":1}", 
   "destId": 19,
   "forwardType": "HTTP", 
   "ruleId": "e901eef7-2e86-9811-a073-2b8c34d970f2" 
 } 
 描述：
 content:推送内容，必填.
            参数格式: JSON
            参数模板：配置发送给应用的消息体的定义；所填的数据全部以body的方式传递。
                      参数模板是HTTP接口请求的参数部分，应当是合法的JSON格式字符串。
		      当不需要参数时，应当填”{}”。当参数需要注入规则执行的输出结果时，
		      可以使用字符%左右包裹变量名，变量名目前不区分大小写；组合规则时指定deviceId的某个属性，格式为%deviceId1.a%。
		      规则的执行结果包括规则语句SELECT和FROM之间的字段和自定义函数的
		      执行结果
destId：目的地ID，必填；参数格式：Int;此参数为目的地管理中心获取。

forwardType:推送类型，参数格式：String；目前仅支持HTTP、MQ，新增、修改推送时，必填；
ruleId：规则ID，参数类型：String。

#### 返回信息

##### 返回参数类型
json

##### 返回结果示例
{ "code": "0", "msg": "ok", "result": "e9ed4b7a-2d7a-13c1-65aa-50470565d4dc" }

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

### API名称：UpdateForward   版本号: 20210327062549

#### 描述

更新转发规则，只有规则状态为停止时才可操作

#### 请求信息

请求路径：/v3/rule/updateForward

请求方法：POST

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|

#### 请求BODY

##### 数据类型：
json

##### 内容描述：
{ 
  "content": "{\"a\":1}", 
   "destId": 19, \ 
   "forwardType": "HTTP", 
   "ruleId": "e901eef7-2e86-9811-a073-2b8c34d970f2" ,
     "forwardId":"b6f03ade-c76f-9ae4-cb8d-337c40309892"
 } 
 描述：
 content:推送内容，必填.
            参数格式: JSON
            参数模板：配置发送给应用的消息体的定义；所填的数据全部以body的方式传递。
                      参数模板是HTTP接口请求的参数部分，应当是合法的JSON格式字符串。
		      当不需要参数时，应当填”{}”。当参数需要注入规则执行的输出结果时，
		      可以使用字符%左右包裹变量名，变量名目前不区分大小写；组合规则时指定deviceId的某个属性，格式为%deviceId1.a%。
		      规则的执行结果包括规则语句SELECT和FROM之间的字段和自定义函数的
		      执行结果
destId：目的地ID，必填；参数格式：Int;此参数为目的地管理中心获取。

forwardType:推送类型，必填，参数格式：String；目前仅支持HTTP、MQ，新增、修改推送时。
ruleId：规则ID，必填，参数类型：String。
forwardId：规则转发ID，必填，参数类型：String。

#### 返回信息

##### 返回参数类型
json

##### 返回结果示例
{
    "code": "0",
    "msg": "ok",
    "result":null
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

### API名称：DeleteForward   版本号: 20210327062539

#### 描述

删除转发规则，只有规则状态为停止时才可操作

#### 请求信息

请求路径：/v3/rule/deleteForward

请求方法：POST

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|

#### 请求BODY

##### 数据类型：
json

##### 内容描述：
{
  "forwardIds": [
    "e9ed4b7a-2d7a-13c1-65aa-50470565d4dc"
  ],
  "ruleId": "e901eef7-2e86-9811-a073-2b8c34d970f2"
}
描述：
forwardIds：规则转发ID号，参数格式：List，必填。
ruleId:规则ID，参数类型：String，必填。

#### 返回信息

##### 返回参数类型
json

##### 返回结果示例
{ "code": "0", "msg": "ok", "result": null }

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

### API名称：GetForwards   版本号: 20210327062531

#### 描述

获取转发规则

#### 请求信息

请求路径：/v3/rule/getForwards

请求方法：GET

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|ruleId|QUERY|String|true||
|productId|QUERY|String|false||
|pageNow|QUERY|Long|false||
|pageSize|QUERY|Long|false||


#### 返回信息

##### 返回参数类型
json

##### 返回结果示例
{
    "code": "0",
    "msg": "ok",
    "result": {
        "endRow": 1,
        "firstPage": 1,
        "hasNextPage": false,
        "hasPreviousPage": false,
        "isFirstPage": true,
        "isLastPage": true,
        "lastPage": 1,
        "list": [
            {
                "forwardConfig": "{"destId":19,"content":"{\"a\":1}"}",
                "forwardType": "HTTP",
                "forwardId": "e9ed4b7a-2d7a-13c1-65aa-50470565d4dc"
            }
        ],
        "navigatePages": 8,
        "navigatepageNums": [
            1
        ],
        "nextPage": 0,
        "pageNum": 1,
        "pageSize": 100,
        "pages": 1,
        "prePage": 0,
        "size": 1,
        "startRow": 1,
        "total": 1
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

### API名称：GetWarns   版本号: 20210423162903

#### 描述

分页获取告警规则

#### 请求信息

请求路径：/v3/rule/getWarns

请求方法：GET

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|ruleId|QUERY|String|true||
|pageNow|QUERY|Long|false||
|pageSize|QUERY|Long|false||


#### 返回信息

##### 返回参数类型
json

##### 返回结果示例
{
    "code": "0",
    "msg": "ok",
    "result": {
        "endRow": 1,
        "firstPage": 1,
        "hasNextPage": false,
        "hasPreviousPage": false,
        "isFirstPage": true,
        "isLastPage": true,
        "lastPage": 1,
        "list": [
            {
                "createTime": 1615950242000,
                "createUser": "1234",
                "modifyTime": 1615950242000,
                "productId": "20002023",
                "ruleId": "e901eef7-2e86-9811-a073-2b8c34d970f2",
                "ruleWarnId": "1ed0be70-120a-670c-53aa-83dde0178891",
                "status": "1000",
                "tenantId": "300",
                "warnConfig": "{"frequency":5,"productId":"20002023","ruleId":"e901eef7-2e86-9811-a073-2b8c34d970f2","smsTemplate":"{\"level\":\"${level}\",\"name\":\"${name}\"}","templateId":"91556621","tenantId":"300","users":[{"mobileId":"18066113862","name":"cbk","tenantId":"300","userId":"0543c156-4aec-0ed7-345d-f5af9287c814"}],"warnContent":"尊敬的客户，您收到一条${level}等级的规则引擎告警通知,告警名称为${name}。","warnLevel":"严重","warnName":"告警测试1","warnType":"sms"}",
                "warnLevel": "严重",
                "warnName": "告警测试1",
                "warnType": "sms",
                "warnUserId": "0543c156-4aec-0ed7-345d-f5af9287c814"
            }
        ],
        "navigatePages": 8,
        "navigatepageNums": [
            1
        ],
        "nextPage": 0,
        "pageNum": 1,
        "pageSize": 100,
        "pages": 1,
        "prePage": 0,
        "size": 1,
        "startRow": 1,
        "total": 1
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

### API名称：DeleteWarn   版本号: 20210423162859

#### 描述

删除告警规则，只有规则状态为停止时才可操作

#### 请求信息

请求路径：/v3/rule/deleteWarn

请求方法：POST

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|

#### 请求BODY

##### 数据类型：
json

##### 内容描述：
{
  "warnIds": [
    "1be1db34-34c2-7f7e-7e2a-b1c540073895"
  ],
  "ruleId": "e901eef7-2e86-9811-a073-2b8c34d970f2"
}
描述：
warnIds：规则告警ID号，参数格式：List<String>，必填。
ruleId:规则ID，参数类型：String，必填。

#### 返回信息

##### 返回参数类型
json

##### 返回结果示例
{ "code": "0", "msg": "ok", "result": null }

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

### API名称：UpdateWarn   版本号: 20210423162906

#### 描述

更新告警规则，只有规则状态为停止时才可操作

#### 请求信息

请求路径：/v3/rule/updateWarn

请求方法：POST

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|

#### 请求BODY

##### 数据类型：
json

##### 内容描述：
{
  "ruleId": "e901eef7-2e86-9811-a073-2b8c34d970f2",
  "warnInfo": {
    "frequency": 10,
    "operator": "测试",
    "warnId": "1ed0be70-120a-670c-53aa-83dde0178891",
    "subject": "测试告警邮件",
    "warnContent": "${Battery_power}${Compressor_power}请告知",
    "warnLevel": "一般",
    "warnName": "测试告警邮件12",
    "warnType": "email",
    "warnUserId": "0fadbbd7-ade5-5eda-2ad6-d8b45543864d"
  }
}
描述：
ruleId：数据类型：String；规则ID。
warnInfo：{
 frequency:数据类型：String；告警频率，取值：5、10、15、20（分钟）
operator：数据类型：String：操作人。
warnId:数据类型：String；告警ID。
subject：数据类型：String;邮箱标题。
warnContent:数据类型：String；告警内容。
warnLevel:数据类型：String；告警等级，取值：严重、一般、微小。
warnName：数据类型：String；告警名称。
warnType：数据类型：String；告警类型；取值：sms、email。
warnUserId：数据类型：String；告警通知用户的id号。
}

#### 返回信息

##### 返回参数类型
json

##### 返回结果示例
{
    "code": "0",
    "msg": "ok",
    "result":null
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

### API名称：CreateWarn   版本号: 20210423162909

#### 描述

创建告警规则，只有规则状态为停止时才可操作

#### 请求信息

请求路径：/v3/rule/addWarn

请求方法：POST

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|

#### 请求BODY

##### 数据类型：
json

##### 内容描述：
{
    "ruleId": "e901eef7-2e86-9811-a073-2b8c34d970f2",
    "warnInfo": {
        "frequency": "5",
        "operator": "test",
        "warnContent": "string",
        "warnLevel": "严重",
        "warnName": "告警测试1",
        "warnType": "sms",
        "warnUserId": "0543c156-4aec-0ed7-345d-f5af9287c814"
    }
}

描述：
ruleId：数据类型：String；规则ID。
warnInfo：{
 frequency:数据类型：String；告警频率，取值：5、10、15、20（分钟）
operator：数据类型：String：操作人。
warnContent:数据类型：String；告警内容。
warnLevel:数据类型：String；告警等级，取值：严重、一般、微小。
warnName：数据类型：String；告警名称。
warnType：数据类型：String；告警类型；取值：sms、email。
warnUserId：数据类型：String；告警通知用户的id号。
}

#### 返回信息

##### 返回参数类型
json

##### 返回结果示例
{ "code": "0", "msg": "ok", "result": "410d9cff-1ef2-4c90-fc72-807fb6c6eb30" }

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

### API名称：CreateAction   版本号: 20210423162837

#### 描述

创建动作规则，只有规则状态为停止时才可操作

#### 请求信息

请求路径：/v3/rule/addAction

请求方法：POST

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|

#### 请求BODY

##### 数据类型：
json

##### 内容描述：
{
  "actConfig": {
    "controlLevel": "device",
    "deviceId": "f32ad3efa3d94cb1927812e319472e14",
    "identifier": "qwe",
    "params": { "aa": 1, "sssss": "2"},
    "productId": "1420002812",
    "serviceId": "8001"
  },
  "actName": "北向添加动作",
  "ruleId": "e901eef7-2e86-9811-a073-2b8c34d970f2"
}
描述：
actConfig：{
  controlLevel:数据类型：String；动作控制级别，取值：device-设备级别，deviceGroup-设备分组级别。
deviceId：数据类型：String；设备ID。
identifier:数据类型：String；服务标识在产品管理中服务定义获取。
params:数据类型：json串；服务参数以及参数值。
productId：数据类型：String；产品ID。
serviceId：数据类型：String；服务ID在产品管理中服务定义获取。
}
actName：数据类型：String；动作名称。
ruleId：数据类型：String；规则ID。

#### 返回信息

##### 返回参数类型
json

##### 返回结果示例
{ "code": "0", "msg": "ok", "result": "d55e01ec-296d-2a5a-dcc7-16ff8cb14ef4" }

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

### API名称：UpdateAction   版本号: 20210423162842

#### 描述

更新动作规则，只有规则状态为停止时才可操作

#### 请求信息

请求路径：/v3/rule/updateAction

请求方法：POST

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|

#### 请求BODY

##### 数据类型：
json

##### 内容描述：
{
  "actConfig": {
    "controlLevel": "device",
    "deviceId": "f32ad3efa3d94cb1927812e319472e14",
    "identifier": "qwe",
    "params": { "aa": 1, "sssss": "2"},
    "productId": "1420002812",
    "serviceId": "8001"
  },
  "actName": "北向添加更新",
  "actId": "d55e01ec-296d-2a5a-dcc7-16ff8cb14ef4",
  "ruleId": "e901eef7-2e86-9811-a073-2b8c34d970f2"
}
描述：
actConfig：{
  controlLevel:数据类型：String；动作控制级别，取值：device-设备级别，deviceGroup-设备分组级别。
deviceId：数据类型：String；设备ID。
identifier:数据类型：String；服务标识在产品管理中服务定义获取。
params:数据类型：json串；服务参数以及参数值。
productId：数据类型：String；产品ID。
serviceId：数据类型：String；服务ID在产品管理中服务定义获取。
}
actName：数据类型：String；动作名称。
actId：数据类型：String；动作规则ID。
ruleId：数据类型：String；规则ID。

#### 返回信息

##### 返回参数类型
json

##### 返回结果示例
{
    "code": "0",
    "msg": "ok",
    "result":null
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

### API名称：DeleteAction   版本号: 20210423162848

#### 描述

删除动作规则，只有规则状态为停止时才可操作

#### 请求信息

请求路径：/v3/rule/deleteAct

请求方法：POST

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|

#### 请求BODY

##### 数据类型：
json

##### 内容描述：
{
  "actIds": [
    "1be1db34-34c2-7f7e-7e2a-b1c540073895"
  ],
  "ruleId": "e901eef7-2e86-9811-a073-2b8c34d970f2"
}
描述：
actIds：规则告警ID号，参数格式：List<String>，必填。
ruleId:规则ID，参数类型：String，必填。

#### 返回信息

##### 返回参数类型
json

##### 返回结果示例
{ "code": "0", "msg": "ok", "result": null }

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

### API名称：GetActions   版本号: 20211028100156

#### 描述

分页获取动作规则

#### 请求信息

请求路径：/v3/rule/getActions

请求方法：GET

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|ruleId|QUERY|String|true||
|pageNow|QUERY|Long|false||
|pageSize|QUERY|Long|false||


#### 返回信息

##### 返回参数类型
json

##### 返回结果示例
{
    "code": "0",
    "msg": "ok",
    "result": {
        "endRow": 2,
        "firstPage": 1,
        "hasNextPage": false,
        "hasPreviousPage": false,
        "isFirstPage": true,
        "isLastPage": true,
        "lastPage": 1,
        "list": [
            {
                "actConfig": "{"actNotify":false,"apiKey":"8dfffa5220054ae4acb0541ffc90173d","controlLevel":"deviceGroup","deviceGroupId":0,"deviceGroupName":"","identifier":"qwe","paramList":[{"aa":1},{"sssss":"2"}],"productId":"1420002812","serviceId":"8001","timingConfig":{"beginTime":"","endTime":"","type":"everyDay"},"timingControl":false}",
                "actName": "北向添加分组动作",
                "actProductId": "1420002812",
                "actServiceId": 8001,
                "actType": "command_control",
                "createTime": 1615364534000,
                "createUser": "1234",
                "orderByCreateTime": false,
                "productId": "20002023",
                "ruleActId": "1be1db34-34c2-7f7e-7e2a-b1c540073895",
                "ruleId": "e901eef7-2e86-9811-a073-2b8c34d970f2",
                "status": "1000",
                "tenantId": "300"
            },
            {
                "actConfig": "{"actNotify":false,"apiKey":"8dfffa5220054ae4acb0541ffc90173d","controlLevel":"device","deviceGroupId":0,"deviceGroupName":"","deviceId":"f32ad3efa3d94cb1927812e319472e14","identifier":"qwe","paramList":[{"aa":1},{"sssss":"2"}],"productId":"1420002812","serviceId":"8001","timingConfig":{"beginTime":"","endTime":"","type":"everyDay"},"timingControl":false}",
                "actDeviceId": "f32ad3efa3d94cb1927812e319472e14",
                "actName": "北向更新动作",
                "actProductId": "1420002812",
                "actServiceId": 8001,
                "actType": "command_control",
                "createTime": 1615357062000,
                "createUser": "1234",
                "modifyTime": 1615876746000,
                "orderByCreateTime": false,
                "productId": "20002023",
                "ruleActId": "d55e01ec-296d-2a5a-dcc7-16ff8cb14ef4",
                "ruleId": "e901eef7-2e86-9811-a073-2b8c34d970f2",
                "status": "1000",
                "tenantId": "300"
            }
        ],
        "navigatePages": 8,
        "navigatepageNums": [
            1
        ],
        "nextPage": 0,
        "pageNum": 1,
        "pageSize": 100,
        "pages": 1,
        "prePage": 0,
        "size": 2,
        "startRow": 1,
        "total": 2
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

### API名称：GetWarnUsers   版本号: 20210423162830

#### 描述

分页获取告警用户信息规则

#### 请求信息

请求路径：/v3/rule/getWarnUsers

请求方法：GET

#### 请求参数

|名称 | 位置| 类型| 必填| 描述|
|:-------|:------|:--------|:--------|:--------|
|pageNow|QUERY|Long|false||
|pageSize|QUERY|Long|false||


#### 返回信息

##### 返回参数类型
json

##### 返回结果示例
{
    "code": "0",
    "msg": "ok",
    "result": {
        "endRow": 9,
        "firstPage": 1,
        "hasNextPage": false,
        "hasPreviousPage": false,
        "isFirstPage": true,
        "isLastPage": true,
        "lastPage": 1,
        "list": [
            {
                "createTime": 1615433370000,
                "email": "",
                "id": "0543c156-4aec-0ed7-345d-f5af9287c814",
                "mobile": "18066113862",
                "modifyTime": 1615433370000,
                "userName": "cbk"
            },
            {
                "createTime": 1603769215000,
                "email": "exmwyj@qq.com",
                "id": "0fadbbd7-ade5-5eda-2ad6-d8b45543864d",
                "mobile": "13360007824",
                "modifyTime": 1603769269000,
                "userName": "test1"
            },
            {
                "createTime": 1615472826000,
                "email": "",
                "id": "258dd640-38fd-0e08-2b63-317383666757",
                "mobile": "18066113862",
                "modifyTime": 1615472826000,
                "userName": "cbkkbc"
            },
            {
                "createTime": 1603865881000,
                "email": "",
                "id": "288c477d-d405-d053-68d6-bae2aa902551",
                "mobile": "13360007824",
                "modifyTime": 1603865881000,
                "userName": "test2"
            },
            {
                "createTime": 1615449270000,
                "email": "",
                "id": "36c1d240-9f8d-64bb-beae-588d040376b2",
                "mobile": "18913381379",
                "modifyTime": 1615449270000,
                "userName": "ljtst"
            },
            {
                "createTime": 1603769936000,
                "email": "741574168@qq.com",
                "id": "3cbad7f7-deec-f586-d247-eb5f14cddb96",
                "mobile": "18825165371",
                "modifyTime": 1603769946000,
                "userName": "10007805"
            },
            {
                "createTime": 1608195892000,
                "email": "412735195@qq.com",
                "id": "832f1911-0f5d-c704-b55e-44b35121c5fc",
                "mobile": "18913381379",
                "modifyTime": 1608262141000,
                "userName": "测试111"
            },
            {
                "createTime": 1615542524000,
                "email": "412735195@qq.com",
                "id": "9793e762-5517-7a5a-2ae9-67fc329ea8bd",
                "mobile": "18913381379",
                "modifyTime": 1615542524000,
                "userName": "tes1112"
            },
            {
                "createTime": 1607648019000,
                "email": "",
                "id": "9a494650-7b94-a23f-18af-aee25ea43caa",
                "mobile": "18913381379",
                "modifyTime": 1607648019000,
                "userName": "ljtest"
            }
        ],
        "navigatePages": 8,
        "navigatepageNums": [
            1
        ],
        "nextPage": 0,
        "pageNum": 1,
        "pageSize": 100,
        "pages": 1,
        "prePage": 0,
        "size": 9,
        "startRow": 1,
        "total": 9
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


# 用户建议反馈

> version: 1.0  
> 
> zhangbin  2018.10.18


# 1. 服务接口定义

<span id="1.1"/>

## 1.问题与建议反馈 
### 1.1 问题列表查询 (多)

getFeedbackList()

#### 描述:


##### Request
<pre>
URL: /api/m/feeback/list
Medthod:    GET
Headers:    token
Character Encoding: utf-8
Content-Type: x-www-form-urlencoded
Query Parameters:
   - limit 查询最大数
</pre>
	   				
##### Response
<pre>
Headers:
Character Encoding: utf-8
Content-Type: application/json
Data: 
  - status	状态码 0 : succ; others : error  
  - errcode	错误码
  - errmsg	错误信息
  - result	array
    - id(s)  记录编号
    - create_time(i)   创建时间
    - title(s)      标题
    - content(s)    内容
    - reply(s)      回复内容
    - replier(s)    回复人
    - reply_time(i)  回复时间
</pre>

### 1.2 问题记录查询 (单对象)

getFeedback(id)

#### 描述:


##### Request
<pre>
URL: /api/m/feedback
Medthod:    GET
Headers:    token
Character Encoding: utf-8
Content-Type: x-www-form-urlencoded
Query Parameters:
   - id(s)  记录编号
</pre>
	   				
##### Response

<pre>

Headers:
Character Encoding: utf-8
Content-Type: application/json
Data: 
  - status	状态码 0 : succ; others : error  
  - errcode	错误码
  - errmsg	错误信息
  - result	object
    - id(s)  记录编号
    - create_time(i)   创建时间
    - title(s)      标题
    - content(s)    内容
    - reply(s)      回复内容
    - replier(s)    回复人
    - reply_time(i)  回复时间

</pre>

### 1.3 问题创建

createFeedback(**kwargs)

#### 描述:


##### Request
<pre>
URL: /api/m/feedback
Medthod:    POST
Headers:    token
Character Encoding: utf-8
Content-Type: x-www-form-urlencoded
Query Parameters:
    - title(s)      标题
    - content(s)    内容
</pre>
	   				
##### Response
<pre>
Headers:
Character Encoding: utf-8
Content-Type: application/json
Data: 
  - status	状态码 0 : succ; others : error  
  - errcode	错误码
  - errmsg	错误信息
  - result	新建记录编号
</pre>

### 1.4 反馈删除

removeFeedback(id,**kwargs)

#### 描述:


##### Request
<pre>
URL: /api/m/feedback
Medthod:    DELETE
Headers:    token
Character Encoding: utf-8
Content-Type: x-www-form-urlencoded
Query Parameters:
   - id(s)               记录编号 
</pre>
	   				
##### Response
<pre>
Headers:
Character Encoding: utf-8
Content-Type: application/json
Data: 
  - status	状态码 0 : succ; others : error  
  - errcode	错误码
  - errmsg	错误信息
  - result	
</pre>

##### Remarks



# 错误表
<pre>
10001 Object-Not-Exist 对象不存在
10002 Access-Denied 权限受限
10003 Permission-Insufficient 权限不够
10004 SystemFault 系统故障 
10005 ParameterInvalid  参数无效
10006 PasswordError  密码错误
20001 DeviceIsOffline  设备离线
20001 DeviceIsBusy   设备繁忙中

</pre>
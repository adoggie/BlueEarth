# 收货地址接口

> version: 1.0  
> 
> zhangbin  2018.10.22


# 1. 服务接口定义

<span id="1.1"/>

## 1.收货地址 
### 1.1 地址列表查询 (多)

getCargoAddressList()

#### 描述:


##### Request
<pre>
URL: /api/m/cargo-address/list
Medthod:    GET
Headers:    token
Character Encoding: utf-8
Content-Type: x-www-form-urlencoded
Query Parameters:
   - 
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
  - result	<array>
    - id(s)  记录编号
    - name(s)   收货人
    - phone(s)  电话
    - address(s) 收货地址
    - order(i)  排序
    - update_time(i) 更新或创建时间
    - is_default(b)  是否是缺省地址 0:非缺省; 1: 缺省
</pre>

### 1.2 地址列表查询 (单对象)

getCargoAddress(id)

#### 描述:


##### Request
<pre>
URL: /api/m/cargo-address
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
    - name(s)   收货人
    - phone(s)  电话
    - address(s) 收货地址
    - order(i)  排序
    - update_time(i) 更新或创建时间
    - is_default(b)  是否是缺省地址

</pre>

### 1.3 地址创建

createCargoAddress(**kwargs)

#### 描述:


##### Request
<pre>
URL: /api/m/cargo-address
Medthod:    POST
Headers:    token
Character Encoding: utf-8
Content-Type: x-www-form-urlencoded
Query Parameters:
   - name(s)   收货人
   - phone(s)  电话
   - address(s) 收货地址
   - order(i)  排序
   - is_default(b)  是否是缺省地址
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
  - result	新建地址记录编号
</pre>


### 1.4 收货地址更新

updateCargoAddress(id,**kwargs)

#### 描述:


##### Request
<pre>
URL: /api/m/cargo-address
Medthod:    PUT
Headers:    token
Character Encoding: utf-8
Content-Type: x-www-form-urlencoded
Query Parameters:
   - id(s)               记录编号 
   - name(s)    [可选]    收货人
   - phone(s)   [可选]    电话
   - address(s) [可选]    收货地址
   - order(i)   [可选]    排序
   - is_default(i) [可选] 是否是缺省地址 0:no, 1: yes
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
  - result	记录编号
</pre>

##### Remarks

### 1.5 地址删除

removeCargoAddress(id,**kwargs)

#### 描述:


##### Request
<pre>
URL: /api/m/cargo-address
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
# 订单管理接口

> version: 1.0  
> 
> zhangbin  2018.10.18


# 1. 订单接口定义

<span id="1.1"/>

## 1.订单 
### 1.1 订单记录查询 (多)

getOrdersList()

#### 描述:


##### Request
<pre>
URL: /api/m/orders/list
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
  - result	(array)
    - id(s)             记录编号
    - serial(s)         订单流水号
    - pay_serial(s)     支付流水号
    - pay_seller(s)     商家操作者
    - order(i)          排序
    - update_time(i)    更新或创建时间
    - cargo_address(object)  收货地址
      - name (s)        联系人名
      - phone (s)       电话
      - address(s)      地址
    - status_list (array)   当前状态
      - issue_time(n)       发生时间
      - status(s)       inited,payed,delivering,finished,cancelled
      - comment(s)      说明（可以是留言、物流信息、订单说明等等）
    - product_list (array)
      - sku(s)          商品编码
      - number(n)       数量
      - price(f)        价格
      - amount(f)       总金额
    
</pre>

### 1.2 订单信息查询 (单对象)

getOrdersInfo(id)

#### 描述:


##### Request
<pre>
URL: /api/m/orders
Medthod:    GET
Headers:    token
Character Encoding: utf-8
Content-Type: x-www-form-urlencoded
Query Parameters:
   - id(s)  订单记录编号
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
  - result	(object)
    - id(s)             记录编号
    - serial(s)         订单流水号
    - pay_serial(s)     支付流水号
    - pay_seller(s)     商家操作者
    - order(i)          排序
    - update_time(i)    更新或创建时间
    - cargo_address(object)  收货地址
      - name (s)        联系人名
      - phone (s)       电话
      - address(s)      地址
    - status_list (array)   当前状态
      - issue_time(n)       发生时间
      - status(s)       inited,payed,delivering,finished,cancelled
      - comment(s)      说明（可以是留言、物流信息、订单说明等等）
    - product_list (array)
      - sku(s)          商品编码
      - number(n)       数量
      - price(f)        价格
      - amount(f)       总金额


</pre>

### 1.3 地址创建

createOrders(**kwargs)

#### 描述:
用户提交订单，目前仅支持单个产品产生单个订单，不支持多产品生成订单。

##### Request
<pre>
URL: /api/m/orders
Medthod:    POST
Headers:    token
Character Encoding: utf-8
Content-Type: x-www-form-urlencoded
Query Parameters:
   - sku(s)     产品编码
   - number(n)  数量
   - comment(s) 说明
   - cargo_address_id(s)    收货地址编号（从地址列表中选择）
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
  - result	新建的订单编号
</pre>


### 1.4 撤销订单

cancelOrders(id,reason)

#### 描述:
在订单创建未支付之前允许用户撤销订单

##### Request
<pre>
URL: /api/m/orders
Medthod:    DELETE
Headers:    token
Character Encoding: utf-8
Content-Type: x-www-form-urlencoded
Query Parameters:
   - id(s)              记录编号 
   - comment(s)         说明
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
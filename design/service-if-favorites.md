# 收藏夹管理接口

> version: 1.0  
> 
> zhangbin  2018.10.22


# 1. 服务接口定义

<span id="1.1"/>

## 1.商品收藏夹 
### 1.1 列表查询 (多)

getFavoritesList()

#### 描述:


##### Request
<pre>
URL: /api/m/favorite/list
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
  - result	array
    - id(s)             记录编号
    - sku(s)            商品编码
    - number(n)         数量
    - create_time(n)    创建时间
    - order(n)          排序
    - comment(s)        备注
    - product
      - sku             代码
      - name            产品名称
      - category        种类
      - price           单价
      - description     描述
      - url             外连接 
      - image_url       产品图像
      

</pre>

### 1.2 收藏商品查询 (单对象)

getFavorite(id)

#### 描述:


##### Request
<pre>
URL: /api/m/favorite
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
    - id(s)             记录编号
    - sku(s)            商品编码
    - name(s)           商品名称
    - category(s)       类型
    - price(f)          价格
    - description(s)    商品描述
    - url(s)            产品链接
    - image_url(s)      产品图像链接 
    - number(n)         数量
    - create_time(n)    创建时间
    - order(n)          排序

</pre>

### 1.3 收藏产品创建

createFavorite(product_id)

#### 描述:
用户添加产品到自己的收藏夹，数量默认:1 

##### Request
<pre>
URL: /api/m/favorite
Medthod:    POST
Headers:    token
Character Encoding: utf-8
Content-Type: x-www-form-urlencoded
Query Parameters:
   - sku(s)   商品编号
   - comment(s)(可选)  备注
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
  - result	新建添加的收藏记录编号
</pre>


### 1.4 收藏删除

removeFavorite(id)

#### 描述:


##### Request
<pre>
URL: /api/m/favorite
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
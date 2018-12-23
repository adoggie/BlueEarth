# 产品信息接口

> version: 1.0  
> 
> zhangbin  2018.10.23


# 1. 服务接口定义

<span id="1.1"/>

## 1.产品 
### 1.1 产品列表查询 (多)

getProductList(category,limit)

#### 描述:


##### Request
<pre>
URL: /api/m/product/list
Medthod:    GET
Headers:    token
Character Encoding: utf-8
Content-Type: x-www-form-urlencoded
Query Parameters:
   - category（s)(optional)  产品分类， 未提供表示全部产品
   
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
  - result	（array)
    - id(s)             记录编号
    - sku(s)            产品编码
    - name(s)           品名
    - category(s)       种类
    - price(f)          价格
    - description(s)    产品描述
    - url(s)            产品url链接介绍
    - image_url(s)      产品图片链接
    - slide_image_url(s) 轮播产品链接
    - content(s)        内容介绍
    - update_time(i)    更新时间
   
</pre>

### 1.2 产品查询 (单对象)

getProductDetail(sku)

#### 描述:


##### Request
<pre>
URL: /api/m/product
Medthod:    GET
Headers:    token
Character Encoding: utf-8
Content-Type: x-www-form-urlencoded
Query Parameters:
   - sku(s)  产品编码
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
     - id(s)            记录编号
    - sku(s)            产品编码
    - name(s)           品名
    - category(s)       种类
    - price(f)          价格
    - description(s)    产品描述
    - url(s)            产品url链接介绍
    - image_url(s)      产品图片链接
    - slide_image_url(s) 轮播产品链接
    - content(s)        内容介绍
    - update_time(i)    更新时间
    - content_urls:   (array) 内容图片数组
      - image_url_2
      - image_url_2
</pre>

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
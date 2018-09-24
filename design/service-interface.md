version: 1.0 
-----
* zhangbin
* 2018.9.23

> 创建第一个版本
> 

# 1. 服务接口定义

<span id="1.1"/>

## 1.1 微信端用户登录 
#### 名称:
userLogin( wx_id)
#### 描述:
微信请求获取用户信息成功之后，用微信用户编号进行系统登录。
返回用户token令牌。

##### Request
<pre>
URL: /api/m/ticket
Medthod: POST
Headers: 
Character Encoding: utf-8
Content-Type: x-www-form-urlencoded
Query Parameters:
   - wx_id 	微信用户id
   
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
  - result	登录token
</pre>

##### Examples:
<pre>
Request:
  /api/m/ticket	
  wx_id=wx_gwe1223332
    
Response:
  { 
    status:0,
    result: oiwurwurioqweuirqwerjqwewriu==
  }		
</pre>	

##### Remarks

<span id="1.2"/>

## 1.2 微信端用户添加设备 
#### 名称:
addDevice()
#### 描述:
用户输入设备ID(imei),电话号，管理密码进行设备添加。id,密码错误则拒绝添加

##### Request
<pre>
URL: /api/m/device
Medthod: POST
Headers: 
    - token : 用户令牌
Character Encoding: utf-8
Content-Type: x-www-form-urlencoded
Query Parameters:
   - device_id  设备编号 
   - password   密码
   - name       名称
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
  - result	设备id 
</pre>

##### Examples:
<pre>
Request:
  /api/m/device	
  - token: oiwurwurioqweuirqwerjqwewriu
  device_id=8600992121233123&password=9999&name=我的Pet
    
Response:
  { 
    status:0,
    result: 8600992121233123
  }		
</pre>	

##### Remarks


<span id="1.3"/>

## 1.3 更新设备信息 
#### 名称:
updateDevice(kvs)
#### 描述:
拥有设备的用户对设备信息进行修改更新 

##### Request
<pre>
URL: /api/m/device
Medthod: PUT
Headers: 
    - token : 用户令牌
Character Encoding: utf-8
Content-Type: x-www-form-urlencoded
Query Parameters:
   - device_id  设备编号 
   - *password   密码
   - *name       名称
   - *mobile     设备电话号
   - *admin_mobile   管理者电话，用于密码找回
   - *image      设备图像
   
   * 可选参数
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

##### Examples:
<pre>
Request:
  /api/m/device	
  - token: oiwurwurioqweuirqwerjqwewriu
  device_id=8600992121233123&password=9999&name=我的Pet&mobile=18601636345
    
Response:
  { 
    status:0,
    result: 
  }		
</pre>	

##### Remarks

<span id="1.4"/>
## 1.4 删除用户设备 
#### 名称:
removeDevice(device_id)
#### 描述:
> 用户删除指定的设备编号，同时将删除此设备的所有共享设备。如果被删除的是共享设备，则直接删除用户与设备关系。

##### Request
<pre>
URL: /api/m/device
Medthod: DELETE
Headers: 
  - token : 用户令牌
Character Encoding: utf-8
Content-Type: x-www-form-urlencoded
Query Parameters:
  - device_id  设备编号 
      
   * 可选参数
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

##### Examples:
<pre>
Request:
  /api/m/device	
  - token: oiwurwurioqweuirqwerjqwewriu
  device_id=8600992121233123
    
Response:
  { 
    status:0,
    result: 
  }		
</pre>	

##### Remarks

</pre>


<span id="1.5"/>
## 1.5 获取用户设备详情 
#### 名称:
getDeviceInfo(device_id)
#### 描述:
> 用户删除指定的设备编号，同时将删除此设备的所有共享设备。如果被删除的是共享设备，则直接删除用户与设备关系。

##### Request
<pre>
URL: /api/m/device
Medthod: GET
Headers: 
  - token : 用户令牌
Character Encoding: utf-8
Content-Type: x-www-form-urlencoded
Query Parameters:
  - device_id  设备编号 
      
   * 可选参数
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
    - device_id         设备编号
    - device_type       设备类型
    - imei              
    - sim
    - mobile            sim卡电话号
    - admin_mobile      管理用户电话
    - name              设备名称
    - image             图像
    - update_time       更新/创建时间
    - is_share_device   是否是共享设备
    - share_user_id     
    - share_device_link
    - 
</pre>

##### Examples:
<pre>
Request:
  /api/m/device	
  - token: oiwurwurioqweuirqwerjqwewriu
  device_id=8600992121233123
    
Response:
  { 
    status:0,
    result: {device_id,device_type,name,...}
  }		
</pre>	

##### Remarks

</pre>


<span id="1.6"/>
## 1.6 获取用户设备 
#### 名称:
queryDeviceList(kvs)
#### 描述:
> 获取用户的设备清单

##### Request
<pre>
URL: /api/m/device/list?s=..&order=+name,+update_time
Medthod: GET
Headers: 
  - token : 用户令牌
Character Encoding: utf-8
Content-Type: x-www-form-urlencoded
Query Parameters:
      
   * 可选参数
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
    - device_id         设备编号
    - device_type       设备类型
    - imei              
    - sim
    - mobile            sim卡电话号
    - admin_mobile      管理用户电话
    - name              设备名称
    - image             图像
    - update_time       更新/创建时间
    - is_share_device   是否是共享设备
    - share_user_id     
    - share_device_link
</pre>

##### Examples:
<pre>
Request:
  /api/m/device	
  - token: oiwurwurioqweuirqwerjqwewriu
 Response:
  { 
    status:0,
    result: {device_id,device_type,name,...}
  }		
</pre>	

##### Remarks

</pre>

# 2. 共享设备
<span id="2.1"/>
## 2.1 创建共享设备 
#### 名称:
createShareDevice(device_id, name ,expire,password,userlimit)

#### 描述:
> 用户创建共享设备，如果用户的设备已经是共享设备了，则不创建，直接返回已是共享设备的share_id.

##### Request
<pre>
URL: /api/m/share-device
Medthod: POST
Headers: 
  - token : 用户令牌
Character Encoding: utf-8
Content-Type: x-www-form-urlencoded
Query Parameters:
  - device_id  设备编号 
  - *name   共享设备别名
  - *expire  共享设备过期时间 30m,1h,5h,10h,1d,15d,1m,永久(默认)
  - *password 访问密码，默认: 无密码
  - *user_limit 最多访问用户数量限制,默认： 无限制 
  * 可选参数
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

##### Examples:
<pre>
Request:
  /api/m/share-device	
  - token: oiwurwurioqweuirqwerjqwewriu
  device_id=8600992121233123&name=王扶风的宠物&password=9999&user_limit=0&expire=0
    
Response:
  { 
    status:0,
    result: A9000123312211
  }		
</pre>	

##### Remarks

</pre>



<span id="2.2"/>
## 2.2 删除共享设备
#### 名称:
> removeShareDevice(share_id)

#### 描述:
> 用户删除自己创建的设备共享，一旦删除共享，将同时删除所有被分享出去的设备 。
> 设备分享S，A—>B,B->C,当A删除S时，B和C的S设备都将被删除。 


##### Request
<pre>
URL: /api/m/share-device
Medthod: DELETE
Headers: 
  - token : 用户令牌
Character Encoding: utf-8
Content-Type: x-www-form-urlencoded
Query Parameters:
  - share_id  设备编号 
  * 可选参数
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

##### Examples:
<pre>
Request:
  /api/m/share-device	
  - token: oiwurwurioqweuirqwerjqwewriu
  share_id=ab00919212322
    
Response:
  { 
    status:0,
    result:
  }		
</pre>	

##### Remarks

</pre>


<span id="2.3"/>

## 2.3 用户添加共享设备
#### 名称:
> addShareDevice(share_id)

#### 描述:
> 当A用户将设备通过微信分享给好友B时，B点击分享链接，确认添加共享设备到自己的设备列表中。
> 如果设备设置了有效期和最大用户数则进行提示设备共享链接无效，如果有密码，则提示用户输入分享密码，通过则加入到当前用户的设备列表中。


##### Request
<pre>
URL: /api/m/share-device/take
Medthod: POST
Headers: 
  - token : 用户令牌
Character Encoding: utf-8
Content-Type: x-www-form-urlencoded
Query Parameters:
  - share_id  设备编号 
  * 可选参数
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
  - result	设备编号
</pre>

##### Examples:
<pre>
Request:
  /api/m/share-device/take
  - token: oiwurwurioqweuirqwerjqwewriu
  share_id=ab00919212322
    
Response:
  { 
    status:0,
    result:
  }		
</pre>	

##### Remarks

</pre>


<span id="2.4"/>

## 2.4 获取共享设备信息
#### 名称:
> getShareDeviceInfo(share_id)

#### 描述:
> 当A用户将设备通过微信分享给好友B时，B点击分享链接，确认添加共享设备到自己的设备列表中。
> 如果设备设置了有效期和最大用户数则进行提示设备共享链接无效，如果有密码，则提示用户输入分享密码，通过则加入到当前用户的设备列表中。


##### Request
<pre>
URL: /api/m/share-device
Medthod: GET
Headers: 
  - token : 用户令牌
Character Encoding: utf-8
Content-Type: x-www-form-urlencoded
Query Parameters:
  - share_id  设备编号 
  * 可选参数
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
    - share_id  
    - name 
    - expire
    - user_limit
</pre>

##### Examples:
<pre>
Request:
  /api/m/share-device	
  - token: oiwurwurioqweuirqwerjqwewriu
  share_id=ab00919212322
    
Response:
  { 
    status:0,
    result: { name,user_limit,expire,share_id}
  }		
</pre>	

##### Remarks

</pre>


<span id="2.5"/>

## 2.5 获取共享设备信息
#### 名称:
> queryShareDeviceList()

#### 描述:
> 获取用户创建的所有共享设备列表

##### Request
<pre>
URL: /api/m/share-device/list
Medthod: GET
Headers: 
  - token : 用户令牌
Character Encoding: utf-8
Content-Type: x-www-form-urlencoded
Query Parameters:
  * 可选参数
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
  - result  array
    - share_id  
    - name 
    - expire
    - user_limit
</pre>

##### Examples:
<pre>
Request:
  /api/m/share-device	
  - token: oiwurwurioqweuirqwerjqwewriu
   
Response:
  { 
    status:0,
    result: [ {name,user_limit,expire,share_id}, 
                .. 
            ]
  }		
</pre>	

##### Remarks

</pre>


# 3. 监控接口

<span id="3.1"/>

## 3.1 获取设备当前位置信息
#### 名称:
> getCurrentPosition(device_id)

#### 描述:
> 获取用户创建的所有共享设备列表

##### Request
<pre>
URL: /api/m/device/pos/last
Medthod: GET
Headers: 
  - token : 用户令牌
Character Encoding: utf-8
Content-Type: x-www-form-urlencoded
Query Parameters:
  - device_id  设备编号
    * 可选参数
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
    - device_id     设备编号
    - device_type   设备类型
    - name          设备名称
    - lon           经度
    - lat           纬度
    - heading       方向
    - speed         速度
    - satellite     卫星数量
    - timestamp     gps定位时间
    - position_source   定位方式
    - lon_bd        
    - lat_bd 
    - address       定位地址
    - located       是否定位
    - alarm         报警类型
    - alarm_name    报警名称
    - voltage       电压
    - gsm           gprs信号
    - charging      是否充电
    - acc           是否车载电源开启
    - update_time   设备更新时间
    - fortify       是否已设防
</pre>

##### Examples:
<pre>
Request:
  /api/m/device/pos/last	
  - token: oiwurwurioqweuirqwerjqwewriu
   
Response:
  { 
    status:0,
    result: {..}
  }		
</pre>	

##### Remarks

</pre>

<span id="3.2"/>

## 3.2 获取设备历史轨迹
#### 名称:
> getTracePosition(device_id)

#### 描述:
> 获取用户创建的所有共享设备列表

##### Request
<pre>
URL: /api/m/device/pos/trace
Medthod: GET
Headers: 
  - token : 用户令牌
Character Encoding: utf-8
Content-Type: x-www-form-urlencoded
Query Parameters:
  - device_id  设备编号
  - start       开始时间
  - end         结束时间
  - *granule     时间颗粒 默认: 5 分钟
    * 可选参数
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
  - result  array
    - device_id     设备编号
    - device_type   设备类型
    - name          设备名称
    - lon           经度
    - lat           纬度
    - heading       方向
    - speed         速度
    - satellite     卫星数量
    - timestamp     gps定位时间
    - position_source   定位方式
    - lon_bd        
    - lat_bd 
    - address       定位地址
    - located       是否定位
    - alarm         报警类型
    - alarm_name    报警名称
    - voltage       电压
    - gsm           gprs信号
    - charging      是否充电
    - acc           是否车载电源开启
    - update_time   设备更新时间
    - fortify       是否已设防
</pre>

##### Examples:
<pre>
Request:
  /api/m/device/pos/last	
  - token: oiwurwurioqweuirqwerjqwewriu
   
Response:
  { 
    status:0,
    result: [{..},..]
  }		
</pre>	

##### Remarks

</pre>

# 4. 设备控制
<span id="4.1"/>

## 4.1 获取设备配置信息
#### 名称:
> getDeviceConfig(device_id)

#### 描述:
> 

##### Request
<pre>
URL: /api/m/device/config
Medthod: GET
Headers: 
  - token : 用户令牌
Character Encoding: utf-8
Content-Type: x-www-form-urlencoded
Query Parameters:
  - device_id  设备编号
    * 可选参数
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
    - device_id     设备编号
    - device_type   设备类型
    - name          设备名称
    - imei 
    - sim
    - ver
    - sos_1
    - sos_2
    - sos_3
    - sos_4
    - server_mode
    - server_ip
    - server_domain
    - server_port
    - pos_mode
    - gps_timer
    - lbs_timer
    - heartbeat_timer
    - battery_alarm_enable
    - shake_alarm_enable
    - sos_alarm_enable
    - fence_alarm_enable
</pre>

##### Examples:
<pre>
Request:
  /api/m/device/config	
  - token: oiwurwurioqweuirqwerjqwewriu
  device_id= 86091233121
Response:
  { 
    status:0,
    result: {..}
  }		
</pre>	

##### Remarks

</pre>


<span id="4.2"/>

## 4.2 设置设备配置信息
#### 名称:
> setDeviceConfig(device_id，kvs)

#### 描述:
> 更新设备的配置参数，可以一次多个或者一个参数

##### Request
<pre>
URL: /api/m/device/config
Medthod: GET
Headers: 
  - token : 用户令牌
Character Encoding: utf-8
Content-Type: x-www-form-urlencoded
Query Parameters:
  - device_id  设备编号
    - *sos_1
    - *sos_2
    - *sos_3
    - *sos_4
    - *server_mode
    - *server_ip
    - *server_domain
    - *server_port
    - *pos_mode
    - *gps_timer
    - *lbs_timer
    - *heartbeat_timer
    - *battery_alarm_enable
    - *shake_alarm_enable
    - *sos_alarm_enable
    - *fence_alarm_enable

    * 可选参数
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

##### Examples:
<pre>
Request:
  /api/m/device/config	
  - token: oiwurwurioqweuirqwerjqwewriu
  device_id= 86091233121
Response:
  { 
    status:0,
    result: {..}
  }		
</pre>	

##### Remarks
</pre>


## 4.3 获取设备围栏信息
#### 名称:
> getFence(device_id)

#### 描述:
> 一个设备一个围栏

##### Request
<pre>
URL: /api/m/device/fence
Medthod: GET
Headers: 
  - token : 用户令牌
Character Encoding: utf-8
Content-Type: x-www-form-urlencoded
Query Parameters:
  - device_id  设备编号

    * 可选参数
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
    - device_id 
    - index
    - name
    - type   circle or rect
    - enable 
    - cx
    - cy
    - radius  单位米
    - inout     围栏设置入还是出围栏检测  IN / OUT
    - alaram_type
    
</pre>

##### Examples:
<pre>
Request:
  /api/m/device/fence	
  - token: oiwurwurioqweuirqwerjqwewriu
  device_id= 86091233121
Response:
  { 
    status:0,
    result: {..}
  }		
</pre>	

##### Remarks
</pre>


## 4.4 更新设备围栏信息
#### 名称:
> updateFence(device_id)

#### 描述:
> 设置围栏的信息，包括可以令围栏停用、启用

##### Request
<pre>
URL: /api/m/device/fence
Medthod: PUT
Headers: 
  - token : 用户令牌
Character Encoding: utf-8
Content-Type: x-www-form-urlencoded
Query Parameters:
    - fence_id  设备编号
    - name
    - type   circle or rect
    - enable 
    - cx
    - cy
    - radius  单位米
    - inout     围栏设置入还是出围栏检测  IN / OUT
    - alaram_type

    * 可选参数
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

##### Examples:
<pre>
Request:
  /api/m/device/fence	
  - token: oiwurwurioqweuirqwerjqwewriu
  fence_id= 86091233121
Response:
  { 
    status:0,
    result: 
  }		
</pre>	

##### Remarks
</pre>

# 5. 控制命令
## 5.1 开始远程录音
#### 名称:
> startAudioRecord(device_id)

#### 描述:
> 启动远程录音

##### Request
<pre>
URL: /api/m/command/audio-record
Medthod: POST
Headers: 
  - token : 用户令牌
Character Encoding: utf-8
Content-Type: x-www-form-urlencoded
Query Parameters:
    - device_id  设备编号
    - duration   录音时长 
    * 可选参数
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

##### Examples:
<pre>
Request:
  /api/m/command/audio-record
  - token: oiwurwurioqweuirqwerjqwewriu
  device_id = 86091233121
Response:
  { 
    status:0,
    result: 
  }		
</pre>	

##### Remarks
</pre>



startAudioRecord(device_id,duration)  开始录音
getLastAudioRecord(device_id)       获取最近的录音记录
getAudioRecordList(device_id,start,end) 获取设备的录音记录


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
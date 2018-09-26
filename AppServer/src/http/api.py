#coding:utf-8

import json
from flask import Flask,request,g
from flask import Response

from flask import render_template
from mantis.fundamental.application.app import  instance
from mantis.fundamental.flask.webapi import ErrorReturn,CR
from mantis.fundamental.utils.timeutils import timestamp_current
from mantis.BlueEarth import model
from mantis.fundamental.utils.useful import object_assign,hash_object
from token import login_check,AuthToken
from mantis.BlueEarth.errors import ErrorDefs
from bson import ObjectId
from mantis.BlueEarth import constants
from mantis.BlueEarth.types import FenceType


def get_ticket():
    """上传微信用wx_id,获取登录token"""
    main = instance.serviceManager.get('main')
    account = request.values.get('wx_id')
    user = model.User.get_or_new(platform='wx',account=account)
    user.platform = 'wx'
    user.last_login = timestamp_current()
    user.save()

    auth = AuthToken()
    auth.login_time = timestamp_current()
    auth.user_id = user.account
    auth.user_name = user.name
    auth.platform = 'wx'
    user.token = auth.encode()

    user.save()
    return CR(result=user.token).response

@login_check
def add_device():
    user = g.user
    device_id = request.values.get('device_id')
    password = request.values.get('password')
    name = request.values.get('name')
    device  = model.Device.get(device_id = device_id)
    if not device:
        return ErrorReturn(ErrorDefs.ObjectNotExist).response

    # 检测设备是否已经添加了
    rel = model.DeviceUserRelation.get(user_id= str(user.id),device_id=device_id )
    if rel:
        return CR(result=str(rel.id)).response

    if password != device.password:
        return ErrorReturn(ErrorDefs.PasswordError).response

    rel = model.DeviceUserRelation()
    rel.user_id = user.id
    rel.device_id = device_id
    rel.update_time = timestamp_current()
    rel.save()
    return CR(result=rel.id).response


@login_check
def update_device():
    user = g.user
    device_id = request.values.get('device_id')
    password = request.values.get('password')
    name = request.values.get('name')
    mobile =request.values.get('mobile') # 设备内置电话号码
    admin_mobile = request.values.get('admin_mobile') # 管理人手机号
    image = request.values.get('image')

    device = model.Device.get(device_id=device_id)
    if not device:
        return ErrorReturn(ErrorDefs.ObjectNotExist).response

    # 检测设备是否已经添加了
    rel = model.DeviceUserRelation.get(user_id=str(user.id), device_id=device_id)
    if not rel: # 设备不存在
        return ErrorReturn(ErrorDefs.ObjectNotExist).response
    if name:
        rel.device_name = name
    if rel.is_share_device: # 共享设备的话，用户只能修改名称
        if name:
            rel.save()
        return CR().response
    kwargs ={}
    if password:
        kwargs['password'] = password
    if mobile:
        kwargs['mobile'] = mobile
    if admin_mobile:
        kwargs['admin_mobile'] = admin_mobile
    if image:
        kwargs['image'] = image

    rel.update(**kwargs)

    return CR().response

@login_check
def remove_device():
    """删除设备时，要连同删除被分享出去的设备"""
    user = g.user
    device_id = request.values.get('device_id')
    rel = model.DeviceUserRelation.get(user_id=str(user.id), device_id=device_id)
    if not rel:  # 设备不存在
        return CR(result=[]).response

    if not rel.is_share_device:
        # 查找设备的分享链接
        link = model.SharedDeviceLink.get(user_id=user.id,device_id=device_id)
        coll = model.DeviceUserRelation.collection()
        coll.delete_many({'is_share_device':True,'share_device_link':link.id})

        link.delete()

    rel.delete()

    return CR().response

@login_check
def get_device_info():
    """"""
    user = g.user
    device_id = request.values.get('device_id')
    rel = model.DeviceUserRelation.get(user_id=str(user.id), device_id=device_id)
    if not rel:  # 设备不存在
        return ErrorReturn(ErrorDefs.ObjectNotExist).response
    device  = model.Device.get(device_id=device_id)

    result = dict(
        device_id = device_id,
        device_type = device.device_type,
        imei = device.imei,
        sim = device.sim ,
        mobile = device.mobile,
        admin_mobile = device.admin_mobile,
        name = rel.device_name,
        image = rel.device_image,
        update_time = rel.update_time,
        is_share_device = rel.is_share_device,
        share_user_id = rel.share_user_id,
        share_device_link = rel.share_device_link
    )
    return CR(result=result).response

@login_check
def get_device_list():
    """查询设备列表"""
    user = g.user
    rs = model.DeviceUserRelation.collection().find({'user_id':user._id})
    result = []
    for r in rs:
        rel = model.DeviceUserRelation()
        rel.assign(r)
        device = model.Device.get(device_id=r['device_id'])
        obj = dict(
            device_id= device.device_id,
            device_type=device.device_type,
            imei=device.imei,
            sim=device.sim,
            mobile=device.mobile,
            admin_mobile=device.admin_mobile,
            name=rel.device_name,
            image=rel.device_image,
            update_time=rel.update_time,
            is_share_device=rel.is_share_device,
            share_user_id=rel.share_user_id,
            share_device_link=rel.share_device_link
        )
        result.append(obj)
    return CR(result=result).response

@login_check
def create_share_device():
    """创建设备共享"""
    user = g.user
    device_id = request.values.get('device_id')
    name = request.values.get('name')
    expire = request.values.get('expire',0,type=int)   # 过期时间
    password = request.values.get('password')
    user_limit = request.values.get('user_limit',0,type=int)

    #1.设备是否存在
    #2.是否已创建共享设备
    rel = model.DeviceUserRelation.get(user_id = user.id,device_id=device_id)
    if not rel:
        return ErrorReturn(ErrorDefs.ObjectNotExist,u'设备不存在').response

    link = model.SharedDeviceLink.get(user_id=user.id, device_id=device_id)
    if  rel:
        return CR(result=link.id).response
    if not password :
        password  = ''
    link = model.SharedDeviceLink()
    link.user_id = user.id
    link.device_id = device_id
    link.name = name
    link.expire_time = expire
    link.password = password
    link.user_limit = user_limit
    link.create_time = timestamp_current()
    link.save()

    return CR(result=link.id).response


@login_check
def remove_share_device():
    """删除设备共享, 共享发起人删除共享的设备，导致所有的共享连接失效"""

    user = g.user
    share_id = request.values.get('share_id')
    link = model.SharedDeviceLink.get(user_id=str(user.id), _id= ObjectId(share_id))
    if not link:  # 设备不存在
        return ErrorReturn(ErrorDefs.ObjectNotExist).response
    # 查找设备的分享链接
    coll = model.DeviceUserRelation.collection()
    coll.delete_many({'is_share_device': True, 'share_device_link': link.id})

    link.delete()
    return CR().response

@login_check
def take_share_device():
    """用户接收共享设备，添加成为自己的设备
        如果设置了密码，且用户未上传密码，则提示密码输入
        @:return 返回新设备id
    """
    user = g.user
    share_id = request.values.get('share_id')
    password = request.values.get('password')
    link = model.SharedDeviceLink.get(_id = ObjectId(share_id))
    if not link:
        return ErrorReturn(ErrorDefs.ObjectNotExist).response
    # 共享设备是否是自己添加好的设备
    rel = model.DeviceUserRelation.get(user_id =user.id,device_id = link.device_id)
    if rel:
        return ErrorReturn(ErrorDefs.ObjectHasExist).response
    # 共享设备是否过期
    if link.expire_time and link.expire_time < timestamp_current():
        return ErrorReturn(ErrorDefs.ResExpired).response
    # 访问上限
    if link.user_limit:
        num = model.DeviceUserRelation.collection().find({'share_device_link':link._id}).count()
        if num >= link.user_limit:
            return ErrorReturn(ErrorDefs.ReachLimit).response
    #是否要提供密码
    if password != link.password:
        return ErrorReturn(ErrorDefs.NeedPassword).response
    #创建设备
    device = model.DeviceUserRelation()
    device.user_id = user.id
    device.device_id = link.device_id
    device.device_name = link.name
    device.update_time = timestamp_current()
    device.is_share_device = True
    device.share_user_id = link.user_id
    device.share_device_link = link.id
    device.save()
    return CR(result= str(device.id) ).response

@login_check
def get_share_device_info():
    """查询本人创建的共享设备信息
    """
    user = g.user
    share_id = request.values.get('share_id')
    link = model.SharedDeviceLink.get(user_id=user.id,_id=ObjectId(share_id))
    if not link:
        return ErrorReturn(ErrorDefs.ObjectNotExist).response
    device = model.Device.get(device_id=link.device_id)
    rel = model.DeviceUserRelation.get(user_id=user.id,device_id=link.device_id)
    result = dict(
        device_id=device.device_id,
        device_type=device.device_type,
        imei=device.imei,
        sim=device.sim,
        mobile=device.mobile,
        admin_mobile=device.admin_mobile,
        name= link.name,
        image=link.image,
        update_time=rel.update_time,
        is_share_device=rel.is_share_device,
        share_user_id=rel.share_user_id,
        share_device_link=rel.share_device_link
    )
    return CR(result=result).response

@login_check
def get_share_device_list():
    """查询本人创建的所有共享设备列表
    """
    user = g.user
    links = model.SharedDeviceLink.find(user_id=user.id)
    result=[]
    for link in links:
        device = model.Device.get(device_id=link.device_id)
        rel = model.DeviceUserRelation.get(user_id=user.id, device_id=link.device_id)
        data = dict(
            device_id=device.device_id,
            device_type=device.device_type,
            imei=device.imei,
            sim=device.sim,
            mobile=device.mobile,
            admin_mobile=device.admin_mobile,
            name=link.name,
            image=link.image,
            update_time=rel.update_time,
            is_share_device=rel.is_share_device,
            share_user_id=rel.share_user_id,
            share_device_link=rel.share_device_link
        )
        result.append(data)
    return CR(result=result).response



@login_check
def get_last_position():
    """查询设备最近的位置信息
    """
    user = g.user
    device_id = request.values.get('device_id')
    name = constants.DevicePositionLastest.format(device_id = device_id)
    redis = instance.serviceManager.get('redis')
    data = redis.hgetall(name)
    pos = model.Position()
    object_assign(pos,data)
    return CR(result=pos.__dict__).response

@login_check
def get_position_path():
    """查询设备历史轨迹点
        start - 开始时间
        end - 结束时间 , 最大时长不能超过 1 周
    """
    DAY = 3600 * 24
    WEEK = 3600 * 24 * 7

    user = g.user
    device_id = request.values.get('device_id')
    start = request.values.get('start',type=int)
    end = request.values.get('end')
    if not end :
        end = start + DAY

    if end - start > WEEK:
        return ErrorReturn(ErrorDefs.ReachLimit).response
    rel = model.DeviceUserRelation.get(user_id=user.id,device_id=device_id)
    if not rel:
        return ErrorReturn(ErrorDefs.ObjectNotExist,u'设备不存在').response
    coll = model.Position.collection()
    rs = coll.find({'device_id':device_id,'timestamp':{'$gte':start,'$lt':end}}).sort('timestamp',1)
    result =[]
    for r in list(rs):
        del r['_id']
        result.append(r)
    return CR(result=result).response


@login_check
def get_device_config():
    """查询设备配置参数
    """
    user = g.user
    device_id = request.values.get('device_id')
    conf= model.DeviceConfig.get(device_id=device_id)
    if not conf:
        return ErrorReturn(ErrorDefs.ObjectNotExist).response
    result = conf.dict()
    return CR(result=result).response

@login_check
def set_device_config():
    """设置设备配置参数
    """
    user = g.user
    device_id = request.values.get('device_id')
    data ={}
    for k,v in  request.args.items():
        data[k] = v

    conf = model.DeviceConfig.get_or_new(device_id=device_id)
    object_assign(conf,data)
    conf.server_port = int(conf.server_port)
    conf.gps_timer = int(conf.gps_timer)
    conf.lbs_timer = int(conf.lbs_timer)
    conf.heartbeat_timer = int(conf.heartbeat_timer)
    conf.battery_alarm_enable = int(conf.battery_alarm_enable)
    conf.shake_alarm_enable = int(conf.shake_alarm_enable)
    conf.sos_alarm_enable = int(conf.sos_alarm_enable)
    conf.fence_alarm_enable = int(conf.fence_alarm_enable)
    conf.save()

    device = model.Device.get(device_id=device_id)
    main = instance.serviceManager.get('main')
    cmds =[]
    cc = main.getCommandController(device.device_type)
    cmd = ''
    if 'server_mode' in request.values.keys():
        address = request.values.get('server_ip', '')
        port = request.values.get('server_port', 0)
        server_mode = request.values.get('server_mode','').lower()
        if  server_mode == 'ip':
            cmd = cc.setIpServer(address,port)
        elif server_mode =='domain':
            cmd = cc.setDomainServer(address,port)

    if cmd :  cmds.append(cmd)
    cmd = ''
    pos_mode = request.values.get('pos_mode')
    if pos_mode == 'smart':
        cmd = cc.setPositionModeSmart()
    elif pos_mode == 'timing':
        cmd = cc.setPositionModeTiming()

    if cmd: cmds.append(cmd)

    gps_timer = request.values.get('gps_timer')
    lbs_timer = request.values.get('lbs_timer')

    cmd = ''
    heartbeat_timer = request.values.get('heartbeat_timer')
    if heartbeat_timer:
        cmd = cc.setHeartBeat(heartbeat_timer)
    if cmd: cmds.append(cmd)

    # battery
    cmd = ''
    battery_alarm_enable = request.values.get('battery_alarm_enable')
    if battery_alarm_enable =='1':
        cmd = cc.enableBatteryAlarm()
    if battery_alarm_enable =='0':
        cmd = cc.disableBatteryAlarm()
    if cmd: cmds.append(cmd)

    # sos
    cmd = ''
    sos_alarm_enable = request.values.get('sos_alarm_enable')
    if sos_alarm_enable =='1':
        cmd = cc.enableSosAlarm()
    if sos_alarm_enable =='0':
        cmd = cc.disableSosAlarm()
    if cmd: cmds.append(cmd)

    # fence
    cmd = ''
    fence_alarm_enable = request.values.get('fence_alarm_enable')
    if fence_alarm_enable == '1':
        cmd = cc.enableFenceAlarm()
    if fence_alarm_enable == '0':
        cmd = cc.disableFenceAlarm()
    if cmd: cmds.append(cmd)

    # sos
    cmd =''
    sos_1 = request.values.get('sos_1')
    sos_2 = request.values.get('sos_2')
    sos_3 = request.values.get('sos_3')
    sos_4 = request.values.get('sos_4')

    args = filter(lambda _:_,(sos_1,sos_2,sos_3,sos_4))
    if args:
        cmd = cc.setSos(*args)
    if cmd: cmds.append(cmd)

    # send all out
    for cmd in cmds :
        main.sendCommand(device_id, cmd)

    return CR().response

@login_check
def get_device_fence():
    """获得设备的围栏参数
    """
    user = g.user
    device_id = request.values.get('device_id')
    fence = model.Fence.get(device_id=device_id)
    if not fence:
        return ErrorReturn(ErrorDefs.ObjectNotExist).response
    result = fence.dict()
    return CR(result=result).response

@login_check
def set_device_fence():
    """设置设备的围栏参数
    """
    user = g.user
    device_id = request.values.get('device_id')
    data = {}
    for k, v in request.args.items():
        data[k] = v

    fence = model.Fence.get_or_new(device_id=device_id)
    object_assign(fence,data)
    if fence.type not in FenceType.ALL:
        return ErrorReturn(ErrorDefs.ParameterInvalid).response
    fence.index = int(fence.index)
    fence.enable = int(fence.enable)
    fence.cx = float(fence.cx)
    fence.cy = float(fence.cy)
    fence.radius = int(fence.radius)
    fence.x1 = float(fence.x1)
    fence.y1 = float(fence.y1)
    fence.x2 = float(fence.x2)
    fence.y2 = float(fence.y2)
    fence.alarm_type = int(fence.alarm_type)



    device = model.Device.get(device_id = device_id)
    main = instance.serviceManager.get('main')
    # 发送设置围栏命令
    cmd = ''
    cc = main.getCommandController(device.device_type)
    if fence.type == FenceType.CIRCLE:
        cmd = cc.setCircleFence(fence.cx,fence.cy,fence.radius,fence.inout)
    if cmd:
        main.sendCommand(device_id,cmd)
    fence.save()
    return CR().response

@login_check
def cmd_start_audio_record():
    """启动远程录像
    """
    user = g.user
    device_id = request.values.get('device_id')
    main = instance.serviceManager.get('main')
    device = model.Device.get(device_id=device_id)
    cc = main.getCommandController(device.device_type)
    cmd = cc.start_audio_record()
    main.sendCommand(device_id, cmd)

@login_check
def cmd_position_now_gps():
    """立即定位
    """
    user = g.user
    device_id = request.values.get('device_id')
    main = instance.serviceManager.get('main')
    device = model.Device.get(device_id=device_id)
    cc = main.getCommandController(device.device_type)
    cmd = cc.positionNowGps()
    main.sendCommand(device_id, cmd)

@login_check
def cmd_position_now_lbs():
    """立即定位
    """
    user = g.user
    device_id = request.values.get('device_id')
    main = instance.serviceManager.get('main')
    device = model.Device.get(device_id=device_id)
    cc = main.getCommandController(device.device_type)
    cmd = cc.positionNowLbs()
    main.sendCommand(device_id, cmd)

@login_check
def cmd_position_now():
    """立即定位
    """
    user = g.user
    device_id = request.values.get('device_id')
    main = instance.serviceManager.get('main')
    device = model.Device.get(device_id=device_id)
    cc = main.getCommandController(device.device_type)
    cmd = cc.positionNowLbs()
    main.sendCommand(device_id, cmd)
    cmd = cc.positionNowGps()
    main.sendCommand(device_id, cmd)
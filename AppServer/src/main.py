# coding:utf-8


import os,sys
from mantis.fundamental.utils.useful import singleton
from mantis.fundamental.application.app import instance
from mantis.trade.service import TradeService,TradeFrontServiceTraits,ServiceType,ServiceCommonProperty
from optparse import OptionParser
from server import Server
from vendor.concox.packet import NetWorkPacketAllocator
from vendor.concox.message import MessageOnlineCommandAllocator

class MainService(TradeService):
    def __init__(self,name):
        TradeService.__init__(self,name)
        self.logger = instance.getLogger()
        self.servers = {}
        self.adapters ={}



    def init(self, cfgs,**kwargs):
        # self.parseOptions()
        super(MainService,self).init(cfgs)
        for svrcfg in self.cfgs.get('servers',[]):
            server = Server().init(svrcfg)
            self.servers[server.name] = server



        generator = RedisIdGenerator().init('be.device.sequence')

        NetWorkPacketAllocator().setSequenceGenerator(generator)
        MessageOnlineCommandAllocator().setSequenceGeneroator(generator)

    def parseOptions(self):
        command = ''
        if len(sys.argv) < 2:
            print 'Error: Command Must Be (CREATE,LIST,PULL,UPLOAD,REMOVE AND RUN ).'
            raise RuntimeError()
        command = sys.argv[1].lower()
        if command not in ('create','list','pull','upload','remove','run'):
            return False

        parser = OptionParser()
        parser.add_option("--user",dest='user')
        parser.add_option("--remote",action='store_false',dest='isremote')   # 策略编号

        parser.add_option("--launcher_id",dest='launcher') # 加载器编号
        args = sys.argv[2:]
        (options, args) = parser.parse_args(args)
        if len(args)==0:
            print 'Error: strategy name missed.'
            return False

    def setupFanoutAndLogHandler(self):
        from mantis.trade.log import TradeServiceLogHandler
        self.initFanoutSwitchers(self.cfgs.get('fanout'))
        handler = TradeServiceLogHandler(self)
        self.logger.addHandler(handler)

    def start(self,block=True):
        TradeService.start(self)
        for server in self.servers:
            server.start()

    def stop(self):
        TradeService.stop(self)

    def initCommandChannels(self):
        TradeService.initCommandChannels(self)
        # channel = self.createServiceCommandChannel(CommandChannelTradeAdapterLauncherSub,open=True)
        # self.registerCommandChannel('trade_adapter_launcher',channel)

    def deviceOnline(self,adatper):
        self.adapters[adatper.device_id] = adatper

    def deviceOffline(self,adapter):
        del self.adapters[adapter.adatper.device_id]

    def sendCommand(self,device_id,command):
        """
        在线设备即刻发送，离线设备寄存发送命令

        """
        key = 'deivce.command.queue.{}'.format(device_id)
        redis = instance.datasourceManager.get('redis').conn
        data = ''
        if isinstance(command,str):
            data = command
        else:
            data = command.bytes()
        redis.rpush(device_id,data)

    def sendDownStreamData(self, device_id,data):
        key = 'deivce.command.queue.{}'.format(device_id)
        redis = instance.datasourceManager.get('redis').conn
        redis.rpush(device_id, data)

@singleton
class RedisIdGenerator(object):
    """交易请求流水号生成器"""
    def __init__(self):
        self.req_id = 0
        self.redis = None
        self.service = None
        self.key = ''
        self.incr = 1


    def init(self,key,incr = 1):
        """从db/redis加载当前的值"""
        self.key = key
        self.incr = incr
        return self

    def next_id(self):
        """提供策略使用的request-id"""
        self.redis = instance.datasourceManager.get('redis').conn
        self.service = instance.serviceManager.get('main')
        request_id = self.redis.incrby(self.key,self.incr)
        return request_id

    next = next_id

"""
Redis
设备最新的位置、报警、心跳时间

Mongodb
各种运行、配置、日志信息 

Redis-Queue/Publish
消息推送、 设备在线命令推送

"""
# coding: utf-8

from mantis.fundamental.nosql.mongo import Connection
from mantis.BlueEarth import model


def get_database():
    db = Connection('BlueEarth').db
    return db

model.get_database = get_database

device = model.Device.create(device_id='868120201788186',device_type='gt03',name='测试机器-1')
device.save()

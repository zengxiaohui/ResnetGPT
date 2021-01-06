from pyminitouch import MNTDevice


_DEVICE_ID = 'FJH5T18A31026410'
device = MNTDevice(_DEVICE_ID)

# single-tap
device.tap([(400, 600)])
# multi-tap
device.tap([(400, 400), (600, 600)])
# set the pressure, default == 100
device.tap([(400, 600)], pressure=50)

# 可以直接用简洁的API调用minitouch提供的强大功能！

# 在使用完成后，需要显式调用stop方法将服务停止
device.stop()
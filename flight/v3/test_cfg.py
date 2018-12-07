import configparser

cfg = configparser.ConfigParser()

#生成实力后需要接入相关的配置文件
cfg.read('cfg_test.cfg')

sp_name = cfg.get('SmallPlane','name')
print(sp_name)

sp_width = cfg.getint('SmallPlane','width')

sp_pth = cfg.get('SmallPlane','img_pth')
print(sp_pth)
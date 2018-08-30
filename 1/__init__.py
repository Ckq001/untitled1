def testCase(platformName,platformVersion,deviceName,app,appPackage,appActivity,port):
  PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
  desired_caps = {}
  desired_caps['platformName'] = platformName #设置平台
  desired_caps['platformVersion'] = platformVersion #系统版本
  desired_caps['deviceName'] = deviceName #设备id
  desired_caps['autoLaunch'] = 'true' #是否自动启动
  desired_caps['app'] = PATH(app)#安装包路径，放在该py文件的目录下)
  desired_caps['appPackage'] = appPackage #包名
  desired_caps['appActivity'] = appActivity #启动的activity
  self.driver = webdriver.Remote('http://localhost:%s/wd/hub', desired_caps) % port
import werobot

robot = werobot.WeRoBot(token='qicaishuo1288')
robot.config["APP_ID"] = "wxe879a75619613e2b"
#robot.config["APP_SECRET"] = "你的 AppSecret"

@robot.text
def hello_world():
    return 'Hello World!'



# robot.config['HOST'] = '0.0.0.0'
# robot.config['PORT'] = 9090
# robot.run()

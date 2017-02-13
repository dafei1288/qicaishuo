from settings import robot

@robot.text
def hello_world():
    return 'Hello World!'


client = robot.client


client.create_menu({
    "button":[{
         "type": "click",
         "name": "今日歌曲",
         "key": "music"
    }]
})

@robot.key_click("music")
def music(message):
    return '你点击了“今日歌曲”按钮'
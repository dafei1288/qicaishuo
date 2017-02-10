from flask import Flask
from robot import robot
from werobot.contrib.flask import make_view

app = Flask(__name__)
app.add_url_rule(rule='/wechat/robot/',
                 endpoint='werobot',
                 view_func=make_view(robot),
                 methods=['GET', 'POST'])

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5050)

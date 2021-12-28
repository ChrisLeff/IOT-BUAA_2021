import json

from flask import Flask, request
from flask_cors import CORS
import apis.aep_device_status
import apis.aep_device_command

app = Flask(__name__)
CORS(app, supports_credentials=True)

body_base = '{ "productId": "15100261", "deviceId": "16749f24ae0e4d118f93b9d9eb2317b5"}'


body_motor_control = \
    '{"content": {"params": { "set_int": %s}, "serviceIdentifier": "motor_control" }, ' \
    '"deviceId": "16749f24ae0e4d118f93b9d9eb2317b5", ' \
    '"operator": "BUAA202116", ' \
    '"productId": "15100261", ' \
    '"ttl": 1, ' \
    '"deviceGroupId": null , ' \
    '"level": 1}'



@app.route('/get_temperature_humidity', methods=['POST', 'GET'])
def get_temperature_humidity():
    result = apis.aep_device_status.QueryDeviceStatusList('D4RcZL9S9Sf', 'ifuketHPjc', body_base)
    postForm = json.loads(result)
    str1 = str(postForm['deviceStatusList']).replace("\'", "\"")
    return str1


@app.route('/get_history_status_page', methods=['POST', 'GET'])
def get_history_status_page():
    if request.method == 'POST':
        print(request.form)

        begin_timestamp = str(1638954000000)
        end_timestamp =   str(1638954600000)
        # 这里是对时间戳进行一个初始化
        # 下面是对于相关参数的设置，具体的参数是从CTWing网站上对应下来的
        body_history = '{"productId": "15100261", ' \
                       '"deviceId":"16749f24ae0e4d118f93b9d9eb2317b5", ' \
                       '"begin_timestamp":"' + begin_timestamp + '", ' \
                       '"end_timestamp":"' + end_timestamp + '", ' \
                       '"page_size":200, ' \
                       '"page_timestamp": null}'
        result = apis.aep_device_status.getDeviceStatusHisInPage('D4RcZL9S9Sf', 'ifuketHPjc', body_history)
        postForm = json.loads(result)
        time = []
        temperature = []
        humidity = []
        datalist = postForm['deviceStatusList']
        total = {}
        for dit in datalist:
            time.append(dit['timestamp'])
            temperature.append(dit['temperature_data'])
            humidity.append(dit['humidity_data'])
        total['timestamp'] = time
        total['temperature_data'] = temperature
        total['humidity_data'] = humidity
        return str(total).replace("\'", "\"")


@app.route('/turn_motor_on', methods=['POST', 'GET'])
def turn_motor_on():
    result = apis.aep_device_command.CreateCommand('D4RcZL9S9Sf', 'ifuketHPjc', 'da940cf2c7484d59800d982b49ccecdd',
                                                   body_motor_control % "1")
    return result


@app.route('/turn_motor_off', methods=['POST', 'GET'])
def turn_motor_off():
    result = apis.aep_device_command.CreateCommand('D4RcZL9S9Sf', 'ifuketHPjc', 'da940cf2c7484d59800d982b49ccecdd',
                                                   body_motor_control % "0")
    return result



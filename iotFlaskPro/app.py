import json

from flask import Flask, request
import apis.aep_device_status
import apis.aep_device_command

app = Flask(__name__)

body_base = '{ "productId": "15099182", "deviceId": "78cb35a72bf840b0a6533d31531d8890"}'


body_motor_control = \
    '{"content": {"params": { "control_int": %s}, "serviceIdentifier": "motor_control" }, ' \
    '"deviceId": "78cb35a72bf840b0a6533d31531d8890", ' \
    '"operator": "kkkk", ' \
    '"productId": "15099182", ' \
    '"ttl": 1, ' \
    '"deviceGroupId": null , ' \
    '"level": 1}'


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/get_temperature_humidity')
def get_temperature_humidity():
    result = apis.aep_device_status.QueryDeviceStatusList('6Dbi6zVTAHc', 'OyB7a81dby', body_base)
    postForm = json.loads(result)
    return str (postForm['deviceStatusList'])


@app.route('/get_history_status_page', methods=['POST', 'GET'])
def get_history_status_page():
    if request.method == 'POST':
        print(request.form)
        begin_timestamp = request.form.get('begin_timestamp')
        end_timestamp = request.form.get('end_timestamp')
        # begin_timestamp = input()
        # end_timestamp = input()
        # begin_timestamp = str(1637856052000)
        # end_timestamp =   str(1637942452000)
        body_history = '{"productId": "15099182",' \
                       ' "deviceId": "78cb35a72bf840b0a6533d31531d8890",' \
                       ' "begin_timestamp":' + begin_timestamp + ',' \
                       ' "end_timestamp":' + end_timestamp + ',' \
                       ' "page_size": 200,' \
                       ' "page_timestamp": null}'
        result = apis.aep_device_status.getDeviceStatusHisInPage('6Dbi6zVTAHc', 'OyB7a81dby', body_history)
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
        return str(total)


@app.route('/turn_motor_on')
def turn_motor_on():
    result = apis.aep_device_command.CreateCommand('6Dbi6zVTAHc', 'OyB7a81dby', 'b8f7794e037644d7a17464c4f3fb0483',
                                                   body_motor_control % "1")
    return result


@app.route('/turn_motor_off')
def turn_motor_off():
    result = apis.aep_device_command.CreateCommand('6Dbi6zVTAHc', 'OyB7a81dby', 'b8f7794e037644d7a17464c4f3fb0483',
                                                   body_motor_control % "0")
    return result


if __name__ == '__main__':
    app.run()

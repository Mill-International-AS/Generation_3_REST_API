"""
This example queries the current control status to obtain current temperature
 and control signal (how much the heater is heating).
Then it changes the set temperature every minute.
"""

import sys
import time

try:
    import requests
except ImportError:
    print("ERROR! Please install requests library! Run `pip3 install requests` and retry!", file=sys.stderr)
    sys.exit(-1)


HEATER_ADDRESS = "10.0.0.176"  # Please specify IP address of your device here


def get_control_status_and_print_it():
    response = requests.get(url=f'http://{HEATER_ADDRESS}/control-status', timeout=5)
    if response.status_code != 200:
        raise Exception(f"Request error! Body={response.text}")

    control_status = response.json()

    ambient_temperature = control_status['ambient_temperature']
    set_temperature = control_status['set_temperature']
    control_signal = control_status['control_signal']
    current_power = control_status['current_power']

    print(f"STATUS:"
          f"  Ambient temperature = {ambient_temperature:.2f}\n"
          f"  Set temperature = {set_temperature:.1f}\n"
          f"  Control signal = {control_signal} %\n"
          f"  Current power = {current_power} W\n")


def set_normal_operation_mode():
    # because the device may be running in weekly program - so make sure it is not
    payload = {'mode': 'Control individually'}
    response = requests.post(url=f'http://{HEATER_ADDRESS}/operation-mode', json=payload, timeout=5)
    if response.status_code != 200:
        raise Exception(f"Request error! Body={response.text}")


def change_temperature(temperature):
    payload = {'type': 'Normal', 'value': temperature}
    response = requests.post(url=f'http://{HEATER_ADDRESS}/set-temperature', json=payload, timeout=5)
    if response.status_code != 200:
        raise Exception(f"Request error! Body={response.text}")


def main():
    get_control_status_and_print_it()

    set_normal_operation_mode()

    for i in range(3):
        print('===========')
        target_temperature = 15 + i / 2
        print(f'Changing the set temperature to {target_temperature:.1f} C...')
        change_temperature(temperature=target_temperature)
        time.sleep(1)
        get_control_status_and_print_it()
        time.sleep(1)


if __name__ == '__main__':
    main()
    print('Done!')


'''
EXAMPLE OUTPUT:
STATUS:  Ambient temperature = 21.24
  Set temperature = 32.0
  Control signal = 100 %
  Current power = 1000 W

===========
Changing the set temperature to 15.0 C...
STATUS:  Ambient temperature = 21.26
  Set temperature = 15.0
  Control signal = 0 %
  Current power = 0 W

===========
Changing the set temperature to 15.5 C...
STATUS:  Ambient temperature = 21.25
  Set temperature = 15.5
  Control signal = 0 %
  Current power = 0 W

===========
Changing the set temperature to 16.0 C...
STATUS:  Ambient temperature = 21.28
  Set temperature = 16.0
  Control signal = 0 %
  Current power = 0 W

Done!
'''

"""
This examples sets a few timers scheduled for the next few minutes,
 and queries the status to confirm the proper behaviour.

Note that the script doesn't need to keep running to have the timers working -
 they are stored and executed inside the device.
"""

import sys
import time
import datetime

try:
    import requests
except ImportError:
    print("ERROR! Please install requests library! Run `pip3 install requests` and retry!", file=sys.stderr)
    sys.exit(-1)


HEATER_ADDRESS = "10.11.12.145"  # Please specify IP address of your device here


def get_control_status_and_print_it():
    response = requests.get(url=f'http://{HEATER_ADDRESS}/control-status')
    if response.status_code != 200:
        raise Exception(f"Request error! Body={response.text}")

    control_status = response.json()

    ambient_temperature = control_status['ambient_temperature']
    set_temperature = control_status['set_temperature']
    control_signal = control_status['control_signal']

    print(f"STATUS:\n" 
          f"  Ambient temperature = {ambient_temperature:.2f}\n"
          f"  Set temperature = {set_temperature:.1f}\n"
          f"  Control signal = {control_signal} %\n")


def set_timezone_offset(timezone_offset):
    payload = {'timezone_offset': timezone_offset}
    response = requests.post(url=f'http://{HEATER_ADDRESS}/timezone-offset', json=payload, timeout=5)
    if response.status_code != 200:
        raise Exception(f"Request error! Body={response.text}")


def set_operation_mode(operation_mode):
    payload = {'mode': operation_mode}
    response = requests.post(url=f'http://{HEATER_ADDRESS}/operation-mode', json=payload, timeout=5)
    if response.status_code != 200:
        raise Exception(f"Request error! Body={response.text}")


def set_temperature_value_for_type(temperature_type, temperature):
    payload = {'type': temperature_type, 'value': temperature}
    response = requests.post(url=f'http://{HEATER_ADDRESS}/set-temperature', json=payload, timeout=5)
    if response.status_code != 200:
        raise Exception(f"Request error! Body={response.text}")


def set_non_repeatable_timers(timers):
    payload = {'non_repeatable_timers': timers}
    response = requests.post(url=f'http://{HEATER_ADDRESS}/non-repeatable-timers', json=payload, timeout=5)
    if response.status_code != 200:
        raise Exception(f"Request error! Body={response.text}")


def change_temperature_in_independent_mode_now(value):
    payload = {'temperature': value}
    response = requests.post(url=f'http://{HEATER_ADDRESS}/set-temperature-in-independent-mode-now', json=payload, timeout=5)
    if response.status_code != 200:
        raise Exception(f"Request error! Body={response.text}")


def get_non_repeatable_timers():
    response = requests.get(url=f'http://{HEATER_ADDRESS}/non-repeatable-timers', timeout=5)
    if response.status_code != 200:
        raise Exception(f"Request error! Body={response.text}")

    weekly_program = response.json()
    print(weekly_program)


def main():
    timezone_offset = 60
    unix_local_timestamp_in_minutes = int(time.time() / 60) + timezone_offset
    target_temperature = 30

    target_timers = [
        {'value_type': 'Normal', 'time': unix_local_timestamp_in_minutes + 1},
        {'value_type': 'Off', 'time': unix_local_timestamp_in_minutes + 2},
        {'value_type': 'Normal', 'time': unix_local_timestamp_in_minutes + 3},
        {'value_type': 'Off', 'time': unix_local_timestamp_in_minutes + 4}
    ]

    set_timezone_offset(timezone_offset=timezone_offset)
    set_operation_mode(operation_mode='Independent device')
    set_temperature_value_for_type(temperature_type='Normal', temperature=target_temperature)
    change_temperature_in_independent_mode_now(target_temperature)
    set_non_repeatable_timers(timers=target_timers)

    while True:
        now = datetime.datetime.now()
        print(f'{now.hour}:{now.minute:02d}:{now.second:02d}')
        get_control_status_and_print_it()
        time.sleep(20)


if __name__ == '__main__':
    main()
    print('Done!')

'''
EXAMPLE OUTPUT:
10:12:57
STATUS:
  Ambient temperature = 19.37
  Set temperature = 30.0
  Control signal = 100 %

10:13:17
STATUS:
  Ambient temperature = 19.37
  Set temperature = 30.0
  Control signal = 100 %

10:13:37
STATUS:
  Ambient temperature = 19.37
  Set temperature = 30.0
  Control signal = 100 %

10:13:57
STATUS:
  Ambient temperature = 19.37
  Set temperature = 30.0
  Control signal = 100 %

10:14:17
STATUS:
  Ambient temperature = 19.37
  Set temperature = 0.0
  Control signal = 0 %

10:14:37
STATUS:
  Ambient temperature = 19.37
  Set temperature = 0.0
  Control signal = 0 %

10:14:58
STATUS:
  Ambient temperature = 19.37
  Set temperature = 0.0
  Control signal = 0 %

10:15:18
STATUS:
  Ambient temperature = 19.37
  Set temperature = 30.0
  Control signal = 100 %

10:15:38
STATUS:
  Ambient temperature = 19.37
  Set temperature = 30.0
  Control signal = 100 %


  
  ...
'''

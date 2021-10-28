"""
This example queries the status of the status device
and set and get the temperature in a given temperature type.
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


def print_device_status():
    response = requests.get(url=f'http://{HEATER_ADDRESS}/status')
    if response.status_code != 200:
        raise Exception(f"Request error! Body={response.text}")

    device_status = response.json()

    name = device_status['name']
    version = device_status['version']
    operation_key = device_status['operation_key']

    print(f"STATUS:\n"
          f"  Name = {name}\n"
          f"  Version = {version}\n"
          f"  Operation key = {operation_key} \n")


def set_temperature_value_for_type(temperature_type, temperature):
    payload = {'type': temperature_type, 'value': temperature}
    response = requests.post(url=f'http://{HEATER_ADDRESS}/set-temperature', json=payload, timeout=5)
    if response.status_code != 200:
        raise Exception(f"Request error! Body={response.text}")


def get_temperature_value_for_temperature_type(temperature_type):
    payload = {'type': temperature_type}
    response = requests.get(url=f'http://{HEATER_ADDRESS}/set-temperature', json=payload, timeout=5)
    if response.status_code != 200:
        raise Exception(f"Request error! Body={response.text}")

    temperature = response.json()
    set_temperature = temperature['value']

    print(f"set_temperature = {set_temperature:.2f}\n")


def main():
    print_device_status()
    target_temperature_type = 'Normal'

    for i in range(3):
        print('===========')
        target_temperature = 15 + i / 2
        print(f'Changing the set temperature to {target_temperature:.1f} C...')
        set_temperature_value_for_type(temperature_type=target_temperature_type, temperature=target_temperature)
        time.sleep(1)
        get_temperature_value_for_temperature_type(target_temperature_type)
        time.sleep(1)


if __name__ == '__main__':
    main()
    print('Done!')

'''
EXAMPLE OUTPUT:
STATUS:
  Name = panel heater gen. 3
  Version = 0x211019
  Operation key =  

===========
Changing the set temperature to 15.0 C...
set_temperature = 15.00

===========
Changing the set temperature to 15.5 C...
set_temperature = 15.50

===========
Changing the set temperature to 16.0 C...
set_temperature = 16.00

Done!

Process finished with exit code 0
'''

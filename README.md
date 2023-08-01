# Millheat heater gen. 3 - local WiFi Control API - version 0x220727 (27.07.2022)

## Overview

Following devices are supported: 

- Panel heaters - Generation 3. 
- Convection heaters - Generation 3.
- Oil heaters - Generation 3.
- Wi-Fi Socket - Generation 3.

Generation 3 heaters expose HTTP server, with a defined REST API. Local HTTP server works both when the device is connected to an existing WiFi network (to a router) or when the device is configured as an Access Point. 
In the first scenario, the device IP address can be found in the router clients list. 
In most cases, it is something like 192.168.1.105 or 10.0.0.95, depending on the local network configuration. 
Once you have an IP address, you can just type it in a web browser (assuming your device is connected to the same WiFi network) to see the main page. It contains a summary of the heater status and reference to this document.
In the Access Point mode the heater has IP address `192.168.4.1`.


## HTTP Requests

All API requests are made by sending a HTTP request using one of the following methods, depending on the action being taken:

- <code>POST</code> create a resource,
- <code>GET</code> get a resource or list of resources.

 Request data is passed as a JSON file content in the request body. Response data is also returned as a JSON file, with the scheme described below.

## HTTP Responses

Each response will include a`result` (`result` will be an object for single-record queries and an array for list queries) and `status` message. The `status` message contain the information of the result of the processing request. The list of status codes can be found in [HTTP Response Codes](#http-esponse-codes). The `result` contains the result of a successful request. For example, a request to the [<code>GET</code> status](#get-status) resource might return this:

```json
{
   "name": "panel heater gen. 3",
   "custom_name": "",
   "version": "0x210927",
   "operation_key": "",
   "mac_address": "XX:XX:XX:XX:XX:XX",
   "status": "ok"
}
```


## HTTP Response Status

Each response will be returned the field <code>status</code> with one of the following description:

- <code>ok</code> - the request was successful,
- <code>Failed to parse message body</code> - the request body is incorrect or the parameters are invalid,
- <code>Failed to execute the request</code> - there was a problem with the processing request, 
- <code>Length of request body too long</code> - the length of the request body is to long, 
- <code>Failed to create response body</code> -  there was a problem with the processing respone.

## Resources

We provide a [Postman](https://www.getpostman.com/) collection with a set of requests that introduce the basic concepts of the API.  The Postman collection and more information are available [here](postman_collection_heaters_gen_3.json). In the collection <code>{{heater_addresss}}</code> is the variable which determines the IP address of the device.   

## Authentication
After setting API key with [<code>POST</code>/set-api-key](#postset-api-key) every request on every endpoint would need to contain this key as header. This operation (settign API key) triggers product to restart to change HTTP server to HTTPS server. That server uses self-signed certificate which can generate some warning messages but will provide better security.
Header's key must be "Authentication" and it's value should be API key.

### Basic communication 

- [<code>GET</code>/status](#getstatus)
- [<code>POST</code>/soft-reset](#postsoft-reset)
- [<code>POST</code>/hard-reset](#posthard-reset)
- [<code>POST</code>/reboot](#postreboot)
- [<code>GET</code>/temperature-calibration-offset](#gettemperature-calibration-offset)
- [<code>POST</code>/temperature-calibration-offset](#posttemperature-calibration-offset)
- [<code>GET</code>/control-status](#getcontrol-status)
- [<code>GET</code>/operation-mode](#getoperation-mode)
- [<code>POST</code>/operation-mode](#postoperation-mode)
- [<code>GET</code>/commercial-lock](#getcommercial-lock)
- [<code>POST</code>/commercial-lock](#postcommercial-lock)
- [<code>GET</code>/child-lock](#getchild-lock)
- [<code>POST</code>/child-lock](#postchild-lock)
- [<code>GET</code>/open-window](#getopen-window)
- [<code>POST</code>/open-window](#postopen-window)
- [<code>GET</code>/weekly-program](#getweekly-program)
- [<code>POST</code>/weekly-program](#postweekly-program)
- [<code>GET</code>/non-repeatable-timers](#getnon-repeatable-timers)
- [<code>POST</code>/non-repeatable-timers](#postnon-repeatable-timers)
- [<code>GET</code>/display-unit](#getdisplay-unit)
- [<code>POST</code>/display-unit](#getdisplay-unit)
- [<code>GET</code>/set-temperature](#getset-temperature)
- [<code>POST</code>/set-temperature](#postset-temperature)
- [<code>GET</code>/oil-heater-power](#getoil-heater-power)
- [<code>POST</code>/oil-heater-power](#postoil-heater-power)
- [<code>GET</code>/predictive-heating-type](#getpredictive-heating-type)
- [<code>POST</code>/predictive-heating-type](#postpredictive-heating-type)
- [<code>POST</code>/overwrite-weekly-program](#postoverwrite-weekly-program)
- [<code>GET</code>/vacation-mode](#getvacation-mode)
- [<code>POST</code>/vacation-mode](#postvacation-mode)
- [<code>GET</code>/timezone-offset](#gettimezone-offset)
- [<code>POST</code>/timezone-offset](#posttimezone-offset)
- [<code>POST</code>/set-temperature-in-independent-mode-now](#postset-temperature-in-independent-mode-now)
- [<code>GET</code>/additional-socket-mode](#getadditional-socket-mode)
- [<code>POST</code>/additional-socket-mode](#postadditional-socket-mode)

### Advanced communication

- [<code>GET</code>/pid-parameters](#getpid-parameters)
- [<code>POST</code>/pid-parameters](#postpid-parameters)
- [<code>GET</code>/cloud-communication](#getcloud-communication)
- [<code>POST</code>/cloud-communication](#postcloud-communication)
- [<code>POST</code>/ota-update](#postota-update)
- [<code>GET</code>/config-parameter](#getconfig-parameter)
- [<code>POST</code>/config-parameter](#postconfig-parameter)
- [<code>POST</code>post/max-heater-power](#postmax-heater-power)
- [<code>POST</code>/ablecloud-message](#postablecloud-message)
- [<code>GET</code>/scan-wifi](#getscan-wifi)
- [<code>POST</code>/device-config](#postdevice-config)
- [<code>GET</code>/hysterersis-parameters](#gethysteresis-parameters)
- [<code>POST</code>/hysterersis-parameters](#posthysteresis-parameters)
- [<code>GET</code>/limited-heating-power](#getlimited-heating-power)
- [<code>POST</code>/limited-heating-power](#postlimited-heating-power)
- [<code>GET</code>/controller-type](#getcontroller-type)
- [<code>POST</code>/controller-type](#postcontroller-type)
- [<code>POST</code>/set-custom-name](#postset-custom-name)
- [<code>POST</code>/increase-set-temperature](#postincrease-set-temperature)
- [<code>POST</code>/decrease-set-temperature](#postdecrease-set-temperature)
- [<code>POST</code>/set-api-key](#postset-api-key)
- [<code>GET</code>/commercial-lock-customization](#getcommercial-lock-customization)
- [<code>POST</code>/commercial-lock-customization](#postcommercial-lock-customization)



## Examples

Here, we provide example Python scripts which can control the Millheat heater gen. 3 via the REST API:

- [examples/python/basic_control.py](heaters/examples/python/basic_control.py) script queries the current control status to obtain current temperature and control signal (how much the heater is heating). Then it changes the set temperature every minute.
- [examples/python/temperature_control.py](heaters/examples/python/temperature_control.py) script queries the status of the status device and set and get the temperature in a given temperature type. Then it changes the set temperature every minute.
- [examples/python/timers.py](heaters/examples/python/timers.py) script sets a few timers scheduled for the next few minutes,  and queries the status to confirm the proper behavior. Note that the script doesn't need to keep running to have the timers working - they are stored and executed inside the device.

We also provide a simple example to control the Millheat heater gen. 3 with a Bash script:

- In [examples/bash/query_ambient_temperature.sh](heaters/examples/bash/query_ambient_temperature.sh) script the ambient temperature is returned every second.

## <code>GET</code>/status

Return a quick summary of the device information. 

### Returned parameters

| Field         | Type   | Description                                                  |
| ------------- | ------ | ------------------------------------------------------------ |
| name          | string | the name of the device                                       |
| custom_name   | string | the custom name of the device                                |
| version       | string | the API version number                                       |
| operation_key | string | if there is some operation problem (like broken temperature sensor), it may be reported in this field |
| mac_address   | string | device's MAC (Media Access Control) address                  |

### Example

#### Request

- Postman: 

  ```html
  GET http://{{heater_address}}/status
  ```

  Request body: empty

- Curl: 

  ```html
  curl -X GET -H "Content-Type: application/json" http://{{heater_address}}/status
  ```

#### Response:

```json
{
   "name": "panel heater gen. 3",
   "custom_name": "",
   "version": "0x210927",
   "operation_key": "",
   "mac_address": "XX:XX:XX:XX:XX:XX",
   "status": "ok"
}
```



## <code>POST</code>/soft-reset

Perform a soft-reset of the device (configuration).

### Example

#### Request

- Postman:

  ```html
  POST http://{{heater_address}}/soft-reset
  ```

  Request body: empty


#### Response

The soft-reset performs before sending response.



## <code>POST</code>/hard-reset

Perform a hard-reset of the device.

### Example

#### Request

- Postman: 

  ```html
  POST http://{{heater_address}}/hard-reset
  ```

  Request body: empty


#### Response

The hard-reset performs before sending response.



## <code>POST</code>/reboot

Perform a reboot of the heater control MCU

### Example

#### Request

- Postman: 

  ```html
  POST http://{{heater_address}}/reboot
  ```

  Request body: empty


#### Response

The reboot performs before sending response.



## <code>GET</code>/temperature-calibration-offset

Return the current value of temperature sensor calibration offset.

### Returned parameters

| Field | Type  | Description                                     |
| ----- | ----- | ----------------------------------------------- |
| value | float | the calibration offset value in Celsius degrees |

### Example

#### Request

- Postman: 

  ```html
  GET http://{{heater_address}}/temperature-calibration-offset
  ```

  Request body: empty

- Curl:

  ```html
  curl -X GET -H "Content-Type: application/json" http://{{heater_address}}/temperature-calibration-offset
  ```

- 

#### Response

```json
{
   "value": 2.5,
   "status": "ok"
}
```



## <code>POST</code>/temperature-calibration-offset

Set a new value of temperature sensor calibration offset.

### Body parameters

| Field | Type  | Description                                     |
| ----- | ----- | ----------------------------------------------- |
| value | float | the calibration offset value in Celsius degrees |

### Example

#### Request

- Postman: 

  ```html
  POST http://{{heater_address}}/temperature-calibration-offset
  ```

  Request body:

  ```json
  {
     "value": 2
  }
  ```

- Curl: 

  ```html
  curl -X POST -H "Content-Type: application/json" -d '{"value": 2}' http://{{heater_address}}/temperature-calibration-offset
  ```


#### Response

```json
{
    "status": "ok"
}
```



## <code>GET</code>/control-status

Return detailed information about the current device state and control status.

### Returned parameters

| Field                   | Type   | Description                                                  |
| ----------------------- | ------ | ------------------------------------------------------------ |
| ambient_temperature     | float  | the temperature measured by sensor in Celsius degrees (with calibration offset value included) |
| current_power           | float  | the current heating power in Watts                                   |
| control_signal          | float  | the control signal of the PID regulator (0-100%)             |
| lock_active             | string | the lock status (see [ELockStatus](#elockstatus))            |
| open_window_active_now  | string | the open widows status (see [EOpenWindowStatus](#eopenwindowstatus)) |
| raw_ambient_temperature | float  | the temperature measured by sensor in Celsius degrees without calibration offset value |
| set_temperature         | float  | the current set temperature in Celsius degrees               |
| switched_on             | float  | true if the device is switched on - whether it is set to working, with heating |
| connected_to_cloud      | bool   | the information whether device has connection with the cloud  |
| operation_mode          | string | the current mode of operation (see [EOprationMode](#eoprationmode)) |

### Example

#### Request

- Postman: 

  ```html
  GET http://{{heater_address}}/control-status
  ```

  Request body: empty

- Curl:

  ```html
  curl -X GET -H "Content-Type: application/json" http://{{heater_address}}/control-status
  ```


#### Response

```json
{
   "ambient_temperature": 22,
   "current_power": 5,
   "control_signal": 100,
   "lock_active": "Child lock",
   "open_window_active_now": "Enabled not active now",
   "raw_ambient_temperature": 21,
   "set_temperature": 1,
   "switched_on": false,
   "connected_to_cloud": true,
   "operation_mode": "Control individually",
   "status": "ok"
}
```



## <code>GET</code>/operation-mode

Return the current operation mode.

### Returned parameters

| Field | Type   | Description                                                  |
| ----- | ------ | ------------------------------------------------------------ |
| mode  | string | the current operation mode (see [EOprationMode](#eoprationmode)) |

### Example

#### Request

- Postman: 

  ```html
  GET http://{{heater_address}}/operation-mode
  ```

  Request body: empty


#### Response

```json
{
   "mode": "Control individually",
   "status": "ok"
}
```



## <code>POST</code>/operation-mode

Set the operation mode.

### Body parameters

| Field | Type   | Description                                                  |
| ----- | ------ | ------------------------------------------------------------ |
| mode  | string | the operation mode to set (see [EOprationMode](#eoprationmode)) |

### Example

#### Request

- Postman: 

  ```html
  POST http://{{heater_address}}/operation-mode
  ```

  Request body:

  ```json
  {
     "mode": "Control individually"
  }
  ```


#### Response

```json
{
   "status": "ok"
}
```



## <code>GET</code>/commercial-lock

Return the status of the commercial lock.

### Returned parameters

| Field | Type | Description                       |
| ----- | ---- | --------------------------------- |
| value | bool | the status of the commercial lock |

### Example

#### Request

- Postman: 

  ```html
  GET http://{{heater_address}}/commercial-lock
  ```

  Request body: empty


#### Response

```json
{
   "value": true,
   "status": "ok"
}
```



## <code>POST</code>/commercial-lock

Set status of the commercial lock.

### Body parameters

| Field | Type | Description                              |
| ----- | ---- | ---------------------------------------- |
| value | bool | the status of the commercial lock to set |

### Example

#### Request

- Postman: 

  ```html
  GET http://{{heater_address}}/commercial-lock
  ```

  Request body:

  ```json
  {
     "value": true
  }
  ```


#### Response

```json
{
    "status": "ok"
}
```



## <code>GET</code>/child-lock

Return the status of the child lock.

### Returned parameters

| Field | Type | Description                  |
| ----- | ---- | ---------------------------- |
| value | bool | the status of the child lock |

### Example

#### Request

- Postman: 

  ```html
  GET http://{{heater_address}}/child-lock
  ```

  Request body: empty


#### Response

```json
{
   "value": false,
   "status": "ok"
}
```



## <code>POST</code>/child-lock

Set status of the child lock.

### Body parameters

| Field | Type | Description                         |
| ----- | ---- | ----------------------------------- |
| value | bool | the status of the child lock to set |

### Example

#### Request

- Postman: 

  ```html
  GET http://{{heater_address}}/child-lock
  ```

  Request body:

  ```json
  {
     "value": false
  }
  ```


#### Response

```json
{
   "status": "ok"
}
```



## <code>GET</code>/open-window

Return the current state of the open window functionality and its configuration parameters.

### Returned parameters

| Field                          | Type  | Description                                                  |
| ------------------------------ | ----- | ------------------------------------------------------------ |
| active_now                     | bool  | true if open window functionality was activated and is active now |
| drop_temperature_threshold     | float | the required temperature drop to trigger (activate) the open window functionality (in Celsius degrees) |
| drop_time_range                | int   | the time range when a drop of temperature will be expected (in seconds) |
| enabled                        | bool  | the state of the open window functionality, true if open window functionality is enabled |
| increase_temperature_threshold | int   | the time range when an increase of temperature will be expected (in seconds) |
| max_time                       | int   | the maximum time duration of the open window activeness      |

### Example

#### Request

- Postman: 

  ```html
  GET http://{{heater_address}}/open-window
  ```

  Request body: empty


#### Response

```json
{
   "active_now": false,
   "drop_temperature_threshold": 5,
   "drop_time_range": 900,
   "enabled": true,
   "increase_temperature_threshold": 3,
   "increase_time_range": 900,
   "max_time": 3600,
   "status": "ok"
}
```



## <code>POST</code>/open-window

Change the open window functionality parameters or enable/disable it.

### Body parameters

| Field                          | Type  | Description                                                  |
| ------------------------------ | ----- | ------------------------------------------------------------ |
| drop_temperature_threshold     | float | the required temperature drop to trigger (activate) the open window functionality (in Celsius degrees) |
| drop_time_range                | int   | the time range when a drop of temperature will be expected (in seconds) |
| enabled                        | bool  | the state of the open window functionality, true if open window functionality is enabled |
| increase_temperature_threshold | int   | the time range when an increase of temperature will be expected (in seconds) |
| increase_time_range            | float | the time range when an increase of temperature will be expected |
| max_time                       | float | the maximum time duration of the open window activeness      |

### Example

#### Request

- Postman: 

  ```html
  POST http://{{heater_address}}/open-window
  ```

  Request body:

  ```json
  {
      "drop_temperature_threshold": 5,
      "drop_time_range": 900,
      "enabled": true,
      "increase_temperature_threshold": 3,
      "increase_time_range": 900,
      "max_time": 3600
  }
  ```


#### Response

```json
{
   "status": "ok"
}
```



## <code>GET</code>/weekly-program

Return the weekly program.

### Returned parameters

| Field  | Type              | Description                                                  |
| ------ | ----------------- | ------------------------------------------------------------ |
| active | bool              | state of the weekly program: true if is active, if false, the device works as an independent device |
| timers | list<string, int> | repeating pairs of values. A single pair represents time and value when the temperature mode should be changed. Time is a week time, in minutes since Monday 00:00, when to switch to a specific temperature type (set in the second field of the pair) (see [ETemperatureType](#etemperaturetype)) |

### Example

#### Request

- Postman: 

  ```html
  GET http://{{heater_address}}/weekly-program
  ```

  Request body: empty

- Curl: 

  ```html
  curl -X GET -H "Content-Type: application/json" http://{{heater_address}}/weekly-program
  ```


#### Response

```json
{
    "timers": [
        {
            "name": "Comfort",
            "timestamp": 12
        },
        {
            "name": "Away",
            "timestamp": 30
        },
        {
            "name": "Sleep",
            "timestamp": 50
        }
    ],
    "active": false,
    "status": "ok"
}
```



## <code>POST</code>/weekly-program

Set the weekly program or repeatable timers. One also needs to set the `timezone-offset`. The device needs to connect to the WiFi to synchronize the time with NTP server after each restart.

To have the weekly program working, one needs to set `operation-mode` to `"Weekly program"` mode.

To have the repeatable timers working, one needs to set `operation-mode` to `"Independent device"` mode.

### Body parameters

| Field  | Type              | Description                                                  |
| ------ | ----------------- | ------------------------------------------------------------ |
| timers | list<string, int> | repeating pairs of values. A single pair represents time and value when the temperature mode should be changed. Time is a week time, in minutes since Monday 00:00 when to switch to a specific temperature type (set in the second field of the pair). For available temperature types (see [<code>GET</code> set temperature)](#get-set-temperature) and [ETemperatureType](#etemperaturetype))|

### Example

#### Request

- Postman: 

  ```html
  POST http://{{heater_address}}/weekly-program
  ```

  Request body:

  ```json
  {
  	"timers": [
  		{
              "name": "Comfort", 
              "timestamp": 12
          },
  		{
              "name": "Away", 
              "timestamp": 30
          },
  		{
              "name": "Sleep", 
              "timestamp": 50
          }
  	]
  }
  ```

- Curl: 

  ```html
  url -X POST -H "Content-Type: application/json" -d '{"timers": [{"name": "Comfort", "timestamp": 12},{"name": "Away", "timestamp": 30},{"name": "Sleep", "timestamp": 50}]}' http://{{heater_address}}/weekly-program
  ```


#### Response

```json
{
   "status": "ok"
}
```



## <code>GET</code>/non-repeatable-timers

Return the non-repeatable timers.

### Returned parameters

| Field  | Type              | Description                                                  |
| ------ | ----------------- | ------------------------------------------------------------ |
| active | bool              | true if operation mode is  "Independent device" (see [EOprationMode](#eoprationmode)), false otherwise |
| timers | list<string, int> | repeating pairs of values. A single pair represents time and value when the temperature mode should be changed. Time defines when to switch to a specific temperature type (set in the second field of the pair). Time is as local unix timestamp, but in minutes, e.g. on 17.05.2021 the time is 27020801.  |

### Example

#### Request

- Postman: 

  ```html
  GET http://{{heater_address}}/non-repeatable-timers
  ```

  Request body: empty


#### Response

```json
{
    "non_repeatable_timers": [
        {
            "name": "Normal",
            "timestamp": 27245338
        },
        {
            "name": "Off",
            "timestamp": 27245339
        },
        {
            "name": "Normal",
            "timestamp": 27245340
        },
        {
            "name": "Off",
            "timestamp": 27245341
        }
    ],
    "active": true,
    "status": "ok"
}
```



## <code>POST</code>/non-repeatable-timers

Set the non-repeatable timers.


One also needs to set the `timezone-offset`. The device needs to connect to the WiFi to synchronize the time with NTP server after each restart.
To have the non-repeatable timers working, one needs to set `operation-mode` to `"Independent device"` mode.
Please refer to example script `examples/python/timers.py`

### Body parameters

| Field  | Type              | Description                                                  |
| ------ | ----------------- | ------------------------------------------------------------ |
| timers | list<string, int> | A single pair represents time and value when the temperature mode should be changed. Time defines when to switch to a specific temperature type (set in the second field of the pair). Time is as local unix timestamp (so timezone is included), but in minutes, e.g. on 17.05.2021 the time is 27020801. Allowed temperature types for timers: "Normal", "Off", "AlwaysHeating" |

### Example

#### Request

- Postman: 

  ```html
  POST http://{{heater_address}}/non-repeatable-timers
  ```

  Request body:

  ```json
  {
  	"non_repeatable_timers": [
  		{
              "name": "Off", 
              "timestamp": 12
          },
  		{
              "name": "Away", 
              "timestamp": 30
          },
  		{
              "name": "Sleep", "
              timestamp": 50
          }
  	]
  }
  ```


#### Response

```json
{
   "status": "ok"
}
```



## <code>GET</code>/display-unit

Return the current temperature units used on the display.

### Returned parameters

| Field | Type   | Description                                              |
| ----- | ------ | -------------------------------------------------------- |
| value | string | the current temperature units: "Celsius" or "Fahrenheit" |

### Example

#### Request

- Postman: 

  ```html
  GET http://{{heater_address}}/display-unit
  ```

  Request body: empty


#### Response

```json
{
   "value": "Farenheit",
   "status": "ok"
}
```



## <code>POST</code>/display-unit

Set the current temperature units used on the display.

### Body parameters

| Field | Type   | Description                                             |
| ----- | ------ | ------------------------------------------------------- |
| value | string | the temperature units: "Celsius" or "Fahrenheit" to set |

### Example

#### Request

- Postman: 

  ```html
  POST http://{{heater_address}}/child-lock
  ```

  Request body:

  ```json
  {
     "value": "Farenheit"
  }
  ```


#### Response

```json
{
   "status": "ok"
}
```



## <code>GET</code>/set-temperature

Return temperature of the specified in body of the request temperature type. 
In operation modes `Control individually` and `Independent device` one usally is interested in `Normal` temperature type.

### Returned parameters

| Field | Type  | Description                       |
| ----- | ----- | --------------------------------- |
| value | float | the temperature in Celsius to set |

### Body parameters

| Field | Type   | Description                                                  |
| ----- | ------ | ------------------------------------------------------------ |
| type  | string | the temperature type to get (see [ETemperatureType](#etemperaturetype)) |

### Example

#### Request

- Postman: 

  ```html
  GET http://{{heater_address}}/set-temperature
  ```

  Request body:

  ```json
  {
     "type": "Normal"
  }
  ```

- Curl:

  ```html
  curl -X GET -H "Content-Type: application/json" -d  '{"type": "Normal"}' http://{{heater_address}}/set-temperature
  ```

#### Response

```json
{
   "value": 30,
   "status": "ok"
}
```



## <code>POST</code>/set-temperature

Set temperature of the specified temperature type. This endpoint doesn't put the device in specific mode, it just sets the temperature
for chosen mode. One cannot send "Off" type using this endpoint as temperature for Off mode cannot be set (it is set to specified value by default). 
If operation mode is `"Control individually"` or `"Independent device"` one is usually interested in `"Normal"` temperature type.


### Body parameters

| Field | Type   | Description                                                  |
| ----- | ------ | ------------------------------------------------------------ |
| type  | string | the temperature type to set (see [ETemperatureType](#etemperaturetype)) |
| value | float  | the temperature in Celsius to set                            |

### Example

#### Request

- Postman: 

  ```html
  POST http://{{heater_address}}/set-temperature
  ```

  Request body:

  ```json
  {
     "type": "Normal",
     "value": 30
  }
  ```
  
- Curl:

  ```html
  curl -X POST -H "Content-Type: application/json" -d '{"type": "Normal", "value": 30}' http://{{heater_address}}/set-temperature
  ```


#### Response

```json
{
   "status": "ok"
}
```



## <code>GET</code>/oil-heater-power

Return the max heating level in percentage of the nominal wattage.
Oil heater allows setting 3 different max power settings (40, 60 or 100% of the power), done by selecting number of active heating elements.

### Returned parameters

| Field                    | Type | Description                     |
| ------------------------ | ---- | ------------------------------- |
| heating_level_percentage | int  | the heating level in percentage |

### Example

#### Request

- Postman: 

  ```html
  GET http://{{heater_address}}/oil-heater-power
  ```

  Request body: empty


#### Response

```json
{
   "value": 100,
   "status": "ok"
}
```



## <code>POST</code>/oil-heater-power

Set the max heating level in percentage of the nominal wattage.
Oil heater allows setting 3 different max power settings (40, 60 or 100% of the power), done by selecting number of active heating elements.

### Body parameters

| Field                    | Type | Description                                              |
| ------------------------ | ---- | -------------------------------------------------------- |
| heating_level_percentage | int  | the heating level in percentage: 0, 40, 60 or 100 to set |

### Example

#### Request

- Postman: 

  ```html
  POST http://{{heater_address}}/oil-heater-power
  ```

  Request body:

  ```json
  {
      "heating_level_percentage": 100
  }
  ```


#### Response

```json
{
   "status": "ok"
}
```



## <code>GET</code>/predictive-heating-type

Return the predictive heating type.

### Returned parameters

| Field                   | Type   | Description                                                  |
| ----------------------- | ------ | ------------------------------------------------------------ |
| predictive_heating_type | string | the predictive heating type (see [EPredictiveHeatingType](#epredictiveheatingtype)) |

### Example

#### Request

- Postman: 

  ```html
  GET http://{{heater_address}}/predictive-heating-type
  ```

  Request body: empty


#### Response

```json
{
   "predictive_heating_type": "Off",
   "status": "ok"
}
```



## <code>POST</code>/predictive-heating-type

Set the predictive heating type.

### Body parameters

| Field                   | Type   | Description                                                  |
| ----------------------- | ------ | ------------------------------------------------------------ |
| predictive_heating_type | string | the predictive heating type (see [EPredictiveHeatingType](#epredictiveheatingtype)) to set |

### Example

#### Request

- Postman: 

  ```html
  POST http://{{heater_address}}/predictive-heating-type
  ```

  Request body:

  ```json
  {
      "predictive_heating_type": "Off"
  }
  ```


#### Response

```json
{
   "status": "ok"
}
```



## <code>POST</code>/overwrite-weekly-program

Overwrite the weekly program.

### Body parameters

| Field    | Type   | Description                                                  |
| -------- | ------ | ------------------------------------------------------------ |
| duration | int    | the overwrite weekly program duration minutes                |
| type     | string | the temperature type to set (see [ETemperatureType](#etemperaturetype)) |

### Example

#### Request

- Postman: 

  ```html
  POST http://{{heater_address}}/overwrite-weekly-program
  ```

  Request body:

  ```json
  {
      "duration": 1,
      "type": "Away"
  }
  ```


#### Response

```json
{
   "status": "ok"
}
```



## <code>GET</code>/vacation-mode

Get the vacation mode settings.

### Returned parameters

| Field           | Type | Description                     |
| --------------- | ---- | ------------------------------- |
| start_timestamp | int  | the 32 bit timestamp in minutes |
| end_timestamp   | int  | the 32 bit timestamp in minutes |

### Example

#### Request

- Postman: 

  ```html
  GET http://{{heater_address}}/vacation-mode
  ```

  Request body: empty


#### Response

```json
{
   "start_timestamp": 0,
   "end_timestamp": 0,
   "status": "ok"
}
```



## <code>POST</code>/vacation-mode

Set the vacation mode settings.

### Body parameters

| Field           | Type | Description                                                  |
| --------------- | ---- | ------------------------------------------------------------ |
| start_timestamp | int  | the 32 bit timestamp in minutes (0 for no vacation mode) to set |
| end_timestamp   | int  | the 32 bit timestamp in minutes (0 for no vacation mode) to set |

### Example

#### Request

- Postman: 

  ```html
  POST http://{{heater_address}}/vacation-mode
  ```

  Request body:

  ```json
  {
     "start_timestamp": 0,
     "end_timestamp": 0
  }
  ```


#### Response

```json
{
   "status": "ok"
}
```



## <code>GET</code>/timezone-offset

Get the timezone offset.

### Returned parameters

| Field           | Type | Description                                      |
| --------------- | ---- | ------------------------------------------------ |
| timezone_offset | int  | the timezone offset in minutes from -840 to +720 |

### Example

#### Request

- Postman: 

  ```Request body: empty
  GET http://{{heater_address}}/timezone-offset
  ```

  Request body: empty


#### Response

```json
{
   "timezone_offset": 1440,
   "status": "ok"
}
```



## <code>POST</code>/timezone-offset

Set the timezone offset. Required to have weekly program and timers working.

### Body parameters

| Field           | Type | Description                                                  |
| --------------- | ---- | ------------------------------------------------------------ |
| timezone_offset | int  | Device timezone offset in minutes |

### Example

#### Request

- Postman: 

  ```html
  POST http://{{heater_address}}/timezone-offset
  ```

  Request body:

  ```json
  {
      "timezone_offset": 60
  }
  ```


#### Response

```json
{
    "status": "ok"
}
```



## <code>POST</code>/set-temperature-in-independent-mode-now

Change temperature in independent mode now. Use values 0.0 and 99.0 to set ALWAYS_ON and ALWAYS_OFF, respectively.
Apart from changing value for some temperature type, in `"Independent device"` operation mode, one also needs to call this command to change the current temperature.

### Body parameters

| Field       | Type  | Description                  |
| ----------- | ----- | ---------------------------- |
| temperature | float | the temperature value to set |

### Example

#### Request

- Postman: 

  ```html
  POST http://{{heater_address}}/set-temperature-in-independent-mode-now
  ```

  Request body:

  ```json
  {
     "temperature": 12.0
  }
  ```


#### Response

```json
{
   "status": "ok"
}
```



## <code>GET</code>/additional-socket-mode

#### Only for socket heaters

Return the additional socket mode.

### Returned parameters

| Field           | Type | Description                |
| --------------- | ---- | -------------------------- |
| additional_mode | int  | the additional socket mode |

### Example

#### Request

- Postman: 

  ```html
  GET http://{{heater_address}}/additional-socket-mode
  ```

  Request body: empty


#### Response

```json
{
   "additional_mode": 3,
   "status": "ok"
}
```



## <code>POST</code>/additional-socket-mode

#### Only for socket heaters

Set the additional socket mode.

Body parameters

| Field           | Type | Description                        |
| --------------- | ---- | ---------------------------------- |
| additional_mode | int  | the additional mode <0 - 4> to set |

### Example

#### Request

- Postman: 

  ```html
  POST http://{{heater_address}}/additional-socket-mode
  ```

  Request body:

  ```json
  {
     "additional_mode": 3
  }
  ```


#### Response

```json
{
   "status": "ok"
}
```



## <code>GET</code>/pid-parameters

#### Only for panel heaters

Return PID parameters of the temperature PID controller.

### Returned parameters

| Field                   | Type  | Description                                      |
| ----------------------- | ----- | ------------------------------------------------ |
| kp                      | float | the proportional part gain                       |
| ki                      | float | the integral part gain                           |
| kd                      | float | the derivative part gain                         |
| kd_filter_N             | float | the derivative filter time coefficient           |
| windup_limit_percentage | float | the windup limit for integral part from 0 to 100 |

### Example

#### Request

- Postman: 

  ```html
  GET http://{{heater_address}}/pid-parameters
  ```

  Request body: empty


#### Response

```json
{
   "kp": 70,
   "ki": 0.02,
   "kd": 4500,
   "kd_filter_N": 60,
   "windup_limit_percentage": 95,
   "status": "ok"
}
```



## <code>POST</code>/pid-parameters

#### Only for panel heaters

Set PID parameters. Setting PID parameters will change current regulator type to PID. PID regulator works only with panel heater.

### Body parameters

| Field                   | Type  | Description                                      |
| ----------------------- | ----- | ------------------------------------------------ |
| kp                      | float | the proportional part gain                       |
| ki                      | float | the integral part gain                           |
| kd                      | float | the derivative part gain                         |
| kd_filter_N             | float | the derivative filter time coefficient           |
| windup_limit_percentage | float | the windup limit for integral part from 0 to 100 |

### Example

#### Request

- Postman: 

  ```html
  POST http://{{heater_address}}/pid-parameters
  ```

  Request body:

  ```json
  {
      "kp": 70,
      "ki": 0.02,
      "kd": 4500,
      "kd_filter_N": 60,
      "windup_limit_percentage": 95,
      "status": "ok"
  }
  ```


#### Response

```json
{
   "status": "ok"
}
```



## <code>GET</code>/cloud-communication

Return the cloud communication activeness status.

### Returned parameters

| Field | Type | Description                                                  |
| ----- | ---- | ------------------------------------------------------------ |
| value | bool | the cloud communication activeness status, true if device is allowed to communicate with cloud |

### Example

#### Request

- Postman: 

  ```html
  GET http://{{heater_address}}/cloud-communication
  ```

  Request body: empty


#### Response

```json
{
   "value": true,
   "status": "ok"
}
```



## <code>POST</code>/cloud-communication

Allows disabling cloud communication completely. Requires a reboot after this command.

### Body parameters

| Field | Type | Description                                                  |
| ----- | ---- | ------------------------------------------------------------ |
| value | bool | the cloud communication activeness status, true if device is allowed to communicate with cloud |

### Example

#### Request

- Postman: 

  ```html
  POST http://{{heater_address}}/cloud-communication
  ```

  Request body:

  ```json
  {
      "value": false
  }
  ```


#### Response

```json
{
   "status": "ok"
}
```



## <code>POST</code>/ota-update

Perform OTA update, to replace the firmware. The device needs to have Internet access to perform it.

### Body parameters

| Field   | Type         | Description                                                  |
| ------- | ------------ | ------------------------------------------------------------ |
| address | string (url) | the address to firmware binary for the heater, http address allowed |

### Example

#### Request

- Postman: 

  ```html
  POST http://{{heater_address}}/ota-update
  ```

  Request body:

  ```json
  {
  	"value": false
  }
  ```


#### Response

```json
{
   "status": "ok"
}
```



## <code>GET</code>/config-parameter

Return the configuration parameter determined by the name in request message.

### Body parameters

| Field | Type   | Description                      |
| ----- | ------ | -------------------------------- |
| name  | string | the name of the parameter to get |

### Returned parameters

| Field | Type   | Description                |
| ----- | ------ | -------------------------- |
| value | string | the value of the parameter |

### Example

#### Request

- Postman: 

  ```html
  GET http://{{heater_address}}/config-parameter
  ```

  Request body:

  ```json
  {
     "name": "Set"
  }
  ```


#### Response

```json
{
   "value": "",
   "status": "ok"
}
```



## <code>POST</code>/config-parameter

Set the configuration parameter determined by the name in request message.

### Body parameters

| Field | Type   | Description                      |
| ----- | ------ | -------------------------------- |
| name  | string | the name of the parameter to set |
| vaule | string | the value of the parameter       |

### Example

#### Request

- Postman: 

  ```html
  POST http://{{heater_address}}/cloud-communication
  ```

  Request body:

  ```json
  {
     "name": "Set",
     "value": 70
  }
  ```


#### Response

```json
{
   "status": "ok"
}
```



## <code>POST</code>/max-heater-power

Set max heater power in Watts.

### Body parameters

| Field     | Type | Description                                        |
| --------- | ---- | -------------------------------------------------- |
| power     | int  | the value of the heater power in Watts             |
| calibrate | bool | whether to perform the calibration with the chip measuring the power usage |

### Example

#### Request

- Postman: 

  ```html
  POST http://{{heater_address}}/max-heater-power
  ```

  Request body:

  ```json
  {
     "power": 12,
     "calibrate": false
  }
  ```


#### Response

```json
{
   "status": "ok"
}
```



## <code>POST</code>/ablecloud-message

Send a message and process it as if it would come from AbleCloud module. 

### Body parameters

| Field        | Type   | Description                                                  |
| ------------ | ------ | ------------------------------------------------------------ |
| message_code | int    | code of the message                                          |
| data         | string | the binary data as hex string, e.g. string "1AB2550C" would be parsed to binary array {0x1A, 0xB2, 0x55, 0x0C} |

### Example

#### Request

- Postman: 

  ```html
  POST http://{{heater_address}}/ablecloud-message
  ```

  Request body:

  ```json
  {
      "message_code": 3,
      "data": 4443
  }
  ```


#### Response

```json
{
    "status": "ok"
}
```


## <code>GET</code>/scan-wifi

The heater has to be configured in the access mode (AP) mode. Then, you have to be connected to the network provided by your heater and check the IP adress which has format "192.168.4.x". The request should be post on this address. 

Returns the list of WiFi networks scanned by ESP32, ordered by best signal  (maximum 20 networks). 

### Returned parameters

| Field | Type | Description                                |
| ----- | ---- | ------------------------------------------ |
| wifi  | list | the list of WiFi networks scanned by ESP32 |

### Example

#### Request

- Postman: 

  ```html
  GET http://192.168.4.x/scan-wifi
  ```

  Request body: empty


#### Response

```json
{
   "value": "",
   "status": "ok"
}
```



## <code>POST</code>/device-config

The heater has to be configured in the access mode (AP) mode. Then, you have to be connected to the network provided by your heater and check the IP adress which has format "192.168.4.x". The request should be post on this address. Post the device configuration, same as the one can be done via BLE. 

### Body parameters

| Field               | Type   | Description                                                  |
| ------------------- | ------ | ------------------------------------------------------------ |
| ssid                | string | the SSID of the WiFi                                         |
| password            | string | the password of the WiFi                                     |
| connectivity_option | string | the connectivity option (see [ECloudAndServerCommunicationType](#ecloudandservercommunicationtype)) |

### Example

#### Request

- Postman: 

  ```html
  POST http://{{heater_address}}/device-config
  ```

  Request body:

  ```json
  {
     "ssid": "wifi_ssid",
     "password": "wifi_password",
     "connectivity_option": "sta_cloud_and_local_api"
  }
  ```


#### Response

```json
{
   "status": "ok"
}
```

## <code>GET</code>/hysteresis-parameters
Get current hysteresis setting.

### Returned parameters

| Field                 | Type  | Description                                  |
| --------------------- | ----- | -------------------------------------------- |
| temp_hysteresis_upper | float | upper offset (set temp + this -> stop heat)  |
| temp_hysteresis_lower | float | lower offset (set temp - this -> start heat) |

### Example

#### Request

- Postman: 

  ```html
  GET http://192.168.4.x/hysteresis-parameters
  ```

  Request body: empty


#### Response

```json
{
    "temp_hysteresis_upper": 2,
    "temp_hysteresis_lower": 1,
    "regulator_type": "hysteresis",
    "status": "ok"
}
```


## <code>POST</code>/hysteresis-parameters
Set hysteresis parameters. Setting hysteresis parameters will change current regulator type to hystersis.

AFTER CHANGING HYSTERESIS PARAMETERS RESTART IS REQUIRED

### Body parameters

| Field                 | Type  | Description                                  |
| --------------------- | ----- | -------------------------------------------- |
| temp_hysteresis_upper | float | upper offset (set temp + this -> stop heat)  |
| temp_hysteresis_lower | flaot | lower offset (set temp - this -> start heat) |

### Example

#### Request

- Postman: 

  ```html
  POST http://{{heater_address}}/hysteresis-parameters
  ```

  Request body:

  ```json
  {
    "temp_hysteresis_upper": 1,
    "temp_hysteresis_lower": 1,
  }
  ```


#### Response

```json
{
   "status": "ok"
}
```


## <code>GET</code>/limited-heating-power
Get current maximum limited heating power (percentage of maximum power) (only Panel and Storage heater).

#### Only for panel heaters

### Returned values

| Field | Type | Description |
| - | - | - |
| limited_heating_power | int | percentage of maximum power that heater can use. Value in range 10 - 100. |
| status | str | "ok" or error message |

### Example

#### Request

- Postman: 

  ```html
  GET http://{{heater_address}}/limited-heating-power
  ```

#### Response
```json
{
    "limited_heating_power": 75,
    "status": "ok"
}
```


## <code>POST</code>/limited-heating-power

#### Only for panel heaters

Set current maximum limited heating power (percentage of maximum power) (only Panel and Storage heater).

### Body parameters

| Field                 | Type  | Description                                  |
| --------------------- | ----- | -------------------------------------------- |
| limited_heating_power | int | percentage of maximum power that heater can use. Value in range 10 - 100. |

### Example

#### Request

- Postman: 

  ```html
  POST http://{{heater_address}}/limited-heating-power
  ```

  Request body:

  ```json
  {
    "limited_heating_power": 75,
  }
  ```

#### Response

```json
{
   "status": "ok"
}
```

## <code>GET</code>/controller-type
Get current current regulator controller type. Hysteresis controller is available for oil, convertor and socket heaters. Slow PID is available for panel and storage heaters.

### Returned values

| Field | Type | Description |
| - | - | - |
| regulator_type | str | type of current controller type ("pid" or "hysteresis_or_slow_pid") |
| status | str | "ok" or error message |

### Example

#### Request

- Postman: 

  ```html
  GET http://{{heater_address}}/controller-type
  ```

#### Response
```json
{
    "regulator_type": "hysteresis_or_slow_pid",
    "status": "ok"
}
```

## <code>POST</code>/controller-type
Set current current regulator controller type. Hysteresis controller is available for oil, convertor and socket heaters. Slow PID is available for panel and storage heaters.

### Body parameters

| Field | Type | Description |
| ----- | ---- | ----------- |
| regulator_type | str | type of current controller type ("pid", "hysteresis_or_slow_pid" or "unknown" - no change) |

### Example

#### Request

- Postman: 

  ```html
  POST http://{{heater_address}}/controller-type
  ```

  Request body:

  ```json
  {
    "regulator_type": "unknown",
  }
  ```

#### Response

```json
{
   "status": "ok"
}
```

## <code>POST</code>/set-custom-name
Change your device's custom name.

### Body parameters

| Field | Type | Description |
| ----- | ---- | ----------- |
| device_name | str | new device custom name, it can have at most 32 characters |

### Example

#### Request

- Postman: 

  ```html
  POST http://{{heater_address}}/set-custom-name
  ```

  Request body:

  ```json
  {
    "device_name": "My new custom name",
  }
  ```

#### Response

```json
{
   "status": "ok"
}
```

## <code>POST</code>/increase-set-temperature
Increase set temperature by one 0.5\*C.

### Body parameters

None

### Example

#### Request

- Postman: 

  ```html
  POST http://{{heater_address}}/increase-set-temperature
  ```

  Request body:

  None

#### Response

```json
{
   "status": "ok"
}
```

## <code>POST</code>/decrease-set-temperature
Decrease set temperature by 0.5\*C.

### Body parameters

None

### Example

#### Request

- Postman: 

  ```html
  POST http://{{heater_address}}/decrease-set-temperature
  ```

  Request body:

  None

#### Response

```json
{
   "status": "ok"
}
```

## <code>POST</code>/set-api-key
Set API key to authenticate users. BE CAREFULL!!! To reset API key one need to perform factory reset.

### Body parameters

| Field | Type | Description |
| ----- | ---- | ----------- |
| api_key | str | new API key, enables authentication and HTTPS server, it can have at most 63 characters |

### Example

#### Request

- Postman: 

  ```html
  POST http://{{heater_address}}/set-api-key
  ```

  Request body:

  ```json
  {
    "api_key": "asdasd"
  }
  ```

#### Response

```json
{
   "status": "ok"
}
```

## <code>GET</code>/commercial-lock-customization
Get commercial lock with range of possible temperature to change.

### Returned values

| Field | Type | Description |
| - | - | - |
| enable | bool | sets commercial lock state |
| min_allowed_temp_in_commercial_lock | float | minimal temperature that can be set while device has active commercial lock |
| max_allowed_temp_in_commercial_lock | float | maximal temperature that can be set while device has active commercial lock |

### Example

#### Request

- Postman: 

  ```html
  GET http://{{heater_address}}/commercial-lock-customization
  ```

#### Response
```json
{
    "enabled": false,
    "min_allowed_temp_in_commercial_lock": 11,
    "max_allowed_temp_in_commercial_lock": 30,
    "status": "ok"
}
```

## <code>POST</code>/commercial-lock-customization
Set commercial lock with range of possible temperature to change.

### Body parameters

| Field | Type | Description |
| ----- | ---- | ----------- |
| enable | bool | sets commercial lock state |
| min_allowed_temp_in_commercial_lock | float | minimal temperature that can be set while device has active commercial lock |
| max_allowed_temp_in_commercial_lock | float | maximal temperature that can be set while device has active commercial lock |
### Example

#### Request

- Postman: 

  ```html
  POST http://{{heater_address}}/commercial-lock-customization
  ```

  Request body:

  ```json
  {
      "enabled": false,
      "min_allowed_temp_in_commercial_lock": 11,
      "max_allowed_temp_in_commercial_lock": 30
  }
  ```

#### Response

```json
{
   "status": "ok"
}
```





## Fields

### ELockStatus

The ELockStatus variable allow to set one of the following lock mode:

| Value             | Description                                                  |
| ----------------- | ------------------------------------------------------------ |
| "No lock"         | all buttons are active                                       |
| "Child lock"      | buttons on the device not active. In order to activate the child lock please turn on the heater and before 5 seconds pass, press the settings button for 3 seconds and release. |
| "Commercial lock" | buttons on the device not active. In order to activate the commercial lock please turn on the heater and before 10 seconds pass, press the settings button for 3 seconds and release. |

### EOpenWindowStatus

The Open Windows function is activated instantly when temperature drops within `x1` min by `x2` degrees 
or more. The heater will automatically stop heating and `FO` will be displayed on in the display 
of the heater. The heater will automatically start heating again if temperature will increase at 
least by `x3` degrees within `x4` minutes.  

| Value                     | Description   |
| ------------------------- | ------------- |
| "Disabled not active now" | Open Windows functionality is disabled, so it is not working at all |
| "Enabled active now"      | Open Window functionality is active, but the window is not detected as open, so the heater operates normally |
| "Enabled not active now"  | Open Window functionality is active, and the window is detected as open, so the heater is not heating |

### EOprationMode

The Heater may operate in four operation modes:

| Value                  | Description                                                  |
| ---------------------- | ------------------------------------------------------------ |
| "Off"                  | the device is in off mode, it is not possible to send any comands to the device. The device doesn't follow neither weekly program nor it is in independent mode, nor in control individually                                          |
| "Weekly program"       | follow the weekly program, changing temperature by display buttons changes the temperature of the current temperature mode |
| "Independent device"   | follow the single set value, with timers enabled             |
| "Control individually" | follow the single set value, but not use any timers or weekly program |
| "Invalid"              |                                                              |

### ETemperatureType

| Value     | Description                                                  |
| --------- | ------------------------------------------------------------ |
| "Off"     | The temperature is set to default value of 0 (so that heater will not heat at all) that cannot be changed by the user. As one cannot set temperature for this type, it cannot be sent through set-temperature endpoint |
| "Normal"  | a single value, used for operation modes "Independent device" and timers |
| "Comfort" | Temperature defined for type Comfort                         |
| "Sleep"   | Temperature defined for type Sleep            |
| "Away"    | Temperature defined for type Away                            |
| "AlwaysHeating"    | Heat all the time, regardless of the temperature. One cannot set temperature for this type.  |

In weekly program one can set all of these types.
For timers, one can set only "Normal", "Off", "AlwaysHeating" types.


### EPredictiveHeatingType

Defines type of predictive heating functionality.

| Value     | Description   |
| --------- | ------------- |
| "Off"     | No predictive heating. Temperature will be change exactly with the weekly program timer |
| "Simple"  | Simple predictive heating. Temperature will be change before the timer, with a fixed time for each Celsius degree |
| "Advanced" | Advanced predictive heating. Temperature will be change before the timer, with a time based on the current room model. Model is estimated while running. |

### ECloudAndServerCommunicationType

Defines how the device communicated via WiFi and cloud.

| Value                         | Description   |
| ----------------------------- | ------------- |
| "sta_cloud_without_local_api" | Device connects to the router. Cloud is enabled, but this WiFi API is disabled |
| "sta_cloud_and_local_api"     | Device connects to the router. Cloud and this WiFi API both enabled |
| "sta_local_api_without_cloud" | Device connects to the router. Cloud is disabled, but this WiFi API is enabled |
| "ap_local_api_without_cloud"  | Device behaves as Access Point. One can connect to the device via WiFi and communicate through this WiFi API|


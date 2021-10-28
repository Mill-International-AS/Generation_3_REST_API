# Millheat heater gen. 3 - local WiFi Control API - version 0x211028 (28.10.2021)

## Overview

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
   "version": "0x210927",
   "operation_key": "",
   "status": "ok"
}
```



## HTTP Response Status

Each response will be returned the field <code>status</code> with one of the following description:

-  <code>ok</code> - the request was successful,
- <code>Failed to parse message body</code> - the request body is incorrect or the parameters are invalid,
- <code>Failed to execute the request</code> - there was a problem with the processing request, 
- <code>Length of request body too long</code> - the length of the request body is to long, 
- <code>Failed to create response body</code> -  there was a problem with the processing respone.

## Resources

We provide a [Postman](https://www.getpostman.com/) collection with a set of requests that introduce the basic concepts of the API.  The Postman collection and more information are available [here](https://gitlab.com/wizzdev/mill-int/heater-gen-3/-/blob/MI6-331_check_the_functionality_of_WiFi_REST_API/misc/rest_api/postman_collection_heaters_gen_3.json). In the collection <code>{{heater_addresss}}</code> is the variable which determines the IP address of the device.   

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



## Examples

Here, we provide example Python scripts which can control the Millheat heater gen. 3 via the REST API:

- [examples/python/basic_control.py](examples/python/basic_control.py) script queries the current control status to obtain current temperature and control signal (how much the heater is heating). Then it changes the set temperature every minute.
- [examples/python/temperature_control.py](examples/python/temperature_control.py) script queries the status of the status device and set and get the temperature in a given temperature type. Then it changes the set temperature every minute.
- [examples/python/timers.py](examples/python/timers.py) script sets a few timers scheduled for the next few minutes,  and queries the status to confirm the proper behavior. Note that the script doesn't need to keep running to have the timers working - they are stored and executed inside the device.

We also provide a simple example to control the Millheat heater gen. 3 with a Bash script:

- In [examples/bash/query_ambient_temperature.sh](examples/bash/query_ambient_temperature.sh) script the ambient temperature is returned every second.

## <code>GET</code>/status

Return a quick summary of the device information. 

### Returned parameters

| Field         | Type   | Description                                                  |
| ------------- | ------ | ------------------------------------------------------------ |
| name          | string | the name of the device                                       |
| version       | string | the API version number                                       |
| operation_key | string | if there is some operation problem (like broken temperature sensor), it may be reported in this field |

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
   "version": "0x210927",
   "operation_key": "",
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
            "type_value": "Normal",
            "time": 27245338
        },
        {
            "type_value": "Off",
            "time": 27245339
        },
        {
            "type_value": "Normal",
            "time": 27245340
        },
        {
            "type_value": "Off",
            "time": 27245341
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
              "value_type": "Off", 
              "time": 12
          },
  		{
              "value_type": "Away", 
              "time": 30
          },
  		{
              "value_type": "Sleep", "
              time": 50
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

Return temperature of the specified temperature type. 
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

Set temperature of the specified temperature type. 
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

Set PID parameters.

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
| "Off"                  | all control disable                                          |
| "Weekly program"       | follow the weekly program, changing temperature by display buttons changes the temperature of the current temperature mode |
| "Independent device"   | follow the single set value, with timers enabled             |
| "Control individually" | follow the single set value, but not use any timers or weekly program |
| "Invalid"              |                                                              |

### ETemperatureType

| Value     | Description                                                  |
| --------- | ------------------------------------------------------------ |
| "Off"     | do no heat at all. One cannot set temperature for this type  |
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


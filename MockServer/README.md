# Mock Server
### Contributers

* **Nagavarun Kanaparthy**

## Usage
```bash
sudo python RestServer.py
```

## Rest API Calls
### Global Definitions
**\<course>** can be the following options:
* courseA
* courseB
* openTest

**\<teamCode>** can follow the regular expression *[a-zA-Z]{2,5}*

### Appendix 4 - Obstacle Avoidance
#### Request: 
HTTP GET ```/obstacleAvoidance/<course>/<teamCode>```
#### Response: JSON Format
```JSON
{
    "gateCode":"(<entrance>,<exit>)"
}
```
##### Definitions
**\<entrance>** can be the following options:
* 1
* 2
* 3

**\<exit>** can be the following options:
* X
* Y
* Z

### Appendix 5 - Automated Docking
#### Request: 
HTTP GET ```/automatedDocking/<course>/<teamCode>```
#### Response: JSON Format
```JSON
{
    "dockingBaySequence":[
        {
            "symbol":"<symbol>",
            "color":"<color>"
        },
        {
            "symbol":"<symbol>",
            "color":"<color>"
        }
    ]
}
```
##### Definitions
**\<symbol>** can be the following options:
* cruciform
* triangle
* circle

**\<color>** can be the following options:
* black
* red
* green
* blue

### Appendix 6 - Interop Challenge
#### Image Upload Request: 
HTTP POST ```/interop/image/<course>/<teamCode>```
##### Request payload: 
Multipart with content-type: "multipart/mixed"
This should be the image of the auv's picture of display.
#### Response: JSON Format
```JSON
{
    "id":<imageID>
}
```
##### Definitions
**\<imageID>** is an ID represented as a string

#### Shape Report Request: 
HTTP POST ```/interop/image/<course>/<teamCode>```
##### Request payload: JSON Format
```JSON
{
    "course":<course>,
    "team":<teamCode>,
    "shape":<shape>,
    "image":<imageID>
}
```
##### Definitions
**\<shape>** is a character found on the display in the range [0-9a-fA-F] case-insensitive

**\<imageID>** is an ID represented as a string given after doing an Image Upload Request.
#### Response: JSON Format
```JSON
{
    "success":<status>
}
```
##### Definitions
**\<status>** is either *true* or *false*

### Appendix 8 - Pinger Location
#### Request: 
HTTP POST ```/pinger/<course>/<teamCode>```
##### Request payload: JSON Format
```JSON
{
    "course":<course>,
    "team":<teamCode>,
    "buoyColor1":<buoyColor>,
    "frequency1":<frequency>,
    "buoyColor2":<buoyColor>,
    "frequency2":<frequency>
}
```
##### Definitions
**\<buoyColor>** is one of the options below:
* yellow
* blue
* black
* green
* red

**\<frequency>** is in the range [25,40]
#### Response: JSON Format
```JSON
{
    "success":<status>
}
```
##### Definitions
**\<status>** is either *true* or *false*

### Appendix 9 - Heartbeat
#### Request: 
HTTP POST ```/heartbeat/<course>/<teamCode>```
##### Request payload: JSON Format
```JSON
{
    "timestamp":<timestamp>,
    "challenge":<challenge>,
    "position":{
        "datum":"WGS84",
        "latitude":<latitude>,
        "longitude":<longitude>
    }
}
```
##### Definitions
**\<timestamp>** is time in UTC in YYYYMMDDHHMMSS format

**\<challenge>** is one of the options below:
* gates
* obstacles
* docking
* pinger
* interop
* return

**\<latitude>** is float in degree decimal format (hddd.dddddd)

**\<longitude>** is float in degree decimal format (hddd.dddddd)

#### Response: JSON Format
```JSON
{
    "success":<status>
}
```
##### Definitions
**\<status>** is either *true* or *false*

### Appendix 10   - Run
#### Start Request: 
HTTP POST ```/run/start/<course>/<teamCode>```
#### Response: JSON Format
```JSON
{
    "success":<status>
}
```
##### Definitions
**\<status>** is either *true* or *false*

#### End Request: 
HTTP POST ```/run/end/<course>/<teamCode>```
#### Response: JSON Format
```JSON
{
    "success":<status>
}
```
##### Definitions
**\<status>** is either *true* or *false*


## Resources
1. **[Flask Classy Documentation](https://pythonhosted.org/Flask-Classy/)**
2. **[Implementing a RESTful Web API with Python & Flask](http://blog.luisrei.com/articles/flaskrest.html)**
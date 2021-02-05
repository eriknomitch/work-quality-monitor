# Work Quality Monitor

## Overview

A personal project to monitor work hours via a simple LED graph (inspired by [Awair Element](https://www.getawair.com/home/element)).

### Disclaimer

This should serve *only as an example* as it will be unmaintained and is only meant to serve my unique application only.

![Work Quality Monitor](docs/images/photo.jpg?raw=true "Work Quality Monitor")

## MicroPython Examples

```
import machine, neopixel

LED_DATA_PIN = 2
LED_COUNT = 24

np = neopixel.NeoPixel(machine.Pin(LED_DATA_PIN), LED_COUNT)

color = (255, 255, 255)

for i in range(24):
  np[i] = color

np.write()
```

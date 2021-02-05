# Work Quality Monitor

## Overview

A personal project to monitor my work hours simple, physical LED graphs (inspired by [Awair Element](https://www.getawair.com/home/element).

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

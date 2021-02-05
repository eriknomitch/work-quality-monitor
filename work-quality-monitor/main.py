import machine
import neopixel
import time
import network
import urequests

# Local
import config

LED_DATA_PIN = 2
LED_COUNT = 24


def connect_wifi():
    ap_if = network.WLAN(network.AP_IF)
    ap_if.active(False)
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print("Connecting to WiFi...")
        sta_if.active(True)
        sta_if.connect(config.WIFI_SSID, config.WIFI_PASSWORD)
        while not sta_if.isconnected():
            time.sleep(1)
    print("Network config:", sta_if.ifconfig())


def leds_set_all(color):
    for i in range(LED_COUNT):
        np[i] = color
    np.write()
    return np


def leds_off():
    for i in range(LED_COUNT):
        np[i] = (0, 0, 0)
    np.write()
    return np


def demo(np):
    n = np.n

    # cycle
    for i in range(4 * n):
        for j in range(n):
            np[j] = (0, 0, 0)
        np[i % n] = (255, 255, 255)
        np.write()
        time.sleep_ms(25)

    # bounce
    for i in range(4 * n):
        for j in range(n):
            np[j] = (0, 0, 128)
        if (i // n) % 2 == 0:
            np[i % n] = (0, 0, 0)
        else:
            np[n - 1 - (i % n)] = (0, 0, 0)
        np.write()
        time.sleep_ms(60)

    # fade in/out
    for i in range(0, 4 * 256, 8):
        for j in range(n):
            if (i // 256) % 2 == 0:
                val = i & 0xFF
            else:
                val = 255 - (i & 0xFF)
            np[j] = (val, 0, 0)
        np.write()

    # clear
    for i in range(n):
        np[i] = (0, 0, 0)
    np.write()


# ------------------------------------------------
# ------------------------------------------------
# ------------------------------------------------
np = neopixel.NeoPixel(machine.Pin(LED_DATA_PIN), LED_COUNT)

leds_set_all((255, 255, 0))

connect_wifi()

leds_set_all((0, 255, 0))

time.sleep(2)

leds_off()

demo(np)

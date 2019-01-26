from time import sleep
from iot_gh.IoTGreenhouseService import IoTGreenhouseService
from iot_gh.GHSwitches import GHSwitch

ghs = IoTGreenhouseService()
number = ghs.greenhouse.house_number

print("IoT Greenhouse - Electronic Devices Introduction.")
print("House Number: " + number)
print()

print("Investigate basic digital electonics.")
print("Use the toggle switch to activate the red LED lamp.")
print("Use the push button switch to end test.")
print("Jumpers must be positioned on J1 as specified in activity.\n")
last_state = None
while ghs.switches.push_button.is_off():
    state = ghs.switches.toggle.get_state()
    if state != last_state:
        if state == GHSwitch.SWITCH_ON:
            ghs.lamps.red.on()
        else:
            ghs.lamps.red.off()
        print("Switch is " + ghs.switches.toggle.get_status() )
        print("Red LED is " + ghs.lamps.red.get_status() )
        print()
        last_state = state
    sleep(.5)
    
print()
print("Test code completed.")

import RoboPiLib as RPL
import post_to_web as PTW
RPL.RoboPiInit("/dev/ttyAMA0",115200)
import time



while True:
    PTW.state['d1'] = RPL.digitalRead(16)
    time.sleep(0.3)
    PTW.post()

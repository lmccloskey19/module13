wm = cwiid.Wiimote()

import time
for i in range(16):
  wm.led = i
  time.sleep(0.5)

for i in range(16):
  wm.led = i
  if i%3:
    wm.rumble= False
  else:
    wm.rumble = True
  time.sleep(0.5)
wm.rumble = False

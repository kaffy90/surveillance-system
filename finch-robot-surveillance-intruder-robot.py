from finch import Finch
import time

finch = Finch()

finch.wheels(0.5,0.5)
time.sleep(3)
finch.wheels(-0.5,-0.5)
time.sleep(3)
finch.wheels(0,0)
finch.close()

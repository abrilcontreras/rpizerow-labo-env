from gpiozero import LED
from time import sleep

led_r = LED(19)
led_g = LED(26)
led_b = LED(13)


while True: 
		led_r.on()
		sleep(1)
		led_r.off()
		led_g.on()
		sleep(0.5)
		led_g.off()
		led_b.on()
		sleep(0.25)
		led_b.off()

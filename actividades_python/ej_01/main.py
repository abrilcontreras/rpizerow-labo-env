from gpiozero import LED, Button
from signal import pause
#importa librerias
led = LED(26) #se asigna el led color azul
button = Button(3)

button.when_pressed = led.on #cuando se apreta el boton, se enciende el led
button.when_released = led.off #cuando se suelta, el led se apaga

pause()

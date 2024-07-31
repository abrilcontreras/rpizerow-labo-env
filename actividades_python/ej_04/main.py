from gpiozero import PWMLED
from time import sleep
import ADS1x15
from math  import log as log

led_rojo = PWMLED(19)
led_azul = PWMLED(26)

ADS = ADS1x15.ADS1115(1)
ADS.setMode(ADS.MODE_SINGLE)
ADS.setGain(ADS.PGA_4_096V)

f = ADS.toVoltage()



while True:
	# Valores iniciales
	potenciometro = ADS.readADC(3)
	termistor = ADS.readADC(1)
	t_volt = termistor * f
	p_volt = potenciometro * f

	# Temperatura y calculos pertinentes

	p_temp = (p_volt * 30) / 3.3
	t_res = (t_volt * 10000)/(3.3 - t_volt)
	t_temp = 3950/((log(t_res/10000)) + (3950/298))
	t_temp = t_temp - 273.15

	print ("temp : {0:3f}".format(t_temp))
	print ("pote numero: {0:3f}".format(p_temp))

	diferencia = p_temp - t_temp

	# 2 if para la diferencia de temperatura. Resolucion de actividad

	if (p_temp < t_temp):
		led_rojo.value = 0
		brillo =  (t_temp / p_temp) / t_temp
		if (diferencia >= 5 ):
			led_azul.value = 1
		else:
			led_azul.value = brillo

	if (p_temp > t_temp):
		led_azul.value = 0
		brillo = (p_temp / t_temp) / p_temp
		if (diferencia >= 5 ):
			led_rojo.value = 1
		else:
			led_rojo.value = brillo

	sleep(1)

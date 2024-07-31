from gpiozero import LED, Buzzer
from time import sleep

# Declaro variables
led_rojo = LED(19)
led_azul = LED(26)
led_verde = LED(13)
buzzer = Buzzer(22)

# Lista de comandos

# [COMANDO] [OPCION]
#   buzz     on/off
#   rgb   red/blue/green

print ("Escriba help para visualizar la lista de comandos")

while True:
	# Incerto comando.
	respuesta = input("prompt: ingrese [COMANDO] seguido de [OPCION], separados por un _: ")

	# 6 opciones de comando, un else de error posible
	if respuesta == "buzz_on":
		buzzer.on()
	elif respuesta == "buzz_off":
		buzzer.off()
	elif respuesta == "rgb_red":
		led_azul.off()
		led_verde.off()
		led_rojo.on()
	elif respuesta == "rgb_blue":
		led_azul.on()
		led_verde.off()
		led_rojo.off()
	elif respuesta == "rgb_green":
		led_azul.off()
		led_verde.on()
		led_rojo.off()
	elif respuesta == "help":
		print("Lista de comandos\n [COMANDO] [OPCION]\n buzz     on/off \n rgb   red/blue/green")
	else:
		print("ERROR: el comando esta mal escrito o no existe. Ej existente: buzz_on")

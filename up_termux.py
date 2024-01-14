#!/usr/bin/env python3
import os
from time import sleep

print("""\033[32m

\t\t░▀█▀░█▀▀░█▀▄░█▄█░█░█░█░█
\t\t░░█░░█▀▀░█▀▄░█░█░█░█░▄▀▄
\t\t░░▀░░▀▀▀░▀░▀░▀░▀░▀▀▀░▀░▀                     

\t  ▁ ▂ ▄ ▅ ▆ ▇ █ packages █ ▇ ▆ ▅ ▄ ▂ ▁
\n\n\033[39m""")

op = input("\033[33mDesea instalar los paquetes de necesarios para iniciar el uso de \033[32mTermux? (s/n): \033[39m")
def sub():
	print("\Sigueme en mi canal para mas contenido\n\n")
	os.system("termux-open https://www.tiktok.com/@devdomainx?_t=8j1l0nNmIpK&_r=1")

if "s".lower() in op:
	print("\033[32m\nCargando ...")
	sleep(5)
	print("\n\nInstalando paquetes obligatorios".upper())
	print("\nCargando ...")
	sleep(5)
	os.system("pkg install root-repo")
	os.system("pkg install unstable-repo")
	os.system("pkg install x11-repo")
	print("\n\nInstalando paquetes de actualizacion ".upper())
	print("\nCargando ...")
	sleep(5)
	os.system("pkg update && pkg install upgrade")
	os.system("apt install bash-completion")
	print("\n\nInstalando paquetes de repositorios ".upper())
	print("\nCargando ...")
	sleep(5)
	os.system("pkg install wget")
	print("\n\nInstalando GIT".upper())
	print("\nCargando ...")
	sleep(5)
	os.system("pkg install git")
	print("\n\nInstalando PYTHON".upper())
	print("\nCargando ...")
	sleep(5)
	os.system("pkg install python && pkg install python2 && pip install --upgrade pip && pip2 install --upgrade pip && pip2 install requests")
	prompt = input("Desea cambiar el prompt a personalizado? (s/n): ")
	if "s" in prompt:
		os.system('echo PS1="[\033[1;30m][\@] [\033[5;42m]DevDomainX@Termux:\w $ [\033[0;37m]" ' )
		sub()
	else:
		sub()
		print("\n\nGracias por usar mi script DevDomain")
else:
	sub()
	print("Gracias por usar mi Script DevDomain")

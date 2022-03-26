#!/usr/bin/env python3

import subprocess

def answerexec (file_answer,ingreso,user):
	
	print("Answer: %s" % ingreso)
	print("User: %s" % user)
	
	#ponemos todo en minusculas
	ingreso = ingreso.lower()
	
	#prepara el string para ejecutar y lo ejecuta
	answerexec_args = file_answer+' '+user+' '+ingreso
	outputcomando = subprocess.run(answerexec_args, stdout=subprocess.PIPE, shell=True)
	resultado = outputcomando.stdout
	
	print('Exec:',answerexec_args)
	print(' >>>:',resultado)
	print('')
	
	return resultado

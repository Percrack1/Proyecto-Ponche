resp="Si"
while resp=="Si":
    num1=float(input("Ingresa el primer numero: "))
    op=input("Ingresa el operador (+,-,*,/): ")
    num2=float(input("Ingresa el segundo numero: "))

if op=="+":  
	res=num1+num2  
elif op=="-":  
	res=num1-num2  
elif op=="*":  
	res=num1*num2  
elif op=="/":  
	res=num1/num2  

print("Resultado:", res)  
resp=input("Desea continuar (Si/No): ")
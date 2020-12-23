peso = float(input("Digite o peso: "))
idade = int(input("Digite a idade: "))
if peso >= 50:
  if idade < 16:
    print("Impedimento:menor de 16 anos.")
  elif idade > 69:
    print("Impedimento:maior de 69 anos.")
  elif 16 < idade < 18:
    print("Restrição:requer autorização do responsável.")
  elif 60 < idade < 69:
    print("Restrição:não pode ser a primeira doação.")
  else:
    if 18 <= idade < 60:
      print("Sem impedimentos ou restrições.")
else:
  print("Você está abaixo do peso")

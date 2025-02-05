nota= float(input("Digite a nota do aluno: "))

while nota < 0 or nota > 10:
    print("Nota inválida. Por favor, digite uma nota entre 0 e 10 ")
    
    nota= float(input("Digite a nota do aluno: "))
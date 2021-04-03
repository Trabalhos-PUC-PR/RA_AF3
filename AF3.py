#1.Criar um Notebook no Google Colab com o nome AF-3
# 2.Para cada problema proposto deverá ser criado uma célula textopara o enunciado do problema, outra para a solução algorítmica e uma terceira célula de código para a App em Python
# 3.O estudante deverá baixar o notebook criado no Colab, no formato .py, e postar o arquivo no Blackboard, na atividade correspondente (Atividades Formativa -> AF-3.

#1) Elabore um algoritmo que leia dois valores inteiros e retorne se a afirmativa de que o primeiro valor é maior ou igual ao segundo é falsa ou verdadeira. 
#2) Elabore um algoritmo que leia três valores lógicos e imprima o resultado da conjunção dos três. 
#3) Elabore um algoritmo que leia duas cadeias de caracteres e imprima se a igualdade é falsa ou verdadeira. 
#4) Dada as variáveis lógicas e a expressão abaixo, desenvolva um algoritmo que imprima se o valor resultante da expressão será verdadeiro ou falso. 
# Lógicos:
# Valor_A, 
# Valor_B, 
# Valor_C, 
# Valor_D, 
# Valor_E, 
# Expressão
# Valor_A<- Falso
# Valor_B<-Verdadeiro
# Valor_C<-Verdadeiro
# Valor_D<-Falso
# Valor_E<-Falso
# Expressão<-(Valor_A ou Valor_B) e (Valor_D e Valor_C) ou não Valor_E

escolha = int(input("Escolha a atividade (1-4):"))
if(escolha>4 or escolha<1):
    exit("Atividade não existente")
else:
    if(escolha==1):#1)
        numeroum = int(input("Digite um valor Inteiro:"))
        numerodois = int(input("Digite outro valor Inteiro:"))
        if(numeroum>=numerodois):
            print("O",numeroum,"é maior que",numerodois," - essa afirmativa é verdadeira")
        else:
            print("O",numeroum,"é maior que",numerodois," - essa afirmativa é falsa")

    if(escolha==2): #2)
        logicoum = bool(int(input("Digite 0 para false e 1 para true: ")))
        logicodois = bool(int(input("Digite outro 0 para false e 1 para true: ")))
        logicotres = bool(int(input("Digite o ultimo 0 para false e 1 para true: ")))
        logicoFinal = logicoum and (logicodois and logicotres)
        print("O valor lógico final é:",logicoFinal) 

    if(escolha==3): #3)
        stringum = str(input("Digite um valor logico: "))
        stringdois = str(input("Digite outro valor logico: "))
        stringfinal = (stringum == stringdois)
        print("As strings são iguais? ",stringfinal)

    if(escolha==4): #4)
        Valor_A = False
        Valor_B = True
        Valor_C = True
        Valor_D = False
        Valor_E = False
        print("Os valores são os seguintes: ", Valor_A,Valor_B,Valor_C,Valor_D,Valor_E)
        Valor_Final = (Valor_A or Valor_B) and (Valor_D and Valor_C) or not Valor_E
        print("Após a expressão '(Valor_A ou Valor_B) e (Valor_D e Valor_C) ou não Valor_E', o resultado é: ",Valor_Final)

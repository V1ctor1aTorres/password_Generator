import string
#fornece constantes comuns para caracteres ASCII
import random
#gerar números pseudoaleatórios

def passGen():
    #atribuindo às variáveis  as sequências de caracteres correspondentes
    #letras minúsculas 
    s1 = string.ascii_lowercase
    #letras maiúsculas 
    s2 = string.ascii_uppercase
    # dígitos
    s3 = string.digits
    #pontuações 
    s4 = string.punctuation

    #comprimento desejado para a senha, armazenado na variável após ser convertido para inteiro
    passLength = int(input('Digite o tamanho da senha: \n'))
    #cria uma lista vazia  e estende essa lista com os caracteres de s1, s2, s3, e s4
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    #O método shuffle é usado para embaralhar a lista de forma aleatória
    random.shuffle(s)
    #Uma senha é criada juntando os primeiros passLength caracteres da lista
    password = ("".join(s[0:passLength]))
    print(password)


passGen()




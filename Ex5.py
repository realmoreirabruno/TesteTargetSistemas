def inverteString(s):
    listaCaracteres = list(s)

    inicio = 0
    fim = len(listaCaracteres) - 1
    
#troca os caracteres do comeco com os do fim ate o meio
    while inicio < fim:
        # Trocar os caracteres
        listaCaracteres[inicio], listaCaracteres[fim] = listaCaracteres[fim], listaCaracteres[inicio]
        # Mover os ponteiros
        inicio += 1
        fim -= 1
    
#a lista volta a ser uma string
    return ''.join(listaCaracteres)

def main():
    string = input("Digite a string que deseja inverter: ")
    string_invertida = inverteString(string)
    print(f"String invertida: {string_invertida}")

if __name__ == "__main__":
    main()

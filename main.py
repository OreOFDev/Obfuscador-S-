### OBFUSCADOR S+ ###

lista = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

listaM = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

obfuscado = ["!j4k", "a4kb4cx12", "dzxcwe", "kf15c", "ghffa", "lmh", "opfg", "dwadasf1", "asdw1", "wdasx","sdgu5341", "sxz", "f5qsd", "f4", "al453t", "fdsadas4", "afasf2", "12f", "ij5", "kfaslffaad24","1fsa23mn", "fsa35no", "pfdsfq", "rfafss", "tfaasf24fu", "vasaf1w"]

class SPlus:
    def obfuscar(palavra : str):
        resultado = ""
        for letra in palavra:
            letra_min = letra.lower()
            if letra_min in lista:
                indice = lista.index(letra_min)
                resultado += obfuscado[indice]
            else:
                resultado += letra
        return resultado    
    
    def desobfuscar(palavra : str):
        resultado = ""
        i = 0
        while i < len(palavra):
            bloco = palavra[i:i+2]
            if bloco in obfuscado:
                indice = obfuscado.index(bloco)
                resultado += lista[indice]
                i += 2
            else:
                resultado += palavra[i]
                i += 1
        return resultado

    def creditos():
        print("Obrigado por usar o S+ Obfuscator (Sw1ft SYnc), (OreOFDev)")


print(SPlus.obfuscar("Cagar"))

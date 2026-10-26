from random import randint

palco = ['', 'O', 'O/', 'O/-', 'O/--', 'O/--<']


def palavra():
    with open('palavras.txt', encoding="utf-8") as lista:
        banco = lista.readlines()
        return banco[randint(0, len(banco) - 1)].strip()


class Forca:
    def __init__(self, palavracerta):
        self.palavra = palavracerta
        self.erros = []
        self.acertos = []

    def adivinha(self, letra):
        if letra in self.palavra and letra not in self.acertos:
            self.acertos.append(letra)
        elif letra not in self.palavra and letra not in self.erros:
            self.erros.append(letra)

    def final(self):
        if self.vitoria() or (len(self.erros) >= 5):
            return True
        return False

    def vitoria(self):
        if '_' not in self.esconde():
            return True
        return False

    def esconde(self):
        status = ''
        for letra in self.palavra:
            if letra not in self.acertos:
                status += '_'
            else:
                status += letra
        return status

    def status(self):
        print('Jogo da Forca!')
        print(palco[len(self.erros)])
        print(f'Palavra: {self.esconde()}')
        print(f'Letras Erradas: {self.erros} ')
        print(f'Letras Corretas: {self.acertos}')


def main():
    jogo = Forca(palavra())

    while not jogo.final():
        jogo.status()
        letra = input('Digite uma letra: ').lower().strip()
        if len(letra) != 1 or not letra.isalpha():
            print('Digite apenas uma letra.')
            continue
        jogo.adivinha(letra)
        jogo.status()

    if jogo.vitoria():
        print('\n Você venceu!')
    else:
        print("Enforcado... X_X")
        print(f"A palavra era {jogo.palavra}")

    print('\nObrigado por jogar! \n')


if __name__ == '__main__':
    main()

# Jogo da Forca

Jogo da forca de terminal em Python. O programa sorteia uma palavra de uma lista e o jogador tenta descobrir as letras antes de completar o boneco (5 erros). Você pode alterar as palavras se quiser (todas devem estar em letras minúsculas).

## Requisitos

Python 3.6 ou superior. Não precisa instalar nenhuma biblioteca.

## Como rodar

Deixe `forca.py` e `palavras.txt` na mesma pasta e execute:

```
python forca.py
```

## Como jogar

- Digite uma letra por vez
- Letras repetidas não gastam tentativas
- Você perde ao chegar a 5 erros
- Para mudar as palavras, edite o `palavras.txt` (uma por linha, sem acentos)

## Exemplo de partida

```
Jogo da Forca!

Palavra: ________
Letras Erradas: [] 
Letras Corretas: []
Digite uma letra: a
Jogo da Forca!
O
Palavra: ________
Letras Erradas: ['a'] 
Letras Corretas: []
Jogo da Forca!
O
Palavra: ________
Letras Erradas: ['a'] 
Letras Corretas: []
Digite uma letra: e
Jogo da Forca!
O
Palavra: ___e_e__
Letras Erradas: ['a'] 
Letras Corretas: ['e']
Jogo da Forca!
O
Palavra: ___e_e__
Letras Erradas: ['a'] 
Letras Corretas: ['e']
Digite uma letra: i
Jogo da Forca!
O
Palavra: _i_e_e__
Letras Erradas: ['a'] 
Letras Corretas: ['e', 'i']
Jogo da Forca!
O
Palavra: _i_e_e__
Letras Erradas: ['a'] 
Letras Corretas: ['e', 'i']
Digite uma letra: r
Jogo da Forca!
O
Palavra: _ire_e__
Letras Erradas: ['a'] 
Letras Corretas: ['e', 'i', 'r']
Jogo da Forca!
O
Palavra: _ire_e__
Letras Erradas: ['a'] 
Letras Corretas: ['e', 'i', 'r']
Digite uma letra: p
Jogo da Forca!
O/
Palavra: _ire_e__
Letras Erradas: ['a', 'p'] 
Letras Corretas: ['e', 'i', 'r']
Jogo da Forca!
O/
Palavra: _ire_e__
Letras Erradas: ['a', 'p'] 
Letras Corretas: ['e', 'i', 'r']
Digite uma letra: n
Jogo da Forca!
O/-
Palavra: _ire_e__
Letras Erradas: ['a', 'p', 'n'] 
Letras Corretas: ['e', 'i', 'r']
Jogo da Forca!
O/-
Palavra: _ire_e__
Letras Erradas: ['a', 'p', 'n'] 
Letras Corretas: ['e', 'i', 'r']
Digite uma letra: s
Jogo da Forca!
O/-
Palavra: _ire_ess
Letras Erradas: ['a', 'p', 'n'] 
Letras Corretas: ['e', 'i', 'r', 's']
Jogo da Forca!
O/-
Palavra: _ire_ess
Letras Erradas: ['a', 'p', 'n'] 
Letras Corretas: ['e', 'i', 'r', 's']
Digite uma letra: w
Jogo da Forca!
O/-
Palavra: wire_ess
Letras Erradas: ['a', 'p', 'n'] 
Letras Corretas: ['e', 'i', 'r', 's', 'w']
Jogo da Forca!
O/-
Palavra: wire_ess
Letras Erradas: ['a', 'p', 'n'] 
Letras Corretas: ['e', 'i', 'r', 's', 'w']
Digite uma letra: l
Jogo da Forca!
O/-
Palavra: wireless
Letras Erradas: ['a', 'p', 'n'] 
Letras Corretas: ['e', 'i', 'r', 's', 'w', 'l']
Jogo da Forca!
O/-
Palavra: wireless
Letras Erradas: ['a', 'p', 'n'] 
Letras Corretas: ['e', 'i', 'r', 's', 'w', 'l']

 Você venceu!

Obrigado por jogar! 

```

## Como funciona

O estado do jogo (palavra, acertos e erros) fica numa classe `Forca`, com métodos para adivinhar, esconder a palavra, checar vitória e fim de jogo.

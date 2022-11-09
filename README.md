# Shipinsane

Projeto de um jogo desenvolvido em Python.

Sobreviva em uma jangada ao enfrentar piratas em mares desconhecidos. A dificuldade
aumentará conforme você sobrevive mais tempo, prepare-se para viver como um verdadeiro
navegador em um barco insano!

<br>

## Como Jogar

Barcos piratas aparecerão ao redor do mapa atirando bolas de canhão em direção à ilha em que se encontra o jogador.
O jogador deve desviar dos tiros e atirar nos barcos com os canhões da ilha. Caso o barco pirata encoste na ilha, piratas aparecerão para matá-lo, não deixe-os encostar!

<br>

### Teclas:

A W S D - Movimento do jogador

Espaço - Ataque corpo-a-corpo do jogador

Setas - Movimento do canhão

Espaço  - Atira com o canhão

R (no baú) - Recarrega o canhão

<br>

## Como Executar o jogo

1- Clone o repositório:

```sh
git clone git@github.com:felipemalli/game-shipinsane.git
```

2- Ative a máquina virtual:
```sh
python3 -m venv .venv && source .venv/bin/activate
```

3- Instale as dependências:
```sh
pip3 install -r requirements.txt
```

4- Entre na pasta do menu:
```sh
cd src/pages/
```

5- Inicialize o jogo:
```sh
python3 ./menu.py
```

<br>

## Equipe de desenvolvimento
<div>
  <div>
    <img width="15" src="https://avatars.githubusercontent.com/u/88905074?v=4" alt="Felipe Vahia" />
    <a href="https://github.com/felipemalli">Felipe Vahia</a>
  </div>

  <div>
    <img width="15" src="https://avatars.githubusercontent.com/u/53090840?v=4" alt="Matheus Francis" />
    <a href="https://github.com/MatheusFrancis">Matheus Francis</a>
  </div>
<div>

<br>

## Tecnologias
- Python
- Pygame
- PPlay

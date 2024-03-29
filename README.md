# Game: Shipinsane

Sobreviva em uma jangada ao enfrentar piratas em mares desconhecidos. A dificuldade
aumentará conforme você sobrevive mais tempo, prepare-se para viver como um verdadeiro
navegador em um barco insano!

<br>

## Como Jogar

Barcos piratas (normais e chefões) aparecerão ao redor do mapa atirando bolas de canhão em direção à ilha em que se encontra o jogador.
O jogador deve desviar dos tiros e atirar nos barcos com os canhões da ilha. Ao derrotar um barco, você recebe pontos proporcional à dificuldade do inimigo enfrentado, que aumenta ao decorrer do tempo! O objetivo é alcançar a maior pontuação possível, divirta-se :D!

### Teclas:

W A S D - Movimento do jogador

Setas - Rotação do canhão

Espaço - Atira com o canhão

R (no baú) - Recarrega as bolas de canhão

F1 - Aparece/Esconde hitbox do jogador e dos inimigos

F2 - Aparece/Esconde informações técnicas sobre o jogador e os inimigos

P - Pausa o jogo

R (após perder) - Recomeça o jogo

ESC - Volta para o menu

<br>

## Demonstração do jogo em vídeo

[![Shipinsane demonstration](https://img.youtube.com/vi/iHFJDzxorlI/0.jpg)](https://www.youtube.com/watch?v=iHFJDzxorlI&ab_channel=FelipeVM "Shipinsane demonstration")

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

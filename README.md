# Snake Game - Trabalho de Faculdade

## Descrição

Este é um projeto desenvolvido para a disciplina "Linguagem de Programação Aplicada" da faculdade. O jogo implementado é
uma versão do clássico Snake (Jogo da Cobrinha), utilizando a linguagem Python 3.12 e a biblioteca Pygame.

O jogo conta com:

- Música de fundo
- Efeitos sonoros para eventos (comer comida, colidir com parede ou com a própria cobra)
- Diferentes estados do jogo, organizados usando o **State Pattern**
- Persistência de pontuações utilizando SQLite

## Tecnologias Utilizadas

- **Python 3.12**
- **Pygame**
- **SQLite**

## Como Executar o Projeto

1. Certifique-se de ter o Python 3.12 instalado em sua máquina.
2. Instale as dependências necessárias executando:
   ```bash
   pip install pygame
   ```
3. Execute o jogo com o comando:
   ```bash
   python main.py
   ```

## Como Jogar

- **Setas do teclado**: Movem a cobra
- **P**: Inicia o jogo
- **S**: Exibe a pontuação
- **Q**: Sai do jogo
- **M**: Retorna ao menu principal

## Estrutura do Projeto

```
/snake_game
├── asset/                 # Arquivos de som e músicas
├── code/
│   ├── Const.py           # Constantes globais do jogo
│   ├── DBProxy.py         # Proxy para interagir com o banco de dados SQLite
│   ├── Food.py            # Classe da comida normal
│   ├── SpecialFood.py     # Classe da comida especial
│   ├── Game.py            # Classe principal do jogo
│   ├── GameState.py       # Classe base para os estados do jogo
│   ├── Menu.py            # Tela de menu inicial
│   ├── PlayingState.py    # Estado quando o jogo está rodando
│   ├── GameOver.py        # Tela de game over
│   ├── HighScore.py       # Tela com os 5 melhores scores
│   ├── Snake.py           # Classe da cobra
│   ├── Utils.py           # Funções utilitárias
└── main.py                # Arquivo principal do jogo
```

## Padrões de Projeto Utilizados

Este projeto implementa diversos padrões de projeto para garantir melhor manutenção e expansão do jogo.

### 1. State Pattern (Padrão de Estado)

O jogo implementa diferentes estados (Menu, Jogando, Game Over, High Score), e a mudança entre eles é realizada
dinamicamente.

- `GameState` é a classe abstrata que define os métodos `handle_input()`, `update()` e `draw()`.
- `Menu`, `PlayingState`, `GameOver` e `HighScore` são subclasses que implementam os estados do jogo.
- `Game` gerencia o estado atual e permite a transição entre eles usando `set_state()`.

### 2. Proxy Pattern (Padrão Proxy)

A classe `DBProxy` atua como um proxy para gerenciar interação com o banco de dados SQLite, controlando o acesso e
garantindo que as consultas sejam realizadas de forma eficiente.

### 3. Singleton Pattern (Padrão Singleton) - Aplicado indiretamente

A biblioteca `pygame` possui um loop principal único que gerencia a renderização do jogo. O objeto `Game` centraliza o
controle do jogo, garantindo que apenas uma instância dele esteja em execução.

### 4. Factory Method (Método de Fábrica)

- `Food` e `SpecialFood` implementam um método `random_position()` para gerar posições aleatórias.
- `SpecialFood` pode ser considerada uma extensão da fábrica, pois é criada apenas sob condições específicas no
  `PlayingState`.

### 5. Observer Pattern (Padrão Observador) - Implementado de forma simplificada

- O `Snake` reage aos eventos do teclado, que são detectados pelo `PlayingState`.
- Quando a cobra colide, o `Game` é notificado e o estado muda para `GameOver`, registrando a pontuação.

## Melhorias Futuras

- Implementar um sistema de leaderboard online.
- Adicionar skins personalizadas para a cobra.
- Criar diferentes modos de jogo (ex: modo arcade, modo hardcore).
- Melhorar os gráficos e animações.

## Autor

Projeto desenvolvido para a disciplina "Linguagem de Programação Aplicada".


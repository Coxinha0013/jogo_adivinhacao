# 🎯 Número Misterioso: Desafio de Adivinhação

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![POO](https://img.shields.io/badge/Paradigma-POO-green?style=for-the-badge)
![SOLID](https://img.shields.io/badge/Princípios-SOLID-red?style=for-the-badge)

Um jogo de estratégia e lógica desenvolvido para demonstrar a aplicação prática de **Arquitetura de Software** e **Programação Orientada a Objetos** em Python.

---

## 🚀 Funcionalidades Premium

O projeto vai além da lógica básica, entregando uma experiência completa de usuário:

* **Identificação de Jogador:** Sistema personalizado para entrada de nomes.
* **Níveis de Dificuldade:** Ajuste dinâmico entre Fácil, Médio e Difícil, alterando o limite de tentativas.
* **Sistema de Pontuação Inteligente:** Cálculo baseado na eficiência do acerto (tentativas restantes).
* **Ranking Top 5:** Monitoramento em tempo real dos melhores desempenhos.
* **Tratamento de Erros:** Proteção contra entradas de dados inválidas (inputs não numéricos).

---

## 🛠️ Engenharia de Software (POO & SOLID)

Este projeto foi construído sob os pilares da engenharia moderna:

### 🔹 Abstração & Contratos
Utilização da classe abstrata `Jogo` (ABC) para definir a interface obrigatória de execução.

### 🔹 Encapsulamento de Dados
Atributos privados (`__nome`, `__pontuacao`, `__numero_secreto`) garantem que o estado do objeto só seja alterado por métodos autorizados.

### 🔹 Princípios SOLID Aplicados
* **SRP (Single Responsibility):** Classes distintas para gerenciar o `Ranking`, o `Jogador` e a lógica do `Jogo`.
* **OCP (Open/Closed):** O sistema é aberto para novos tipos de jogos (extensão), mas fechado para modificação da base.
* **LSP (Liskov Substitution):** `JogoAdivinhacao` pode substituir a classe base `Jogo` sem quebrar a aplicação.

---

## 💻 Como Rodar o Desafio

1. Certifique-se de ter o **Python 3.x** instalado.
2. Clone este repositório ou baixe o arquivo `jogo.py`.
3. No terminal, execute o comando:
   ```bash
   python jogo.py
   

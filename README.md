# 💱 Conversor de Moedas

## 📌 Descrição
Este projeto consiste em um sistema de conversão de moedas desenvolvido em Python.  
O sistema permite converter valores entre diferentes moedas (USD, BRL, EUR) de forma simples e eficiente.

---

## 🎯 Objetivo
Desenvolver uma aplicação funcional aplicando conceitos de programação, testes unitários e metodologia ágil (Scrum).

---

## ⚙️ Funcionalidades
- Conversão entre moedas (USD, BRL, EUR)
- Entrada de dados pelo usuário
- Validação de moedas inválidas
- Arredondamento automático

---

## 🧠 Lógica do Sistema

1. O usuário informa:
   - Valor
   - Moeda de origem
   - Moeda de destino

2. O sistema:
   - Converte o valor para USD
   - Converte para a moeda destino

3. Retorna o valor convertido

---

## 🔁 Fluxo do Sistema (Diagrama)

Entrada → Validação → Conversão para USD → Conversão final → Saída

---

## 🔌 Interfaces

### Entrada:
- Valor (float)
- Moeda origem (string)
- Moeda destino (string)

### Saída:
- Valor convertido (float)

---

## 💾 Armazenamento

O sistema não utiliza banco de dados.  
As taxas de conversão são armazenadas em memória utilizando estruturas de dados (dicionários).

---

## 🌐 Integrações

Este projeto não utiliza APIs externas.  
As taxas de conversão são fixas para fins acadêmicos.

---

## 🗂 Estrutura do Projeto

---

## 🧪 Testes Unitários

Os testes foram implementados com a biblioteca `unittest`.

### Casos testados:
- Conversão de USD → BRL
- Conversão de BRL → USD
- Moeda inválida

### Execução dos testes:

python -m unittest
Digite o valor: 10
Moeda origem: USD
Moeda destino: BRL

Resultado: 50.0

Quadro Scrum (Trello): https://trello.com/invite/b/69e42cf2e220b2873dcd6ff9/ATTI1bfb243f56b9a5cfcc93e94f6637549f99D08BC0/agile-docs-code-sprint

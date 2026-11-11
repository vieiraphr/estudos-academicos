# POO em Python: Encapsulamento

![Python 3](https://img.shields.io/badge/Python-3-3776AB?logo=python&logoColor=white)
![Exercícios](https://img.shields.io/badge/exercícios-10-green)

Lista de 10 exercícios sobre **encapsulamento**, um dos pilares da Programação Orientada a Objetos, feita na faculdade de Análise e Desenvolvimento de Sistemas.

## Como rodar

Abra o terminal na pasta `python` e execute o exercício que quiser:

 ```bash
python exercicio1.py
 ```

Troque `exercicio1.py` pelo exercício desejado. Em alguns sistemas o comando é `python3`. Não há dependências externas.

## Conceitos praticados

| Conceito | Para que serve |
|---|---|
| Atributos privados (`__atributo`) | Esconder dados dentro da classe |
| Getters e setters | Controlar leitura e escrita |
| `@property` e `@setter` | Acessar métodos como se fossem atributos |
| `raise ValueError` | Impedir valores inválidos |
| Cópia defensiva de listas | Evitar alteração externa dos dados |

## Exercícios

1. Conta bancária: saldo protegido, regras de saque e depósito
2. Cadastro de alunos: validação de notas (0 a 10)
3. Controle de produtos: estoque e preços com `@property`
4. Cadastro de funcionários: reajustes salariais seguros
5. Sistema de biblioteca: empréstimos e devoluções
6. Controle de temperatura: sensores com limites e alertas
7. Sistema de notas escolares: médias e cópia defensiva
8. Controle de estoque: entradas, saídas e histórico
9. Sistema de autenticação: validação de senha sem expor o atributo
10. Gerenciamento de veículos: controle de velocidade máxima

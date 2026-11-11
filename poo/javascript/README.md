# AlunoPOO

Aplicação web simples de **cadastro de alunos** que demonstra os conceitos de **Programação Orientada a Objetos (POO)** em JavaScript: classes, herança e polimorfismo. Desenvolvida como exercício da *Aula 6 de POO*.

## Funcionalidades

- Formulário para cadastrar alunos com nome, idade e turma
- Validação de campos obrigatórios via HTML
- Listagem dinâmica dos alunos cadastrados na tela
- Mensagem de apresentação gerada a partir das classes `Pessoa` e `Aluno`

## Conceitos de POO aplicados

| Conceito | Onde aparece |
|---|---|
| **Classe** | `Pessoa` e `Aluno` em `script.js` |
| **Herança** | `Aluno extends Pessoa` |
| **Construtor / `super`** | `Aluno` reaproveita o construtor de `Pessoa` |
| **Polimorfismo** | O método `apresentar()` é sobrescrito em `Aluno` e chama `super.apresentar()` |

### Exemplo

```js
const aluno = new Aluno("Maria", 20, "3A");
aluno.apresentar();
// "Olá, meu nome é Maria. Tenho 20 anos e estudo na turma de 3A."
```

## Estrutura do projeto

```
.
├── index.html     # Estrutura da página e formulário
├── script.js      # Classes Pessoa/Aluno e lógica do formulário
├── css/
│   └── style.css  # Estilos da página
└── README.md
```

## Tecnologias

- HTML5
- CSS3
- JavaScript (ES6+)

## Como executar

Não é necessário instalar nada.

1. Clone ou baixe o repositório:
   ```bash
   git clone <url-do-repositorio>
   ```
2. Abra o arquivo `index.html` em qualquer navegador moderno.

Opcionalmente, use uma extensão como o **Live Server** (VS Code) para recarregar a página automaticamente durante o desenvolvimento.

## Como usar

1. Preencha **Nome**, **Idade** e **Turma**.
2. Clique em **Cadastrar**.
3. O aluno aparece na lista abaixo do formulário com sua apresentação.

> Os dados ficam apenas em memória: ao recarregar a página, a lista é apagada.


// Criação da classe Pessoa
class Pessoa {
    constructor(nome, idade) {
        this.nome = nome;
        this.idade = idade;
    }

// Método para apresentar a pessoa 
    apresentar() {
        return `Olá, meu nome é ${this.nome}.`;
    }
}


// Subclasse Aluno que herda atributos e metodos da classe Pessoa
class Aluno extends Pessoa {
    constructor(nome, idade, turma) {
        super(nome, idade);
        this.turma = turma;
    }

// Sobrescreve o método apresentar da classe Pessoa
    apresentar() {
        return `${super.apresentar()} Tenho ${this.idade} anos e estudo na turma de ${this.turma}.`;
    }
}

// Selecionando elementos do DOM e inicializando array de alunos    
const form = document.querySelector("#cadastroForm");
const lista = document.querySelector("#lista");
const alunos = [];

// Adicionando evento de submit ao formulário   
form.addEventListener("submit", (event) => {
    event.preventDefault();

// Obtendo valores dos campos do formulário    
    const nome = document.querySelector("#nome").value;
    const idade = Number(document.querySelector("#idade").value);
    const turma = document.querySelector("#turma").value;

// Criando um novo objeto Aluno e adicionando à lista de alunos    
    const aluno = new Aluno(nome, idade, turma);
    alunos.push(aluno);

// Criando um novo item de lista e adicionando à lista no DOM    
    const item = document.createElement("li");
    item.textContent = aluno.apresentar();
    lista.appendChild(item);

// Resetando o formulário após o envio      
    form.reset();
});
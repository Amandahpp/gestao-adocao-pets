CREATE TABLE Adotante (
    cpf VARCHAR(14) PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    telefone VARCHAR(20)
);

CREATE TABLE Abrigo (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nome VARCHAR(100) NOT NULL
);

CREATE TABLE Animal (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    idade INTEGER,
    sexo VARCHAR(20),
    status VARCHAR(30)
);
CREATE TABLE SolicitacaoAdocao (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    animal_id INTEGER NOT NULL,
    adotante_cpf VARCHAR(14) NOT NULL,
    estado VARCHAR(30) NOT NULL,
    status VARCHAR(30),
    FOREIGN KEY (animal_id) REFERENCES Animal(id),
    FOREIGN KEY (adotante_cpf) REFERENCES Adotante(cpf)
);
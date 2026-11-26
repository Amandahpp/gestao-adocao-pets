-- Banco de dados do sistema Patinhas Felizes (PostgreSQL 12 ou superior).
-- ATENÇÃO: este script APAGA e recria as tabelas. Use só em banco de desenvolvimento.
--
-- Como executar:
--   psql -U postgres -c "CREATE DATABASE patinhas;"
--   psql -U postgres -d patinhas -f database/banco.sql

DROP TABLE IF EXISTS SolicitacaoAdocao;
DROP TABLE IF EXISTS Animal;
DROP TABLE IF EXISTS Abrigo;
DROP TABLE IF EXISTS Adotante;

CREATE TABLE Adotante (
    cpf VARCHAR(14) PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    telefone VARCHAR(20)
);

CREATE TABLE Abrigo (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nome VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE Animal (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    idade INTEGER CHECK (idade >= 0),
    sexo VARCHAR(20) CHECK (sexo IN ('Macho', 'Fêmea')),
    status VARCHAR(30) NOT NULL DEFAULT 'Disponível'
        CHECK (status IN ('Disponível', 'Adotado')),
    tipo VARCHAR(10) NOT NULL CHECK (tipo IN ('Cachorro', 'Gato')),
    raca VARCHAR(100),      -- só para cachorro
    pelagem VARCHAR(100),   -- só para gato
    abrigo_id INTEGER REFERENCES Abrigo(id),
    CHECK (
        (tipo = 'Cachorro' AND raca IS NOT NULL) OR
        (tipo = 'Gato' AND pelagem IS NOT NULL)
    )
);

CREATE TABLE SolicitacaoAdocao (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    animal_id INTEGER NOT NULL,
    adotante_cpf VARCHAR(14) NOT NULL,
    estado VARCHAR(30) NOT NULL
        CHECK (estado IN ('Pendente', 'Aprovada', 'Rejeitada')),
    status VARCHAR(30),
    FOREIGN KEY (animal_id) REFERENCES Animal(id),
    FOREIGN KEY (adotante_cpf) REFERENCES Adotante(cpf)
);

-- Regra do sistema: cada animal pode ter só uma solicitação pendente.
CREATE UNIQUE INDEX uq_solicitacao_pendente_por_animal
    ON SolicitacaoAdocao (animal_id)
    WHERE estado = 'Pendente';

-- Dados de exemplo para demonstração. Execute DEPOIS de banco.sql:
--   psql -U postgres -d patinhas -f database/insercao.sql
-- O nome do abrigo precisa ser igual ao usado pelo programa ("Patinhas Felizes").

INSERT INTO Abrigo (nome) VALUES ('Patinhas Felizes');

INSERT INTO Animal (nome, idade, sexo, tipo, raca, pelagem, abrigo_id) VALUES
    ('Rex',  3, 'Macho', 'Cachorro', 'Labrador', NULL,    (SELECT id FROM Abrigo WHERE nome = 'Patinhas Felizes')),
    ('Bela', 1, 'Fêmea', 'Cachorro', 'SRD',      NULL,    (SELECT id FROM Abrigo WHERE nome = 'Patinhas Felizes')),
    ('Mimi', 2, 'Fêmea', 'Gato',     NULL,       'Curta', (SELECT id FROM Abrigo WHERE nome = 'Patinhas Felizes')),
    ('Tom',  4, 'Macho', 'Gato',     NULL,       'Longa', (SELECT id FROM Abrigo WHERE nome = 'Patinhas Felizes'));

INSERT INTO Adotante (cpf, nome, telefone) VALUES
    ('12345678901', 'Ana Souza',    '(54) 99999-0001'),
    ('98765432100', 'Carlos Lima',  '(54) 99999-0002');

-- Uma solicitação pendente (Rex) e uma já aprovada (Tom, que passa a "Adotado").
INSERT INTO SolicitacaoAdocao (animal_id, adotante_cpf, estado, status) VALUES
    ((SELECT id FROM Animal WHERE nome = 'Rex'), '12345678901', 'Pendente', 'Pendente'),
    ((SELECT id FROM Animal WHERE nome = 'Tom'), '98765432100', 'Aprovada', 'Aprovada');

UPDATE Animal SET status = 'Adotado' WHERE nome = 'Tom';

-- Using Database FeA
USE FeA
GO

-- Tabela de Balan�o Cont�bil das Empresas Listadas
CREATE TABLE Balances(
	Ticker VARCHAR(25),
	Moeda VARCHAR(25),
	Data_do_Reporte DATE,
	Receita_a_pagar FLOAT,
	Receitas_a_receber FLOAT,
	Bens_de_Capital FLOAT

);

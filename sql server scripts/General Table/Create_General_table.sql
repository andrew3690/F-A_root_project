-- Using Database FeA
USE FeA
GO

-- Create table General
CREATE TABLE General(
	Ticker VARCHAR(20),
	Preco_Atual FLOAT,
	Fluxo_de_Caixa FLOAT,
	EBITDA FLOAT,
	Divida_Total FLOAT, 
    Liquidez_imediata FLOAT,
    Liquidez_corrente FLOAT,
    ROE FLOAT,
    ROA FLOAT,
    Receita_Total FLOAT,
    Divida_patrimonio FLOAT,
    Fluxo_de_caixa_operacional FLOAT,
    Crescimento_de_receita_3t FLOAT,
    Margem_Bruta FLOAT,
    Margem_Ebitida FLOAT,
    Margem_Operacional FLOAT,
    Margem_liquida FLOAT,
    Crescimento_dos_ganhos_3t FLOAT,
    valor_de_mercado FLOAT
);

-- Case if necessary Drop table
-- DROP TABLE General;

SELECT * FROM General;
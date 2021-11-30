create database atacadao;
use atacadao;
show tables;
show databases;
create table if not exists fornecedor(
idfornecedor integer auto_increment,
nome long NOT NULL,
cnpj varchar(25) NOT NULL,
constraint fornecedor_pkey primary key (idfornecedor) -- Chave primaria da tabela
);

create table if not exists produto (
idproduto integer auto_increment,
idfornecedor integer NOT NULL,
descricao long NOT NULL,
preco numeric(10,2) NOT NULL,
quantestoque integer NOT NULL,
constraint produto_pkey primary key (idproduto), # Chaves primarias da tabela
constraint produto_fkeyfornecedor foreign key (idfornecedor) references fornecedor(idfornecedor)
);

create table if not exists vendedor (
idvendedor integer auto_increment,
nome long NOT NULL,
cpf varchar(25) NOT NULL,
endereco varchar(30) NOT NULL,
telefone varchar(20) NOT NULL,
constraint vendedor_pkey primary key (idvendedor) # Chaves primarias da tabela
);

create table if not exists vendas (
idvenda integer auto_increment,
idproduto integer NOT NULL,
idvendedor integer NOT NULL,
valortotal numeric(10,2) NOT NULL,
comissao numeric(10,2) NOT NULL,
constraint vendas_pkey primary key (idvenda), # Chaves primarias da tabela
constraint vendas_fkeyproduto foreign key (idproduto) references produto(idproduto),
constraint vendas_fkeyvendedor foreign key (idvendedor) references vendedor(idvendedor)
);

#select * from fornecedor;
#select * from produto;
#select * from vendas;
#select * from vendedor;

#drop database atacadao;
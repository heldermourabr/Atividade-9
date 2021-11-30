show databases;
use atacadao;
show tables;
select * from vendas;

select V.nome, Ven.valortotal from vendedor V, vendas Ven where V.idvendedor = Ven.idvendedor and Ven.idvendedor = (select idvendedor from vendas where valortotal = (select max(valortotal) from vendas)) order by Ven.valortotal desc;

select V.nome, count(Ven.idvenda) from vendedor V, vendas Ven where V.idvendedor = Ven.idvendedor group by V.nome order by count(Ven.idvenda) desc;


select F.nome, count(F.idfornecedor) from fornecedor F where F.idfornecedor in (select idfornecedor from produto where idproduto in (select idproduto from vendas)) group by F.nome order by count(F.idfornecedor) desc;


select V.nome, sum(Ven.comissao) from vendedor V, vendas Ven where V.idvendedor = Ven.idvendedor group by V.nome order by V.nome; 

select * from vendas;


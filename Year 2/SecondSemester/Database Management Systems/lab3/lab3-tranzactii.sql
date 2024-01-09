go
use Biblioteca
go

create table LogTable(
Lid int identity primary key,
TypeOperation Varchar(50),
TableOperation Varchar(50),
Execution Datetime)
go

select * from Genuri

--validare autor
go
create or alter function validare_autor(@Nume varchar(1000))
returns varchar(1500) as
begin
	declare @msg_eroare varchar(1500);
	set @msg_eroare = ' ';
	if (@Nume like '%[0-9!@#$%^&*()_-+=]%')
	begin
		set @msg_eroare = @msg_eroare + 'Numele ar trebui sa contina doar litere'
	end
	if len(@Nume) > 50 or len(@Nume) < 1 set @msg_eroare = @msg_eroare + 'Dimensiunea numelui  trebuie sa fie intre 1 si 50 de caractere!'

	set @msg_eroare = replace(@msg_eroare, ',', char(10));
	return @msg_eroare;
end
go

--validare carti
go
create or alter function validare_carti(@Titlu varchar(1000))
returns varchar(1500) as
begin
	declare @msg_eroare varchar(1500);
	set @msg_eroare = ' ';
	if (@Titlu like '%[!@#$%^&*()_-+=]%')
	begin
		set @msg_eroare = @msg_eroare + 'Titlul ar trebui sa contina doar litere sau cifre'
	end

	if len(@Titlu) > 50 or len(@Titlu) < 1 set @msg_eroare = @msg_eroare + 'Dimensiunea titlului trebuie sa fie intre 1 si 50 de caractere!'

	set @msg_eroare = replace(@msg_eroare, ',', char(10));
	return @msg_eroare;
end
go

--returnam urmatorul id in din tabela 'Autori'
go
create or alter function get_next_id_Autori()
returns int
as
begin
	declare @id int
	set @id = 0
	select top 1 @id = Auid from Autori order by Auid desc
	set @id = @id + 1;
	return @id
end
go

--returnam un id de gen pt cheie straina in carti
go
create or alter function get_gid()
returns int
as
begin
	declare @gid int
	set @gid = 0
	select top 1 @gid = Gid from Genuri order by Gid desc
	return @gid
end
go


--returnam urmatorul id in din tabela 'Carti'
go
create or alter function get_next_id_Carti()
returns int
as
begin
	declare @id int
	set @id = 0
	select top 1 @id = Cid from Carti order by Cid desc
	set @id = @id + 1;
	return @id
end
go

--procedura stocata ce insereaza datele, daca esueaza, roll-back total
go
create or alter procedure insert_total_rollback @nume_autor varchar(30), @an_nastere_autor int, @titlu_carte varchar(30), @nr_carti_carte int, @data_imprumut_carte datetime, @gid_carte int
as
begin
	begin tran
		begin try
			declare @msg_eroare_autor varchar(1500)
			declare @msg_eroare_carte varchar(1500)
			set @msg_eroare_autor = dbo.validare_autor(@nume_autor)
			set @msg_eroare_carte = dbo.validare_carti(@titlu_carte)
			if (len(@msg_eroare_autor) > 0  or len(@msg_eroare_carte) > 0)
			begin 
				declare @msg_eroare varchar(5000)
					set @msg_eroare = @msg_eroare_autor + @msg_eroare_carte
					print(@msg_eroare)
					raiserror(@msg_eroare, 14,1)
			end

			declare @id_autor int
			set @id_autor = dbo.get_next_id_Autori();
			insert into LogTable(TypeOperation, TableOperation, Execution) values ('select Auid from', 'Autori', GETDATE())
			insert into Autori(Nume,An_Nastere) values ( @nume_autor,@an_nastere_autor)
			insert into LogTable(TypeOperation, TableOperation, Execution) values ('insert into', 'Autori', GETDATE())
			
			declare @id_carte int
			set @id_carte = dbo.get_next_id_Carti();
			insert into LogTable(TypeOperation, TableOperation, Execution) values ('select Cid from', 'Carti', GETDATE())
			insert into Carti(Titlu, Nr_Carti, Data_Imprumut, Gid) values (@titlu_carte, @nr_carti_carte, @data_imprumut_carte, @gid_carte)
			insert into LogTable(TypeOperation, TableOperation, Execution) values ('insert into', 'Carti', GETDATE())

			insert into CartiAutori(Cid, Auid) values(@id_carte, @id_autor)
			insert into LogTable(TypeOperation, TableOperation, Execution) values ('insert into', 'CartiAutori', GETDATE())

			commit tran
			select 'Transaction committed'
		end try

		begin catch
			rollback tran
			select ERROR_MESSAGE()
			select 'Transaction rollbacked'
		end catch
end
go


delete from LogTable

select * from Autori
select * from Carti
select * from CartiAutori
select @@TRANCOUNT as TranCount
--commit cu succes
exec insert_total_rollback 'Adolfo Bioy Casares ', '1914', 'După-amiaza unui faun', '8', '2020-11-05', '60'
--commit gresit
exec insert_total_rollback '123', '1889', 'Ben?!','6' ,'2019-09-01', '60'

select * from Autori
select * from Carti
select * from CartiAutori
select @@TRANCOUNT as TranCount

select * from LogTable

insert into Carti(Titlu, Nr_Carti, Data_Imprumut, Gid) values ('Cili', '7', '1998-09-11', '60')
insert into Autori(Nume, An_Nastere) values ('Leroy Forest', '1867')


--procedura stocata care insereaza date, daca esueaza sa se pastreze cat mai mult posibil
go
create or alter procedure insert_partial_rollback @nume_autor varchar(30), @an_nastere_autor int, @titlu_carte varchar(30), @nr_carti_carte int, @data_imprumut_carte datetime, @gid_carte int
as
begin
	declare @id_autor int
	set @id_autor = -1
	declare @id_carte int
	set @id_carte = -1
	begin tran
		begin try
			declare @msg_eroare_autor varchar(1500)
			set @msg_eroare_autor = dbo.validare_autor(@nume_autor)
			if (len(@msg_eroare_autor ) > 0)
			begin
				raiserror(@msg_eroare_autor,14,1)
			end
			set @id_autor = dbo.get_next_id_Autori();
			insert into LogTable(TypeOperation, TableOperation, Execution) values('select Auid from', 'Autori', GETDATE())
			insert into Autori(Nume,An_Nastere) values ( @nume_autor,@an_nastere_autor)
			insert into LogTable(TypeOperation, TableOperation, Execution) values('insert into', 'Autori', GETDATE())

			commit tran
			select 'Transaction committed for Autori'
		end try

		begin catch
			rollback tran
			select 'Transaction rollbacked for Autori'
		end catch

	begin tran
		begin try
			declare @msg_eroare_carte varchar(1500)
				set @msg_eroare_carte = dbo.validare_carti(@titlu_carte)
				if (len(@msg_eroare_carte ) > 0)
				begin
					raiserror(@msg_eroare_carte,14,1)
				end
				set @id_carte = dbo.get_next_id_Carti();
				insert into LogTable(TypeOperation, TableOperation, Execution) values('select Cid from', 'Carti', GETDATE())
				insert into Carti(Titlu, Nr_Carti, Data_Imprumut, Gid) values (@titlu_carte, @nr_carti_carte, @data_imprumut_carte, @gid_carte)
				insert into LogTable(TypeOperation, TableOperation, Execution) values('insert into', 'Carti', GETDATE())

				commit tran
				select 'Transaction committed for Carti'
		end try

		begin catch
			rollback tran
			select 'Transaction rollbacked for Carti'
		end catch

	begin tran
		begin try
			if (@id_autor = -1 or @id_carte = -1)
			begin 
				raiserror('Nu se poate face inserarea in tabela CartiAutori',14,1)
			end
			insert into CartiAutori(Cid, Auid) values(@id_carte, @id_autor)
			insert into LogTable(TypeOperation, TableOperation, Execution) values ('insert into', 'CartiAutori', GETDATE())

			commit tran
			select 'Transaction committed for CartiAutori'
		end try

		begin catch
			rollback tran
			select 'Transaction rollback for CartiAutori'
		end catch
end
go


delete from LogTable
select * from Autori
select * from Carti
select * from CartiAutori
select @@TRANCOUNT as TranCount
--commit cu succes toate tabelele
exec insert_partial_rollback 'Silvia Moreno-Garcia', '1981', 'Mexican Gothic', '4', '1978-11-01', '60'
--commit cu succes doar in tabela Autori
exec insert_partial_rollback 'Alejo Carpentier', '1978', 'Micul Print!?', '4', '2017-08-01', '60'
--commit cu succes doar in tabela Carti
exec insert_partial_rollback '123', '1900', 'Pașii pierduţi', '4', '2016-11-10', '60'
--commit gresit
exec insert_partial_rollback '123', '1900', 'Micul Print!!??', '4', '2007-01-12', '60'

select * from Autori
select * from Carti
select * from CartiAutori
select @@TRANCOUNT as TranCount

select * from LogTable
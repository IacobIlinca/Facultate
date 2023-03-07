use Biblioteca
go

Create function dbo.TestNrCarti(@nr int)
RETURNS INT
AS
BEGIN
IF @nr> 0  SET @nr = 1
ELSE SET @nr = 0
RETURN @nr
END
go

Create function dbo.TestAnNastere(@an int)
RETURNS INT
AS
BEGIN
IF @an> 1500  SET @an = 1
ELSE SET @an = 0
RETURN @an
END

GO
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO


alter procedure [dbo].[CRUD_Autori]
@table_name Varchar(50),
@nume varchar(50),
@an_nastere int
AS
BEGIN
	SET NOCOUNT ON;
	-- verify the parameters - at least one from the list
	IF (dbo.TestAnNastere(@an_nastere)=1)
	BEGIN
		--CREATE=INSERT
		insert into Autori(Nume, An_Nastere) Values(@nume, @an_nastere)
		-- READ=SELECT
		select * from Autori
		-- UPDATE
		update Autori set An_Nastere='1970'
		where An_Nastere>1950 and Nume LIKE 'S%'
		-- DELETE
		delete from CartiAutori
		delete from Autori
		where An_Nastere < 1900
		print 'CRUD operations for table ' + @table_name
		END
	ELSE
	BEGIN
		PRINT 'Error'
		RETURN
	END
END
go

EXEC CRUD_Autori 'Autori', 'Heil Gaiman', 1960 --EXECUTIE CU SUCCES
go
EXEC CRUD_Autori 'Autori', 'Mihai Eminescu', -98 --EXECUTIE FARA SUCCES ->ERROR
go


alter procedure [dbo].[CRUD_Carti]
@table_name Varchar(50),
@titlu varchar(50),
@nr_carti int,
@data_imprumut DATETIME
AS
BEGIN
	SET NOCOUNT ON;
	-- verify the parameters - at least one from the list
	IF (dbo.TestNrCarti(@nr_carti)=1)
	BEGIN
		--CREATE=INSERT
		declare @gid int
		SELECT TOP 1 @gid = Gid FROM dbo.Genuri
		insert into Carti(Titlu, Nr_Carti,Data_Imprumut,Gid) Values(@titlu, @nr_carti, @data_imprumut,@gid)
		-- READ=SELECT
		select * from Carti
		-- UPDATE
		update Carti set Nr_Carti='10'
		where Titlu LIKE 'C%'
		-- DELETE
		delete from CartiAutori
		delete from Inregistrari
		delete from Carti
		where Nr_Carti < 3
		print 'CRUD operations for table ' + @table_name
		END
	ELSE
	BEGIN
		PRINT 'Error'
		RETURN
	END
END
go

EXEC CRUD_Carti 'Carti', 'The Sandman', 3, '2813-12-03'  --EXECUTIE CU SUCCES
go

EXEC CRUD_Carti 'Carti', 'Infernul', -93, '2013-12-03'  --EXECUTIE FARA SUCCES -> ERROR
go


alter procedure [dbo].[CRUD_CartiAutori]
@table_name Varchar(50)
AS
BEGIN
	SET NOCOUNT ON;
	-- verify the parameters - at least one from the list
	BEGIN
		--CREATE=INSERT
		--insert into CartiAutori(Cid, Auid) values ('5005','5004')
		--insert into CartiAutori(Cid, Auid) values ('5007','5002')
		declare @cid int
		SELECT TOP 1 @cid = Cid FROM dbo.Carti
		declare @auid int
		SELECT TOP 1 @auid = Auid FROM dbo.Autori
		insert into CartiAutori(Cid,Auid) Values(@cid, @auid)
		-- READ=SELECT
		select * from CartiAutori
		-- UPDATE
		update CartiAutori set Cid='5008'
		where Auid LIKE '5001'
		-- DELETE
		delete from CartiAutori
		where Cid = 5008
		print 'CRUD operations for table ' + @table_name
		END
END

EXEC CRUD_CartiAutori 'CartiAutori'
go

CREATE VIEW vw_Carti 
AS
SELECT c.Nr_Carti
FROM  Carti c
where c.Nr_Carti > 2;
go

select * from Carti
select * from Autori
go


alter VIEW vw_Autori_CartiAutori
AS
SELECT a.Nume, a.Auid
FROM  Autori a inner join CartiAutori ca on a.Auid = ca.Auid
where a.Nume like 'C%';

go

go
alter VIEW vw_Autori_CartiAutori2
AS
SELECT a.Auid
FROM  Autori a inner join CartiAutori ca on a.Auid = ca.Auid
--where a.Nume like 'C%';
go

select * from  vw_Carti					--PRIMUL BUN
select * from  vw_Autori_CartiAutori
select * from  vw_Autori_CartiAutori2	--AL DOILEA BUN

--PRIMUL BUN!!
IF EXISTS (SELECT NAME FROM sys.indexes WHERE name='N_idx_carti_nr_carti')
DROP INDEX N_idx_carti_nr_carti ON Carti
CREATE NONCLUSTERED INDEX N_idx_carti_nr_carti ON Carti (Nr_Carti)

select * from vw_Carti		--PRIMUL BUN

go
IF EXISTS (SELECT NAME FROM sys.indexes WHERE name='N_idx_autori_cartiautori_auid_nume')
DROP INDEX N_idx_autori_cartiautori_auid_nume ON Autori
CREATE NONCLUSTERED INDEX N_idx_autori_cartiautori_auid_nume ON Autori (Nume, Auid)

select * from Genuri
insert into Autori(Nume, An_Nastere) Values('Charles Dickens', '1812'), ('J. K. Rowling','1965'), ('Jane Austen','1775'),('William Blake','1757')
insert into Autori(Nume, An_Nastere) Values ('Chabon Michael','1970'),('Campbell Eddie','1967')
select * from Autori
insert into Carti(Titlu, Nr_Carti, Data_Imprumut, Gid) Values('Harry Potter1', '2','2022-01-09','62'), ('Harry Potter2','1','2009-09-09','62'), ('Emma','3','2008-01-01','61'),('Tigrul','1','2004-09-01','61')
select * from Autori
select * from Carti
insert into CartiAutori(Cid, Auid) values ('5014','5011'), ('5017','5012'), ('5018','5013')


go
--AL DOILEA BUN!!
IF EXISTS (SELECT NAME FROM sys.indexes WHERE name='N_idx_autori_cartiautori_auid_nume2')
DROP INDEX N_idx_autori_cartiautori_auid_nume2 ON Carti
CREATE NONCLUSTERED INDEX N_idx_autori_cartiautori_auid_nume2 ON CartiAutori (Auid)

select * from  vw_Autori_CartiAutori2	--AL DOILEA BUN


go
create VIEW vw_Autori_CartiAutori3
AS
SELECT a.Nume, a.Auid
FROM  Autori a inner join CartiAutori ca on a.Auid = ca.Auid
go

select * from vw_Autori_CartiAutori3
order by Auid

--AL TREILEA BUN!!
create view vw_Autori
as
select a.Nume
from Autori a 
where a.Nume like 'C%'
go

select * from vw_Autori --BUN
select * from CartiAutori
select * from Autori
insert into CartiAutori(Cid, Auid) values ('5017','5019')
go


--ULTIMA BUNA!!!!!!
alter view vw_Carti_CartiAutori
as
select c.Gid
from Carti c inner join CartiAutori ca on c.Cid = ca.Cid
inner join Genuri g on g.Gid = c.Gid
where c.Gid >= 60 
go


select * from vw_Carti_CartiAutori

IF EXISTS (SELECT NAME FROM sys.indexes WHERE name='N_idx_carti_cartiautori_gid')
DROP INDEX N_idx_carti_cartiautori_gid ON Carti
CREATE NONCLUSTERED INDEX N_idx_carti_cartiautori_gid ON Carti (Gid)

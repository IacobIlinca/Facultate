use Biblioteca
go


insert into Tables(Name) values ('Carti')

insert into Tables(Name) values ('CartiAutori')

insert into Tables(Name) values ('Autori')

select * from Tables

select * from Autori

go

CREATE VIEW view_1 AS
select Nume,An_Nastere
	from Autori a
	where a.An_Nastere>1950
GO

create procedure exec_view1
as 
begin
	select * from View_1
end

exec exec_view1
go

select * from Carti
go

create view view_2 as
	select c.Titlu,c.Nr_Carti,c.Data_Imprumut
	from Carti c INNER JOIN Genuri g on c.Gid=g.Gid
	where c.Nr_Carti >= 5
go

create procedure exec_view2
as 
begin
	select * from View_2
end
exec exec_view2
go


select * from CartiAutori
select * from Carti
select * from Autori
insert into CartiAutori(Cid,Auid) values (15,12)
insert into CartiAutori(Cid,Auid) values (16,9)
insert into CartiAutori(Cid,Auid) values (17,9)
insert into CartiAutori(Cid,Auid) values (18,10)
insert into CartiAutori(Cid,Auid) values (18,11)
go

create view view_3 as
	select	ca.Auid, avg(c.Nr_Carti) as MediumNumberOfBooks
	from Carti c INNER JOIN CartiAutori ca on c.Cid=ca.Cid
	group by ca.Auid
	having avg(c.Nr_Carti)>3
go

create procedure exec_view3
as 
begin
	select * from View_3
end

exec exec_view3

go

insert into Views(name) values('View_1')

insert into Views(name) values('View_2')

insert into Views(name) values('View_3')

select * from Views

go

insert into Tests(Name) values('DI_Autori')
insert into Tests(Name) values('DI_Carti')
insert into Tests(Name) values('Select_View_CartiAutori')
select * from Tests
go


alter procedure DI_Autori @nr int as
begin
	delete from CartiAutori
	delete from Autori
	declare @i int
	set @i=1
	DBCC CHECKIDENT ('[Autori]', RESEED, 0)
	while @i<=@nr
	begin
		insert into Autori(Nume,An_Nastere) Values('nume'+cast(@i as varchar(12)),1900+@i)
		set @i=@i+1
	end
end

exec DI_Autori 30

select * from Autori
go

create procedure fk_sectoare as
begin
select min(s.Sid)
from Sectoare s
end
go

SELECT * FROM Adrese_Bibliotecari
go
delete from Carti
go

alter procedure DI_Carti @nr int as
begin
	delete from Autori
	delete from CartiAutori
	delete from Inregistrari
	delete from Carti
	delete from Genuri
	delete from Bibliotecari
	delete from Sectoare
	delete from Adrese_Bibliotecari
	insert into Adrese_Bibliotecari(Strada,Numar,Oras) values ('Mihai Eminescu',100,'Cluj Napoca') 
	insert into Sectoare(Denumire,Etaj,Cladire) values ('Istorie',5,'Centrala')

	declare @fk_s int
	SELECT TOP 1 @fk_s = Sid FROM dbo.Sectoare
	declare @fk_adbid int
	SELECT TOP 1 @fk_adbid = AdBid FROM dbo.Adrese_Bibliotecari
	insert into Bibliotecari(Nume,Nr_Telefon,AdBid,Sid) values ('Popa Ioan', 0725671112,@fk_adbid,@fk_s)

	declare @fk_bid int
	SELECT TOP 1 @fk_bid = Bid FROM dbo.Bibliotecari
	insert into Genuri(Denumire, Bid) values ('SF',@fk_bid)



	declare @i int
	declare @Gid int
	set @i=1
	DBCC CHECKIDENT ('[Carti]', RESEED, 0);
	while @i<=@nr
	begin
		SELECT TOP 1 @Gid = Gid FROM dbo.Genuri
		insert into Carti(Titlu,Nr_Carti,Data_Imprumut,Gid) Values('titlu'+cast(@i as varchar(12)),@i,cast(@i+2020 as varchar(12))+'-01-01',@Gid)
		set @i=@i+1
	end
end

exec DI_Carti 30

go
select * from Carti
go

create procedure Select_View_CartiAutori as
begin
	exec DI_Carti 10
	exec DI_Autori 10
	declare @i int
	declare @j int
	declare @poz1 int
	declare @poz2 int
	set @i=1
	while @i<=10
	begin
		set @j=1
		while @j<=10
		begin
			SELECT @poz1 = Cid FROM dbo.Carti where Carti.Cid=@i
			SELECT @poz2 = Auid FROM dbo.Autori where Autori.Auid=@j
			insert into CartiAutori(Cid,Auid) Values(@j,@i)
			set @j=@j+1
		end
		set @i=@i+1
	end
	select * from view_3
end

exec Select_View_CartiAutori

--add in test views
insert into TestViews(TestID,ViewID) values (1,1)

insert into TestViews(TestID,ViewID) values (1,2)

insert into TestViews(TestID,ViewID) values (2,1)

insert into TestViews(TestID,ViewID) values (2,2)

select * from TestViews

go
-- add to TestTables
create procedure populateTestTables @nr int as
begin
	delete from TestTables
	insert into TestTables(TestID,TableID,NoOfRows,Position) Values (1,1,@nr,1)
	insert into TestTables(TestID,TableID,NoOfRows,Position) Values (2,2,@nr,2)
	select * from TestTables
end

go
create procedure run1 as
begin
	DECLARE @ds DATETIME -- start time test
	DECLARE @di DATETIME -- intermediate time test
	DECLARE @de DATETIME -- end time test
	declare @NoOfRows int
	SELECT TOP 1 @NoOfRows = NoOfRows FROM dbo.TestTables
	where TableID=1
	SET @ds = GETDATE()
	-- delete from table
	-- insert into table
	exec DI_Autori @NoOfRows
	SET @di=GETDATE()
	-- evaluate (select from) view
	Select * from view_1
	SET @de=GETDATE()
	Print DATEDIFF(millisecond,@de, @ds)
	
	delete from TestRuns
	where Description='AutoriTest'
	DBCC CHECKIDENT ('[TestRuns]', RESEED, 0)
	insert into TestRuns(Description,StartAt,EndAt) Values ('AutoriTest',@ds,@de)
	insert into TestRunTables(TestRunID,TableID,StartAt,EndAt) Values (1,1,@ds,@di)
	insert into TestRunViews(TestRunID,ViewID,StartAt,EndAt) Values (1,1,@di,@de)
end
go

create procedure run2 as
begin
	DECLARE @ds DATETIME-- start time test
	DECLARE @di DATETIME-- intermediate time test
	DECLARE @de DATETIME-- end time test
	declare @NoOfRows int
	SELECT TOP 1 @NoOfRows = NoOfRows FROM dbo.TestTables
	where TableID=2
	SET @ds = GETDATE()
	-- delete from table
	-- insert into table
	exec DI_Carti @NoOfRows
	SET @di=GETDATE()
	-- evaluate (select from) view
	Select * from view_2
	SET @de=GETDATE()
	Print DATEDIFF(millisecond,@de, @ds)
	
	delete from TestRuns
	where Description='CartiTest'
	
	--BCC CHECKIDENT ('[TestRuns]', RESEED, 0)
	insert into TestRuns(Description,StartAt,EndAt) Values ('CartiTest',@ds,@de)
	declare @TestRunID int
	SELECT TOP 1 @TestRunID = TestRunId FROM dbo.TestRuns
	where Description='CartiTest'
	insert into TestRunTables(TestRunID,TableID,StartAt,EndAt) Values (@TestRunID,2,@ds,@di)
	insert into TestRunViews(TestRunID,ViewID,StartAt,EndAt) Values (@TestRunID,2,@di,@de)
end


exec populateTestTables 5000
exec run1
exec run2

select * from TestRuns
select * from TestRunTables
select * from TestRunViews
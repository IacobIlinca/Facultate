use Biblioteca
go

--Modifica tipul unei coloane
--v1
create procedure ModificaColoana as begin 
	alter table Adrese_Persoane
	alter column Numar smallint
	print 'Coloana a fost modificata'
end
go

--invers v1
create procedure UndoModificaColoana as begin
	alter table Adrese_Persoane
	alter column Numar int
	print 'Coloana a fost resetata la tipul initial'
end
go

--exec ModificaColoana
--exec UndoModificaColoana

--Adauga o costrângere de “valoare implicita” pentru un câmp
--v2
create procedure AddConstraint as begin
	alter table Sectoare
	add constraint df_SectoareEtaj default 1 for Etaj
	print 'Etajul unui sector a fost setat default la 1'
end
go


--invers v2
create procedure UndoAddConstraint as begin
	alter table Sectoare
	drop constraint df_SectoareEtaj
	print 'Sectoarele nu mai au 1 etaje default'
end
go

--exec AddConstraint
--exec UndoAddConstraint

--create table
--v3
create procedure AddTable2 as begin
	create table Orar_Bibliotecari(
	Oid int primary key identity,
	Ora_incepere int)
	print 'A fost creat tabel Orar_Bibliotecari'
end
go

drop table Orar_Bibliotecari
go


--invers v3
create procedure UndoAddTable2 as begin
	drop table Orar_Bibliotecari
	print 'A fost stearsa tabela Orar_Bibliotecari'
end 
go

--exec AddTable2
--exec UndoAddTable2

--adauga un camp nou
--v4
create procedure AddCamp as begin
	alter table Orar_Bibliotecari
	add Ora_Inchidere int
	print 'A fost adaugat un camp nou'
end
go

create procedure AddCamp1 as begin
	alter table Orar_Bibliotecari
	add Bid int
	print 'A fost adaugat un camp nou'
end
go

--invers v4
create procedure UndoAddCamp as begin
	alter table Orar_Bibliotecari
	drop column Ora_Inchidere 
	print 'A fost stersa coloana'
end
go

create procedure UndoAddCamp1 as begin
	alter table Orar_Bibliotecari
	drop column Bid 
	print 'A fost stersa coloana'
end
go

--exec AddCamp1
--exec UndoAddCamp

--creea o constrângere de cheie str?in?
--v5
create procedure AddConstrFK as begin
	alter table Orar_Bibliotecari
	add constraint fk_Orar foreign key(Bid)
	references Bibliotecari(Bid)
	print 'A fost adaugata constrangerea de cheie straine'
end
go

--invers v5
create procedure UndoAddConstrFK as begin
	alter table Orar_Bibliotecari
	drop constraint fk_Orar
	print 'A fost stearsa constrangerea de cheie straine'
end 
go

exec AddConstrFK
exec UndoAddConstrFK

create table Versiuni(
	versiune int)

insert into versiuni values (0)
go

create procedure mainBun
    @wantedVersion tinyint
as
begin
    declare @vers tinyint
    set @vers = (select versiune from dbo.Versiuni)


	 if(@wantedVersion < 0 OR @wantedVersion > 5) begin
        print('Versiunea trebuie sa fie un numar intre 0 si 5!')
        goto SKIPPER
    end

    while(@vers < @wantedVersion)
    begin
        if(@vers = 0) begin
            exec ModificaColoana
        end
        if(@vers = 1) begin
            exec AddConstraint
        end
        if(@vers = 2) begin
            exec AddTable2
        end
        if(@vers = 3) begin
            exec AddCamp
			exec AddCamp1
        end
        if(@vers = 4) begin
            exec AddConstrFK
        end
        set @vers = @vers +1;
    end

    while(@vers > @wantedVersion)
    begin
        if(@vers = 5) begin
            exec UndoAddConstrFK
        end
        if(@vers = 4) begin
            exec UndoAddCamp
			exec UndoAddCamp1
        end
        if(@vers = 3) begin
            exec UndoAddTable2
        end
        if(@vers = 2) begin
            exec UndoAddConstraint
        end
        if(@vers = 1) begin
            exec UndoModificaColoana
        end
        set @vers = @vers -1;
    end

    if(@vers = @wantedVersion)
    begin
        print 'Baza de date a fost adusa la versiunea dorita!'
        update dbo.Versiuni
        set versiune = @vers
    end

    skipper:
end
go

exec mainBun 22
select * from Versiuni

drop table Versiuni















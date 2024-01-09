use Biblioteca
go

-- dirty reads
select * from Carti

BEGIN TRANSACTION
UPDATE Carti SET Titlu='Dune 6' WHERE Cid = 5005
WAITFOR DELAY '00:00:20'
ROLLBACK TRANSACTION

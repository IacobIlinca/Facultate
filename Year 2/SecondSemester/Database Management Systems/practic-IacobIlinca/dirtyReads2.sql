use S9
go

-- dirty reads
select * from Copii

BEGIN TRANSACTION
UPDATE Copii SET Varsta='5' WHERE Cid = 1
WAITFOR DELAY '00:00:20'
ROLLBACK TRANSACTION
-- nonrepeatable reads
use Biblioteca
select * from Carti
INSERT INTO Carti(Titlu, Nr_Carti,Data_Imprumut, Gid) VALUES ('Peter Pan','3','2011-09-02','60')
delete from Carti where Titlu='Peter Pan'

--asta
BEGIN TRAN
WAITFOR DELAY '00:00:10'
UPDATE Carti SET Nr_Carti='5' WHERE Titlu = 'Peter Pan'
COMMIT TRAN





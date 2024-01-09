-- phantom reads
use Biblioteca
select * from Carti

BEGIN TRAN
WAITFOR DELAY '00:00:10'
INSERT INTO Carti(Titlu, Nr_Carti,Data_Imprumut, Gid) VALUES ('At the end of the world','3','2012-09-02','60')
COMMIT TRAN

delete from Carti where Titlu = 'At the end of the world'
-- deadlock
-- transaction 1
begin tran
update Carti set Titlu='deadlock Carti Transaction 1' where Cid=5028
-- this transaction has exclusively lock on table Books
waitfor delay '00:00:10'
update Autori set Nume='deadlock Autori Transaction 1' where Auid=5011
commit tran

select * from Autori
--deadlock
-- transaction 2
SET DEADLOCK_PRIORITY HIGH
-- SET DEADLOCK_PRIORITY LOW
begin tran
update Autori set Nume='deadlock Autori Transaction 2' where Auid=5011
-- this transaction has exclusively lock on table Authors
waitfor delay '00:00:10'
update Carti set Titlu='deadlock Carti Transaction 2' where Cid=5028
commit tran

select * from Autori
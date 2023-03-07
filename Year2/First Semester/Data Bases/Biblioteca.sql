Create database Biblioteca
go
Use Biblioteca
go

CREATE TABLE Sectoare
(Sid INT PRIMARY KEY IDENTITY,
Denumire varchar(50),
Etaj int,
Cladire varchar(100))


CREATE TABLE Adrese_Bibliotecari
(AdBid INT PRIMARY KEY IDENTITY,
Strada varchar(50),
Numar INT,
Oras varchar(50))



CREATE TABLE Bibliotecari
(Bid INT PRIMARY KEY IDENTITY,
Nume varchar(100),
Nr_Telefon int,
AdBid INT FOREIGN KEY REFERENCES Adrese_Bibliotecari(AdBid),
Sid INT FOREIGN KEY REFERENCES Sectoare(Sid))



CREATE TABLE Genuri
(Gid INT PRIMARY KEY IDENTITY,
Denumire varchar(50),
Bid INT FOREIGN KEY REFERENCES Bibliotecari(Bid))


CREATE TABLE Carti
(Cid INT PRIMARY KEY IDENTITY,
Titlu varchar(100),
Nr_Carti int,
Data_Imprumut DATETIME UNIQUE,
Gid INT FOREIGN KEY REFERENCES Genuri(Gid))

CREATE TABLE Autori
(Auid INT PRIMARY KEY IDENTITY,
Nume varchar(100),
An_Nastere int)

CREATE TABLE CartiAutori
(Cid INT FOREIGN KEY REFERENCES Carti(Cid),
Auid INT FOREIGN KEY REFERENCES Autori(Auid)
CONSTRAINT pk_CartiAutori PRIMARY KEY (Cid, Auid))

CREATE TABLE Adrese_Persoane
(AdPid INT PRIMARY KEY IDENTITY,
Strada varchar(100),
Numar int,
Oras varchar(100))

CREATE TABLE Persoane 
(Pid INT PRIMARY KEY IDENTITY,
NUME varchar(50),
Prenume varchar(50),
Email varchar(50),
Aid INT FOREIGN KEY REFERENCES Adrese_Persoane(AdPid))

CREATE TABLE Inregistrari
(Cid INT FOREIGN KEY REFERENCES Carti(Cid),
Pid INT FOREIGN KEY REFERENCES Persoane(Pid),
CONSTRAINT pk_Inregistrari PRIMARY KEY (Cid, Pid))

Use Biblioteca
go

INSERT INTO Sectoare(Denumire, Etaj, Cladire) 
VALUES ('SF', '2', 'Nicolae Iorga')

INSERT INTO Sectoare(Denumire, Etaj, Cladire) 
VALUES ('Thriller', '1', 'Nicolae Iorga')

INSERT INTO Sectoare(Denumire, Etaj, Cladire) 
VALUES ('Romance', '0', 'Nicolae Iorga')

INSERT INTO Sectoare(Denumire, Etaj, Cladire) 
VALUES ('Drama', '0', 'Mihai Eminescu')

INSERT INTO Sectoare(Denumire, Etaj, Cladire) 
VALUES ('Politica', '1', 'Mihai Eminescu')

INSERT INTO Sectoare(Denumire, Etaj, Cladire) 
VALUES ('Istorie', '2', 'Mihai Eminescu')


SELECT * FROM Sectoare
delete from Sectoare

INSERT INTO Adrese_Bibliotecari(Strada, Numar, Oras) 
VALUES ('Aurel Vlaicu', '1', 'Alba Iulia')

INSERT INTO Adrese_Bibliotecari(Strada, Numar, Oras) 
VALUES ('Aurel Vlaicu', '5', 'Alba Iulia')

INSERT INTO Adrese_Bibliotecari(Strada, Numar, Oras) 
VALUES ('Republicii', '12', 'Cluj Napoca')

INSERT INTO Adrese_Bibliotecari(Strada, Numar, Oras) 
VALUES ('Republicii', '3', 'Cluj Napoca')


INSERT INTO Adrese_Bibliotecari(Strada, Numar, Oras) 
VALUES ('Lalelor', '2', 'Turda')

INSERT INTO Adrese_Bibliotecari(Strada, Numar, Oras) 
VALUES ('Eugen Ionescu', '8', 'Turda')

SELECT * FROM Sectoare
SELECT * from Adrese_Bibliotecari
delete from Adrese_Bibliotecari


INSERT INTO Bibliotecari(Nume, Nr_Telefon, AdBid, Sid) 
VALUES ('Popa Florina', '0723506789', '60' , '60')

INSERT INTO Bibliotecari(Nume, Nr_Telefon, AdBid, Sid) 
VALUES ('Marin Adriana', '0726586231', '63' , '59')

INSERT INTO Bibliotecari(Nume, Nr_Telefon, AdBid, Sid) 
VALUES ('Popa Matei', '0737786931', '60' , '63')

INSERT INTO Bibliotecari(Nume, Nr_Telefon, AdBid, Sid) 
VALUES ('Anton Daniel', '0778560131', '62' , '61')

INSERT INTO Bibliotecari(Nume, Nr_Telefon, AdBid, Sid) 
VALUES ('Calin Vlad', '0706566151', '61' , '61')

INSERT INTO Bibliotecari(Nume, Nr_Telefon, AdBid, Sid) 
VALUES ('Marcu Andrei', '0743491721', '65' , '59')

INSERT INTO Bibliotecari(Nume, Nr_Telefon, AdBid, Sid) 
VALUES ('Pascu Iulia', '0726892753', '62' , '59')

INSERT INTO Bibliotecari(Nume, Nr_Telefon, AdBid, Sid) 
VALUES ('Marian Petru', '0726444753', '62' , '61')

SELECT * FROM Bibliotecari
delete from Bibliotecari
select * from Bibliotecari
select * from Adrese_Bibliotecari
select * from Sectoare 
INSERT INTO Genuri(Denumire, Bid) 
VALUES ('Fantasy', '72')

INSERT INTO Genuri(Denumire, Bid) 
VALUES ('Crima', '72')

INSERT INTO Genuri(Denumire, Bid) 
VALUES ('Dragoste', '73')

INSERT INTO Genuri(Denumire, Bid) 
VALUES ('YoungAdult', '75')

INSERT INTO Genuri(Denumire, Bid) 
VALUES ('Politist', '73')

INSERT INTO Genuri(Denumire, Bid) 
VALUES ('Dezvoltare personala', '74')

SELECT * FROM Genuri
delete from Genuri


INSERT INTO Carti(Titlu,Data_Imprumut,Nr_Carti, Gid) 
VALUES ('Dune','2022-11-10 12:35:23', '5', '59')

INSERT INTO Carti(Titlu,Data_Imprumut,Nr_Carti, Gid) 
VALUES ('Moarte pe Nil','2022-04-17', '2', '60')

INSERT INTO Carti(Titlu,Data_Imprumut,Nr_Carti, Gid) 
VALUES ('Crima din Orient Express','2022-09-15', '3', '60')

INSERT INTO Carti(Titlu,Data_Imprumut,Nr_Carti, Gid) 
VALUES ('Cronicile lui Magnus Bane','2022-02-23', '7', '62')

select * from Carti

INSERT INTO Autori(Nume,An_Nastere) 
VALUES ('Agatha Christie','1890')

INSERT INTO Autori(Nume,An_Nastere) 
VALUES ('Cassandra Claire','1973')

INSERT INTO Autori(Nume,An_Nastere) 
VALUES ('Sarah Rees Brennan','1983')

INSERT INTO Autori(Nume,An_Nastere) 
VALUES ('Frank Herbert','1920')

select * from Carti

select * from Autori
delete from Autori

INSERT INTO CartiAutori(Cid,Auid) 
VALUES ('5005','5004')

INSERT INTO CartiAutori(Cid,Auid) 
VALUES ('5006','5001')

INSERT INTO CartiAutori(Cid,Auid) 
VALUES ('5007','5001')

INSERT INTO CartiAutori(Cid,Auid) 
VALUES ('5008','5002')

INSERT INTO CartiAutori(Cid,Auid) 
VALUES ('5008','5003')

select * from CartiAutori
delete from CartiAutori

INSERT INTO Adrese_Persoane(Strada,Numar,Oras) 
VALUES ('Vasile Alecsandri','2', 'Alba Iulia')

INSERT INTO Adrese_Persoane(Strada,Numar,Oras) 
VALUES ('George Topirceanu','4', 'Alba Iulia')

INSERT INTO Adrese_Persoane(Strada,Numar,Oras) 
VALUES ('Victor Babes','12', 'Turda')

INSERT INTO Adrese_Persoane(Strada,Numar,Oras) 
VALUES ('Republicii','23', 'Cluj Napoca')

INSERT INTO Adrese_Persoane(Strada,Numar,Oras) 
VALUES ('Republicii','21', 'Cluj Napoca')

INSERT INTO Adrese_Persoane(Strada,Numar,Oras) 
VALUES ('Ion Barbu','32', 'Alba Iulia')

delete from Adrese_Persoane
where Strada = 'George Topirceanu'

select * from Persoane
select * from Adrese_Persoane
delete from Adrese_Persoane


INSERT INTO Persoane(Nume,Prenume,Email,Aid) 
VALUES ('Popa','Andrei','popaand@gmail.com','37')

INSERT INTO Persoane(Nume,Prenume,Email,Aid) 
VALUES ('Popa','Maria','popama@gmail.com','37')

INSERT INTO Persoane(Nume,Prenume,Email,Aid) 
VALUES ('Popa','Ioana','popaioana@gmail.com','37')

INSERT INTO Persoane(Nume,Prenume,Email,Aid) 
VALUES ('Muntean','Aurelian','aure23@gmail.com','38')

INSERT INTO Persoane(Nume,Prenume,Email,Aid) 
VALUES ('Argene','Mirela','mire45@gmail.com','39')

INSERT INTO Persoane(Nume,Prenume,Email,Aid) 
VALUES ('Eradu','Paul','eradup78@gmail.com','40')

INSERT INTO Persoane(Nume,Prenume,Email,Aid) 
VALUES ('Octav','Mircea','mirceaf@gmail.com','41')

INSERT INTO Persoane(Nume,Prenume,Email,Aid) 
VALUES ('Octav','Violeta','vio_leta@gmail.com','41')

INSERT INTO Persoane(Nume,Prenume,Email,Aid) 
VALUES ('Albu','Razvan','razvii@gmail.com','42')

INSERT INTO Persoane(Nume,Prenume,Email,Aid) 
VALUES ('Albu','Ecaterina','e_cat@gmail.com','42')

INSERT INTO Persoane(Nume,Prenume,Email,Aid) 
VALUES ('Armin','Elena','e_armin@gmail.com','42')


select* from Carti
select * from Persoane

INSERT INTO Inregistrari(Cid, Pid) 
Values('5005', '23')

INSERT INTO Inregistrari(Cid, Pid) 
Values('5005', '26')

INSERT INTO Inregistrari(Cid, Pid) 
Values('5006', '24')

INSERT INTO Inregistrari(Cid, Pid) 
Values('5007', '25')

INSERT INTO Inregistrari(Cid, Pid) 
Values('5007', '24')

INSERT INTO Inregistrari(Cid, Pid) 
Values('5008', '27')

INSERT INTO Inregistrari(Cid, Pid) 
Values('5008', '28')

INSERT INTO Inregistrari(Cid, Pid) 
Values('5005', '29')

INSERT INTO Inregistrari(Cid, Pid) 
Values('5006', '30')

INSERT INTO Inregistrari(Cid, Pid) 
Values('5007', '30')

INSERT INTO Inregistrari(Cid, Pid) 
Values('5005', '33')

INSERT INTO Inregistrari(Cid, Pid) 
Values('5005', '31')

INSERT INTO Inregistrari(Cid, Pid) 
Values('5005', '32')

INSERT INTO Inregistrari(Cid, Pid) 
Values('5006', '32')

select * from Inregistrari


/*1. Cate carti 'Dune' inchiriaza persoanele a caror nume incepe cu litera 'A'.
pe relatia m-n.
*/

select p.NUME, COUNT(i.Pid) AS NrCarti
from Persoane p
inner join Inregistrari i on
p.Pid = i.Pid
inner join Carti c on
i.Cid = c.Cid
where c.Titlu = 'Dune' and p.NUME like 'A%'
group by p.NUME
having count(i.pid) >=1

/*2. Numarul de carti inchiriate de fiecare persoana care sta in Alba Iulia.
relatie m-n.
*/

select p.nume,p.Prenume, count(i.cid) AS NrCarti
from Persoane p
inner join Adrese_Persoane a on
p.Aid = a.AdPid
inner join Inregistrari i on
p.Pid = i.Pid
inner join Carti c on
i.Cid = c.Cid
where a.Oras = 'Alba Iulia' 
group by p.NUME, p.Prenume
having count(i.cid) >=1

/*3.Numarul de bibliotecari care lucreaza la fiecare etaj din Cluj Napoca.
*/

select s.Etaj, count(s.etaj) as NrBibliotecariPerEtaj
from Sectoare s
inner join Bibliotecari b on
s.Sid = b.Sid
inner join Adrese_Bibliotecari a on
b.AdBid = a.AdBid
where a.Oras = 'Cluj Napoca'
group by s.Etaj



/*4. Bibliotecarii care lucreaza in cladirea Nicolae Iorga din Turda.
*/

select b.Nume, s.Etaj
from Bibliotecari b
inner join Sectoare s on
s.Sid = b.Sid
inner join Adrese_Bibliotecari a on
a.AdBid = b .AdBid
where s.Cladire = 'Nicolae Iorga' and a.Oras = 'Turda'

/*5. Numele persoanelor cu nume distincte care au inchiriat cartea Dune din Alba Iulia.
*/

select distinct p.nume 
from Persoane p
inner join Adrese_Persoane a on
p.Aid = a.AdPid
inner join Inregistrari i on
p.Pid = i.Pid
inner join Carti c on
i.Cid = c.Cid
where a.Oras = 'Alba Iulia' and c.Titlu = 'Dune'



/*6. Strazile pe care stau bibliotecarii din Turda ce lucreaza la etajul 0.
*/

select distinct a.Strada
--, b.Nume
from Adrese_Bibliotecari a 
inner join Bibliotecari b
on b.AdBid = a.AdBid
inner join Sectoare s on
s.Sid = b.Sid
where a.Oras = 'Cluj Napoca' and s.Etaj = '0'



/*7. Cartile care au autori nascuti in secolul 20 si au nr exemplarelor mai mare de 2.
*/

select c.Titlu, a.An_Nastere, c.Nr_Carti
from Carti c
inner join CartiAutori ca on
ca.Cid = c.Cid
inner join Autori a on
a.Auid  = ca.Auid
where c.Nr_Carti >= 2 and a.An_Nastere >= 1900


/*8. Cartile de genul Crima care au mai mult de 2 exemplare.
*/

select c.Titlu,a.Nume
from Carti c
inner join Genuri g on
g.Gid = c.Gid
inner join CartiAutori ca on
ca.Cid = c.Cid
inner join Autori a on
a.Auid  = ca.Auid
where c.Nr_Carti >= 2 and g.Denumire = 'Crima' 
group by c.Titlu ,a.Nume



/*9. Cartile care sunt din genul Crima sau Fantasy si au mai mult de 4 exemplare.
*/

select c.Titlu, a.An_Nastere
from Carti c
inner join Genuri g on
g.Gid = c.Gid
inner join CartiAutori ca on
ca.Cid = c.Cid
inner join Autori a on
a.Auid  = ca.Auid
where g.Denumire = 'Crima' or g.Denumire = 'Fantasy'
group by c.Titlu ,a.An_Nastere



/*10. Persoanele care au imprumutat Moarte pe Nil in anul 2022.
*/

select  p.nume, i.Cid as CarteId, i.Pid AS PersoanaId 
from Persoane p
inner join Adrese_Persoane a on
p.Aid = a.AdPid
inner join Inregistrari i on
p.Pid = i.Pid
inner join Carti c on
i.Cid = c.Cid
where c.Titlu = 'Moarte pe Nil' and c.Data_Imprumut like '%2022%'

/*11. Numele unic al persoanelor(familiile) din Alba Iulia ce au inchiriat carti.
*/
select distinct p.NUME 
from Persoane p
inner join Adrese_Persoane a on p.Aid = a.AdPid
where a.Oras = 'Alba Iulia'
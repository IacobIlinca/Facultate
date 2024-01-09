use S9
go

SELECT Varsta FROM Copii WHERE Varsta > 6;

CREATE INDEX IX_Copii_Varsta_asc ON Copii
(Varsta ASC);


using ConsoleApp1.models;

namespace NBA1.Domain;

public class Elev : Entitate<String>
{
    
    public string Nume  { get; set; }
    public NumeScoala Scoala { get; set; }

    public Elev(string id, string nume, NumeScoala scoala) : base(id)
    {
        Nume = nume;
        Scoala = scoala;
    }
}
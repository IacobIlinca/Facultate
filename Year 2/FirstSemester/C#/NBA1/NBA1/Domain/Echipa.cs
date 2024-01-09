using ConsoleApp1.models;

namespace NBA1.Domain;

public class Echipa : Entitate<string>
{

    public NumeEchipa Nume { get; set; }
    
    public Echipa(string id) : base(id)
    {
    }
    
    public Echipa(string id, NumeEchipa nume) : base(id)
    {
        Id = id;
        Nume = nume;
    }
    
    public override string ToString()
    {
        return Id + " " + Nume;
    }
}
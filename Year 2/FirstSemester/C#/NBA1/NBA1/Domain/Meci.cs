using ConsoleApp1.models;

namespace NBA1.Domain;

public class Meci : Entitate<string>
{
    public Echipa Echipa1;
    public Echipa Echipa2;
    public DateTime Data { get; set; }

    public Meci(string id, Echipa echipa1, Echipa echipa2, DateTime data) : base(id)
    {
        Echipa1 = echipa1;
        Echipa2 = echipa2;
        Data = data;
    }
}
using ConsoleApp1.models;

namespace NBA1.Domain;

public class Jucator : Elev
{
    
    public Echipa Echipa  { get; set; }


    public Jucator(string id, string nume, NumeScoala scoala, Echipa echipa) : base(id, nume, scoala)
    {
        Echipa = echipa;
    }
}
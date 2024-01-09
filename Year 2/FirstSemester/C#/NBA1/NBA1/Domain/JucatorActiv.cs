using ConsoleApp1.models;

namespace NBA1.Domain;

public class JucatorActiv : Entitate<string>
{
    public string idJucator  { get; set; }
    public string idMeci  { get; set; }
    public int nrPuncteInscrise  { get; set; }
    public Tip tip  { get; set; }

    public JucatorActiv(string id, string idJucator, string idMeci, int nrPuncteInscrise, Tip tip) : base(id)
    {
        this.idJucator = idJucator;
        this.idMeci = idMeci;
        this.nrPuncteInscrise = nrPuncteInscrise;
        this.tip = tip;
    }
}
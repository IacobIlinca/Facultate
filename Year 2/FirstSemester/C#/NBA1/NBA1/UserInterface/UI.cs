using NBA1.Domain;
using NBA1.Service;

namespace NBA1.UserInterface;

public class UI
{
    private ServiceEchipa srvEchipe;
    private ServiceJucatori srvJucatori;
    private ServiceJucatorActivi srvJucatorActivi;
    private ServiceMeciuri srvMeciuri;

    public UI(ServiceEchipa srvEchipe, ServiceJucatori srvJucatori, ServiceJucatorActivi srvJucatorActivi, ServiceMeciuri srvMeciuri)
    {
        this.srvEchipe = srvEchipe;
        this.srvJucatori = srvJucatori;
        this.srvJucatorActivi = srvJucatorActivi;
        this.srvMeciuri = srvMeciuri;
    }

    public void belongsTo()
    {
        Console.WriteLine("Nume: ");
        var nume = Console.ReadLine();
        var jucatori = srvJucatori.belongsTo(nume);
        foreach (var j in jucatori)
        {
            Console.WriteLine(j.Nume);
        }
    }
    
    
    public void belongsTo2()
    {
        //Sa se afiseze toti jucatorii unei echipe dată.
        Console.WriteLine("Nume: ");
        var nume = Console.ReadLine();
        var jucatori = srvJucatori.GetAll().ToList();
        var res = (from j in jucatori
                                    where j.Echipa.Id == nume
                                    select j.Nume);
        foreach (var juc in res)
        {
            Console.WriteLine(juc);
        }
        
    }


    public void joaca()
    {
        Console.WriteLine("Echipa: ");
        var echipa = Console.ReadLine();
        Console.WriteLine("Meci: ");
        var meci = Console.ReadLine();
        var jucatori = srvJucatorActivi.getJucatoriEchipa(echipa, meci);
        foreach (var j in jucatori)
        {
            Console.WriteLine(j.Id);
        }
    }

    public void joaca2()
    {
        Console.WriteLine("Echipa: ");
        var echipa = Console.ReadLine();
        Console.WriteLine("Meci: ");
        var meci = Console.ReadLine();
        var jucatoriActivi = srvJucatorActivi.GetAll();
        var jucatori = srvJucatori.GetAll();
        var juc = (from jc in jucatoriActivi
            where jc.idMeci == meci && jucatori.SingleOrDefault(j => j.Id == jc.idJucator).Echipa.Id == echipa
            select jc.idJucator);
        foreach (var m in juc)
        {
            Console.WriteLine(m);
        }
    }
    
    public void meciData()
    {
        Console.WriteLine("Data inceput perioada:");
        var dateStart = Console.ReadLine();
        Console.WriteLine("Data sfarsit perioada:");
        var dateEnd = Console.ReadLine();
        var meciuri = srvMeciuri.meciuriPerioada(DateTime.Parse(dateStart), DateTime.Parse(dateEnd));
        foreach (var m in meciuri)
        {
            Console.WriteLine(m.Id);
        }

    }
    
    public void meciData2()
    {
        //Sa se afiseze toate meciurile dintr-o anumita perioada calendaristica.
        Console.WriteLine("Data inceput perioada:");
        var dateStart = Console.ReadLine();
        DateTime dateStartDateTime = DateTime.Parse(dateStart);
        Console.WriteLine("Data sfarsit perioada:");
        var dateEnd = Console.ReadLine();
        DateTime dateEndDateTime = DateTime.Parse(dateEnd);
        var meciuri = srvMeciuri.GetAll();
        var res = (from m in meciuri
            where m.Data >= dateStartDateTime && m.Data <= dateEndDateTime
            select m.Id);
        foreach (var meci in res)
        {
            Console.WriteLine(meci);
        }

    }

    public void addEchipa()
    {
        Console.WriteLine("Introduceti id-ul echipei: ");
        var id = Console.ReadLine();
        Console.WriteLine("Intoduceti numele echipei: ");
        var nume = Console.ReadLine();
        Echipa echipa = new Echipa(id, (NumeEchipa)Enum.Parse(typeof(NumeEchipa), nume));
        srvEchipe.Save(echipa);

    }

    public void score()
    {
        List<Meci> meciuri = srvMeciuri.GetAll();
        List<JucatorActiv> jucatoriActivi = srvJucatorActivi.GetAll();
        List<Jucator> jucatori = srvJucatori.GetAll();
        Console.WriteLine("Introduceti id-ul meciului: ");
        string meciId= Console.ReadLine();
        var meci = meciuri.SingleOrDefault(m => m.Id == meciId);
        var e1 = meci.Echipa1.Id;
        var e2 = meci.Echipa2.Id;
        var echipa1 = (from m in jucatoriActivi
            where m.idMeci == meciId && jucatori.SingleOrDefault(j => j.Id == m.idJucator).Echipa.Id == e1
            select m.nrPuncteInscrise);
        var echipa2 = (from m in jucatoriActivi
            where m.idMeci == meciId && jucatori.SingleOrDefault(j => j.Id == m.idJucator).Echipa.Id == e2
            select m.nrPuncteInscrise);
        Console.WriteLine($"{meci.Echipa1} : {echipa1.Sum()} - {echipa2.Sum()} : {meci.Echipa2}");
        
    }

    public void score2()
    {
        List<Meci> meciuri = srvMeciuri.GetAll();
        List<JucatorActiv> jucatoriActivi = srvJucatorActivi.GetAll();
        List<Jucator> jucatori = srvJucatori.GetAll();
        Console.WriteLine("Introduceti id-ul meciului: ");
        string meciId= Console.ReadLine();
        var meci = meciuri.SingleOrDefault(m => m.Id == meciId);
        var matchScore = 
            from pa in jucatoriActivi
            join pl in jucatori on pa.idJucator equals pl.Id
            where pa.idMeci == meciId
            group pa by pl.Echipa into g
            select new { Team = g.Key, Score = g.Sum(a => a.nrPuncteInscrise)};
        var scorEchipa1 = matchScore.SingleOrDefault(ms => ms.Team == meci.Echipa1)?.Score ?? 0;
        var scorEchipa2 = matchScore.SingleOrDefault(ms => ms.Team == meci.Echipa2)?.Score ?? 0;
        Console.WriteLine($"{meci.Echipa1} : {scorEchipa1} - {scorEchipa2} : {meci.Echipa2}");
    }


    public void showUi()
    {
        while (true)
        {
            Console.WriteLine("Optiunile dumneavoastra sunt:");
            Console.WriteLine("0.Opreste programul.");
            Console.WriteLine("1.Sa se afiseze toti jucatorii unei echipe dată.");
            Console.WriteLine("2.Sa se afiseze toti jucatorii activi ai unei echipe de la un anumit meci.");
            Console.WriteLine("3.Sa se afiseze toate meciurile dintr-o anumita perioada calendaristica.");
            Console.WriteLine("4.Sa se determine si sa se afiseze scorul de la un anumit meci.");

            var input = Console.ReadLine();
            if (input == "1")
            {
                //this.belongsTo();
                this.belongsTo2();
            }
            else if (input == "2")
            {
                //this.joaca();
                this.joaca2();
            }
            else if (input == "3")
            {
                //this.meciData();
                this.meciData2();
            }
            else if (input == "4")
            {
                this.score();
            }
            else if (input == "5")
            {
                this.addEchipa();
            }
            else if (input == "0")
            {
                break;
            }
        }
    }
}
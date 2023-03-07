using NBA1.Domain;
using NBA1.Repository;

namespace NBA1.Service;

public class ServiceJucatori
{
    private IRepository<string, Jucator> repository;

    public ServiceJucatori(IRepository<string, Jucator> repository)
    {
        this.repository = repository;
    }

    public List<Jucator> GetAll()
    {
        return repository.FindAll().ToList();
    }

    public List<Jucator> belongsTo(string echipa)
    {
        var jucatori = repository.FindAll().ToList();
        var echipe = new List<Jucator>();
        foreach (var j in jucatori)
        {
            if (j.Echipa.Id == echipa)
            {
                echipe.Add(j);
            }
        }

        
        return echipe;
    }

    public IEnumerable<string> belongsTo3(string echipa)
    {
        var jucatori = repository.FindAll().ToList();
        IEnumerable<string> res = from j in jucatori
            where j.Echipa.Id == echipa
            select j.ToString();
        return res;
    }
   
}
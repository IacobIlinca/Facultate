using NBA1.Domain;
using NBA1.Repository;

namespace NBA1.Service;

public class ServiceJucatorActivi
{
    private IRepository<string, Jucator> repository;
    private IRepository<string, JucatorActiv> repositoryActivi;

    public ServiceJucatorActivi(IRepository<string, Jucator> repository, IRepository<string, JucatorActiv> repositoryActivi)
    {
        this.repository = repository;
        this.repositoryActivi = repositoryActivi;
    }

    public List<JucatorActiv> GetAll()
    {
        return repositoryActivi.FindAll().ToList();
    }
    
    public List<JucatorActiv> getJucatoriEchipa(string echipa, string meci)
    {
        var jucatoriActivi = repositoryActivi.FindAll();
        var echipe = new List<JucatorActiv>();
        foreach (var juc in jucatoriActivi)
        {
            if (juc.idMeci == meci)
            {
                var j = repository.FindOne(juc.idJucator);
                if (j.Echipa.Id == echipa)
                {
                    echipe.Add(juc);
                }
            }
        }

        return echipe;
    }
}
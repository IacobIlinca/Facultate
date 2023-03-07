using NBA1.Domain;
using NBA1.Repository;

namespace NBA1.Service;

public class ServiceMeciuri
{
    private IRepository<string, Meci> repository;

    public ServiceMeciuri(IRepository<string, Meci> repository)
    {
        this.repository = repository;
    }

    public List<Meci> GetAll()
    {
        return repository.FindAll().ToList();
    }

    public Meci Save(Meci meci)
    {
        return repository.Save(meci);
    }

    public List<Meci> meciuriPerioada(DateTime dateStart, DateTime dateEnd)
    {
        var meciuri = repository.FindAll().ToList();
        var meciData = new List<Meci>();
        foreach (var m in meciuri)
        {
            if (m.Data >= dateStart && m.Data <= dateEnd)
            {
                meciData.Add(m);
            }
        }

        return meciData;
    }

}
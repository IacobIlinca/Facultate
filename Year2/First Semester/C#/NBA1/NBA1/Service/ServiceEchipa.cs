using NBA1.Domain;
using NBA1.Repository;

namespace NBA1.Service;

public class ServiceEchipa
{
    private IRepository<string, Echipa> repository;

    public ServiceEchipa(IRepository<string, Echipa> repository)
    {
        this.repository = repository;
    }

    public List<Echipa> GetAll()
    {
        return repository.FindAll().ToList();
    }

    public Echipa Save(Echipa echipa)
    {
        return repository.Save(echipa);
    }

}


using ConsoleApp1.models;
using NBA1.Repository;
using NBA1.Validators;

namespace ConsoleApp1.repository;

public class InMemoryRepository<ID, E> : IRepository<ID, E> where E : Entitate<ID>
{
    protected IDictionary<ID, E> Entitati = new Dictionary<ID, E>();
    protected IValidator<E> Validator;

    public InMemoryRepository(IValidator<E> validator)
    {
        Validator = validator;
    }

    public E FindOne(ID id)
    {
         if (Entitati.ContainsKey(id))
        {
            return Entitati[id];
        }

        return null;
    }

    public IEnumerable<E> FindAll()
    {
        return Entitati.Values.ToList<E>();
    }

    public E Save(E e)
    {
        this.Validator.Valideaza(e);
        if (Entitati.ContainsKey(e.Id))
        {
            return e;
        }

        Entitati.Add(e.Id, e);
        return e;
    }

    public E Delete(ID id)
    {
        throw new NotImplementedException();
    }

    public E Update(E e)
    {
        throw new NotImplementedException();
    }
}
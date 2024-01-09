using ConsoleApp1.models;

namespace NBA1.Repository;

public interface IRepository<ID, E> where E : Entitate<ID>
{
    E FindOne(ID id);

    IEnumerable<E> FindAll();

    E Save(E e);

    E Delete(ID id);

    E Update(E e);
}
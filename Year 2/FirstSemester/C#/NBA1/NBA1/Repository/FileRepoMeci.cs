using NBA1.Domain;
using NBA1.Validators;

namespace NBA1.Repository;

public class FileRepoMeci : FileRepository<string, Meci>
{
    public FileRepoMeci(IValidator<Meci> validator, string numeFisier) : base(validator, numeFisier,
        DelegateEntitiesFromFile.DelegateMeci)
    {
    }

}
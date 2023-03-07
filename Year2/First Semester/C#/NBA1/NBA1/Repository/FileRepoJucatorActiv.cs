using NBA1.Domain;
using NBA1.Validators;

namespace NBA1.Repository;

public class FileRepoJucatorActiv : FileRepository<string, JucatorActiv>
{
    public FileRepoJucatorActiv(IValidator<JucatorActiv> validator, string numeFisier) : base(validator, numeFisier,
        DelegateEntitiesFromFile.DelegateJucatorActiv)
    {
    }
}
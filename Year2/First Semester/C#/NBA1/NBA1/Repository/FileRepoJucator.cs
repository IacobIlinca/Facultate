using NBA1.Domain;
using NBA1.Validators;

namespace NBA1.Repository;

public class FileRepoJucator : FileRepository<string, Jucator>
{
    public FileRepoJucator(IValidator<Jucator> validator, string numeFisier) : base(validator, numeFisier,
        DelegateEntitiesFromFile.DelegateJucator)
    {
    }

}
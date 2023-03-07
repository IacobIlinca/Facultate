using NBA1.Domain;
using NBA1.Validators;

namespace NBA1.Repository;

public class FileRepoEchipa : FileRepository<string, Echipa>
{
    public FileRepoEchipa(IValidator<Echipa> validator, string numeFisier) : base(validator, numeFisier,
        DelegateEntitiesFromFile.DelegateEchipa)
    {
    }

}



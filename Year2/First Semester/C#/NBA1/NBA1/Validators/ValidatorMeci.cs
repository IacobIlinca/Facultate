using NBA1.Domain;

namespace NBA1.Validators;

public class ValidatorMeci : IValidator<Meci>
{
    public void Valideaza(Meci meci)
    {
        if (meci.Data > DateTime.Now)
        {
            throw new ExceptieValidare("Data invalida");
        }
    }
    
}
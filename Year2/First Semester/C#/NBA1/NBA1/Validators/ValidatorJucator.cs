using NBA1.Domain;

namespace NBA1.Validators;

public class ValidatorJucator : IValidator<Jucator>
{
    public void Valideaza(Jucator jucator)
    {
        if (jucator.Nume == null )
        {
            throw new ExceptieValidare("Numele jucatorului este vid");
        }
    }
}
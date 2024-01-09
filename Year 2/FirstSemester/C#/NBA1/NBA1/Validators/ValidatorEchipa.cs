using NBA1.Domain;

namespace NBA1.Validators;

public class ValidatorEchipa : IValidator<Echipa>
{
    public void Valideaza(Echipa echipa)
    {
        if (echipa.Nume == null )
        {
            throw new ExceptieValidare("Numele echipei este vid");
        }
    }
}
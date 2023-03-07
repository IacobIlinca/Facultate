using NBA1.Domain;

namespace NBA1.Validators;

public class ValidatorJucatorActiv : IValidator<JucatorActiv>
{
    public void Valideaza(JucatorActiv jucatorActiv)
    {
        if (jucatorActiv.nrPuncteInscrise < 0 )
        {
            throw new ExceptieValidare("Nr de puncte nu poate fi negativ ");
        }
    }
}
namespace NBA1.Validators;

public interface IValidator<E>
{
    void Valideaza(E entitate);
    
}
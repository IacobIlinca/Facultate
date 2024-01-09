namespace NBA1.Validators;

public class ExceptieValidare : ApplicationException
{
    public ExceptieValidare(string? message) : base(message)
    {
    }
}
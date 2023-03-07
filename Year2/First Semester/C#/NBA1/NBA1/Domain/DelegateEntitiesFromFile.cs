namespace NBA1.Domain;

public class DelegateEntitiesFromFile
{
    private static char Separator = ';';

    public static Echipa DelegateEchipa(string line)
    {
        string[] splitEchipa = line.Split(Separator);
        Echipa echipa = new Echipa(splitEchipa[0], (NumeEchipa)Enum.Parse(typeof(NumeEchipa), splitEchipa[1]));
        return echipa;
    }
    
    public static Jucator DelegateJucator(string line)
    {
        string[] splitJucator = line.Split(Separator);
        Jucator jucator = new Jucator(splitJucator[0], splitJucator[1], (NumeScoala)Enum.Parse(typeof(NumeScoala), splitJucator[2]), new Echipa(splitJucator[3], (NumeEchipa)Enum.Parse(typeof(NumeEchipa),splitJucator[4])));
        return jucator;
    }
    
    public static Meci DelegateMeci(string line)
    {
        string[] splitMeci= line.Split(Separator);
        Echipa Echipa1 = new Echipa(splitMeci[1], (NumeEchipa)Enum.Parse(typeof(NumeEchipa), splitMeci[2]));
        Echipa Echipa2 = new Echipa(splitMeci[3], (NumeEchipa)Enum.Parse(typeof(NumeEchipa), splitMeci[4]));
        Meci meci = new Meci(splitMeci[0], Echipa1, Echipa2, DateTime.Parse(splitMeci[5]));
        return meci;
    }
    
    public static JucatorActiv DelegateJucatorActiv(string line)
    {
        string[] splitJucatorActiv = line.Split(Separator);
        JucatorActiv jucatorActiv = new JucatorActiv(splitJucatorActiv[0],splitJucatorActiv[1], splitJucatorActiv[2],int.Parse(splitJucatorActiv[3]),
            (Tip)Enum.Parse(typeof(Tip), splitJucatorActiv[4]));
        return jucatorActiv;
    }
}
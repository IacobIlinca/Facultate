using NBA1.Repository;
using NBA1.Service;
using NBA1.UserInterface;
using NBA1.Validators;

public class Program
{
    public static void Main(string[] args)
    {
        ValidatorEchipa validatorEchipa = new ValidatorEchipa();
        FileRepoEchipa fileRepoEchipa = new FileRepoEchipa(validatorEchipa, "C:\\Users\\Ilinca\\RiderProjects\\NBA1\\NBA1\\Data\\echipe.txt");
        
        ValidatorJucator validatorJucator = new ValidatorJucator();
        FileRepoJucator fileRepoJucator = new FileRepoJucator(validatorJucator, "C:\\Users\\Ilinca\\RiderProjects\\NBA1\\NBA1\\Data\\jucatori.txt");

        ValidatorJucatorActiv validatorJucatorActiv = new ValidatorJucatorActiv();
        FileRepoJucatorActiv fileRepoJucatorActiv = new FileRepoJucatorActiv(validatorJucatorActiv,
            "C:\\Users\\Ilinca\\RiderProjects\\NBA1\\NBA1\\Data\\jucatoriActivi.txt");

        ValidatorMeci validatorMeci = new ValidatorMeci();
        FileRepoMeci fileRepoMeci =
            new FileRepoMeci(validatorMeci, "C:\\Users\\Ilinca\\RiderProjects\\NBA1\\NBA1\\Data\\meci.txt");

        ServiceJucatorActivi srvJucatorActivi = new ServiceJucatorActivi(fileRepoJucator,fileRepoJucatorActiv);
        ServiceJucatori srvJucatori = new ServiceJucatori(fileRepoJucator);
        ServiceMeciuri srvMeciuri = new ServiceMeciuri(fileRepoMeci);
        ServiceEchipa srvEchipe = new ServiceEchipa(fileRepoEchipa);
        
        UI ui = new UI(srvEchipe, srvJucatori, srvJucatorActivi, srvMeciuri);
        
        ui.showUi();
    }
}

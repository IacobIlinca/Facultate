package com.example.clinica;

import com.example.clinica.Domain.Consultatie;
import com.example.clinica.Domain.Medic;
import com.example.clinica.Domain.Sectie;
import com.example.clinica.Repository.DBConsultatieRepo;
import com.example.clinica.Repository.DBMedicRepo;
import com.example.clinica.Repository.DBSectieRepo;
import com.example.clinica.Service.Service;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.*;
import javafx.scene.control.cell.PropertyValueFactory;

import java.sql.Date;
import java.sql.Time;
import java.time.LocalDate;
import java.time.LocalTime;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class ConsultatieController {
    @FXML
    private Button faConsultatieBtn;
    @FXML
    private Spinner<String > oraSpinner;
    @FXML
    private TextField numePacientTxtFld;
    @FXML
    private TextField cnpPacientTxtFld;
    @FXML
    private TableColumn<Consultatie, String > rezidentColumn;
    @FXML
    private TableColumn<Consultatie, Integer> vechimeColumn;
    @FXML
    private TableColumn<Consultatie, String > numeColumn;
    @FXML
    private TableColumn<Consultatie, Long> idColumn;
    @FXML
    private TableColumn<Consultatie, Long> idSectieColumn;
    @FXML
    private TableView<Medic> tblViewMediciDinConsultatii;
    @FXML
    private DatePicker dataDatePicker;

    String url = "jdbc:postgresql://localhost:5432/clinica";
    String username = "postgres";
    String password = "password";

    DBSectieRepo repoSectie = new DBSectieRepo(url, username, password);
    DBMedicRepo repoMedic = new DBMedicRepo(url, username, password);

    DBConsultatieRepo repoConsultatie = new DBConsultatieRepo(url, username, password);

    Service service = Service.getInstance(repoSectie, repoMedic, repoConsultatie);
    private final ObservableList<Medic> medicModel = FXCollections.observableArrayList();

    private final ObservableList<String> oreModel = FXCollections.observableArrayList("08:00","08:30","09:00","09:30","10:00","10:30","11:00");


    @FXML
    public void initialize() {

        tblViewMediciDinConsultatii.setVisible(true);
        List<Medic> medici = new ArrayList<>();
        for (Medic medic : service.getAllMedici()) {
            medici.add(medic);
        }

        //aici trebuie numele atributelor date in clasa
        //la ce e id, pune id!
        medicModel.setAll(medici);
        idColumn.setCellValueFactory(new PropertyValueFactory<>("id"));
        idSectieColumn.setCellValueFactory(new PropertyValueFactory<>("idSectie"));
        numeColumn.setCellValueFactory(new PropertyValueFactory<>("nume"));
        vechimeColumn.setCellValueFactory(new PropertyValueFactory<>("vechime"));
        rezidentColumn.setCellValueFactory(new PropertyValueFactory<>("rezident"));

        tblViewMediciDinConsultatii.setItems(medicModel);

        SpinnerValueFactory<String > valueFactory = new SpinnerValueFactory.ListSpinnerValueFactory<String >(oreModel);
        valueFactory.setValue("07:00");
        oraSpinner.setValueFactory(valueFactory);

    }


    public void onRezervaConsultClicked(ActionEvent actionEvent) {
        Long idMedic = tblViewMediciDinConsultatii.getSelectionModel().getSelectedItem().getId();
        Random rand = new Random();
        Long id = rand.nextLong(1000)+1;
        Long cnpPacient = Long.valueOf(cnpPacientTxtFld.getText());
        String numePacient = numePacientTxtFld.getText();
        LocalDate data = dataDatePicker.getValue();
        LocalTime timp = LocalTime.parse(oraSpinner.getValue());
        Consultatie consultatie = new Consultatie(id,idMedic,cnpPacient,numePacient,data,timp);
        repoConsultatie.save(consultatie);
        Alert message = new Alert(Alert.AlertType.CONFIRMATION);
        message.setHeaderText("Confirmation!");
        message.setContentText("Consultatie progaramat cu succes!");
        message.showAndWait();

    }


}

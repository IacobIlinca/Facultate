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
import javafx.fxml.FXML;
import javafx.scene.control.TableColumn;
import javafx.scene.control.TableView;
import javafx.scene.control.cell.PropertyValueFactory;

import java.sql.Date;
import java.sql.Time;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

public class MedicController {

    @FXML
    private TableColumn<Consultatie,Long> cnpPacientColumn;
    @FXML
    private TableColumn<Consultatie,String > numepacientColumn;
    @FXML
    private TableColumn<Consultatie, Date> dataColumn;
    @FXML
    private TableColumn<Consultatie, Time> oraColumn;
    @FXML
    private TableColumn<Consultatie,Long> idMedicColumn;
    @FXML
    private TableColumn<Consultatie, Long> ididColumn;
    @FXML
    private TableView<Consultatie> tblVwMedic;
    String url = "jdbc:postgresql://localhost:5432/clinica";
    String username = "postgres";
    String password = "password";

    DBSectieRepo repoSectie = new DBSectieRepo(url, username, password);
    DBMedicRepo repoMedic = new DBMedicRepo(url, username, password);
    DBConsultatieRepo repoConsultatie = new DBConsultatieRepo(url, username, password);

    Service service = Service.getInstance(repoSectie, repoMedic, repoConsultatie);
    private final ObservableList<Consultatie> consultatieModel = FXCollections.observableArrayList();
    private Medic medic;

    @FXML
    public void initialize(Medic medic) {
        this.medic = medic;

        tblVwMedic.setVisible(true);
        List<Consultatie> consultatii = new ArrayList<>();
        for (Consultatie cons : service.getAllConsultatii()) {
            if(Objects.equals(cons.getIdMedic(), medic.getId())){
                consultatii.add(cons);
            }
        }

        //aici trebuie numele atributelor date in clasa
        //la ce e id, pune id!
        consultatieModel.setAll(consultatii);
        ididColumn.setCellValueFactory(new PropertyValueFactory<>("id"));
        idMedicColumn.setCellValueFactory(new PropertyValueFactory<>("idMedic"));
        cnpPacientColumn.setCellValueFactory(new PropertyValueFactory<>("CNPPacient"));
        numepacientColumn.setCellValueFactory(new PropertyValueFactory<>("numePacient"));
        dataColumn.setCellValueFactory(new PropertyValueFactory<>("data"));
        oraColumn.setCellValueFactory(new PropertyValueFactory<>("ora"));

        tblVwMedic.setItems(consultatieModel);
    }
}

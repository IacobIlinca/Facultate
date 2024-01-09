package com.example.ati_v1;

import com.example.ati_v1.Domain.Pat;
import com.example.ati_v1.Observer.Observer;
import com.example.ati_v1.Repository.DBPacientRepo;
import com.example.ati_v1.Repository.DBPatRepo;
import com.example.ati_v1.Service.Service;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.Label;
import javafx.scene.control.TableColumn;
import javafx.scene.control.TableView;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.stage.Stage;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class PatController extends Observer {

    @FXML
    private Label nrPaturiLibereLbl;
    @FXML
    private TableColumn<Pat, String> cnppacientColumn;
    @FXML
    private TableColumn<Pat, String> ventilatieColumn;
    @FXML
    private TableColumn<Pat, String> tipColumn;
    @FXML
    private TableView<Pat> tableViewPat;

    String url = "jdbc:postgresql://localhost:5432/ati";
    String username = "postgres";
    String password = "password";

    DBPatRepo repoPat = new DBPatRepo(url,username, password);
    DBPacientRepo repoPacient = new DBPacientRepo(url, username,password);

    private Service service;

    private final ObservableList<Pat> patModel = FXCollections.observableArrayList();

    public PatController(Service service) {
        this.service = service;
        service.addObserver(this);
    }

    @FXML
    public void initialize() throws IOException {



        tableViewPat.setVisible(true);
        List<Pat> paturi = new ArrayList<>();

        for (Pat pat : service.getAllPaturi()) {
            if (!(pat.getCnpPacient() == null)) {
                paturi.add(pat);
            }
        }
        //aici trebuie numele atributelor date in clasa
        patModel.setAll(paturi);
        tipColumn.setCellValueFactory(new PropertyValueFactory<>("tip"));
        ventilatieColumn.setCellValueFactory(new PropertyValueFactory<>("ventilatie"));
        cnppacientColumn.setCellValueFactory(new PropertyValueFactory<>("cnpPacient"));
        tableViewPat.setItems(patModel);

        int paturi_libere = 0;
        for (Pat pat : service.getAllPaturi()) {
            if (pat.getCnpPacient() == null) {
                paturi_libere ++;
            }
        }

        nrPaturiLibereLbl.setText(String.valueOf(paturi_libere));

        FXMLLoader pacient_loader = new FXMLLoader(HelloApplication.class.getResource("pacient.fxml"));

        PacientController pacientController = new PacientController(service);
        //pacient_loader.setController(pacientController);
        Scene pacient_scene = new Scene(pacient_loader.load(),600,400 );
        Stage pacient_stage = new Stage();
        pacient_stage.setTitle("Pacienti in asteptare");
        pacient_stage.setScene(pacient_scene);
        pacientController.initialize();
        pacient_stage.show();

    }

    @Override
    public void update() throws IOException {
        initialize();
    }

}

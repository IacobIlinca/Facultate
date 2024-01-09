package com.example.ati_v1;

import com.example.ati_v1.Domain.Pacient;
import com.example.ati_v1.Domain.Pat;
import com.example.ati_v1.Domain.Tip;
import com.example.ati_v1.Observer.Observer;
import com.example.ati_v1.Repository.DBPacientRepo;
import com.example.ati_v1.Repository.DBPatRepo;
import com.example.ati_v1.Service.Service;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.*;
import javafx.scene.control.cell.PropertyValueFactory;

import java.io.IOException;
import java.util.*;

public class PacientController extends Observer {
    @FXML
    private Button rezervaBtn;
    @FXML
    private RadioButton tiipRdBtn;
    @FXML
    private RadioButton ticRdBtn;
    @FXML
    private RadioButton timRdBtn;
    @FXML
    private TableColumn<Pacient, String> cnpColumn;
    @FXML
    private TableColumn<Pacient, Integer> gravitateColumn;
    @FXML
    private TableColumn<Pacient, String> diagnosticPrincipalColumn;
    @FXML
    private TableColumn<Pacient, String> prematurColumn;
    @FXML
    private TableColumn<Pacient, Integer> varstaColumn;
    @FXML
    private TableView<Pacient> tableViewPacient;
    String url = "jdbc:postgresql://localhost:5432/ati";
    String username = "postgres";
    String password = "password";

    DBPatRepo repoPat = new DBPatRepo(url, username, password);
    DBPacientRepo repoPacient = new DBPacientRepo(url, username, password);

    private Service service;

    private final ObservableList<Pacient> pacientModel = FXCollections.observableArrayList();

    public PacientController(Service service) {
        this.service = service;
        service.addObserver(this);
    }

    @FXML
    public void initialize() {

        tableViewPacient.setVisible(true);
        List<Pacient> pacienti = new ArrayList<>();

        for (Pacient pacient : service.getAllPacienti()) {
            String cnp = pacient.getId();
            int ok = 0;
            for (Pat pat : service.getAllPaturi())
                if (Objects.equals(pat.getCnpPacient(), cnp)) {
                    ok = 1;
                    break;
                }
            if (ok == 0) {
                pacienti.add(pacient);
            }

        }

        for (int i = 0; i < pacienti.size(); i++)

            for (int j = i + 1; j < pacienti.size(); j++) {
                if (pacienti.get(i).getGravitate() < pacienti.get(j).getGravitate()) {
                    Collections.swap(pacienti, i, j);
                }
            }


        //aici trebuie numele atributelor date in clasa
        pacientModel.setAll(pacienti);

        cnpColumn.setCellValueFactory(new PropertyValueFactory<>("id"));
        varstaColumn.setCellValueFactory(new PropertyValueFactory<>("varsta"));
        prematurColumn.setCellValueFactory(new PropertyValueFactory<>("prematur"));
        diagnosticPrincipalColumn.setCellValueFactory(new PropertyValueFactory<>("diagnosticPrincipal"));
        gravitateColumn.setCellValueFactory(new PropertyValueFactory<>("gravitate"));
        tableViewPacient.setItems(pacientModel);
    }

    @FXML
    public void onRezervaBtnClick(ActionEvent actionEvent) throws IOException {
        Pacient pacient = tableViewPacient.getSelectionModel().getSelectedItem();
        List<Pat> paturi = new ArrayList<>();
        int ok = 0;
        for (Pat pat : service.getAllPaturi()) {
            paturi.add(pat);
        }
        if (timRdBtn.isSelected()) {
            for (Pat pat : paturi) {
                if (pat.getTip().equals(Tip.TIM) && pat.getCnpPacient() == null) {
                    pat.setCnpPacient(pacient.getId());
                    service.updatePaturi(pat);
                    ok = 1;
                }
            }

        }

        if (ticRdBtn.isSelected()) {
            for (Pat pat : paturi) {
                if (pat.getTip().equals(Tip.TIC) && pat.getCnpPacient() == null) {
                    pat.setCnpPacient(pacient.getId());
                    service.updatePaturi(pat);
                    ok = 1;
                }
            }
        }

        if (tiipRdBtn.isSelected()) {
            for (Pat pat : paturi) {
                if (pat.getTip().equals(Tip.TIIP) && pat.getCnpPacient() == null) {
                    pat.setCnpPacient(pacient.getId());
                    service.updatePaturi(pat);
                    ok = 1;
                }
            }

        }

        if (ok == 1) {
            this.initialize();
            Alert message = new Alert(Alert.AlertType.CONFIRMATION);
            message.setHeaderText("Confirmation!");
            message.setContentText("Rezervare facuta cu succes!");
            message.showAndWait();
        } else {
            Alert message = new Alert(Alert.AlertType.WARNING);
            message.setHeaderText("Warning!");
            message.setContentText("Rezervare esuata!");
            message.showAndWait();
        }


    }

    @Override
    public void update() {
        initialize();
    }
}

package com.example.anar;

import com.example.anar.Domain.Localitate;
import com.example.anar.Domain.Rau;
import com.example.anar.Repository.DBLocalitateRepo;
import com.example.anar.Repository.DBRauRepo;
import com.example.anar.Service.Service;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXML;
import javafx.scene.control.TableColumn;
import javafx.scene.control.TableView;
import javafx.scene.control.cell.PropertyValueFactory;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

public class LocalitateController {

    @FXML
    private TableView<Localitate> tblVwLocalitateMajor;
    @FXML
    private TableColumn<Localitate, String> numeColumnMajor;
    @FXML
    private TableColumn<Localitate, String> rauColumnMajor;
    @FXML
    private TableColumn<Localitate, Integer> cotaMinimaColumnMajor;
    @FXML
    private TableColumn<Localitate, Integer> cotaMaximaColumnMajor;
    @FXML
    private TableView<Localitate> tblVwLocalitateRedus;
    @FXML
    private TableColumn<Localitate, String> numeColumnRedus;
    @FXML
    private TableColumn<Localitate, String> rauColumnRedus;
    @FXML
    private TableColumn<Localitate, Integer> cotaMinimaColumnRedus;
    @FXML
    private TableColumn<Localitate, Integer> cotaMaximaColumnRedus;
    @FXML
    private TableView<Localitate> tblVwLocalitateMediu;
    @FXML
    private TableColumn<Localitate, String> numeColumnMediu;
    @FXML
    private TableColumn<Localitate, String> rauColumnMediu;
    @FXML
    private TableColumn<Localitate, Integer> cotaMinimaColumnMediu;
    @FXML
    private TableColumn<Localitate, Integer> cotaMaximaColumnMediu;

    String url = "jdbc:postgresql://localhost:5432/anar";
    String username = "postgres";
    String password = "password";

    DBRauRepo repoRau = new DBRauRepo(url, username, password);
    DBLocalitateRepo repoLocalitate = new DBLocalitateRepo(url, username, password);

    Service service = Service.getInstance(repoRau, repoLocalitate);

    private final ObservableList<Localitate> localitateModelMajor = FXCollections.observableArrayList();
    private final ObservableList<Localitate> localitateModelMediu = FXCollections.observableArrayList();
    private final ObservableList<Localitate> localitateModelRedus = FXCollections.observableArrayList();


    @FXML
    public void initialize() {
        List<Localitate> locRiscMajor = new ArrayList<>();
        List<Localitate> locRiscMediu = new ArrayList<>();
        List<Localitate> locRiscRedus = new ArrayList<>();
        for (Localitate loc : service.getAllLocalitati()) {
            String numeRau = loc.getRau();
            int cota = 0;
            for (Rau rau : service.getAllRauri()) {
                if (Objects.equals(rau.getId(), numeRau)) {
                    cota = rau.getCotaMedie();
                }
            }
            if (cota > loc.getCotaMaximaAdmisa()) {
                locRiscMajor.add(loc);
            }
            else if(cota >loc.getCotaMinimaDeRisc()){
                locRiscMediu.add(loc);
            }
            else {
                locRiscRedus.add(loc);
            }
        }


        tblVwLocalitateMajor.setVisible(true);
        tblVwLocalitateMediu.setVisible(true);
        tblVwLocalitateRedus.setVisible(true);

        //aici trebuie numele atributelor date in clasa
        //la ce e id, pune id!
        localitateModelMajor.setAll(locRiscMajor);
        numeColumnMajor.setCellValueFactory(new PropertyValueFactory<>("id"));
        rauColumnMajor.setCellValueFactory(new PropertyValueFactory<>("rau"));
        cotaMinimaColumnMajor.setCellValueFactory(new PropertyValueFactory<>("cotaMinimaDeRisc"));
        cotaMaximaColumnMajor.setCellValueFactory(new PropertyValueFactory<>("cotaMinimaDeRisc"));
        tblVwLocalitateMajor.setItems(localitateModelMajor);

        localitateModelMediu.setAll(locRiscMediu);
        numeColumnMediu.setCellValueFactory(new PropertyValueFactory<>("id"));
        rauColumnMediu.setCellValueFactory(new PropertyValueFactory<>("rau"));
        cotaMinimaColumnMediu.setCellValueFactory(new PropertyValueFactory<>("cotaMinimaDeRisc"));
        cotaMaximaColumnMediu.setCellValueFactory(new PropertyValueFactory<>("cotaMinimaDeRisc"));
        tblVwLocalitateMediu.setItems(localitateModelMediu);

        localitateModelRedus.setAll(locRiscRedus);
        numeColumnRedus.setCellValueFactory(new PropertyValueFactory<>("id"));
        rauColumnRedus.setCellValueFactory(new PropertyValueFactory<>("rau"));
        cotaMinimaColumnRedus.setCellValueFactory(new PropertyValueFactory<>("cotaMinimaDeRisc"));
        cotaMaximaColumnRedus.setCellValueFactory(new PropertyValueFactory<>("cotaMinimaDeRisc"));
        tblVwLocalitateRedus.setItems(localitateModelRedus);

    }
}

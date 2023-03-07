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


    public void showLoc(List<Localitate> localitati) {

        tblVwLocalitateMajor.setVisible(true);


        //aici trebuie numele atributelor date in clasa
        //la ce e id, pune id!
        localitateModelMajor.setAll(localitati);
        numeColumnMajor.setCellValueFactory(new PropertyValueFactory<>("id"));
        rauColumnMajor.setCellValueFactory(new PropertyValueFactory<>("rau"));
        cotaMinimaColumnMajor.setCellValueFactory(new PropertyValueFactory<>("cotaMinimaDeRisc"));
        cotaMaximaColumnMajor.setCellValueFactory(new PropertyValueFactory<>("cotaMinimaDeRisc"));
        tblVwLocalitateMajor.setItems(localitateModelMajor);


    }
}

package com.example.anar;

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

public class RauController {

    @FXML
    private TableColumn<Rau, Integer> cotaMedieColumn;
    @FXML
    private TableColumn<Rau, String> numeColumn;
    @FXML
    private TableView<Rau> tableViewRau;

    String url = "jdbc:postgresql://localhost:5432/anar";
    String username = "postgres";
    String password = "password";

    DBRauRepo repoRau = new DBRauRepo(url,username, password);
    DBLocalitateRepo repoLocalitate = new DBLocalitateRepo(url, username, password);

    Service service =  Service.getInstance(repoRau, repoLocalitate);

    private final ObservableList<Rau> rauModel = FXCollections.observableArrayList();

    @FXML
    public void initialize() {

        tableViewRau.setVisible(true);
        List<Rau> rauri = new ArrayList<>();
        for (Rau rau : service.getAllRauri()) {
            rauri.add(rau);
        }

        //aici trebuie numele atributelor date in clasa
        //la ce e id, pune id!
        rauModel.setAll(rauri);
        numeColumn.setCellValueFactory(new PropertyValueFactory<>("id"));
        cotaMedieColumn.setCellValueFactory(new PropertyValueFactory<>("cotaMedie"));
        tableViewRau.setItems(rauModel);
    }

}

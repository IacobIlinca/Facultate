package com.example.zboruri;

import com.example.zboruri.Domain.Client;
import com.example.zboruri.Domain.Ticket;
import com.example.zboruri.Domain.Zbor;
import com.example.zboruri.Repository.DBClientRepo;
import com.example.zboruri.Repository.DBTicketRepo;
import com.example.zboruri.Repository.DBZborRepo;
import com.example.zboruri.Service.Service;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.*;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.scene.input.InputMethodEvent;
import javafx.scene.input.KeyEvent;

import java.time.LocalDateTime;
import java.util.*;

public class ZboruriController {

    @FXML
    private TextField searchFromTxtFld;
    @FXML
    private Button cumparaBtn;
    @FXML
    private TableView<Zbor> tblViewwZboruri;
    @FXML
    private Button bookFlightBtn;
    @FXML
    private DatePicker departureDateDaetPicker;
    @FXML
    private ComboBox<String> toCmbBox;
    @FXML
    private ComboBox<String> fromCmbBox;
    @FXML
    private TableColumn<Zbor, Integer> seatsColumn;
    @FXML
    private TableColumn<Zbor, LocalDateTime> landingDateColumn;
    @FXML
    private TableColumn<Zbor, LocalDateTime> departureDateColumn;
    @FXML
    private TableColumn<Zbor, String> toColumn;
    @FXML
    private TableColumn<Zbor, String> fromColumn;
    @FXML
    private TableColumn<Zbor, Long> idColumn;

    String url = "jdbc:postgresql://localhost:5432/zboruri";
    String username = "postgres";
    String password = "password";

    DBClientRepo repoClient = new DBClientRepo(url, username, password);
    DBZborRepo repoZbor = new DBZborRepo(url, username, password);
    DBTicketRepo repoTicket = new DBTicketRepo(url, username, password);

    Service service = Service.getInstance(repoClient, repoZbor, repoTicket);

    private String usernameClient;


    private final ObservableList<Zbor> zborModel = FXCollections.observableArrayList();
    private final ObservableList<String> fromModel = FXCollections.observableArrayList();
    private final ObservableList<String> toModel = FXCollections.observableArrayList();


    public void initModel() {
        Set<String> froms = new TreeSet<>();
        for (Zbor zbor : service.getAllZboruri()) {
            froms.add(zbor.getLocalitateStart());
        }
        fromModel.setAll(froms);

        Set<String> tos = new TreeSet<>();
        for (Zbor zbor : service.getAllZboruri()) {
            tos.add(zbor.getLocalitateEnd());
        }
        toModel.setAll(tos);
    }

    @FXML
    public void initialize(String client) {

        toCmbBox.setItems(toModel);
        fromCmbBox.setItems(fromModel);
        initModel();
        tblViewwZboruri.setVisible(true);
        this.usernameClient = client;
    }


    public void onBookFlightBtn(ActionEvent actionEvent) {
        List<Zbor> zboruri = new ArrayList<>();
        String from = fromCmbBox.getValue();
        String to = toCmbBox.getValue();
        LocalDateTime departure_date = departureDateDaetPicker.getValue().atStartOfDay();
        for (Zbor zbor : service.getAllZboruri()) {
            if (zbor.getLocalitateStart().equals(from) && zbor.getLocalitateEnd().equals(to) && zbor.getDepartureTime().equals(departure_date)) {
                zboruri.add(zbor);
            }
        }

        //aici trebuie numele atributelor date in clasa
        zborModel.setAll(zboruri);
        idColumn.setCellValueFactory(new PropertyValueFactory<>("id"));
        fromColumn.setCellValueFactory(new PropertyValueFactory<>("localitateStart"));
        toColumn.setCellValueFactory(new PropertyValueFactory<>("localitateEnd"));
        departureDateColumn.setCellValueFactory(new PropertyValueFactory<>("departureTime"));
        landingDateColumn.setCellValueFactory(new PropertyValueFactory<>("landingTime"));
        seatsColumn.setCellValueFactory(new PropertyValueFactory<>("seats"));
        tblViewwZboruri.setItems(zborModel);
    }

    public void onCumparaBtnClick(ActionEvent actionEvent) {
        Zbor zbor = tblViewwZboruri.getSelectionModel().getSelectedItem();
        Random rand = new Random();
        Long id = rand.nextLong(1000)+1;
        Ticket ticket = new Ticket(id,usernameClient,zbor.getId(),LocalDateTime.now());
        repoTicket.save(ticket);

        Alert message = new Alert(Alert.AlertType.CONFIRMATION);
        message.setHeaderText("Confirmation!");
        message.setContentText("Flight booked successfully!");
        message.showAndWait();
    }

    public void onSearchFrom(ActionEvent actionEvent) {

    }

    public void onKeyPressedSearch(KeyEvent keyEvent) {

            List<Zbor> zboruri = new ArrayList<>();
            String from = searchFromTxtFld.getText();
            for (Zbor zbor : service.getAllZboruri()) {
                if (zbor.getLocalitateStart().contains(from)) {
                    zboruri.add(zbor);
                }
            }
            zborModel.setAll(zboruri);
            idColumn.setCellValueFactory(new PropertyValueFactory<>("id"));
            fromColumn.setCellValueFactory(new PropertyValueFactory<>("localitateStart"));
            toColumn.setCellValueFactory(new PropertyValueFactory<>("localitateEnd"));
            departureDateColumn.setCellValueFactory(new PropertyValueFactory<>("departureTime"));
            landingDateColumn.setCellValueFactory(new PropertyValueFactory<>("landingTime"));
            seatsColumn.setCellValueFactory(new PropertyValueFactory<>("seats"));
            tblViewwZboruri.setItems(zborModel);
        }



    public void textChangedSearch(InputMethodEvent inputMethodEvent) {
//        List<Zbor> zboruri = new ArrayList<>();
//        String from = searchFromTxtFld.getText();
//        for(Zbor zbor:service.getAllZboruri()){
//            if (zbor.getLocalitateStart().contains(from)){
//                zboruri.add(zbor);
//            }
//        }
//        zborModel.setAll(zboruri);
//        idColumn.setCellValueFactory(new PropertyValueFactory<>("id"));
//        fromColumn.setCellValueFactory(new PropertyValueFactory<>("localitateStart"));
//        toColumn.setCellValueFactory(new PropertyValueFactory<>("localitateEnd"));
//        departureDateColumn.setCellValueFactory(new PropertyValueFactory<>("departureTime"));
//        landingDateColumn.setCellValueFactory(new PropertyValueFactory<>("landingTime"));
//        seatsColumn.setCellValueFactory(new PropertyValueFactory<>("seats"));
//        tblViewwZboruri.setItems(zborModel);
    }
}

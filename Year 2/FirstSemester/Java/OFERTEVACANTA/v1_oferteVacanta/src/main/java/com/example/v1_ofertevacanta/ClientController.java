package com.example.v1_ofertevacanta;

import com.example.v1_ofertevacanta.Domain.Client;
import com.example.v1_ofertevacanta.Domain.Hotel;
import com.example.v1_ofertevacanta.Domain.Reservation;
import com.example.v1_ofertevacanta.Domain.SpecialOffer;
import com.example.v1_ofertevacanta.Repository.*;
import com.example.v1_ofertevacanta.Service.Service;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.stage.Stage;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class ClientController {
    @FXML
    public TableColumn<Client, LocalDate> startDateColumn;
    @FXML
    public TableColumn<Client, LocalDate> endDateColumn;
    @FXML
    public TableColumn<Client, Integer> percentsColumn;
    @FXML
    private Button reserveBtn;
    @FXML
    private DatePicker endDatePicker;
    @FXML
    private DatePicker startDatePicker;
    @FXML
    private TableView<SpecialOffer> tableViewClient;
    String url = "jdbc:postgresql://localhost:5432/ofertevacanta";
    String username = "postgres";
    String password = "password";
    String client;

    DBHotelRepository repoHotel = new DBHotelRepository(url,username, password);
    DBLocationRepository repoLocation = new DBLocationRepository(url, username,password);
    DBOfferRepository repoOffer = new DBOfferRepository(url, username,password);
    DBClientRepository repoClient = new DBClientRepository(url, username,password);
    DBReservationRepository repoReservation = new DBReservationRepository(url, username,password);

    Service service =  Service.getInstance(repoLocation, repoHotel, repoOffer, repoClient, repoReservation);

    private final ObservableList<SpecialOffer> clientModel = FXCollections.observableArrayList();


    @FXML
    public void initialize(String client) {
        startDateColumn.setCellValueFactory(new PropertyValueFactory<>("startDate"));
        endDateColumn.setCellValueFactory(new PropertyValueFactory<>("endDate"));
        percentsColumn.setCellValueFactory(new PropertyValueFactory<>("percents"));
        tableViewClient.setItems(clientModel);
        this.client = client;
        showOffers(client);
    }


    public void showOffers(String client) {
        Long id_client = Long.parseLong(client);
        Client client_complet = repoClient.findOne(id_client);
        List<SpecialOffer> offers=new ArrayList<>();
        int fidelityGrade= client_complet.getFidelityGrade();
        for(SpecialOffer specialOffer:service.getAllOffers()){
            if(fidelityGrade>specialOffer.getPercents()){
                offers.add(specialOffer);
            }
        }
        clientModel.setAll(offers);
    }

    public void onReserveBtn(ActionEvent actionEvent) {
        SpecialOffer offer=tableViewClient.getSelectionModel().getSelectedItem();
        Double hotel_id = offer.getHotelId();
        Long client_id = Long.parseLong(client);
        LocalDate start = startDatePicker.getValue();
        //LocalDateTime startDate = LocalDateTime.parse(startDatePicker.getValue().toString());
        LocalDate endDate = endDatePicker.getValue();
        Random rand = new Random();
        Double id = rand.nextDouble(1000)+1;
        Integer cnt_init = repoReservation.countReservations();
        Reservation reservation = new Reservation(id,client_id,hotel_id,endDate.getDayOfMonth()-start.getDayOfMonth());
        repoReservation.save(reservation);

        if(repoReservation.countReservations() == cnt_init+1) {
            Alert message = new Alert(Alert.AlertType.CONFIRMATION);
            message.setHeaderText("Confirmation!");
            message.setContentText("Reservation made successfully!");
            message.showAndWait();
        }
        else {
            Alert message = new Alert(Alert.AlertType.WARNING);
            message.setHeaderText("Warning!");
            message.setContentText("Reservation made unsuccessfully!");
            message.showAndWait();
        }
    }
}

package com.example.v1_ofertevacanta;

import com.example.v1_ofertevacanta.Domain.Client;
import com.example.v1_ofertevacanta.Domain.SpecialOffer;
import com.example.v1_ofertevacanta.Repository.DBClientRepository;
import com.example.v1_ofertevacanta.Repository.DBHotelRepository;
import com.example.v1_ofertevacanta.Repository.DBLocationRepository;
import com.example.v1_ofertevacanta.Repository.DBOfferRepository;
import com.example.v1_ofertevacanta.Service.Service;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXML;
import javafx.scene.control.TableColumn;
import javafx.scene.control.TableView;
import javafx.scene.control.cell.PropertyValueFactory;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

public class ClientController {
    @FXML
    public TableColumn<Client, LocalDate> startDateColumn;
    @FXML
    public TableColumn<Client, LocalDate> endDateColumn;
    @FXML
    public TableColumn<Client, Integer> percentsColumn;
    @FXML
    private TableView<SpecialOffer> tableViewClient;
    String url = "jdbc:postgresql://localhost:5432/ofertevacanta";
    String username = "postgres";
    String password = "password";

    DBHotelRepository repoHotel = new DBHotelRepository(url,username, password);
    DBLocationRepository repoLocation = new DBLocationRepository(url, username,password);
    DBOfferRepository repoOffer = new DBOfferRepository(url, username,password);
    DBClientRepository repoClient = new DBClientRepository(url, username,password);
    Service service =  Service.getInstance(repoLocation, repoHotel, repoOffer, repoClient);

    private final ObservableList<SpecialOffer> clientModel = FXCollections.observableArrayList();


    @FXML
    public void initialize(String client) {
        startDateColumn.setCellValueFactory(new PropertyValueFactory<>("startDate"));
        endDateColumn.setCellValueFactory(new PropertyValueFactory<>("endDate"));
        percentsColumn.setCellValueFactory(new PropertyValueFactory<>("percents"));
        tableViewClient.setItems(clientModel);
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
}

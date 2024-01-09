package com.example.v1_ofertevacanta;

import com.example.v1_ofertevacanta.Domain.Hotel;
import com.example.v1_ofertevacanta.Domain.Location;
import com.example.v1_ofertevacanta.Domain.Type;
import com.example.v1_ofertevacanta.Repository.*;
import com.example.v1_ofertevacanta.Service.Service;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.ComboBox;
import javafx.scene.control.TableColumn;
import javafx.scene.control.TableView;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.stage.Stage;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class HotelController {

    @FXML
    private Button showOffersBtn;
    @FXML
    private Button showHotelsBtn;
    @FXML
    private ComboBox<String> comboboxLocation;

    @FXML
    private TableView<Hotel> hotelTableView;
    @FXML
    private TableColumn<Hotel, String> nameColumn;
    @FXML
    private TableColumn<Hotel, Integer> roomsColumn;
    @FXML
    private TableColumn<Hotel, Double> priceColumn;
    @FXML
    private TableColumn<Hotel, String> typeColumn;

     String url = "jdbc:postgresql://localhost:5432/ofertevacanta";
    String username = "postgres";
    String password = "password";

    DBHotelRepository repoHotel = new DBHotelRepository(url,username, password);
    DBLocationRepository repoLocation = new DBLocationRepository(url, username,password);
    DBOfferRepository repoOffer = new DBOfferRepository(url, username,password);
    DBClientRepository repoClient = new DBClientRepository(url, username,password);
    DBReservationRepository repoReservation = new DBReservationRepository(url, username,password);

    Service service =  Service.getInstance(repoLocation, repoHotel, repoOffer, repoClient, repoReservation);


    private final ObservableList<String> locationModel = FXCollections.observableArrayList();
    private final ObservableList<Hotel> hotelModel = FXCollections.observableArrayList();

//    public void setService(Service service) {
//        this.service = service;
//
//    }

    public void initModel() {
        List<String> locations = new ArrayList<>();
//        Location loc = new Location(3.0,"mamaia");
//        List<Location> lista = new ArrayList<>();
//        lista.add(loc);
//        setService(service);
        for (Location location : service.getAllLocations()) {
            locations.add(location.getLocationName());
        }
        locationModel.setAll(locations);
    }

    @FXML
    public void initialize() {

        comboboxLocation.setItems(locationModel);
        initModel();
    }

    public void onShowHotelsBtnClick() {
        hotelTableView.setVisible(true);
        List<Hotel> hotels = new ArrayList<>();
        String location = comboboxLocation.getValue();
        Double idLocation = null;
        for (Location location1 : service.getAllLocations()) {
            if (location1.getLocationName().equals(location)) {
                idLocation = location1.getId();
            }
        }
        for (Hotel hotel : service.getAllHotels()) {
            if (hotel.getLocationId().equals(idLocation)) {
                hotels.add(hotel);
            }
        }
        //aici trebuie numele atributelor date in clasa
        hotelModel.setAll(hotels);
        nameColumn.setCellValueFactory(new PropertyValueFactory<>("hotelName"));
        roomsColumn.setCellValueFactory(new PropertyValueFactory<>("noRooms"));
        priceColumn.setCellValueFactory(new PropertyValueFactory<>("pricePerNight"));
        typeColumn.setCellValueFactory(new PropertyValueFactory<>("Type"));
        hotelTableView.setItems(hotelModel);
    }


    public void onShowOffersBtn(ActionEvent actionEvent) throws IOException {
        Hotel hotel=hotelTableView.getSelectionModel().getSelectedItem();
        Stage stage = new Stage();
        FXMLLoader fxmlLoader = new FXMLLoader(HelloApplication.class.getResource("offer.fxml"));
        Scene scene = new Scene(fxmlLoader.load(), 600, 400);
        stage.setTitle("OFFERS FOR "+hotel.getHotelName()+" HOTEL!");
        stage.setScene(scene);
        stage.show();
    }



}

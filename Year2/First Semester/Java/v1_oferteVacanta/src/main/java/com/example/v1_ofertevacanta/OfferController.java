package com.example.v1_ofertevacanta;

import com.example.v1_ofertevacanta.Domain.SpecialOffer;
import com.example.v1_ofertevacanta.Repository.DBClientRepository;
import com.example.v1_ofertevacanta.Repository.DBHotelRepository;
import com.example.v1_ofertevacanta.Repository.DBLocationRepository;
import com.example.v1_ofertevacanta.Repository.DBOfferRepository;
import com.example.v1_ofertevacanta.Service.Service;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.DatePicker;
import javafx.scene.control.TableColumn;
import javafx.scene.control.TableView;
import javafx.scene.control.cell.PropertyValueFactory;

import java.time.LocalDate;
import java.time.ZoneId;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;

public class OfferController {

    @FXML
    private TableColumn<SpecialOffer, Integer> percentsColumn;
    @FXML
    private TableColumn<SpecialOffer, Date> endDateColumn;
    @FXML
    private TableColumn<SpecialOffer, Date> startDateColumn;
    @FXML
    private TableView<SpecialOffer> tableViewOffer;
    @FXML
    private Button selectDateBtn;
    @FXML
    private DatePicker endDatePicker;
    @FXML
    private DatePicker startDatePicker;

    String url = "jdbc:postgresql://localhost:5432/ofertevacanta";
    String username = "postgres";
    String password = "password";

    DBHotelRepository repoHotel = new DBHotelRepository(url,username, password);
    DBLocationRepository repoLocation = new DBLocationRepository(url, username,password);
    DBOfferRepository repoOffer = new DBOfferRepository(url, username,password);
    DBClientRepository repoClient = new DBClientRepository(url, username,password);
    Service service =  Service.getInstance(repoLocation, repoHotel, repoOffer, repoClient);

    private final ObservableList<SpecialOffer> offerModel = FXCollections.observableArrayList();


    public void onSelectDatesBtnClick(ActionEvent actionEvent) {
        List<SpecialOffer> offers=new ArrayList<>();
        LocalDate startDate = startDatePicker.getValue();
        LocalDate endDate = endDatePicker.getValue();
        for (SpecialOffer specialOffer : service.getAllOffers()){
            if(specialOffer.getStartDate().compareTo(startDate)<=0 && specialOffer.getEndDate().compareTo(endDate)>=0){
                offers.add(specialOffer);
            }
        }
        offerModel.setAll(offers);
        System.out.println(offers.size());
        startDateColumn.setCellValueFactory(new PropertyValueFactory<>("startDate"));
        endDateColumn.setCellValueFactory(new PropertyValueFactory<>("endDate"));
        percentsColumn.setCellValueFactory(new PropertyValueFactory<>("percents"));
        tableViewOffer.setItems(offerModel);
    }
}

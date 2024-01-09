package com.example.v1_ofertevacanta;

import com.example.v1_ofertevacanta.Repository.DBHotelRepository;
import com.example.v1_ofertevacanta.Repository.DBLocationRepository;
import com.example.v1_ofertevacanta.Service.Service;
import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.stage.Stage;

import java.io.IOException;
import java.lang.reflect.Parameter;
import java.util.List;

public class HelloApplication extends Application {

    @Override
    public void start(Stage stage) throws IOException {

//        String url = "jdbc:postgresql://localhost:5432/ofertevacanta";
//        String username = "postgres";
//        String password = "password";
//
//        DBHotelRepository repoHotel = new DBHotelRepository(url,username, password);
//        DBLocationRepository repoLocation = new DBLocationRepository(url, username,password);
//        Service service = new Service(repoHotel, repoLocation);

        FXMLLoader fxmlLoader = new FXMLLoader(HelloApplication.class.getResource("hotel.fxml"));
        Scene scene = new Scene(fxmlLoader.load(), 700, 400);
        stage.setTitle("Oferte vacanta!");
        HotelController hotelController = fxmlLoader.getController();
//        hotelController.setService(service);
        hotelController.initialize();

        Parameters arg = getParameters();
        List<String> clienti = arg.getRaw();
        for(var client: clienti)
        {
            FXMLLoader client_loader = new FXMLLoader(HelloApplication.class.getResource("client.fxml"));
            Scene client_scene = new Scene(client_loader.load(),600,400 );
            Stage client_stage = new Stage();
            client_stage.setTitle("Client " + client);
            client_stage.setScene(client_scene);

            ClientController clientController = client_loader.getController();
            clientController.initialize(client);
            client_stage.show();

        }




        stage.setScene(scene);
        stage.show();




}


    public static void main(String[] args) {
        launch(args);
    }
}
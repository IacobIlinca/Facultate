package com.example.ati_v1;

import com.example.ati_v1.Repository.DBPacientRepo;
import com.example.ati_v1.Repository.DBPatRepo;
import com.example.ati_v1.Service.Service;
import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.stage.Stage;

import java.io.IOException;

public class HelloApplication extends Application {
    @Override
    public void start(Stage stage) throws IOException {

        String url = "jdbc:postgresql://localhost:5432/restaurants";
        String username = "postgres";
        String password = "password";
        DBPatRepo repoPat = new DBPatRepo(url , username , password);
        DBPacientRepo repoPacient = new DBPacientRepo(url,username,password);

        Service service = new Service(repoPat, repoPacient);

        FXMLLoader fxmlLoader = new FXMLLoader(HelloApplication.class.getResource("pat.fxml"));
        PatController patController = new PatController(service);
        fxmlLoader.setController(patController);
        Scene scene = new Scene(fxmlLoader.load());
        stage.setTitle("Paturi ATI");
        stage.setScene(scene);
        patController.initialize();

        stage.show();

        //deschide fereastra noua
//        FXMLLoader pacient_loader = new FXMLLoader(HelloApplication.class.getResource("pacient.fxml"));
//
//        PacientController pacientController = new PacientController(service);
//        pacient_loader.setController(pacientController);
//        Scene pacient_scene = new Scene(pacient_loader.load(),600,400 );
//        Stage pacient_stage = new Stage();
//        pacient_stage.setTitle("Pacienti in asteptare");
//        pacient_stage.setScene(pacient_scene);
//        pacientController.initialize();
//
//        pacient_stage.show();
    }

    public static void main(String[] args) {
        launch();
    }
}
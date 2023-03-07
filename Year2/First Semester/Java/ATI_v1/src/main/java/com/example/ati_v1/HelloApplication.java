package com.example.ati_v1;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.stage.Stage;

import java.io.IOException;

public class HelloApplication extends Application {
    @Override
    public void start(Stage stage) throws IOException {
        FXMLLoader fxmlLoader = new FXMLLoader(HelloApplication.class.getResource("pat.fxml"));
        Scene scene = new Scene(fxmlLoader.load(), 700, 400);
        stage.setTitle("Paturi ATI");
        stage.setScene(scene);
        PatController patController = fxmlLoader.getController();
        patController.initialize();

        stage.show();

        //deschide fereastra noua
        FXMLLoader pacient_loader = new FXMLLoader(HelloApplication.class.getResource("pacient.fxml"));
        Scene pacient_scene = new Scene(pacient_loader.load(),600,400 );
        Stage pacient_stage = new Stage();
        pacient_stage.setTitle("Pacienti in asteptare");
        pacient_stage.setScene(pacient_scene);

        PacientController pacientController = pacient_loader.getController();
        pacientController.initialize();
        pacient_stage.show();
    }

    public static void main(String[] args) {
        launch();
    }
}
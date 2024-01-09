package com.example.anar;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.stage.Stage;

import java.io.IOException;

public class HelloApplication extends Application {
    @Override
    public void start(Stage stage) throws IOException {
        FXMLLoader fxmlLoader = new FXMLLoader(HelloApplication.class.getResource("rau.fxml"));
        Scene scene = new Scene(fxmlLoader.load(), 700, 500);
        stage.setTitle("Rauri");
        stage.setScene(scene);
        stage.show();

        FXMLLoader loc_loader = new FXMLLoader(HelloApplication.class.getResource("localitate.fxml"));
        Scene loc_scene = new Scene(loc_loader.load(),700,700 );
        Stage loc_stage = new Stage();
        loc_stage.setTitle("Localitati");
        loc_stage.setScene(loc_scene);

        LocalitateController locController = loc_loader.getController();
        locController.initialize();
        loc_stage.show();
    }

    public static void main(String[] args) {
        launch();
    }
}
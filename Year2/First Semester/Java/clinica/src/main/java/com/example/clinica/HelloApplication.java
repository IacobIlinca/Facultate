package com.example.clinica;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.stage.Stage;

import java.io.IOException;

public class HelloApplication extends Application {
    @Override
    public void start(Stage stage) throws IOException {
        FXMLLoader fxmlLoader = new FXMLLoader(HelloApplication.class.getResource("sectie.fxml"));
        Scene scene = new Scene(fxmlLoader.load(), 600, 400);
        stage.setTitle("Sectii");
        stage.setScene(scene);

        SectieController sectieController = fxmlLoader.getController();
        sectieController.initialize();
        sectieController.showMedici();


        stage.show();
    }

    public static void main(String[] args) {
        launch();
    }
}
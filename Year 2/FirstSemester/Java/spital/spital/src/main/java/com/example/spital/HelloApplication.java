package com.example.spital;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.stage.Stage;

import java.io.IOException;

public class HelloApplication extends Application {
    @Override
    public void start(Stage stage) throws IOException {
        FXMLLoader fxmlLoader = new FXMLLoader(HelloApplication.class.getResource("beds.fxml"));
        Scene scene = new Scene(fxmlLoader.load(), 280, 230);
        stage.setScene(scene);
        stage.show();

        FXMLLoader fxmlLoader1 = new FXMLLoader(HelloApplication.class.getResource("pacienti-view.fxml"));
        Scene scene1 = new Scene(fxmlLoader1.load(), 600, 321);
        Stage stage1 = new Stage();
        stage1.setScene(scene1);
        stage1.show();
    }

    public static void main(String[] args) {
        launch();
    }
}
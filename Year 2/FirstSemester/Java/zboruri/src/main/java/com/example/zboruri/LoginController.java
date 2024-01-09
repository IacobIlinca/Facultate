package com.example.zboruri;

import com.example.zboruri.Domain.Client;
import com.example.zboruri.Repository.DBClientRepo;
import com.example.zboruri.Repository.DBTicketRepo;
import com.example.zboruri.Repository.DBZborRepo;
import com.example.zboruri.Service.Service;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.stage.Stage;

import java.io.IOException;

public class LoginController {

    @FXML
    private Button loginButton;
    @FXML
    private TextField loginTxtFld;

    String url = "jdbc:postgresql://localhost:5432/zboruri";
    String username = "postgres";
    String password = "password";

    DBClientRepo repoClient = new DBClientRepo(url,username, password);
    DBZborRepo repoZbor = new DBZborRepo(url, username,password);
    DBTicketRepo repoTicket = new DBTicketRepo(url, username,password);

    Service service =  Service.getInstance(repoClient, repoZbor, repoTicket);


    public void onLoginButton(ActionEvent actionEvent) throws IOException {
        String username = loginTxtFld.getText();
        Client client = repoClient.findOne(username);
        Stage stage = new Stage();
        FXMLLoader fxmlLoader = new FXMLLoader(HelloApplication.class.getResource("zboruri.fxml"));
        Scene scene = new Scene(fxmlLoader.load(), 600, 400);
        stage.setTitle("ZBORURI pentru: " + username);
        stage.setScene(scene);

        ZboruriController zboruriController = fxmlLoader.getController();
        zboruriController.initialize(username);

        stage.show();
    }
}

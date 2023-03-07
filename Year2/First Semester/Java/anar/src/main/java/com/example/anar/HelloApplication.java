package com.example.anar;

import com.example.anar.Domain.Localitate;
import com.example.anar.Domain.Rau;
import com.example.anar.Repository.DBLocalitateRepo;
import com.example.anar.Repository.DBRauRepo;
import com.example.anar.Service.Service;
import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.stage.Stage;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

public class HelloApplication extends Application {

    String url = "jdbc:postgresql://localhost:5432/anar";
    String username = "postgres";
    String password = "password";

    DBRauRepo repoRau = new DBRauRepo(url, username, password);
    DBLocalitateRepo repoLocalitate = new DBLocalitateRepo(url, username, password);

    Service service = Service.getInstance(repoRau, repoLocalitate);


    @Override
    public void start(Stage stage) throws IOException {
        FXMLLoader fxmlLoader = new FXMLLoader(HelloApplication.class.getResource("rau.fxml"));
        RauController rauController = new RauController();
        //fxmlLoader.setController(rauController);
        Scene scene = new Scene(fxmlLoader.load(), 600, 250);
        stage.setTitle("Rauri");
        stage.setScene(scene);
        stage.show();



        List<Localitate> locRiscMajor = new ArrayList<>();
        List<Localitate> locRiscMediu = new ArrayList<>();
        List<Localitate> locRiscRedus = new ArrayList<>();
        for (Localitate loc : service.getAllLocalitati()) {
            String numeRau = loc.getRau();
            int cota = 0;
            for (Rau rau : service.getAllRauri()) {
                if (Objects.equals(rau.getId(), numeRau)) {
                    cota = rau.getCotaMedie();
                }
            }
            if (cota > loc.getCotaMaximaAdmisa()) {
                locRiscMajor.add(loc);
            }
            else if(cota >loc.getCotaMinimaDeRisc()){
                locRiscMediu.add(loc);
            }
            else {
                locRiscRedus.add(loc);
            }
        }


        FXMLLoader loc_loader1 = new FXMLLoader(HelloApplication.class.getResource("localitate.fxml"));
        Scene loc_scene1 = new Scene(loc_loader1.load(),500,500 );
        Stage loc_stage1 = new Stage();
        loc_stage1.setTitle("Localitati");
        loc_stage1.setScene(loc_scene1);
        LocalitateController locController1= loc_loader1.getController();
        //locController.initialize();
        locController1.showLoc(locRiscMajor);
        loc_stage1.show();

        FXMLLoader loc_loader2 = new FXMLLoader(HelloApplication.class.getResource("localitate.fxml"));
        Scene loc_scene2 = new Scene(loc_loader2.load(),500,500 );
        Stage loc_stage2 = new Stage();
        loc_stage2.setTitle("Localitati");
        loc_stage2.setScene(loc_scene2);
        LocalitateController locController2 = loc_loader2.getController();
        locController2.showLoc(locRiscMediu);
        loc_stage2.show();

        FXMLLoader loc_loader3 = new FXMLLoader(HelloApplication.class.getResource("localitate.fxml"));
        Scene loc_scene3 = new Scene(loc_loader3.load(),500,500 );
        Stage loc_stage3 = new Stage();
        loc_stage3.setTitle("Localitati");
        loc_stage3.setScene(loc_scene3);
        LocalitateController locController3 = loc_loader3.getController();
        locController3.showLoc(locRiscRedus);
        loc_stage3.show();



    }

    public static void main(String[] args) {
        launch();
    }
}
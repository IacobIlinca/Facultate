package com.example.examenpractic;

import com.example.examenpractic.Domain.Oras;
import com.example.examenpractic.Domain.Persoana;
import com.example.examenpractic.Repository.DBNevoiRepository;
import com.example.examenpractic.Repository.DBPersoanaRepository;
import com.example.examenpractic.Service.Service;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.stage.Stage;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Random;

public class InregistrareController {

    @FXML
    private Button logInBtn;
    @FXML
    private ListView<String> useriLstVw;
    @FXML
    private Button registerBtn;
    @FXML
    private TextField parolaTxtFld;
    @FXML
    private TextField ussernameTxtFld;
    @FXML
    private TextField prenumeTxtFld;
    @FXML
    private TextField telefonTxtFld;
    @FXML
    private TextField nrStradaTxtFld;
    @FXML
    private TextField stradaTxtFld;
    @FXML
    private TextField numeTxtFld;
    @FXML
    private ComboBox<String> orasCmbBox;

    String url = "jdbc:postgresql://localhost:5432/examen";
    String username = "postgres";
    String password = "password";

    DBPersoanaRepository repoPersoana = new DBPersoanaRepository(url, username, password);
    DBNevoiRepository repoNevoi = new DBNevoiRepository(url, username, password);

    Service service = Service.getInstance(repoPersoana, repoNevoi);
    private final ObservableList<Oras> orasModel = FXCollections.observableArrayList();
    private final ObservableList<String> orasStModel = FXCollections.observableArrayList();
    private final ObservableList<String> usernameModel = FXCollections.observableArrayList();

    public void initModel() {
        List<Oras> orase = Arrays.asList(Oras.valueOf("CLUJ"), Oras.valueOf("GALATI"), Oras.valueOf("MURES"), Oras.valueOf("ORADEA"), Oras.valueOf("CRAIOVA"));
        orasModel.setAll(orase);
    }

    @FXML
    public void initialize() {

        initModel();
        List<String> orasele = new ArrayList<>();
        for (Oras oras : orasModel) {
            orasele.add(oras.toString());

        }
        orasStModel.setAll(orasele);
        orasCmbBox.setItems(orasStModel);

        List<String> usernameuri = new ArrayList<>();
        for (Persoana pers : service.getAllPersoane()) {
            usernameuri.add(pers.getUsername());
        }
        usernameModel.setAll(usernameuri);
        useriLstVw.setItems(usernameModel);

    }

    public void onRegisterBtnClicked(ActionEvent actionEvent) {
        Random rand = new Random();
        Long id = rand.nextLong(1000) + 1;
        String nume = numeTxtFld.getText();
        String prenume = prenumeTxtFld.getText();
        String username = ussernameTxtFld.getText();
        String parola = parolaTxtFld.getText();
        Oras oras = Oras.valueOf(orasCmbBox.getValue());
        String strada = stradaTxtFld.getText();
        String nrStrada = nrStradaTxtFld.getText();
        String telefon = telefonTxtFld.getText();
        Persoana persoana = new Persoana(id, nume, prenume, username, parola, oras, strada, nrStrada, telefon);

        if (!(numeTxtFld.getText().trim().isEmpty() || numeTxtFld.getText() == null) ||
                prenumeTxtFld.getText().trim().isEmpty() || prenumeTxtFld.getText() == null ||
                ussernameTxtFld.getText().trim().isEmpty() || ussernameTxtFld.getText() == null ||
                parolaTxtFld.getText().trim().isEmpty() || parolaTxtFld.getText() == null ||
                stradaTxtFld.getText().trim().isEmpty() || stradaTxtFld.getText() == null ||
                nrStradaTxtFld.getText().trim().isEmpty() || nrStradaTxtFld.getText() == null ||
                telefonTxtFld.getText().trim().isEmpty() || telefonTxtFld.getText() == null
        ) {
            repoPersoana.save(persoana);
            initialize();


            Alert message = new Alert(Alert.AlertType.CONFIRMATION);
            message.setHeaderText("Confirmation!");
            message.setContentText("Utilizator inregistrat cu succes!");
            message.showAndWait();

            numeTxtFld.clear();
            prenumeTxtFld.clear();
            ussernameTxtFld.clear();
            parolaTxtFld.clear();
            stradaTxtFld.clear();
            nrStradaTxtFld.clear();
            telefonTxtFld.clear();
        } else {
            Alert message = new Alert(Alert.AlertType.WARNING);
            message.setHeaderText("WARNING!");
            message.setContentText("Completati toate campurile!");
            message.showAndWait();
        }
    }

    public void onLogInBtnClicked(ActionEvent actionEvent) throws IOException {
        String username = useriLstVw.getSelectionModel().getSelectedItem();
        Stage stage = new Stage();
        FXMLLoader fxmlLoader = new FXMLLoader(HelloApplication.class.getResource("nevoi.fxml"));
        Scene scene = new Scene(fxmlLoader.load(), 600, 400);
        stage.setTitle("User-ul logat : " + username);
        stage.setScene(scene);
        stage.show();

        NevoiController ajutorController = fxmlLoader.getController();
        ajutorController.initialize(username);
    }
}

package com.example.clinica;

import com.example.clinica.Domain.Medic;
import com.example.clinica.Domain.Sectie;
import com.example.clinica.Repository.DBConsultatieRepo;
import com.example.clinica.Repository.DBMedicRepo;
import com.example.clinica.Repository.DBSectieRepo;
import com.example.clinica.Service.Service;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.TableCell;
import javafx.scene.control.TableColumn;
import javafx.scene.control.TableRow;
import javafx.scene.control.TableView;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.scene.input.MouseEvent;
import javafx.stage.Stage;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class SectieController {


    @FXML
    private TableColumn<Sectie, Integer> durataColumn;
    @FXML
    private TableColumn<Sectie, Float> pretConsultatieColumn;
    @FXML
    private TableColumn<Sectie, Long> sefDeSectieColumn;
    @FXML
    private TableColumn<Sectie, String> numeColumn;
    @FXML
    private TableColumn<Sectie, Long> idColumn;
    @FXML
    private TableView<Sectie> tblViewSectie;

    String url = "jdbc:postgresql://localhost:5432/clinica";
    String username = "postgres";
    String password = "password";

    DBSectieRepo repoSectie = new DBSectieRepo(url, username, password);
    DBMedicRepo repoMedic = new DBMedicRepo(url, username, password);

    DBConsultatieRepo repoConsultatie = new DBConsultatieRepo(url, username, password);

    Service service = Service.getInstance(repoSectie, repoMedic, repoConsultatie);
    private final ObservableList<Sectie> sectieModel = FXCollections.observableArrayList();

    @FXML
    public void initialize() {

        tblViewSectie.setVisible(true);
        List<Sectie> sectii = new ArrayList<>();
        for (Sectie sectie : service.getAllSectii()) {
            sectii.add(sectie);
        }

        //aici trebuie numele atributelor date in clasa
        //la ce e id, pune id!
        sectieModel.setAll(sectii);
        idColumn.setCellValueFactory(new PropertyValueFactory<>("id"));
        numeColumn.setCellValueFactory(new PropertyValueFactory<>("nume"));
        sefDeSectieColumn.setCellValueFactory(new PropertyValueFactory<>("idSefDeSectie"));
        pretConsultatieColumn.setCellValueFactory(new PropertyValueFactory<>("pretPerConsultatie"));
        durataColumn.setCellValueFactory(new PropertyValueFactory<>("durataMaximaConsultatie"));

        tblViewSectie.setItems(sectieModel);

        customiseFactory(numeColumn);
    }

    public void showMedici() throws IOException {
        for (Medic medic : service.getAllMedici()) {
            Stage stage = new Stage();
            FXMLLoader fxmlLoader = new FXMLLoader(HelloApplication.class.getResource("medic.fxml"));
            Scene scene = new Scene(fxmlLoader.load(), 600, 400);
            stage.setTitle("medic: " + medic.getNume());
            MedicController medicController = fxmlLoader.getController();
            medicController.initialize(medic);
            stage.setScene(scene);
            stage.show();
        }
    }

    public void pressedLineSectie(MouseEvent mouseEvent) throws IOException {
        Sectie sectie = tblViewSectie.getSelectionModel().getSelectedItem();
        Stage stage = new Stage();
        FXMLLoader fxmlLoader = new FXMLLoader(HelloApplication.class.getResource("consultatie.fxml"));
        Scene scene = new Scene(fxmlLoader.load(), 600, 400);
        stage.setTitle("Programare consultatii pentru sectia: " + sectie.getNume());
        stage.setScene(scene);
        stage.show();
        Long idSectie = sectie.getId();

        ConsultatieController consultatieController = fxmlLoader.getController();
        consultatieController.initialize();

    }

    private void customiseFactory(TableColumn<Sectie, String> calltypel) {
        calltypel.setCellFactory(column -> {
            return new TableCell<Sectie, String>() {
                @Override
                protected void updateItem(String item, boolean empty) {
                    super.updateItem(item, empty);

                    setText(empty ? "" : getItem().toString());
                    setGraphic(null);

                    TableRow<Sectie> currentRow = getTableRow();

                    if (!isEmpty()) {

                        if(item.startsWith("U"))
                            currentRow.setStyle("-fx-background-color:lightcoral");
                        else
                            currentRow.setStyle("-fx-background-color:lightgreen");
                    }
                }
            };
        });
    }
}

package com.example.examenpractic;

import com.example.examenpractic.Domain.Nevoi;
import com.example.examenpractic.Domain.NevoiDTO;
import com.example.examenpractic.Domain.Persoana;
import com.example.examenpractic.Repository.DBNevoiRepository;
import com.example.examenpractic.Repository.DBPersoanaRepository;
import com.example.examenpractic.Service.Service;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.*;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.scene.input.MouseEvent;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;
import java.util.Random;

public class NevoiController {
    @FXML
    private TableView<NevoiDTO> tblView1Nevoi;
    @FXML
    private TableColumn<Nevoi, Long> idColumn;
    @FXML
    private TableColumn<Nevoi, String> titluColumn;
    @FXML
    private TableColumn<Nevoi, String> descriereColumn;
    @FXML
    private TableColumn<Nevoi, String> omInNevoieColumn;
    @FXML
    private TableColumn<Nevoi, String> omSalvatorColumn;
    @FXML
    private TableColumn<Nevoi, String> statusColumn;
    @FXML
    private TableView<NevoiDTO> tblView2Nevoi;
    @FXML
    private TableColumn<Nevoi, Long> idColumn2;
    @FXML
    private TableColumn<Nevoi, String> titluColumn2;
    @FXML
    private TableColumn<Nevoi, String> descriereColumn2;
    @FXML
    private TableColumn<Nevoi, LocalDateTime> deadlineColumn2;
    @FXML
    private TableColumn<Nevoi, String> omInNevoieColumn2;
    @FXML
    private TableColumn<Nevoi, String> omSalvatorColumn2;
    @FXML
    private TableColumn<Nevoi, String> statusColumn2;
    @FXML
    private TextField titluTxtFld;
    @FXML
    private TextField descrietreTxtFld;
    @FXML
    private DatePicker deadlineDtPck;
    @FXML
    private Button adaugaNevoieBtn;
    @FXML
    private TableColumn<Nevoi, LocalDateTime> deadlineColumn;

    String url = "jdbc:postgresql://localhost:5432/examen";
    String username = "postgres";
    String password = "password";

    DBPersoanaRepository repoPersoana = new DBPersoanaRepository(url, username, password);
    DBNevoiRepository repoNevoi = new DBNevoiRepository(url, username, password);

    Service service = Service.getInstance(repoPersoana, repoNevoi);

    private final ObservableList<Nevoi> nevoiModel = FXCollections.observableArrayList();
    private final ObservableList<NevoiDTO> nevoiDTOModel = FXCollections.observableArrayList();
    private final ObservableList<NevoiDTO> nevoiModel2 = FXCollections.observableArrayList();
    private String usernamePersoana = null;


    @FXML
    public void initialize(String username) {

        List<Nevoi> nevoi = new ArrayList<>();
        List<NevoiDTO> listanevoiDTO = new ArrayList<>();
        String oras = null;
        for (Persoana pers : service.getAllPersoane()) {
            if (Objects.equals(pers.getUsername(), username)) {
                oras = pers.getOras().toString();
            }
        }

        for (Nevoi nevoie : service.getAllNevoi()) {
            Long idPers = nevoie.getOmInNevoie();
            Persoana persoana = null;
            for (Persoana pers : service.getAllPersoane()) {
                if (Objects.equals(idPers, pers.getId())) {
                    persoana = pers;
                }
            }
            if (Objects.equals(persoana.getOras().toString(), oras)) {
                Long omNev = nevoie.getOmInNevoie();
                Long omSalv = nevoie.getOmSalvator();
                String omNevSt = null;
                String omSalvSt = null;
                for (Persoana pers : service.getAllPersoane()) {
                    if (Objects.equals(pers.getId(), omNev)) {
                        omNevSt = pers.getNume();
                    }
                    if (Objects.equals(pers.getId(), omSalv)) {
                        omSalvSt = pers.getNume();
                    }
                }
                Long vfId = null;
                for (Persoana per : service.getAllPersoane()) {
                    if (Objects.equals(per.getUsername(), this.usernamePersoana)) {
                        vfId = per.getId();
                    }
                }

                if (!Objects.equals(nevoie.getOmInNevoie(), vfId)) {
                    NevoiDTO nevoiDTO = new NevoiDTO(nevoie.getId(), nevoie.getTitlu(), nevoie.getDescriere(), nevoie.getDeadline(), omNevSt, omSalvSt, nevoie.getStatus());
                    listanevoiDTO.add(nevoiDTO);
                }
            }
        }


        nevoiDTOModel.setAll(listanevoiDTO);
        idColumn.setCellValueFactory(new PropertyValueFactory<>("id"));
        titluColumn.setCellValueFactory(new PropertyValueFactory<>("titlu"));
        descriereColumn.setCellValueFactory(new PropertyValueFactory<>("descriere"));
        deadlineColumn.setCellValueFactory(new PropertyValueFactory<>("deadline"));
        omInNevoieColumn.setCellValueFactory(new PropertyValueFactory<>("omInNevoie"));
        omSalvatorColumn.setCellValueFactory(new PropertyValueFactory<>("omSalvator"));
        statusColumn.setCellValueFactory(new PropertyValueFactory<>("status"));
        tblView1Nevoi.setItems(nevoiDTOModel);
        this.usernamePersoana = username;


        //al doilea tabel
        List<NevoiDTO> listanevoiDTO2 = new ArrayList<>();


        List<NevoiDTO> nevoi2 = new ArrayList<>();
        Long person = null;
        for (Persoana pers : service.getAllPersoane()) {
            if (Objects.equals(pers.getUsername(), username)) {
                person = pers.getId();
            }
        }
        for (Nevoi nevoie2 : service.getAllNevoi()) {
            if (Objects.equals(nevoie2.getOmSalvator(), person)) {
//                List<NevoiDTO> listanevoiDTO3 = new ArrayList<>();
                Long omNev = nevoie2.getOmInNevoie();
                Long omSalv = nevoie2.getOmSalvator();
                String omNevSt = null;
                String omSalvSt = null;
                for (Persoana pers : service.getAllPersoane()) {
                    if (Objects.equals(pers.getId(), omNev)) {
                        omNevSt = pers.getNume();
                    }
                    if (Objects.equals(pers.getId(), omSalv)) {
                        omSalvSt = pers.getNume();
                    }
                }
                NevoiDTO nevoiDTO = new NevoiDTO(nevoie2.getId(), nevoie2.getTitlu(), nevoie2.getDescriere(), nevoie2.getDeadline(), omNevSt, omSalvSt, nevoie2.getStatus());
                listanevoiDTO2.add(nevoiDTO);
                nevoi2.add(nevoiDTO);
            }
        }


        nevoiModel2.setAll(nevoi2);
        idColumn2.setCellValueFactory(new PropertyValueFactory<>("id"));
        titluColumn2.setCellValueFactory(new PropertyValueFactory<>("titlu"));
        descriereColumn2.setCellValueFactory(new PropertyValueFactory<>("descriere"));
        deadlineColumn2.setCellValueFactory(new PropertyValueFactory<>("deadline"));
        omInNevoieColumn2.setCellValueFactory(new PropertyValueFactory<>("omInNevoie"));
        omSalvatorColumn2.setCellValueFactory(new PropertyValueFactory<>("omSalvator"));
        statusColumn2.setCellValueFactory(new PropertyValueFactory<>("status"));
        tblView2Nevoi.setItems(nevoiModel2);


    }

    public void onNevoieMouseClicked(MouseEvent mouseEvent) {
        NevoiDTO nevoieDto = tblView1Nevoi.getSelectionModel().getSelectedItem();
        Long idOmNev = null;
        Long idOmSalv = null;
        for (Persoana pers : service.getAllPersoane()) {
            if (Objects.equals(nevoieDto.getOmInNevoie(), pers.getNume())) {
                idOmNev = pers.getId();
            }
            if (Objects.equals(nevoieDto.getOmSalvator(), pers.getNume())) {
                idOmSalv = pers.getId();
            }
        }

        Nevoi nevoie = new Nevoi(nevoieDto.getId(), nevoieDto.getTitlu(), nevoieDto.getDescriere(), nevoieDto.getDeadline(), idOmNev);
        int ok = 0;
        if (nevoieDto.getOmSalvator() != null) {
            ok = 1;
        }
        if (ok == 0) {
            Persoana persoana = null;
            for (Persoana pers : service.getAllPersoane()) {
                if (Objects.equals(pers.getUsername(), usernamePersoana)) {
                    persoana = pers;
                }
            }
            nevoie.setOmSalvator(persoana.getId());
            nevoie.setStatus("Erou gasit!");
            repoNevoi.update(nevoie);
            initialize(persoana.getUsername());

            Alert message = new Alert(Alert.AlertType.CONFIRMATION);
            message.setHeaderText("Confirmation!");
            message.setContentText("Nevoie salvata!");
            message.showAndWait();
        } else {
            Alert message = new Alert(Alert.AlertType.WARNING);
            message.setHeaderText("Warning!");
            message.setContentText("Nevoie nu mai trebuie salvata!");
            message.showAndWait();

        }
    }

    public void onAdaugaNevoieBtn(ActionEvent actionEvent) {
        String titlu = titluTxtFld.getText();
        String descriere = descrietreTxtFld.getText();
        LocalDateTime deadline = deadlineDtPck.getValue().atStartOfDay();
        Persoana omInNevoie = null;
        for (Persoana per : service.getAllPersoane()) {
            if (Objects.equals(per.getUsername(), usernamePersoana)) {
                omInNevoie = per;
            }
        }
        Random rand = new Random();
        Long id = rand.nextLong(1000) + 1;
        Nevoi nevoie = new Nevoi(id, titlu, descriere, deadline, omInNevoie.getId());

        List<Nevoi> resultInit = new ArrayList<Nevoi>();
        repoNevoi.findAll().forEach(resultInit::add);
        //System.out.println(resultInit.size());


        repoNevoi.save(nevoie);
        initialize(usernamePersoana);

        List<Nevoi> resultFinal = new ArrayList<Nevoi>();
        repoNevoi.findAll().forEach(resultFinal::add);
        //System.out.println(resultFinal.size());

        if (resultInit.size() < resultFinal.size()) {
            Alert message = new Alert(Alert.AlertType.CONFIRMATION);
            message.setHeaderText("Confirmation!");
            message.setContentText("Nevoie adaugata!");
            message.showAndWait();
            titluTxtFld.clear();
            descrietreTxtFld.clear();

        } else {
            Alert message = new Alert(Alert.AlertType.WARNING);
            message.setHeaderText("Warning!");
            message.setContentText("Nevoie nu a putut fi adaugata!");
            message.showAndWait();
        }
    }

}

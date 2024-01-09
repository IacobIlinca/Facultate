package com.example.spital;

import com.example.spital.domain.Pacient;
import com.example.spital.domain.Pat;
import com.example.spital.domain.Type;
import com.example.spital.repository.file.PacientRepo;
import com.example.spital.repository.file.PatRepo;
import com.example.spital.service.Service;
import com.example.spital.utils.Observable;
import com.example.spital.utils.Observer;
import com.example.spital.utils.events.PatEvent;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.*;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;

public class PacientiView implements Observer<PatEvent> {



    Service service = Service.getInstance(new PatRepo("D:\\An2_MAP\\spital\\src\\main\\java\\com\\example\\spital\\paturi.txt"), new PacientRepo("D:\\An2_MAP\\spital\\src\\main\\java\\com\\example\\spital\\pacienti.txt"));

    private final ObservableList<Pacient> pacientModel = FXCollections.observableArrayList();

    @FXML
    private ListView<Pacient> listaPacienti;
    @FXML
    private RadioButton checkTIC;
    @FXML
    private RadioButton checkTIM;
    @FXML
    private RadioButton checkTIIP;

    @FXML
    public void initialize(){
        listaPacienti.setItems(pacientModel);
        service.addObserver(this);
        initModel();
    }
    private void initModel(){
        List<Pacient> pacienti = new ArrayList<>();

        for (Pacient pacient:service.getAllPacient()){
            int ok = 0;
            for (Pat pat:service.getAllBeds()){
                if (pat.getPacientId().equals(pacient.getId())) {
                    ok = 1;
                    break;
                }
            }
            if (ok == 0){
                pacienti.add(pacient);
            }
        }
        List<Pacient> sortedPacienti = pacienti.stream().sorted(Comparator.comparingInt(Pacient::getGravitate).reversed()).collect(Collectors.toList());
        pacientModel.setAll(sortedPacienti);

    }
    @FXML
    public void onClickButton(ActionEvent actionEvent) {
        Integer id = listaPacienti.getSelectionModel().getSelectedItem().getId();
        if (checkTIC.isSelected()){

            int idpat = 0;
            for (Pat pat:service.getAllBeds())
            {
                if (pat.getPacientId() == 0 && pat.getTip().equals(Type.TIC)){
                    idpat = pat.getId();
                    break;}
            }
            if (idpat != 0)
                service.interneazaPacient(idpat,id);
        }
        else if (checkTIM.isSelected()){

            int idpat = 0;
            for (Pat pat:service.getAllBeds())
            {
                if (pat.getPacientId() == 0 && pat.getTip().equals(Type.TIM)){
                    idpat = pat.getId();
                    break;}
            }
            if (idpat != 0)
                service.interneazaPacient(idpat,id);
        }
        else if (checkTIIP.isSelected()){
            int idpat = 0;
            for (Pat pat:service.getAllBeds())
            {
                if (pat.getPacientId() == 0 && pat.getTip().equals(Type.TIIP)){
                    idpat = pat.getId();
                    break;}
            }
            if (idpat != 0)
                service.interneazaPacient(idpat,id);
        }
        else{
            Alert alert = new Alert(Alert.AlertType.ERROR);
            alert.setTitle("");
            alert.setHeaderText("ERROR");
            alert.setContentText("Check one bed type!");
            alert.show();
        }
        initModel();
    }

    @Override
    public void update(PatEvent event) {
        initModel();
    }
}

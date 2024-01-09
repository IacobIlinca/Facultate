package com.example.spital;

import com.example.spital.domain.Type;
import com.example.spital.repository.file.PacientRepo;
import com.example.spital.repository.file.PatRepo;
import com.example.spital.service.Service;
import com.example.spital.utils.Observable;
import com.example.spital.utils.Observer;
import com.example.spital.utils.events.PatEvent;
import javafx.fxml.FXML;
import javafx.scene.control.TextField;

import java.util.concurrent.atomic.AtomicInteger;

public class Beds implements Observer<PatEvent> {
    Service service = Service.getInstance(new PatRepo("D:\\An2_MAP\\spital\\src\\main\\java\\com\\example\\spital\\paturi.txt"), new PacientRepo("D:\\An2_MAP\\spital\\src\\main\\java\\com\\example\\spital\\pacienti.txt"));
    @FXML
    public TextField paturiOcupateTxtFld;
    @FXML
    public TextField TIIPtxt;
    @FXML
    public TextField TICtxt;
    @FXML
    public TextField TIMtxt;

    @FXML
    public void initialize() {
        service.addObserver(this);
        AtomicInteger ocupate = new AtomicInteger();
        AtomicInteger ocupateTIC = new AtomicInteger();
        AtomicInteger ocupateTIM = new AtomicInteger();
        AtomicInteger ocupateTIIP = new AtomicInteger();
        service.getAllBeds().forEach(pat -> {
            if (pat.getPacientId() != 0) {
                ocupate.set(ocupate.get() + 1);
            } else if (pat.getPacientId() == 0) {
                if (pat.getTip() == Type.TIC) {
                    ocupateTIC.set(ocupateTIC.get() + 1);
                } else if (pat.getTip() == Type.TIM) {
                    ocupateTIM.set(ocupateTIM.get() + 1);
                } else {
                    ocupateTIIP.set(ocupateTIIP.get() + 1);
                }
            }
        });
        paturiOcupateTxtFld.setText(ocupate.toString());

        TICtxt.setText(ocupateTIC.toString());
        TIMtxt.setText(ocupateTIM.toString());
        TIIPtxt.setText(ocupateTIIP.toString());
    }


    @Override
    public void update(PatEvent event) {
        initialize();
    }
}

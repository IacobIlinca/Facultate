package com.example.spital.service;

import com.example.spital.domain.Pacient;
import com.example.spital.domain.Pat;
import com.example.spital.domain.Type;
import com.example.spital.repository.Repository;
import com.example.spital.repository.file.PacientRepo;
import com.example.spital.repository.file.PatRepo;
import com.example.spital.utils.ConcreteObservable;
import com.example.spital.utils.Observer;
import com.example.spital.utils.events.ChangeEvent;
import com.example.spital.utils.events.PatEvent;

public class Service extends ConcreteObservable<PatEvent> {
    private final PatRepo paturiRepository;
    private final PacientRepo pacientiRepository;
    private static Service service = null;

    private Service(PatRepo paturiRepository, PacientRepo pacientiRepository) {
        this.paturiRepository = paturiRepository;
        this.pacientiRepository = pacientiRepository;
    }
    public static Service getInstance(PatRepo paturiRepository, PacientRepo pacientiRepository){
        if (service == null){
            service = new Service(paturiRepository,pacientiRepository);
        }
        return service;
    }

    public Iterable<Pat> getAllBeds(){
        return paturiRepository.getAll();
    }

    public Iterable<Pacient> getAllPacient(){
        return pacientiRepository.getAll();
    }

    public void addObservers(Observer<PatEvent> observer){
        addObserver(observer);
    }
    public void interneazaPacient(Integer idPat, Integer idPacient){
        Pat pat = paturiRepository.findOne(idPat);
        paturiRepository.update(new Pat(idPat,pat.getTip(),pat.getVentilatie(),idPacient));
        pat.setPacientId(idPacient);
        this.notifyObservers(new PatEvent(ChangeEvent.UPDATE,pat));
    }
}


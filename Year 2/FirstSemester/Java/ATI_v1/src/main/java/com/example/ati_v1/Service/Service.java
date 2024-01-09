package com.example.ati_v1.Service;

import com.example.ati_v1.Domain.Pacient;
import com.example.ati_v1.Domain.Pat;
import com.example.ati_v1.Observer.Observable;
import com.example.ati_v1.Repository.DBPacientRepo;
import com.example.ati_v1.Repository.DBPatRepo;
import com.example.ati_v1.Repository.Repository;

import java.io.IOException;

public class Service extends Observable {
    private Repository<Pat, Long> repoPat;
    private Repository<Pacient, String> repoPacient;


    public Service(Repository<Pat, Long> repoPat, Repository<Pacient, String> repoPacient) {
        this.repoPat = repoPat;
        this.repoPacient = repoPacient;
    }

    public Iterable<Pat> getAllPaturi() {
        return repoPat.findAll();
    }

    public Iterable<Pacient> getAllPacienti() {
        return repoPacient.findAll();
    }

    public Pat updatePaturi(Pat pat) throws IOException {
        this.notification();
        return repoPat.update(pat);
    }


}

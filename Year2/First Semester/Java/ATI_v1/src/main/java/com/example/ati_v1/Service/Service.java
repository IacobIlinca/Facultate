package com.example.ati_v1.Service;

import com.example.ati_v1.Domain.Pacient;
import com.example.ati_v1.Domain.Pat;
import com.example.ati_v1.Observer.Observable;
import com.example.ati_v1.Repository.DBPacientRepo;
import com.example.ati_v1.Repository.DBPatRepo;
import com.example.ati_v1.Repository.Repository;

public class Service extends Observable {
    private static Service service = null;
    private Repository<Pat, Long> repoPat;
    private Repository<Pacient, String> repoPacient;


    public synchronized static Service getInstance(DBPatRepo repoPat, DBPacientRepo repoPacient) {
        if (service == null)
            service = new Service(repoPat, repoPacient);
        return service;
    }

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

    public Pat updatePaturi(Pat pat){
        this.notification();
        return repoPat.update(pat);
    }


}

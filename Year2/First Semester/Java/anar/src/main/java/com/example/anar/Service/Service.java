package com.example.anar.Service;

import com.example.anar.Domain.Localitate;
import com.example.anar.Domain.Rau;
import com.example.anar.Repository.DBLocalitateRepo;
import com.example.anar.Repository.DBRauRepo;
import com.example.anar.Repository.Repository;

public class Service {
    private static Service service = null;
    private Repository<Rau, String> repoRau;
    private Repository<Localitate, String> repoLocalitate;

    public synchronized static Service getInstance(DBRauRepo repoRau, DBLocalitateRepo repoLocalitate) {
        if (service == null)
            service = new Service(repoRau, repoLocalitate);
        return service;
    }

    public Service(Repository<Rau, String> repoRau, Repository<Localitate, String> repoLocalitate) {
        this.repoRau = repoRau;
        this.repoLocalitate = repoLocalitate;
    }

    public Iterable<Rau> getAllRauri() {
        return repoRau.findAll();
    }

    public Iterable<Localitate> getAllLocalitati() {
        return repoLocalitate.findAll();
    }

    public Rau updateRauuri(Rau rau){
        return repoRau.update(rau);
    }

}

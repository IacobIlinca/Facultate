package com.example.examenpractic.Service;

import com.example.examenpractic.Domain.Nevoi;
import com.example.examenpractic.Domain.Persoana;
import com.example.examenpractic.Repository.DBNevoiRepository;
import com.example.examenpractic.Repository.DBPersoanaRepository;
import com.example.examenpractic.Repository.Repository;

public class Service {
    private static Service service = null;
    private Repository<Persoana, Long> repoPersoana;
    private Repository<Nevoi, Long> repoNevoi;

    public synchronized static Service getInstance(DBPersoanaRepository repoPersoana, DBNevoiRepository repoNevoi) {
        if (service == null)
            service = new Service(repoPersoana, repoNevoi);
        return service;
    }

    public Service(Repository<Persoana, Long> repoPersoana, Repository<Nevoi, Long> repoNevoi) {
        this.repoPersoana = repoPersoana;
        this.repoNevoi = repoNevoi;
    }

    public Iterable<Persoana> getAllPersoane() {
        return repoPersoana.findAll();
    }

    public Iterable<Nevoi> getAllNevoi() {
        return repoNevoi.findAll();
    }
}

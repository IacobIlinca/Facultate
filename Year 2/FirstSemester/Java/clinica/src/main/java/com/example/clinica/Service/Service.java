package com.example.clinica.Service;

import com.example.clinica.Domain.Consultatie;
import com.example.clinica.Domain.Medic;
import com.example.clinica.Domain.Sectie;
import com.example.clinica.Repository.DBConsultatieRepo;
import com.example.clinica.Repository.DBMedicRepo;
import com.example.clinica.Repository.DBSectieRepo;
import com.example.clinica.Repository.Repository;

public class Service {
    private static Service service = null;
    private Repository<Sectie, Long> repoSectie;
    private Repository<Medic, Long> repoMedic;
    private Repository<Consultatie, Long> repoConsultatie;

    public synchronized static Service getInstance(DBSectieRepo repoSectie, DBMedicRepo repoMedic, DBConsultatieRepo repoConsultatie) {
        if (service == null)
            service = new Service(repoSectie, repoMedic, repoConsultatie);
        return service;
    }

    public Service(Repository<Sectie, Long> repoSectie, Repository<Medic, Long> repoMedic, Repository<Consultatie, Long> repoConsultatie) {
        this.repoSectie = repoSectie;
        this.repoMedic = repoMedic;
        this.repoConsultatie = repoConsultatie;
    }

    public Iterable<Sectie> getAllSectii() {
        return repoSectie.findAll();
    }

    public Iterable<Medic> getAllMedici() {
        return repoMedic.findAll();
    }

    public Iterable<Consultatie> getAllConsultatii() {
        return repoConsultatie.findAll();
    }
}

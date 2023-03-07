package com.example.examenpractic.Domain;

import java.time.LocalDateTime;

public class NevoiDTO {
    private Long Id;
    private String titlu;
    private String descriere;
    private LocalDateTime deadline;
    private String  omInNevoie;
    private String  omSalvator;
    private String status;

    public NevoiDTO(Long id, String titlu, String descriere, LocalDateTime deadline, String omInNevoie, String omSalvator, String status) {
        Id = id;
        this.titlu = titlu;
        this.descriere = descriere;
        this.deadline = deadline;
        this.omInNevoie = omInNevoie;
        this.omSalvator = omSalvator;
        this.status = status;
    }

    public Long getId() {
        return Id;
    }

    public void setId(Long id) {
        Id = id;
    }

    public String getTitlu() {
        return titlu;
    }

    public void setTitlu(String titlu) {
        this.titlu = titlu;
    }

    public String getDescriere() {
        return descriere;
    }

    public void setDescriere(String descriere) {
        this.descriere = descriere;
    }

    public LocalDateTime getDeadline() {
        return deadline;
    }

    public void setDeadline(LocalDateTime deadline) {
        this.deadline = deadline;
    }

    public String getOmInNevoie() {
        return omInNevoie;
    }

    public void setOmInNevoie(String omInNevoie) {
        this.omInNevoie = omInNevoie;
    }

    public String getOmSalvator() {
        return omSalvator;
    }

    public void setOmSalvator(String omSalvator) {
        this.omSalvator = omSalvator;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
}

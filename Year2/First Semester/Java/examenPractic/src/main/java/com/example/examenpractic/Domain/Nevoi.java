package com.example.examenpractic.Domain;

import java.time.LocalDateTime;
import java.util.Objects;

public class Nevoi extends Entity<Long> {

    private String titlu;
    private String descriere;
    private LocalDateTime deadline;
    private Long omInNevoie;
    private Long omSalvator;
    private String status;

    public Nevoi(Long aLong, String titlu, String descriere, LocalDateTime deadline, Long omInNevoie) {
        super(aLong);
        this.titlu = titlu;
        this.descriere = descriere;
        this.deadline = deadline;
        this.omInNevoie = omInNevoie;
        this.omSalvator = null;
        this.status = "Caut erou!";
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

    public Long getOmInNevoie() {
        return omInNevoie;
    }

    public void setOmInNevoie(Long omInNevoie) {
        this.omInNevoie = omInNevoie;
    }

    public Long getOmSalvator() {
        return omSalvator;
    }

    public void setOmSalvator(Long omSalvator) {
        this.omSalvator = omSalvator;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    @Override
    public String toString() {
        return "Nevoi{" +
                "titlu='" + titlu + '\'' +
                ", descriere='" + descriere + '\'' +
                ", deadline=" + deadline +
                ", omInNevoie=" + omInNevoie +
                ", omSalvator=" + omSalvator +
                ", status='" + status + '\'' +
                '}';
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        if (!super.equals(o)) return false;
        Nevoi nevoi = (Nevoi) o;
        return Objects.equals(titlu, nevoi.titlu) && Objects.equals(descriere, nevoi.descriere) && Objects.equals(deadline, nevoi.deadline) && Objects.equals(omInNevoie, nevoi.omInNevoie) && Objects.equals(omSalvator, nevoi.omSalvator) && Objects.equals(status, nevoi.status);
    }

    @Override
    public int hashCode() {
        return Objects.hash(super.hashCode(), titlu, descriere, deadline, omInNevoie, omSalvator, status);
    }
}

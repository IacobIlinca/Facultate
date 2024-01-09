package com.example.spital.domain;

public class Pacient extends Entity<Integer>{
    private Integer varsta;
    private String prematur;
    private String diagnostic;
    private Integer gravitate;

    public Pacient(Integer integer, Integer varsta, String prematur, String diagnostic, Integer gravitate) {
        super(integer);
        this.varsta = varsta;
        this.prematur = prematur;
        this.diagnostic = diagnostic;
        this.gravitate = gravitate;
    }

    @Override
    public String toString() {
        return "Pacient " +super.getId() +
                ", diagnostic='" + diagnostic + '\'' +
                ", gravitate=" + gravitate ;

    }

    public Integer getVarsta() {
        return varsta;
    }

    public void setVarsta(Integer varsta) {
        this.varsta = varsta;
    }

    public String getPrematur() {
        return prematur;
    }

    public void setPrematur(String prematur) {
        this.prematur = prematur;
    }

    public String getDiagnostic() {
        return diagnostic;
    }

    public void setDiagnostic(String diagnostic) {
        this.diagnostic = diagnostic;
    }

    public Integer getGravitate() {
        return gravitate;
    }

    public void setGravitate(Integer gravitate) {
        this.gravitate = gravitate;
    }
}

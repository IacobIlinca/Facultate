package com.example.ati_v1.Domain;

import java.util.Objects;

public class Pacient extends Entity<String>{
    private Integer varsta;
    private Ventilatie prematur;
    private String diagnosticPrincipal;
    private Integer gravitate;

    public Pacient(String s, Integer varsta, Ventilatie prematur, String diagnosticPrincipal, Integer gravitate) {
        super(s);
        this.varsta = varsta;
        this.prematur = prematur;
        this.diagnosticPrincipal = diagnosticPrincipal;
        this.gravitate = gravitate;
    }

    public Integer getVarsta() {
        return varsta;
    }

    public void setVarsta(Integer varsta) {
        this.varsta = varsta;
    }

    public Ventilatie getPrematur() {
        return prematur;
    }

    public void setPrematur(Ventilatie prematur) {
        this.prematur = prematur;
    }

    public String getDiagnosticPrincipal() {
        return diagnosticPrincipal;
    }

    public void setDiagnosticPrincipal(String diagnosticPrincipal) {
        this.diagnosticPrincipal = diagnosticPrincipal;
    }

    public Integer getGravitate() {
        return gravitate;
    }

    public void setGravitate(Integer gravitate) {
        this.gravitate = gravitate;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        if (!super.equals(o)) return false;
        Pacient pacient = (Pacient) o;
        return varsta.equals(pacient.varsta) && prematur == pacient.prematur && diagnosticPrincipal.equals(pacient.diagnosticPrincipal) && gravitate.equals(pacient.gravitate);
    }

    @Override
    public int hashCode() {
        return Objects.hash(super.hashCode(), varsta, prematur, diagnosticPrincipal, gravitate);
    }

    @Override
    public String toString() {
        return "Pacient{" +
                "varsta=" + varsta +
                ", prematur=" + prematur +
                ", diagnosticPrincipal='" + diagnosticPrincipal + '\'' +
                ", gravitate=" + gravitate +
                '}';
    }
}

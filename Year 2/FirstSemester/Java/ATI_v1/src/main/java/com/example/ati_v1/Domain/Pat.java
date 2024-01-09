package com.example.ati_v1.Domain;

import java.util.Objects;

public class Pat extends Entity<Long>{
    private Tip tip;
    private Ventilatie ventilatie;
    private String cnpPacient ;

    public Pat(Long aLong, Tip tip, Ventilatie ventilatie) {
        super(aLong);
        this.tip = tip;
        this.ventilatie = ventilatie;
        this.cnpPacient = null;
    }

    public Tip getTip() {
        return tip;
    }

    public void setTip(Tip tip) {
        this.tip = tip;
    }

    public Ventilatie getVentilatie() {
        return ventilatie;
    }

    public void setVentilatie(Ventilatie ventilatie) {
        this.ventilatie = ventilatie;
    }

    public String getCnpPacient() {
        return cnpPacient;
    }

    public void setCnpPacient(String cnpPacient) {
        this.cnpPacient = cnpPacient;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        if (!super.equals(o)) return false;
        Pat pat = (Pat) o;
        return tip == pat.tip && ventilatie == pat.ventilatie && Objects.equals(cnpPacient, pat.cnpPacient);
    }

    @Override
    public int hashCode() {
        return Objects.hash(super.hashCode(), tip, ventilatie, cnpPacient);
    }

    @Override
    public String toString() {
        return "Pat{" +
                "tip=" + tip +
                ", ventilatie=" + ventilatie +
                ", cnpPacient='" + cnpPacient + '\'' +
                '}';
    }
}

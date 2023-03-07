package com.example.anar.Domain;

import java.util.Objects;

public class Localitate extends Entity<String>{
    private String rau;
    private Integer cotaMinimaDeRisc;
    private Integer cotaMaximaAdmisa;

    public Localitate(String s, String rau, Integer cotaMinimaDeRisc, Integer cotaMaximaAdmisa) {
        super(s);
        this.rau = rau;
        this.cotaMinimaDeRisc = cotaMinimaDeRisc;
        this.cotaMaximaAdmisa = cotaMaximaAdmisa;
    }

    public String getRau() {
        return rau;
    }

    public void setRau(String rau) {
        this.rau = rau;
    }

    public Integer getCotaMinimaDeRisc() {
        return cotaMinimaDeRisc;
    }

    public void setCotaMinimaDeRisc(Integer cotaMinimaDeRisc) {
        this.cotaMinimaDeRisc = cotaMinimaDeRisc;
    }

    public Integer getCotaMaximaAdmisa() {
        return cotaMaximaAdmisa;
    }

    public void setCotaMaximaAdmisa(Integer cotaMaximaAdmisa) {
        this.cotaMaximaAdmisa = cotaMaximaAdmisa;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        if (!super.equals(o)) return false;
        Localitate that = (Localitate) o;
        return rau.equals(that.rau) && cotaMinimaDeRisc.equals(that.cotaMinimaDeRisc) && cotaMaximaAdmisa.equals(that.cotaMaximaAdmisa);
    }

    @Override
    public int hashCode() {
        return Objects.hash(super.hashCode(), rau, cotaMinimaDeRisc, cotaMaximaAdmisa);
    }

    @Override
    public String toString() {
        return "Localitate{" +
                "rau='" + rau + '\'' +
                ", cotaMinimaDeRisc=" + cotaMinimaDeRisc +
                ", cotaMaximaAdmisa=" + cotaMaximaAdmisa +
                '}';
    }
}

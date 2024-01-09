package com.example.clinica.Domain;

import java.util.Objects;

public class Sectie extends Entity<Long>{
    private String nume;
    private Long idSefDeSectie;
    private Float pretPerConsultatie;
    private Integer durataMaximaConsultatie;

    public Sectie(Long aLong, String nume, Long idSefDeSectie, Float pretPerConsultatie, Integer durataMaximaConsultatie) {
        super(aLong);
        this.nume = nume;
        this.idSefDeSectie = idSefDeSectie;
        this.pretPerConsultatie = pretPerConsultatie;
        this.durataMaximaConsultatie = durataMaximaConsultatie;
    }

    public String getNume() {
        return nume;
    }

    public void setNume(String nume) {
        this.nume = nume;
    }

    public Long getIdSefDeSectie() {
        return idSefDeSectie;
    }

    public void setIdSefDeSectie(Long idSefDeSectie) {
        this.idSefDeSectie = idSefDeSectie;
    }

    public Float getPretPerConsultatie() {
        return pretPerConsultatie;
    }

    public void setPretPerConsultatie(Float pretPerConsultatie) {
        this.pretPerConsultatie = pretPerConsultatie;
    }

    public Integer getDurataMaximaConsultatie() {
        return durataMaximaConsultatie;
    }

    public void setDurataMaximaConsultatie(Integer durataMaximaConsultatie) {
        this.durataMaximaConsultatie = durataMaximaConsultatie;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        if (!super.equals(o)) return false;
        Sectie sectie = (Sectie) o;
        return nume.equals(sectie.nume) && idSefDeSectie.equals(sectie.idSefDeSectie) && pretPerConsultatie.equals(sectie.pretPerConsultatie) && durataMaximaConsultatie.equals(sectie.durataMaximaConsultatie);
    }

    @Override
    public int hashCode() {
        return Objects.hash(super.hashCode(), nume, idSefDeSectie, pretPerConsultatie, durataMaximaConsultatie);
    }

    @Override
    public String toString() {
        return "Sectie{" +
                "nume='" + nume + '\'' +
                ", idSefDeSectie=" + idSefDeSectie +
                ", pretPerConsultatie=" + pretPerConsultatie +
                ", durataMaximaConsultatie=" + durataMaximaConsultatie +
                '}';
    }
}

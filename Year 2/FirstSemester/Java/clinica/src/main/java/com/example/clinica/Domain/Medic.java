package com.example.clinica.Domain;

import java.util.Objects;

public class Medic extends Entity<Long>{
    private Long idSectie;
    private String nume;
    private Integer vechime;
    private Tip rezident;

    public Medic(Long aLong, Long idSectie, String nume, Integer vechime, Tip rezident) {
        super(aLong);
        this.idSectie = idSectie;
        this.nume = nume;
        this.vechime = vechime;
        this.rezident = rezident;
    }

    public Long getIdSectie() {
        return idSectie;
    }

    public void setIdSectie(Long idSectie) {
        this.idSectie = idSectie;
    }

    public String getNume() {
        return nume;
    }

    public void setNume(String nume) {
        this.nume = nume;
    }

    public Integer getVechime() {
        return vechime;
    }

    public void setVechime(Integer vechime) {
        this.vechime = vechime;
    }

    public Tip getRezident() {
        return rezident;
    }

    public void setRezident(Tip rezident) {
        this.rezident = rezident;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        if (!super.equals(o)) return false;
        Medic medic = (Medic) o;
        return idSectie.equals(medic.idSectie) && nume.equals(medic.nume) && vechime.equals(medic.vechime) && rezident == medic.rezident;
    }

    @Override
    public int hashCode() {
        return Objects.hash(super.hashCode(), idSectie, nume, vechime, rezident);
    }

    @Override
    public String toString() {
        return "Medic{" +
                "idSectie=" + idSectie +
                ", nume='" + nume + '\'' +
                ", vechime=" + vechime +
                ", rezident=" + rezident +
                '}';
    }
}

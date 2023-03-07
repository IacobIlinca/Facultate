package com.example.clinica.Domain;

import java.sql.Time;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.LocalTime;
import java.util.Date;
import java.util.Objects;

public class Consultatie extends Entity<Long>{
    private Long idMedic;
    private Long CNPPacient;
    private String numePacient;
    private LocalDate data;
    private LocalTime ora;

    public Consultatie(Long aLong, Long idMedic, Long CNPPacient, String numePacient, LocalDate data, LocalTime ora) {
        super(aLong);
        this.idMedic = idMedic;
        this.CNPPacient = CNPPacient;
        this.numePacient = numePacient;
        this.data = data;
        this.ora = ora;
    }

    public Long getIdMedic() {
        return idMedic;
    }

    public void setIdMedic(Long idMedic) {
        this.idMedic = idMedic;
    }

    public Long getCNPPacient() {
        return CNPPacient;
    }

    public void setCNPPacient(Long CNPPacient) {
        this.CNPPacient = CNPPacient;
    }

    public String getNumePacient() {
        return numePacient;
    }

    public void setNumePacient(String numePacient) {
        this.numePacient = numePacient;
    }

    public LocalDate getData() {
        return data;
    }

    public void setData(LocalDate data) {
        this.data = data;
    }

    public LocalTime getOra() {
        return ora;
    }

    public void setOra(LocalTime ora) {
        this.ora = ora;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        if (!super.equals(o)) return false;
        Consultatie that = (Consultatie) o;
        return idMedic.equals(that.idMedic) && CNPPacient.equals(that.CNPPacient) && numePacient.equals(that.numePacient) && data.equals(that.data) && ora.equals(that.ora);
    }

    @Override
    public int hashCode() {
        return Objects.hash(super.hashCode(), idMedic, CNPPacient, numePacient, data, ora);
    }

    @Override
    public String toString() {
        return "Consultatie{" +
                "idMedic=" + idMedic +
                ", CNPPacient=" + CNPPacient +
                ", numePacient='" + numePacient + '\'' +
                ", data=" + data +
                ", ora=" + ora +
                '}';
    }
}

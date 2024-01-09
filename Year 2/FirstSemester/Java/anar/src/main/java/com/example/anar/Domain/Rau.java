package com.example.anar.Domain;

import java.util.Objects;

public class Rau extends Entity<String>{
    private Integer cotaMedie;

    public Rau(String s, Integer cotaMedie) {
        super(s);
        this.cotaMedie = cotaMedie;
    }

    public Integer getCotaMedie() {
        return cotaMedie;
    }

    public void setCotaMedie(Integer cotaMedie) {
        this.cotaMedie = cotaMedie;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        if (!super.equals(o)) return false;
        Rau rau = (Rau) o;
        return cotaMedie.equals(rau.cotaMedie);
    }

    @Override
    public int hashCode() {
        return Objects.hash(super.hashCode(), cotaMedie);
    }

    @Override
    public String toString() {
        return "Rau{" +
                "cotaMedie=" + cotaMedie +
                '}';
    }
}

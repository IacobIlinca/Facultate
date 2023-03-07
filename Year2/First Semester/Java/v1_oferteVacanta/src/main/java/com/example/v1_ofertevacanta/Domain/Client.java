package com.example.v1_ofertevacanta.Domain;

import java.util.Objects;

public class Client extends  Entity<Long>{
    private String name;
    private Integer fidelityGrade;
    private Integer varsta;
    private Hobby hobby;

    public Client(Long aLong, String name, Integer fidelityGrade, Integer varsta, Hobby hobby) {
        super(aLong);
        this.name = name;
        this.fidelityGrade = fidelityGrade;
        this.varsta = varsta;
        this.hobby = hobby;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Integer getFidelityGrade() {
        return fidelityGrade;
    }

    public void setFidelityGrade(Integer fidelityGrade) {
        this.fidelityGrade = fidelityGrade;
    }

    public Integer getVarsta() {
        return varsta;
    }

    public void setVarsta(Integer varsta) {
        this.varsta = varsta;
    }

    public Hobby getHobby() {
        return hobby;
    }

    public void setHobby(Hobby hobby) {
        this.hobby = hobby;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        if (!super.equals(o)) return false;
        Client client = (Client) o;
        return name.equals(client.name) && fidelityGrade.equals(client.fidelityGrade) && varsta.equals(client.varsta) && hobby == client.hobby;
    }

    @Override
    public int hashCode() {
        return Objects.hash(super.hashCode(), name, fidelityGrade, varsta, hobby);
    }

    @Override
    public String toString() {
        return "Client{" +
                "name='" + name + '\'' +
                ", fidelityGrade=" + fidelityGrade +
                ", varsta=" + varsta +
                ", hobby=" + hobby +
                '}';
    }
}

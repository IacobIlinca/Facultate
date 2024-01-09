package com.example.zboruri.Domain;

import java.util.Objects;

public class Client extends Entity<String>{
    private String nume;

    public Client(String s, String nume) {
        super(s);
        this.nume = nume;
    }

    public String getNume() {
        return nume;
    }

    public void setNume(String nume) {
        this.nume = nume;
    }



    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        if (!super.equals(o)) return false;
        Client client = (Client) o;
        return nume.equals(client.nume) ;
    }

    @Override
    public int hashCode() {
        return Objects.hash(super.hashCode(), nume);
    }

    @Override
    public String toString() {
        return "Client{" +
                "nume='" + nume + '\'' +
                '}';
    }
}

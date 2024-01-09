package com.example.zboruri.Domain;

import java.time.LocalDateTime;
import java.util.Objects;

public class Ticket extends Entity<Long>{

    private String username;
    private Long flightId;
    private LocalDateTime purchaseDate;

    public Ticket(Long aLong, String username, Long flightId, LocalDateTime purchaseDate) {
        super(aLong);
        this.username = username;
        this.flightId = flightId;
        this.purchaseDate = purchaseDate;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public Long getFlightId() {
        return flightId;
    }

    public void setFlightId(Long flightId) {
        this.flightId = flightId;
    }

    public LocalDateTime getPurchaseDate() {
        return purchaseDate;
    }

    public void setPurchaseDate(LocalDateTime purchaseDate) {
        this.purchaseDate = purchaseDate;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        if (!super.equals(o)) return false;
        Ticket ticket = (Ticket) o;
        return username.equals(ticket.username) && flightId.equals(ticket.flightId) && purchaseDate.equals(ticket.purchaseDate);
    }

    @Override
    public int hashCode() {
        return Objects.hash(super.hashCode(), username, flightId, purchaseDate);
    }

    @Override
    public String toString() {
        return "Ticket{" +
                "username='" + username + '\'' +
                ", flightId=" + flightId +
                ", purchaseDate=" + purchaseDate +
                '}';
    }
}

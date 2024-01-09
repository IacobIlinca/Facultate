package com.example.v1_ofertevacanta.Domain;

import java.time.LocalDateTime;
import java.util.Objects;

public class Reservation extends Entity<Double>{
    private Long clientId;
    private Double hotelId;
    private LocalDateTime startDate = LocalDateTime.now();
    private Integer noNights;

    public Reservation(Double aDouble, Long clientId, Double hotelId,Integer noNights) {
        super(aDouble);
        this.clientId = clientId;
        this.hotelId = hotelId;
        this.startDate = LocalDateTime.now();
        this.noNights = noNights;
    }

    public Long getClientId() {
        return clientId;
    }

    public void setClientId(Long clientId) {
        this.clientId = clientId;
    }

    public Double getHotelId() {
        return hotelId;
    }

    public void setHotelId(Double hotelId) {
        this.hotelId = hotelId;
    }

    public LocalDateTime getStartDate() {
        return startDate;
    }

    public void setStartDate(LocalDateTime startDate) {
        this.startDate = startDate;
    }

    public Integer getNoNights() {
        return noNights;
    }

    public void setNoNights(Integer noNights) {
        this.noNights = noNights;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        if (!super.equals(o)) return false;
        Reservation that = (Reservation) o;
        return clientId.equals(that.clientId) && hotelId.equals(that.hotelId) && startDate.equals(that.startDate) && noNights.equals(that.noNights);
    }

    @Override
    public int hashCode() {
        return Objects.hash(super.hashCode(), clientId, hotelId, startDate, noNights);
    }

    @Override
    public String toString() {
        return "Reservation{" +
                "clientId=" + clientId +
                ", hotelId=" + hotelId +
                ", startDate=" + startDate +
                ", noNights=" + noNights +
                '}';
    }
}

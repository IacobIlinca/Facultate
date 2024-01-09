package com.example.v1_ofertevacanta.Domain;

import java.util.Objects;

public class Hotel extends Entity<Double> {
    private Double locationId;
    private String hotelName;
    private Integer noRooms;
    private Double pricePerNight;
    private Type type;

    public Hotel(Double aDouble,Double locationId, String hotelName, Integer noRooms, Double pricePerNight, Type type) {
        super(aDouble);
        this.locationId = locationId;
        this.hotelName = hotelName;
        this.noRooms = noRooms;
        this.pricePerNight = pricePerNight;
        this.type = type;
    }

    public Double getLocationId() {
        return locationId;
    }

    public void setLocationId(Double locationId) {
        this.locationId = locationId;
    }

    public String getHotelName() {
        return hotelName;
    }

    public void setHotelName(String hotelName) {
        this.hotelName = hotelName;
    }

    public Integer getNoRooms() {
        return noRooms;
    }

    public void setNoRooms(Integer noRooms) {
        this.noRooms = noRooms;
    }

    public Double getPricePerNight() {
        return pricePerNight;
    }

    public void setPricePerNight(Double pricePerNight) {
        this.pricePerNight = pricePerNight;
    }

    public Type getType() {
        return type;
    }

    public void setType(Type type) {
        this.type = type;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        if (!super.equals(o)) return false;
        Hotel hotel = (Hotel) o;
        return locationId.equals(hotel.locationId) && hotelName.equals(hotel.hotelName) && noRooms.equals(hotel.noRooms) && pricePerNight.equals(hotel.pricePerNight) && type == hotel.type;
    }

    @Override
    public int hashCode() {
        return Objects.hash(super.hashCode(), locationId, hotelName, noRooms, pricePerNight, type);
    }

    @Override
    public String toString() {
        return "Hotel{" +
                "locationId=" + locationId +
                ", hotelName='" + hotelName + '\'' +
                ", noRooms=" + noRooms +
                ", pricePerNight=" + pricePerNight +
                ", type=" + type +
                '}';
    }
}

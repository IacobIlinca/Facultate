package com.example.v1_ofertevacanta.Domain;

import java.util.Objects;

public class Location extends Entity<Double>{

    private String locationName;


    public Location(Double aDouble,String locationName) {
        super(aDouble);
        this.locationName = locationName;
    }



    public String getLocationName() {
        return locationName;
    }

    public void setLocationName(String locationName) {
        this.locationName = locationName;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        if (!super.equals(o)) return false;
        Location location = (Location) o;
        return locationName.equals(location.locationName);
    }

    @Override
    public int hashCode() {
        return Objects.hash(super.hashCode(), locationName);
    }

    @Override
    public String toString() {
        return "Location{" +
                "locationName='" + locationName + '\'' +
                '}';
    }
}

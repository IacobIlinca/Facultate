package com.example.zboruri.Domain;

import java.time.LocalDateTime;
import java.util.Objects;

public class Zbor extends Entity<Long>{
    private String localitateStart;
    private String localitateEnd;
    private LocalDateTime departureTime;
    private LocalDateTime landingTime;
    private Integer seats;

    public Zbor(Long aLong, String localitateStart, String localitateEnd, LocalDateTime departureTime, LocalDateTime landingTime, Integer seats) {
        super(aLong);
        this.localitateStart = localitateStart;
        this.localitateEnd = localitateEnd;
        this.departureTime = departureTime;
        this.landingTime = landingTime;
        this.seats = seats;
    }

    public String getLocalitateStart() {
        return localitateStart;
    }

    public void setLocalitateStart(String localitateStart) {
        this.localitateStart = localitateStart;
    }

    public String getLocalitateEnd() {
        return localitateEnd;
    }

    public void setLocalitateEnd(String localitateEnd) {
        this.localitateEnd = localitateEnd;
    }

    public LocalDateTime getDepartureTime() {
        return departureTime;
    }

    public void setDepartureTime(LocalDateTime departureTime) {
        this.departureTime = departureTime;
    }

    public LocalDateTime getLandingTime() {
        return landingTime;
    }

    public void setLandingTime(LocalDateTime landingTime) {
        this.landingTime = landingTime;
    }

    public Integer getSeats() {
        return seats;
    }

    public void setSeats(Integer seats) {
        this.seats = seats;
    }

    @Override
    public String toString() {
        return "Zbor{" +
                "localitateStart='" + localitateStart + '\'' +
                ", localitateEnd='" + localitateEnd + '\'' +
                ", departureTime=" + departureTime +
                ", landingTime=" + landingTime +
                ", seats=" + seats +
                '}';
    }
}

package com.example.v1_ofertevacanta.Domain;

import java.time.LocalDate;
import java.util.Date;
import java.util.Objects;

public class SpecialOffer extends Entity<Double>{
    private Double hotelId;
    private LocalDate startDate;
    private LocalDate endDate;
    private Integer percents;

    public SpecialOffer(Double aDouble, Double hotelId, LocalDate startDate, LocalDate endDate, Integer percents) {
        super(aDouble);
        this.hotelId = hotelId;
        this.startDate = startDate;
        this.endDate = endDate;
        this.percents = percents;
    }

    public Double getHotelId() {
        return hotelId;
    }

    public void setHotelId(Double hotelId) {
        this.hotelId = hotelId;
    }

    public LocalDate getStartDate() {
        return startDate;
    }

    public void setStartDate(LocalDate startDate) {
        this.startDate = startDate;
    }

    public LocalDate getEndDate() {
        return endDate;
    }

    public void setEndDate(LocalDate endDate) {
        this.endDate = endDate;
    }

    public Integer getPercents() {
        return percents;
    }

    public void setPercents(Integer percents) {
        this.percents = percents;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        if (!super.equals(o)) return false;
        SpecialOffer that = (SpecialOffer) o;
        return hotelId.equals(that.hotelId) && startDate.equals(that.startDate) && endDate.equals(that.endDate) && percents.equals(that.percents);
    }

    @Override
    public int hashCode() {
        return Objects.hash(super.hashCode(), hotelId, startDate, endDate, percents);
    }

    @Override
    public String toString() {
        return "SpecialOffer{" +
                "hotelId=" + hotelId +
                ", startDate=" + startDate +
                ", endDate=" + endDate +
                ", percents=" + percents +
                '}';
    }
}

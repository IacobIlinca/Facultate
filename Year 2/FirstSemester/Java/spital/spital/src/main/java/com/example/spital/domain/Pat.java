package com.example.spital.domain;

public class Pat extends Entity<Integer> {
    private Type tip;
    private String ventilatie;
    private Integer pacientId;

    public Pat(Integer integer, Type tip, String ventilatie, Integer pacientId) {
        super(integer);
        this.tip = tip;
        this.ventilatie = ventilatie;
        this.pacientId = pacientId;
    }

    @Override
    public String toString() {
        return "Pat{" +
                "tip=" + tip +
                ", ventilatie='" + ventilatie + '\'' +
                ", pacientId=" + pacientId +
                '}';
    }

    public Type getTip() {
        return tip;
    }

    public void setTip(Type tip) {
        this.tip = tip;
    }

    public String getVentilatie() {
        return ventilatie;
    }

    public void setVentilatie(String ventilatie) {
        this.ventilatie = ventilatie;
    }

    public Integer getPacientId() {
        return pacientId;
    }

    public void setPacientId(Integer pacientId) {
        this.pacientId = pacientId;
    }
}

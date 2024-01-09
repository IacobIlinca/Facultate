package com.example.v1_ofertevacanta.Repository;

import com.example.v1_ofertevacanta.Domain.Hotel;
import com.example.v1_ofertevacanta.Domain.Reservation;
import com.example.v1_ofertevacanta.Domain.SpecialOffer;
import com.example.v1_ofertevacanta.Domain.Type;

import java.sql.*;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;

public class DBReservationRepository implements Repository<Reservation, Double> {
    private String url;
    private String username;
    private String password;

    public DBReservationRepository(String url, String username, String password) {
        this.url = url;
        this.username = username;
        this.password = password;
    }

    @Override
    public Reservation save(Reservation entity) {
        String query = "INSERT INTO reservation(reservation_id, client_id, hotel_id,start_date,no_nights) VALUES(?, ?, ?,?,?)";
        try (Connection connection = DriverManager.getConnection(this.url, this.username, this.password);
             PreparedStatement statement = connection.prepareStatement(query)
        ) {
            statement.setDouble(1, entity.getId());
            statement.setLong(2, entity.getClientId());
            statement.setDouble(3, entity.getHotelId());
            //!!!!!
            statement.setTimestamp(4, Timestamp.valueOf(LocalDateTime.now()));
            statement.setInt(5, entity.getNoNights());
            statement.executeUpdate();

        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
        return entity;
    }

    @Override
    public Reservation delete(Double aDouble) {
        return null;
    }

    @Override
    public Reservation findOne(Double aDouble) {
        return null;
    }

    @Override
    public Reservation update(Reservation entity) {
        return null;
    }

    @Override
    public Iterable<Reservation> findAll() {
        return null;
    }

    public Integer countReservations() {
        List<Reservation> reservations = new ArrayList<>();
        Integer cnt = 0;
        String query = "SELECT * from reservation";
        try (Connection connection = DriverManager.getConnection(this.url, this.username, this.password);
             PreparedStatement statement = connection.prepareStatement(query);
             ResultSet resultSet = statement.executeQuery()
        ) {
            while (resultSet.next()) {
                cnt ++;
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }

        return cnt;
    }

}
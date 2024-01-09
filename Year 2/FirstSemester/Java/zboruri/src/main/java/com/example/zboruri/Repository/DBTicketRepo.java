package com.example.zboruri.Repository;

import com.example.zboruri.Domain.Ticket;

import java.sql.*;
import java.time.LocalDateTime;

public class DBTicketRepo implements Repository<Ticket, Long> {
    private String url;
    private String username;
    private String password;

    public DBTicketRepo(String url, String username, String password) {
        this.url = url;
        this.username = username;
        this.password = password;
    }

    @Override
    public Ticket save(Ticket entity) {
        String query = "INSERT INTO ticket(ticket_id, username, flight_id,purchase_time) VALUES(?, ?, ?,?)";
        try (Connection connection = DriverManager.getConnection(this.url, this.username, this.password);
             PreparedStatement statement = connection.prepareStatement(query)
        ) {
            statement.setLong(1, entity.getId());
            statement.setString(2, entity.getUsername());
            statement.setLong(3, entity.getFlightId());
            //!!!!!
            statement.setTimestamp(4, Timestamp.valueOf(entity.getPurchaseDate()));
            statement.executeUpdate();

        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
        return entity;
    }

    @Override
    public Ticket delete(Long aLong) {
        return null;
    }

    @Override
    public Ticket findOne(Long aLong) {
        return null;
    }

    @Override
    public Ticket update(Ticket entity) {
        return null;
    }

    @Override
    public Iterable<Ticket> findAll() {
        return null;
    }
}

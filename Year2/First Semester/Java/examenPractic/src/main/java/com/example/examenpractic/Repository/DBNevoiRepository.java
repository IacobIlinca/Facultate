package com.example.examenpractic.Repository;

import com.example.examenpractic.Domain.Nevoi;

import java.sql.*;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;

public class DBNevoiRepository implements Repository<Nevoi,Long> {
    private String url;
    private String username;
    private String password;

    public DBNevoiRepository(String url, String username, String password) {
        this.url = url;
        this.username = username;
        this.password = password;
    }

    @Override
    public Nevoi save(Nevoi entity) {
        String query = "INSERT INTO nevoi(id, titlu, descriere,deadline,om_in_nevoie,om_salvator,status) VALUES(?, ?,?,?,?,?,?)";
        try (Connection connection = DriverManager.getConnection(this.url, this.username, this.password);
             PreparedStatement statement = connection.prepareStatement(query)
        ) {
            statement.setLong(1, entity.getId());
            statement.setString(2, entity.getTitlu());
            statement.setString(3, entity.getDescriere());
            statement.setTimestamp(4, Timestamp.valueOf(entity.getDeadline()));
            statement.setLong(5, entity.getOmInNevoie());

            statement.setNull(6, Types.INTEGER);
            statement.setString(7, entity.getStatus());
            statement.executeUpdate();

        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
        return entity;
    }

    @Override
    public Nevoi delete(Long aLong) {
        return null;
    }

    @Override
    public Nevoi findOne(Long aLong) {
        return null;
    }

    @Override
    public Nevoi update(Nevoi entity) {
        String sql = "UPDATE nevoi SET om_salvator = ?, status = ? WHERE id = ?";
        try (Connection connection = DriverManager.getConnection(this.url, this.username, this.password);
             PreparedStatement statement = connection.prepareStatement(sql)) {

            statement.setLong(1, entity.getOmSalvator());
            statement.setString(2, entity.getStatus());
            statement.setLong(3, entity.getId());

            statement.executeUpdate();
        } catch (SQLException sqlException) {
            sqlException.printStackTrace();
        }

        return entity;
    }

    @Override
    public Iterable<Nevoi> findAll() {
        List<Nevoi> nevoi = new ArrayList<>();

        String query = "SELECT * from nevoi";
        try(Connection connection = DriverManager.getConnection(this.url, this.username, this.password);
            PreparedStatement statement = connection.prepareStatement(query);
            ResultSet resultSet = statement.executeQuery()
        ) {
            while (resultSet.next()) {
                Long id = resultSet.getLong("id");
                String titlu = resultSet.getString("titlu");
                String descriere = resultSet.getString("descriere");
                LocalDateTime deadline = resultSet.getTimestamp("deadline").toLocalDateTime();
                Long omInNevoie = resultSet.getLong("om_in_nevoie");
                Long omSalvator = resultSet.getLong("om_salvator");
                String status = resultSet.getString("status");

                Nevoi nevoie =new Nevoi(id,titlu,descriere,deadline,omInNevoie);
                nevoie.setStatus(status);
                nevoie.setOmSalvator(omSalvator);
                nevoi.add(nevoie);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }

        return nevoi;
    }
}

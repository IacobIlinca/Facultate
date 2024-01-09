package com.example.zboruri.Repository;

import com.example.zboruri.Domain.Zbor;

import java.sql.*;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;

public class DBZborRepo implements Repository<Zbor, Long> {
    private String url;
    private String username;
    private String password;

    public DBZborRepo(String url, String username, String password) {
        this.url = url;
        this.username = username;
        this.password = password;
    }

    @Override
    public Zbor save(Zbor entity) {
        return null;
    }

    @Override
    public Zbor delete(Long aLong) {
        return null;
    }

    @Override
    public Zbor findOne(Long aLong) {
        return null;
    }

    @Override
    public Zbor update(Zbor entity) {
        return null;
    }

    @Override
    public Iterable<Zbor> findAll() {
        List<Zbor> zboruti = new ArrayList<>();

        String query = "SELECT * from zboruri";
        try(Connection connection = DriverManager.getConnection(this.url, this.username, this.password);
            PreparedStatement statement = connection.prepareStatement(query);
            ResultSet resultSet = statement.executeQuery()
        ) {
            while (resultSet.next()) {
                Long id = resultSet.getLong("id");
                String localitateStart = resultSet.getString("from");
                String localitateEnd = resultSet.getString("to");
                LocalDateTime departure_time = resultSet.getTimestamp("departure_time").toLocalDateTime();
                LocalDateTime landing_time = resultSet.getTimestamp("landing_time").toLocalDateTime();
                Integer seats = resultSet.getInt("seats");
                Zbor zbor = new Zbor(id, localitateStart, localitateEnd, departure_time,landing_time, seats);
                zboruti.add(zbor);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }

        return zboruti;
    }
}

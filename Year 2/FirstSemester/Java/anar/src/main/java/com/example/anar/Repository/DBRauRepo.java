package com.example.anar.Repository;

import com.example.anar.Domain.Rau;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class DBRauRepo implements Repository<Rau, String> {
    private String url;
    private String username;
    private String password;

    public DBRauRepo(String url, String username, String password) {
        this.url = url;
        this.username = username;
        this.password = password;
    }

    @Override
    public Rau save(Rau entity) {
        return null;
    }

    @Override
    public Rau delete(String s) {
        return null;
    }

    @Override
    public Rau findOne(String s) {
        return null;
    }

    @Override
    public Rau update(Rau entity) {
        return null;
    }

    @Override
    public Iterable<Rau> findAll() {
        List<Rau> rauri = new ArrayList<>();

        String query = "SELECT * from rau";
        try (Connection connection = DriverManager.getConnection(this.url, this.username, this.password);
             PreparedStatement statement = connection.prepareStatement(query);
             ResultSet resultSet = statement.executeQuery()
        ) {
            while (resultSet.next()) {
                String nume = resultSet.getString("nume");
                int cotaMedie = resultSet.getInt("cota_medie");

                Rau rau = new Rau(nume, cotaMedie);
                rauri.add(rau);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }

        return rauri;
    }
}

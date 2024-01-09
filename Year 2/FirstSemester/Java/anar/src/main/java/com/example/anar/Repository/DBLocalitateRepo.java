package com.example.anar.Repository;

import com.example.anar.Domain.Localitate;
import com.example.anar.Domain.Rau;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class DBLocalitateRepo implements Repository<Localitate, String> {
    private String url;
    private String username;
    private String password;

    public DBLocalitateRepo(String url, String username, String password) {
        this.url = url;
        this.username = username;
        this.password = password;
    }

    @Override
    public Localitate save(Localitate entity) {
        return null;
    }

    @Override
    public Localitate delete(String s) {
        return null;
    }

    @Override
    public Localitate findOne(String s) {
        return null;
    }

    @Override
    public Localitate update(Localitate entity) {
        return null;
    }

    @Override
    public Iterable<Localitate> findAll() {
        List<Localitate> localitati = new ArrayList<>();

        String query = "SELECT * from localitate";
        try (Connection connection = DriverManager.getConnection(this.url, this.username, this.password);
             PreparedStatement statement = connection.prepareStatement(query);
             ResultSet resultSet = statement.executeQuery()
        ) {
            while (resultSet.next()) {
                String nume = resultSet.getString("nume");
                String rau = resultSet.getString("rau");
                int cotaMinima = resultSet.getInt("cota_minima_de_risc");
                int cotaMaxima = resultSet.getInt("cota_maxima_admisa");

                Localitate loc = new Localitate(nume, rau, cotaMinima, cotaMaxima);
                localitati.add(loc);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }

        return localitati;
    }
}

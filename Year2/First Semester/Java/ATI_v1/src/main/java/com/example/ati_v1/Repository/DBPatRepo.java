package com.example.ati_v1.Repository;

import com.example.ati_v1.Domain.Pat;
import com.example.ati_v1.Domain.Tip;
import com.example.ati_v1.Domain.Ventilatie;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class DBPatRepo implements Repository<Pat, Long> {
    private String url;
    private String username;
    private String password;

    public DBPatRepo(String url, String username, String password) {
        this.url = url;
        this.username = username;
        this.password = password;
    }

    @Override
    public Pat save(Pat entity) {
        return null;
    }

    @Override
    public Pat delete(Long aLong) {
        return null;
    }

    @Override
    public Pat findOne(Long aLong) {
        return null;
    }

    @Override
    public Pat update(Pat entity) {

        String sql = "UPDATE pat SET cnp_pacient = ? WHERE pat_id = ?";
        try (Connection connection = DriverManager.getConnection(this.url, this.username, this.password);
             PreparedStatement statement = connection.prepareStatement(sql)) {

            statement.setString(1, entity.getCnpPacient());
            statement.setLong(2, entity.getId());

            statement.executeUpdate();
        } catch (SQLException sqlException) {
            sqlException.printStackTrace();
        }

        return entity;
    }

    @Override
    public Iterable<Pat> findAll() {
        List<Pat> paturi = new ArrayList<>();

        String query = "SELECT * from pat";
        try (Connection connection = DriverManager.getConnection(this.url, this.username, this.password);
             PreparedStatement statement = connection.prepareStatement(query);
             ResultSet resultSet = statement.executeQuery()
        ) {
            while (resultSet.next()) {
                Long idPat = resultSet.getLong("pat_id");
                Tip tip = Tip.valueOf(resultSet.getString("tip"));
                Ventilatie ventilatie = Ventilatie.valueOf(resultSet.getString("ventilatie"));
                String pacient = resultSet.getString("cnp_pacient");

                Pat pat = new Pat(idPat, tip, ventilatie);
                pat.setCnpPacient(pacient);
                paturi.add(pat);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }

        return paturi;
    }
}

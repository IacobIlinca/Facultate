package com.example.examenpractic.Repository;

import com.example.examenpractic.Domain.Oras;
import com.example.examenpractic.Domain.Persoana;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class DBPersoanaRepository implements Repository<Persoana,Long> {
    private String url;
    private String username;
    private String password;

    public DBPersoanaRepository(String url, String username, String password) {
        this.url = url;
        this.username = username;
        this.password = password;
    }


    @Override
    public Persoana findOne(Long aLong) {
        return null;
    }

    @Override
    public Persoana save(Persoana entity) {
        String query = "INSERT INTO persoana(id, nume, prenume,username,parola,oras,strada,numar_strada,telefon) VALUES(?, ?, ?,?,?,?,?,?,?)";
        try (Connection connection = DriverManager.getConnection(this.url, this.username, this.password);
             PreparedStatement statement = connection.prepareStatement(query)
        ) {
            statement.setLong(1, entity.getId());
            statement.setString(2, entity.getNume());
            statement.setString(3, entity.getPrenume());
            statement.setString(4, entity.getUsername());
            statement.setString(5, entity.getParola());
            statement.setString(6, entity.getOras().toString());
            statement.setString(7, entity.getStrada());
            statement.setString(8, entity.getNumarStrada());
            statement.setString(9, entity.getTelefon());
            statement.executeUpdate();

        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
        return entity;
    }

    @Override
    public Persoana delete(Long aLong) {
        return null;
    }


    public Persoana findOneString(String  user) {
        String query = "SELECT * FROM persoana WHERE username=?";
        Persoana pers = null;
        try(Connection connection = DriverManager.getConnection(this.url, this.username, this.password);
            PreparedStatement statement = connection.prepareStatement(query)

        ) {
            statement.setString(1, user);
            ResultSet resultSet = statement.executeQuery();
            while (resultSet.next()) {
                Long id = resultSet.getLong("id");
                String nume = resultSet.getString("nume");
                String prenume = resultSet.getString("prenume");
                String parola = resultSet.getString("parola");
                Oras type = Oras.valueOf(resultSet.getString("oras"));
                String starda = resultSet.getString("strada");
                String nr = resultSet.getString("nr_strada");
                String telefon = resultSet.getString("telefon");

                pers=new Persoana(id,nume,prenume, user,parola, type,starda,nr,telefon );
                pers.setUsername(user);
            }


        } catch (SQLException e) {
            e.printStackTrace();
        }
        return pers;
    }

    @Override
    public Persoana update(Persoana entity) {
        return null;
    }

    @Override
    public Iterable<Persoana> findAll() {
        List<Persoana> persoane = new ArrayList<>();

        String query = "SELECT * from persoana";
        try(Connection connection = DriverManager.getConnection(this.url, this.username, this.password);
            PreparedStatement statement = connection.prepareStatement(query);
            ResultSet resultSet = statement.executeQuery()
        ) {
            while (resultSet.next()) {
                Long id = resultSet.getLong("id");
                String nume = resultSet.getString("nume");
                String prenume = resultSet.getString("prenume");
                String username = resultSet.getString("username");
                String parola = resultSet.getString("parola");
                Oras oras = Oras.valueOf(resultSet.getString("oras"));
                String strada = resultSet.getString("strada");
                String nr = resultSet.getString("numar_strada");
                String telefon = resultSet.getString("telefon");

                Persoana per=new Persoana(id,nume,prenume,username,parola,oras,strada,nr,telefon);
                persoane.add(per);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }

        return persoane;
    }
}

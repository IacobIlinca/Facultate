package com.example.zboruri.Repository;

import com.example.zboruri.Domain.Client;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class DBClientRepo implements Repository<Client, String>{
    private String url;
    private String username;
    private String password;

    public DBClientRepo(String url, String username, String password) {
        this.url = url;
        this.username = username;
        this.password = password;
    }

    @Override
    public Client save(Client entity) {
        return null;
    }

    @Override
    public Client delete(String aLong) {
        return null;
    }

    @Override
    public Client findOne(String aLong) {
        String query = "SELECT * FROM client WHERE username=?";
        Client client = null;
        try(Connection connection = DriverManager.getConnection(this.url, this.username, this.password);
            PreparedStatement statement = connection.prepareStatement(query)

        ) {
            statement.setString(1, aLong);
            ResultSet resultSet = statement.executeQuery();
            while (resultSet.next()) {
                String nume = resultSet.getString("nume");
                client = new Client(aLong, nume);
                client.setId(aLong);
            }


        } catch (SQLException e) {
            e.printStackTrace();
        }
        return client;
    }

    @Override
    public Client update(Client entity) {
        return null;
    }

    @Override
    public Iterable<Client> findAll() {
        List<Client> clienti = new ArrayList<>();

        String query = "SELECT * from client";
        try(Connection connection = DriverManager.getConnection(this.url, this.username, this.password);
            PreparedStatement statement = connection.prepareStatement(query);
            ResultSet resultSet = statement.executeQuery()
        ) {
            while (resultSet.next()) {
                String  id = resultSet.getString("username");
                String nume = resultSet.getString("nume");
                Client client = new Client(id, nume);
                clienti.add(client);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }

        return clienti;
    }
}

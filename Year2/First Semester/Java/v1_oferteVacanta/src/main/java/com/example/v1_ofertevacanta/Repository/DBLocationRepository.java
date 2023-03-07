package com.example.v1_ofertevacanta.Repository;

import com.example.v1_ofertevacanta.Domain.Location;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class DBLocationRepository implements Repository<Location, Double>{
    private String url;
    private String username;
    private String password;

    public DBLocationRepository(String url, String username, String password) {
        this.url = url;
        this.username = username;
        this.password = password;
    }

    @Override
    public Location save(Location entity) {
        String query = "INSERT INTO location(location_id,location_name) VALUES(?, ?)";
        try(Connection connection = DriverManager.getConnection(this.url, this.username, this.password);
            PreparedStatement statement = connection.prepareStatement(query)
        ) {
            statement.setDouble(1, entity.getId());
            statement.setString(2, entity.getLocationName());
            statement.executeUpdate();

        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
        return entity;
    }


    @Override
    public Location delete(Double aDouble) {
        String query = "DELETE FROM location WHERE location_id = ?";

        try(Connection connection = DriverManager.getConnection(this.url, this.username, this.password);
            PreparedStatement statement = connection.prepareStatement(query)
        ) {
            statement.setDouble(1, aDouble);
            statement.executeUpdate();

        } catch (SQLException e) {
            throw new RuntimeException(e);
        }

        return findOne(aDouble);
    }

    @Override
    public Location findOne(Double aDouble) {
        String query = "SELECT * FROM location WHERE location_id=?";
        Location location = null;
        try(Connection connection = DriverManager.getConnection(this.url, this.username, this.password);
            PreparedStatement statement = connection.prepareStatement(query)

        ) {
            statement.setDouble(1, aDouble);
            ResultSet resultSet = statement.executeQuery();
            while (resultSet.next()) {
                String locationName = resultSet.getString("location_name");
                location = new Location(aDouble, locationName);
                location.setId(aDouble);
            }


        } catch (SQLException e) {
            e.printStackTrace();
        }
        return location;
    }

    @Override
    public Location update(Location entity) {
        return null;
    }

    @Override
    public Iterable<Location> findAll() {
        List<Location> locations = new ArrayList<>();

        String query = "SELECT * from location";
        try(Connection connection = DriverManager.getConnection(this.url, this.username, this.password);
            PreparedStatement statement = connection.prepareStatement(query);
             ResultSet resultSet = statement.executeQuery()
        ) {
            while (resultSet.next()) {
                Double id = resultSet.getDouble("location_id");
                String locationName = resultSet.getString("location_name");
                Location location = new Location(id, locationName);
                locations.add(location);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }

        return locations;
    }

}

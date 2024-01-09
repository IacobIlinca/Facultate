package com.example.v1_ofertevacanta.Repository;

import com.example.v1_ofertevacanta.Domain.Hotel;
import com.example.v1_ofertevacanta.Domain.Type;

import java.sql.*;
import java.util.*;

public class DBHotelRepository implements Repository<Hotel, Double> {
    private String url;
    private String username;
    private String password;

    public DBHotelRepository(String url, String username, String password) {
        this.url = url;
        this.username = username;
        this.password = password;
    }

    @Override
    public Hotel findOne(Double aDouble) {
        String query = "SELECT * FROM hotel WHERE hotel_id=?";
        Hotel hotel = null;
        try(Connection connection = DriverManager.getConnection(this.url, this.username, this.password);
            PreparedStatement statement = connection.prepareStatement(query)

        ) {
            statement.setDouble(1, aDouble);
            ResultSet resultSet = statement.executeQuery();
            while (resultSet.next()) {
                Double locationId = resultSet.getDouble("location_id");
                String hotelName = resultSet.getString("hotel_name");
                int noRooms = resultSet.getInt("no_rooms");
                double price = resultSet.getDouble("price_per_night");
                Type type = Type.valueOf(resultSet.getString("type"));
                hotel=new Hotel(aDouble,locationId,hotelName,noRooms,price,type);
                hotel.setId(aDouble);
            }


        } catch (SQLException e) {
            e.printStackTrace();
        }
        return hotel;
    }


    @Override
    public Iterable<Hotel> findAll() {
        List<Hotel> hotels = new ArrayList<>();

        String query = "SELECT * from hotel";
        try(Connection connection = DriverManager.getConnection(this.url, this.username, this.password);
            PreparedStatement statement = connection.prepareStatement(query);
             ResultSet resultSet = statement.executeQuery()
        ) {
            while (resultSet.next()) {
                Double idHotel = resultSet.getDouble("hotel_id");
                Double idLocation = resultSet.getDouble("location_id");
                String hotelName = resultSet.getString("hotel_name");
                int rooms = resultSet.getInt("no_rooms");
                double price = resultSet.getDouble("price_per_night");
                Type type = Type.valueOf(resultSet.getString("type"));

                Hotel hotel=new Hotel(idHotel,idLocation,hotelName,rooms,price,type);
                hotels.add(hotel);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }

        return hotels;
    }

    @Override
    public Hotel save(Hotel entity) {
        String query = "INSERT INTO hotel(hotel_id, location_id, hotel_name,no_rooms,price_per_night,type) VALUES(?, ?, ?,?,?,?)";
        try(Connection connection = DriverManager.getConnection(this.url, this.username, this.password);
            PreparedStatement statement = connection.prepareStatement(query)
        ) {
            statement.setDouble(1, entity.getId());
            statement.setDouble(2, entity.getLocationId());
            statement.setString(3, entity.getHotelName());
            statement.setInt(4, entity.getNoRooms());
            statement.setDouble(5, entity.getPricePerNight());
            statement.setString(6, entity.getType().toString());
            statement.executeUpdate();

        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
        return entity;
    }


    @Override
    public Hotel delete(Double aDouble) {
        String query = "DELETE FROM hotel WHERE id_hotel = ?";

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
    public Hotel update(Hotel entity) {
        return null;
    }
}


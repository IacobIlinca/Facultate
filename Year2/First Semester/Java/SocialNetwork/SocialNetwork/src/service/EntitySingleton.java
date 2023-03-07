package service;

import domain.Friendship;
import domain.Tuple;
import domain.User;
import exceptions.ValidationException;
import graph.Graph;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.time.format.DateTimeFormatterBuilder;
import java.time.temporal.ChronoField;
import java.util.ArrayList;
import java.util.List;

public class EntitySingleton {
    private static EntitySingleton instance = null;

    public EntitySingleton() {
    }

    /**
     * Singleton Pattern
     * @return an entity of this type
     */
    public static EntitySingleton getInstance() {
        if (instance == null) instance = new EntitySingleton();
        return instance;
    }

    /**
     * creates an user
     * @param email the new user's email
     * @param name the new user's name
     * @return the new user
     */
    public User getUser(String name, String email) {
        return new User(name, email);
    }

    /**
     * creates an user
     * @param ID the new user's id
     * @param email the new user's email
     * @param name the new user's name
     * @return the new user
     */
    public User getUserID(Long ID,String email, String name) {
        return new User(ID,name, email);
    }

    /**
     * creates a new instance of Friendship
     * @param id the id of the Friendship created
     * @param id1 the id of the first user
     * @param id2 the id of the second user
     * @return the created Friendship
     * @throws ValidationException if the ids are not of type Long (couldn't be converted to Long)
     */
    public Friendship getFriendShip(String id, String id1, String id2, String frFrom) throws ValidationException {
        try {
            Long userId1 = Long.parseLong(id1);
            Long userId2 = Long.parseLong(id2);
            Long friendshipId = Long.parseLong(id);
            DateTimeFormatter formatter = new DateTimeFormatterBuilder()
                    .appendPattern("yyyy-MM-dd[ HH:mm:ss]")
                    .parseDefaulting(ChronoField.HOUR_OF_DAY, 0)
                    .parseDefaulting(ChronoField.MINUTE_OF_HOUR, 0)
                    .parseDefaulting(ChronoField.SECOND_OF_MINUTE, 0)
                    .toFormatter();
            LocalDateTime since=LocalDateTime.parse(frFrom,formatter);
            return new Friendship(friendshipId, userId1, userId2,since);
        } catch (NumberFormatException ex) {
            throw new ValidationException("invalid friendship");
        }
    }

    public Graph<Long> getFriendshipToGraph(List<Friendship> friendships) {
        List<Tuple<Long, Long>> nodesList = new ArrayList<>();
        for (Friendship friendship : friendships) {
            nodesList.add(new Tuple<>(friendship.getIdUser1(), friendship.getIdUser2()));
        }
        return new Graph<>(nodesList);
    }

}

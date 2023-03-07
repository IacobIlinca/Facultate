package repository.fileRepo;

import domain.Entity;
import domain.User;
import exceptions.ValidationException;

import java.util.List;

public class FileUserRepo extends AbstractFileRepository<Long, User> implements UserRepo {
    private long maxId;

    public FileUserRepo(String fileName) {
        super(fileName);
        maxId = findAll().stream()
                .mapToLong(Entity::getId)
                .max().orElse(0);
    }

    /**
     * Saves the user in the repo file
     * @param user the user to save
     *         entity must be not null
     * @return the saved user
     * @throws ValidationException - if the user is invalid
     */
    @Override
    public User save(User user) throws ValidationException {
        if (user.getId() == null) {
            maxId++;
            user.setId(maxId);
        } else  {
            maxId = Math.max(maxId, user.getId());
        }
        if (getUserById(user.getId()) != null) return null;
        return super.save(user);
    }

    /**
     * Maps the saved string to the user
     * @param attributes - a list of string representing the arguments of the user class
     * @return the converted user
     */
    @Override
    User extractEntity(List<String> attributes) {
        try {
            long id = Long.parseLong(attributes.get(0));
            return new User(
                    id,
                    attributes.get(2),
                    attributes.get(1)
            );
        } catch (NumberFormatException | ArrayIndexOutOfBoundsException exception) {
            return null;
        }
    }

    /**
     * Maps the user to the saved string
     * @param user - the user to convert
     * @return the string converted
     */
    @Override
    String entityToString(User user) {
        return String.format("%s;%s;%s", user.getId().toString(), user.getEmail(), user.getName());
    }

    /**
     * Finds the user by its email
     * @param email the user's to find email
     * @return the needed user
     */
    @Override
    public User getUserByEmail(String email) {
        return findAll().stream()
                .filter(user -> user.getEmail().equals(email))
                .findFirst()
                .orElse(null);
    }


    @Override
    public User getUserById(Long id) {
        return findAll().stream()
                .filter(user -> user.getId().equals(id))
                .findFirst()
                .orElse(null);
    }
}


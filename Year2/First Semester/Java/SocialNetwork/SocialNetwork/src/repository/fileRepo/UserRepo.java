package repository.fileRepo;

import domain.User;
import repository.memoryRepo.Repository;

public interface UserRepo extends Repository<Long, User> {
    /**
     * Finds a user by its email
     * @param email the email of the user we need
     * @return the needed user
     */
    User getUserByEmail(String email);
    User getUserById(Long id);
}

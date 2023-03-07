package service;

import Validators.ValidatorType;
import domain.Friendship;
import domain.User;
import exceptions.ValidationException;
import repository.memoryRepo.Repository;

public class UserService extends BaseService<Long, User> {
    private final Repository<Long, Friendship> friendshipRepo;

    public UserService(Repository<Long, User> repository, Repository<Long, Friendship> friendshipRepo) {
        super(ValidatorType.USER, repository);
        this.friendshipRepo = friendshipRepo;
    }

    /**
     * creates a new instance of the user and adds it to the repo
     * @param email the email of the user
     * @param name the name of the user
     * @throws ValidationException if the user is invalid
     */
    public void addUser(String email, String name) throws ValidationException {
        User user = EntitySingleton.getInstance().getUser(email, name);
        super.addEntity(user);
    }



    /**
     * creates a new instance of the user and adds it to the repo
     * @param ID the id of the user
     * @param email the email of the user
     * @param name the name of the user
     * @throws ValidationException if the user is invalid
     */
    public void addUserID(Long ID, String name, String email) throws ValidationException {
        //!!!!!!
        //User user = EntitySingleton.getInstance().getUserID(ID, name, email);
        User user = EntitySingleton.getInstance().getUserID(ID, email, name);
        super.addEntity(user);
    }

    /**
     * Removes an user and the removes all the friendships related to him
     * @param userId the id of the removed user
     * @return the removed user
     */
    @Override
    public Long deleteEntity(Long userId) {
        Long deletedId = super.deleteEntity(userId);
        friendshipRepo.findAll()
                .forEach(friendship -> {
                    if (friendship.getIdUser1().equals(userId) || friendship.getIdUser2().equals(userId)) {
                        friendshipRepo.delete(friendship.getId());
                    }
                });
        return deletedId;
    }

}

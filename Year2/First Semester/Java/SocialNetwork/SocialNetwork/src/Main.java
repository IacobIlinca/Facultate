import UI.Console;
import domain.Friendship;
import domain.User;
import repository.fileRepo.FileFriendshipRepo;
import repository.fileRepo.FileUserRepo;
import repository.memoryRepo.InMemoryRepository;
import service.FriendshipService;
import service.UserService;

public class Main {
    public static void main(String[] args) {

//        InMemoryRepository<Long, User> repoUser =  new InMemoryRepository<>();
//        InMemoryRepository<Long, Friendship> repoFriendship =  new InMemoryRepository<>();

        FileUserRepo fileUserRepo = new FileUserRepo("C:\\Users\\Ilinca\\Desktop\\facultate\\AN II\\semestrul 1\\map\\seminar\\SocialNetwork\\src\\users.csv");
        FileFriendshipRepo fileFriendshipRepo = new FileFriendshipRepo("C:\\Users\\Ilinca\\Desktop\\facultate\\AN II\\semestrul 1\\map\\seminar\\SocialNetwork\\src\\friendships.csv", fileUserRepo);


//        UserService userService = new UserService(repoUser, repoFriendship);
//        FriendshipService friendshipService = new FriendshipService(repoFriendship, repoUser);

        UserService userService = new UserService(fileUserRepo, fileFriendshipRepo);
        FriendshipService friendshipService = new FriendshipService(fileFriendshipRepo, fileUserRepo);

        Console consoleUI = new Console(userService, friendshipService);
        consoleUI.showUi();

    }
}
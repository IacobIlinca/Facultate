package com.example.javafxrezerva;

import com.example.javafxrezerva.Main;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.control.*;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.scene.layout.AnchorPane;
import social_network.Observer.Observer;
import social_network.domain.*;
import social_network.domain.UserDTOFriend;
import social_network.service.AppService;

import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.stream.Collectors;

public class MainController implements Observer {
    public TextField searchUserTextField;
    private ObservableList<User> usersList = FXCollections.observableArrayList();
    private ObservableList<UserDTOFriend> friendList = FXCollections.observableArrayList();

    private ObservableList<User> friendRequestsList = FXCollections.observableArrayList();

    public ObservableList<User> sentRequestsList = FXCollections.observableArrayList();


    @FXML
    public Label connectedUserLabel;
    @FXML
    private Button refreshButton;
    @FXML
    public Label emailUserLabel;


    private AppService service;
    private User loggedUser = null;
    @FXML
    public Button logoutButton;
    @FXML
    public TableColumn<User, String> firstNameColumn;
    @FXML
    public TableColumn<User, String> lastNameColumn;
    @FXML
    public TableColumn<User, String> emailColumn;
    @FXML
    public TableColumn<UserDTOFriend, String> friendFirstNameColumn;
    @FXML
    public TableColumn<UserDTOFriend, String> friendLastNameColumn;
    @FXML
    public TableColumn<UserDTOFriend, String> friendsSinceColumn;
    @FXML
    public TableView<UserDTOFriend> friendsTableView;

    @FXML
    public TableView<User> usersTable;

//    @FXML
//    public Button acceptButton;

    @FXML
    public Button addFriendshipButton;
//    @FXML
//    public Button rejectButton;
    @FXML
    public Button ChatButton;

    @FXML
    public Button deleteSentRequestButton;
    @FXML
    public TableView<User> sentRequestsTableView;
    @FXML
    public TableColumn<User, String> sentRequestsFirst_nameColumn;
    @FXML
    public TableColumn<User, String> sentRequestsLast_nameColumn;
    @FXML
    public TableColumn<User, String> sentRequestsEmailColumn;




    public void setService(AppService service, String email) {
        this.service = service;
        this.service.addObserver(this);
        this.loggedUser = service.getUserByEmail(email);

        connectedUserLabel.setText(loggedUser.getFirst_name());
        emailUserLabel.setText(loggedUser.getEmail());
        initLists();
    }

    @Override
    public void update() {
        initLists();
    }

    public void logOut() throws IOException {
        Main main = new Main();
        main.switchToLogIn("login.fxml");
    }

    public void openChat() throws IOException {
        Main main = new Main();
        main.switchToChat("message.fxml",loggedUser);
    }

    @FXML
    public void onSearchUserTextField() {
        //cautare dupa first name
        List<User> users = service.getAllUsers();
        List<User> usersTemp = new ArrayList<>();
        for (User user : users) {
            String name = user.getFirst_name();
            if (name.startsWith(searchUserTextField.getText()) && user.getId() != loggedUser.getId() && service.getRelationByUsers(loggedUser.getId(), user.getId()) == null)
                usersTemp.add(user);
        }
        usersList.setAll(usersTemp);
        usersTable.setItems(usersList);
    }


    @FXML
    public void initialize() {
        friendFirstNameColumn.setCellValueFactory(new PropertyValueFactory<UserDTOFriend, String>("first_name"));
        friendLastNameColumn.setCellValueFactory(new PropertyValueFactory<UserDTOFriend, String>("last_name"));
        friendsSinceColumn.setCellValueFactory(new PropertyValueFactory<UserDTOFriend, String>("friendsSince"));


        firstNameColumn.setCellValueFactory(new PropertyValueFactory<User, String>("first_name"));
        lastNameColumn.setCellValueFactory(new PropertyValueFactory<User, String>("last_name"));
        emailColumn.setCellValueFactory(new PropertyValueFactory<User, String>("email"));

        sentRequestsFirst_nameColumn.setCellValueFactory(new PropertyValueFactory<User, String>("first_name"));
        sentRequestsLast_nameColumn.setCellValueFactory(new PropertyValueFactory<User, String>("last_name"));
        sentRequestsEmailColumn.setCellValueFactory(new PropertyValueFactory<User, String>("email"));

        usersTable.setItems(usersList);
//        friendRequestsListView.setItems(friendRequestsList);
        friendsTableView.setItems(friendList);
        sentRequestsTableView.setItems(sentRequestsList);

        addFriendshipButton.setStyle("-fx-background-color: #90EE90; ");
        //acceptButton.setStyle("-fx-background-color: #90EE90; ");
        //rejectButton.setStyle("-fx-background-color: #FF0000; ");
        //removeFriendButton.setStyle("-fx-background-color: #FF0000; ");

    }


    private void initLists() {
        HashMap<User, String> friendsOfUser = service.getFriends(loggedUser.getId());
        List<UserDTOFriend> friendsTemp = new ArrayList<>();
        for (User user : friendsOfUser.keySet()) {
            friendsTemp.add(new UserDTOFriend(user, friendsOfUser.get(user)));
        }
        friendList.setAll(friendsTemp);


        List<User> friendReqTemp = new ArrayList<>();
        List<User> friendReqOfUsers = service.getFriendRequests(loggedUser.getId());
        for (User user : friendReqOfUsers) {
            friendReqTemp.add(user);
        }

        friendRequestsList.setAll(friendReqTemp);


        List<User> allUsers = service.getAllUsers();
        List<User> allUsersTempList = allUsers.stream()
                .filter(user -> user.getId() != loggedUser.getId())
                .filter(user-> service.getRelationByUsers(loggedUser.getId(),user.getId())==null)
                .collect(Collectors.toList());

        usersList.setAll(allUsersTempList);

        List<User> sentRequests = new ArrayList<>();
        List<User> friendRequests = service.getSentRequests(loggedUser.getId());
        for (User user : friendReqOfUsers) {
            sentRequests.add(user);
        }

        sentRequestsList.setAll(friendRequests);


    }



    @FXML
    public void onAddFriendButton() {
        try {
            User userToAskFriendship = usersTable.getSelectionModel().getSelectedItem();
            service.addFriendship( loggedUser.getId(),userToAskFriendship.getId());
            Alert alert = new Alert(Alert.AlertType.INFORMATION, "Sent friendrequest", ButtonType.OK);
            alert.show();

        } catch (NullPointerException npe) {
            Alert alert = new Alert(Alert.AlertType.WARNING, "No user selected!", ButtonType.OK);
            alert.show();
        } catch (Exception ex) {
            Alert alert = new Alert(Alert.AlertType.ERROR, ex.getMessage(), ButtonType.OK);
            alert.show();
        }
    }

    public void onRemoveFriendButton() {

        try {
            long friendID = friendsTableView.getSelectionModel().getSelectedItem().getUID();
            service.removeFriendship(friendID, loggedUser.getId());
        } catch (NullPointerException npe) {
            Alert alert = new Alert(Alert.AlertType.WARNING, "No friend selected!", ButtonType.OK);
            alert.show();
        } catch (Exception ex) {
            ex.printStackTrace();
            Alert alert = new Alert(Alert.AlertType.ERROR, ex.getMessage(), ButtonType.OK);
            alert.show();
        }
    }
    public void onRemoveSendRequestButton() {

        try {
            long friendID = sentRequestsTableView.getSelectionModel().getSelectedItem().getId();
            service.removeFriendship(friendID, loggedUser.getId());
        } catch (NullPointerException npe) {
            Alert alert = new Alert(Alert.AlertType.WARNING, "No friend selected!", ButtonType.OK);
            alert.show();
        } catch (Exception ex) {
            ex.printStackTrace();
            Alert alert = new Alert(Alert.AlertType.ERROR, ex.getMessage(), ButtonType.OK);
            alert.show();
        }
    }

    public void onrequestsButton() throws IOException {
        Main main = new Main();
        main.switchToRequests("requests.fxml",loggedUser);
    }
}







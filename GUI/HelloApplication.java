package com.example.robotguiproject;

import javafx.application.Application;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.scene.control.Button;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.layout.BorderPane;
import javafx.scene.text.Font;
import javafx.stage.Stage;
import org.json.simple.JSONObject;
import java.io.IOException;

public class HelloApplication extends Application {
    @Override
    public void start(Stage stage) throws IOException {
        try{
            FXMLLoader fxmlLoader = new FXMLLoader(HelloApplication.class.getResource("ROBOTGUI.fxml"));

            BorderPane root = new BorderPane();

            // Button visual
            Image image = new Image(getClass().getResourceAsStream("Button.png"));
            ImageView imageView = new ImageView(image);
            Button button = new Button("_On / Off", imageView);
            root.setLeft(button);
            button.setFont(new Font("Times New Roman", 20));
            //root.setCenter(button);
            //button.setText("_On / Off");
            //button.setGraphic(imageView);
            //button.setRotate(30);

            // Label Robot State:
            // Display data somehow
            // Set the label from a variable?

            // Take in encoder data and display into screen
            // Swap some public variable from 0 to 1
            // Create Synchronous Task
            // Action
            button.setOnAction(new EventHandler<ActionEvent>() {
                @Override
                public void handle(ActionEvent actionEvent) {
                    // Accepts action even that is passed through this function
                    // Action that we want is to turn on the server connection
                    // To turn on the robot?

                    SynchronousJson synchronousJson = new SynchronousJson();
                    Server server = new Server();

                    Thread jsonThread = new Thread(synchronousJson);
                    Thread serverThread = new Thread(server);

                    // If class only used once, maybe use Lambda Expression?
                    serverThread.start();
                    try { Thread.sleep(10); } catch(Exception e) { }
                    jsonThread.start();

                    // Use synchronized keyword for the change variable class
                }
            });

            Scene scene = new Scene(root, 1000, 600);

            //Scene scene = new Scene(fxmlLoader.load(), 320, 240);

            stage.setTitle("On / Off Button");
            stage.setScene(scene);
            stage.show();
        } catch(Exception e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        launch(args);
    }
}
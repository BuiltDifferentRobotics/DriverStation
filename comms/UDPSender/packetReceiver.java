import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;

public class packetReceiver implements Runnable{
    int port;
    public packetReceiver(int por){
        this.port = por;
    }


    @Override
    public void run() {

        try {
            DatagramSocket clientSocket = new DatagramSocket(port);

            byte[] buffer = new byte[65507]; // max buffer size

            clientSocket.setSoTimeout(3000);
            while (true){
                DatagramPacket datagramPacket = new DatagramPacket(buffer, 0, buffer.length);
                clientSocket.receive(datagramPacket);

                byte[] receivedMessage = datagramPacket.getData();
//                receivedMessage =  receivedMessage.replaceAll("[\u0000]", "");
//                double [] arr = receivedMessage;
                System.out.println(receivedMessage);

            }
        } catch (IOException e) {
            System.out.println("Timed Out");
        }

    }
}
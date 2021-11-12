import java.io.IOException;
import java.net.*;
import java.nio.ByteBuffer;
import java.nio.charset.StandardCharsets;
import java.util.Arrays;

public class packetSend implements Runnable{
    private int listeningPort;
    String message;
    double[] msg2 = {1.22, 2.33, 1.223};
    ByteBuffer bb = ByteBuffer.allocate(msg2.length * 8);
    public packetSend(int port, String msg){
        this.listeningPort = port;
        this.message = msg;
        ByteBuffer bb = ByteBuffer.allocate(msg2.length * 8);
        for(double d : msg2) {
            bb.putDouble(d);
        }
    }


    @Override
    public void run() {
        try(DatagramSocket serverSocket = new DatagramSocket(listeningPort+1)) {
            while (true){
                DatagramPacket datagramPacket = new DatagramPacket(
                        message.getBytes(),
                        message.length(),
                        new InetSocketAddress("192.168.211.69", listeningPort)
//                        bb.array(),
//                        bb.array().length,
//                        new InetSocketAddress(InetAddress.getLocalHost(), listeningPort)
                );

                serverSocket.send(datagramPacket);
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

}
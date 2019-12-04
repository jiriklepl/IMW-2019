import java.util.Random;
import java.util.Scanner;

import org.jgroups.JChannel;
import org.jgroups.Message;

public class Peer {

    public static void main (String [] arguments) {
        try {
            JChannel channel = new JChannel ();
            channel.connect ("SharedHashMap");
            channel.setReceiver (new ReceiverEventHandler ());

            Scanner scanner = new Scanner (System.in);
            Random generator = new Random();
            int i = 0;

            while (true) {
                UpdateEvent line = new UpdateEvent(generator.nextInt(), "message" + i++);
                Message message = new Message (null, line);
                channel.send (message);
                Thread.sleep(500);
            }
        }
        catch (Exception e) {
            System.out.println (e);
        }
    }
}

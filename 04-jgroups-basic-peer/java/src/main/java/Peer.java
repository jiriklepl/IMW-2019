import java.util.Scanner;

import org.jgroups.JChannel;
import org.jgroups.Message;


import java.io.Serializable;

public class UpdateEvent implements Serializable {
    private static final long serialVersionUID = 0xBAADBAADBAADL;
    public int key;
    public String value;
}

public class Peer {

    public static void main (String [] arguments) {
        try {
            JChannel channel = new JChannel ();
            channel.connect ("SharedHashMap");
            channel.setReceiver (new ReceiverEventHandler ());

            Scanner scanner = new Scanner (System.in);
            while (true) {
                UpdateEvent line = new UpdateEvent(0, "message");
                Message message = new Message (null, line);
                channel.send (message);
            }
        }
        catch (Exception e) {
            System.out.println (e);
        }
    }
}

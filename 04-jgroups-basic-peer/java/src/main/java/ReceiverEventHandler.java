import org.jgroups.ReceiverAdapter;
import org.jgroups.Message;
import org.jgroups.View;

import java.util.HashMap;


public class ReceiverEventHandler extends ReceiverAdapter {
    public void viewAccepted (View view) {
        System.out.println ("New view contains " + view.size () + " members.");
        System.out.println ("- " + view);
    }

    public void receive (Message message) {
        // System.out.println ("Message received.");
        // System.out.println ("- " + message);
        // System.out.println ("- " + message.getObject ());

        // state is shared so we should lock it just in case
        synchronized (state) {
            
            UpdateEvent event = (UpdateEvent)message.getObject();

            state.put(event.key, event.value);

            System.out.printf("Map (%d elements):\n", state.size());
            for (Integer item : state.keySet()) {
                System.out.printf("\t%d: %s\n", item, state.get(item));
            }
        }
    }

    HashMap<Integer, String> state = new HashMap<Integer, String>();
}


import java.io.Serializable;

public class UpdateEvent implements Serializable {
    public UpdateEvent(int new_key, String new_string) {
        key = new_key;
        value = new_string;
    }

    private static final long serialVersionUID = 0xBAADBAADBAADL;
    public int key;
    public String value;
}

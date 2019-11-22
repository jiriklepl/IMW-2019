# JGroups: Multicast Messaging


## Part One

Implement a process that will update a shared hash map:
- The shared hash map is available through `SharedHashMap` channel.
- The updates are transmitted through `UpdateEvent` class.

```
import java.io.Serializable;

public class UpdateEvent implements Serializable {
    private static final long serialVersionUID = 0xBAADBAADBAADL;
    public int key;
    public String value;
}
```


## Part Two

Implement a process that will track and display a shared hash map state.

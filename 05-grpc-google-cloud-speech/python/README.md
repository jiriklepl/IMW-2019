# Speech Recognition with gRPC Interface

## Getting audio sample

Use for example [voxforge](http://www.voxforge.org). The service can accept WAV and FLAC files.

## Running the example

```bash
> python3 -m venv .
> bin/pip install requests protobuf grpcio google-auth
> git clone http://github.com/googleapis/googleapis.git
> cd googleapis
> make OUTPUT=.. LANGUAGE=python GRPCPLUGIN=$(pkg-config --variable=prefix grpc++)/usr/bin/grpc_python_plugin
> cd ..
> bin/python client.py /path/to/speech.wav
```

## Running the solution

just run the client script:

```bash
./client.sh
```

Expected result:

```log
Recognized: Painted the sockets in the wall Bill Green the child crawled into the dense. Grass Brides fail. We're honest men work.
Confidence: 0.6708846688270569
Translation: Maloval zásuvky na zdi Bill Green, dítě se plazilo do husté. Travní nevěsty selhávají. Jsme čestní muži.

Recognized:  Trampled the spark else the Flames will spread the hilt of the sword was carved with Fine Designs a round hole was drilled through the thin board.
Confidence: 0.6806400418281555
Translation: Plamenem jiskra, jinak se plameny rozšíří jílec meče byl vyřezán s jemnými vzory, kulatá díra byla vyvrtána přes tenkou desku.

Recognized:  Footprints show to the path he took up the beach
Confidence: 0.5989740490913391
Translation: Stopy ukazují na cestu, po které se vydal po pláži

Recognized:  She was waiting at my front lawn.
Confidence: 0.7792003154754639
Translation: Čekala na můj přední trávník.

Recognized:  Isn't nearly as brought in fresh air.
Confidence: 0.6504870653152466
Translation: Není to skoro tak čerstvý vzduch.

Recognized:  prod the old mule with a Crooked Stick
Confidence: 0.6841939091682434
Translation: prodávejte starou mezek křivou tyčí
```

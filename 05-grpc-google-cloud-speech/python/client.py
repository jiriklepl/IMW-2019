import io
import sys
import grpc
import six

from google.cloud.speech.v1.cloud_speech_pb2 import *
from google.cloud.speech.v1.cloud_speech_pb2_grpc import *

from google import auth as google_auth
from google.oauth2 import service_account as google_oauth2_service_account
from google.auth.transport import grpc as google_auth_transport_grpc
from google.auth.transport import requests as google_auth_transport_requests

from google.cloud import translate_v2 as translate

SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
SERVICE = 'speech.googleapis.com:443'


# We will need credentials to call the service. The default approach
# requires setting the GOOGLE_APPLICATION_CREDENTIALS environment variable.
scoped_credentials, project = google_auth.default (scopes = SCOPES)

# Alternative approach where file is specified directly.
# credentials = google_oauth2_service_account.Credentials.from_service_account_file ('account.json')
# scoped_credentials = credentials.with_scopes (SCOPES)

# The request object represents an HTTP transport layer used to renew tokens.
request = google_auth_transport_requests.Request ()

def speech_text(file):
    with google_auth_transport_grpc.secure_authorized_channel (scoped_credentials, request, SERVICE) as channel:
        # Encoding and sample rate are only needed for RAW files.
        # When using WAV or FLAC files it is detected automatically.
        stub = SpeechStub (channel)

        config = RecognitionConfig ()
        # config.encoding = RecognitionConfig.LINEAR16
        # config.sample_rate_hertz = 16000
        config.language_code = 'en_US'

        audio = RecognitionAudio ()
        audio.content = open (file, 'rb').read ()

        # Create a stub object that provides the service interface.

        message = RecognizeRequest (config = config, audio = audio)
        # print ('Message:')
        # print (message)

        # Call the service through the stub object.
        response = stub.Recognize (message)

        translate_client = translate.Client()

    for result in response.results:
        for alternative in result.alternatives:
            text = alternative.transcript

            if isinstance(text, six.binary_type):
                text = text.decode('utf-8')

            translated = translate_client.translate(
                text, target_language='cs')

            print(u'Recognized: {}'.format(alternative.transcript))
            print(u'Confidence: {}'.format(alternative.confidence))
            print(u'Translation: {}'.format(translated['translatedText']))
        print()

# Just create a channel, the request object could also be None if token renewal is not needed.
for file in sys.argv[1:]:
    speech_text(file)

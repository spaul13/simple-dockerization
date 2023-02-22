import zmq, sys
#from PIL import Image
import json

context = zmq.Context()



socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5556")

def send():
	#frame = cv2.imread(img)
	#frame = Image.open(img)
	socket.send_pyobj([1,2])

	message = socket.recv_json()
	print(message)
	#output_json = json.loads(message)
	return message
send()
#out = send(sys.argv[1])
#print(out)

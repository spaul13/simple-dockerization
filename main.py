import os, sys
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5556")

def main():
	while True:
		l = socket.recv_pyobj()
		print(l)
		result = {"sum": sum(l)}
		socket.send_json(result)
	#a = 1
	#b = 2
	#print("the sum is %f"%(a+b))

if __name__ == "__main__":
	main()

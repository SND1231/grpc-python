import grpc
import sample_pb2
import sample_pb2_grpc

def hello_server(stub, name, num1, num2):
    messages = []
    messages.append(sample_pb2.HelloMessage(name=name, num1=num1, num2=num2))
    responses = stub.HelloServer(iter(messages))
    for response in responses:
        print('Received message {}'.format(response.reply_msg))

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = sample_pb2_grpc.SampleServiceStub(channel)
        print('--Please input your name--')
        while True:
            name = input("What's your name? > ")
            num1 = int(input("What's your number1? > "))
            num2 = int(input("What's your number2? > "))
            hello_server(stub, name, num1, num2)

if __name__ == '__main__':
    run()
    


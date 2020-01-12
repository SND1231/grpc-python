import time
from concurrent import futures
import grpc
import sample_pb2
import sample_pb2_grpc

class SampleServiceServicer(sample_pb2_grpc.SampleServiceServicer):

    def __init__(self):
        pass

    def HelloServer(self, request_iterator, context):
        for new_msg in request_iterator:
            reply_msgs = []
            calc_result = new_msg.num1 + new_msg.num2
            print('Receive new message! [name: {}, calc result: {}]'.format(new_msg.name, str(calc_result)))
            reply_msgs.append(sample_pb2.ReplyMessage(reply_msg='Hey!! {}'.format(new_msg.name)))
            reply_msgs.append(sample_pb2.ReplyMessage(reply_msg='calclate result is {}'.format(str(calc_result))))
            for message in reply_msgs:
                yield message

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    sample_pb2_grpc.add_SampleServiceServicer_to_server(SampleServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print('Starting gRPC sample server...')
    try:
        while True:
            time.sleep(3600)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()


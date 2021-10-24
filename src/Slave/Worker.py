import threading

class Worker(threading.Thread):

    def __init__(self):
        super(Worker, self).__init__()
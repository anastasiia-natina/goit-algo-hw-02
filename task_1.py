from queue import Queue
import random
import time
import threading

class Request:
    def __init__(self, request_id):
        self.request_id = request_id

class ServiceCenter:
    def __init__(self):
        self.request_queue = Queue()

    def generate_request(self):
        while True:

            request_id = random.randint(1, 1000)

            new_request = Request(request_id)

            self.request_queue.put(new_request)
            print(f"Заявка {request_id} додана до черги.")

            time.sleep(random.uniform(0.5, 2))

    def process_request(self):
        while True:
            if not self.request_queue.empty():

                request = self.request_queue.get()
                print(f"Заявка {request.request_id} обробляється.")

                time.sleep(random.uniform(1, 3))
            else:
                print("Черга порожня. Очікується нова заявка.")

                time.sleep(1)


service_center = ServiceCenter()


generate_thread = threading.Thread(target=service_center.generate_request)
process_thread = threading.Thread(target=service_center.process_request)

generate_thread.start()
process_thread.start()


input("Натисніть Enter для завершення програми\n")
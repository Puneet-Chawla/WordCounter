'''import threading

class Messenger(threading.Thread):
    def run(self):

        for _ in range(10,0,-10):
            print(threading.current_thread().getName())


n = Messenger(name="hello")
n.start()

m = Messenger(name="hi")
m.start()
'''
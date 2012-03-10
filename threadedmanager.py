import time
import multiprocessing
import threading

module_max_duration = 3
prio_list = { }

class ThreadModule(multiprocessing.Process):

    def stop(self):
        self.terminate()

    def setModule(self, w, data):
        self.module = w
        self.data = data
        self.time = time.time()

    def duration(self):
        return int(round((time.time() - self.time),0))

    def run(self):
        self.module.main(self.data)
        

class ThreadedManager(threading.Thread):
    proccesses = []
    running = True

    def stop(self):
        self.running = False

    def setCommunication(self, communication):
        self.communication = communication

    def runModule(self, module, data):
        t = ThreadModule()

        t.setModule(module, data)
        self.proccesses.append(t)
        t.start()

    def run(self):

        while self.running:
            for proc in self.proccesses:
                duration = proc.duration()

                if proc.module.name in prio_list.keys():
                    max_duration = prio_list[proc.module.name]
                else:
                    max_duration = module_max_duration
                
                if not proc.is_alive():
                    self.proccesses.remove(proc)

                elif duration >= max_duration:
                    self.communication.say(proc.data['channel'], 
                            'Running of %s took too long (limit=%ds).' % (proc.module.name, max_duration))

                    proc.stop()
                    self.proccesses.remove(proc)

            time.sleep(0.3)


import threading


class PrimeNumber(threading.Thread):
    def __init__(self, number):
        threading.Thread.__init__(self)
        self.Number = number

    def run(self):
        counter = 2
        while counter*counter < self.Number:
            if self.Number % 2 == 0:
                print("{0} is not a prime because {0} = {1} {0} / {1}".format(self.Number, counter))
                return
            counter += 1
        print("{0} is prime".format(self.Number))

threads = []

while True:
    num = int(input("number: " ))
    if num < 1:
        break

    thread = PrimeNumber(num)
    threads += [thread]
    thread.start()

for x in threads:
    x.join()
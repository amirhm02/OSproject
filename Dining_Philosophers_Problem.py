
import threading

class Philosopher(threading.Thread):
    def __init__(self, name, left_fork, right_fork):
        threading.Thread.__init__(self)
        self.name = name
        self.left_fork = left_fork
        self.right_fork = right_fork

    def run(self):
        while True:
            # خوردن
            self.left_fork.acquire()
            self.right_fork.acquire()

            print(f"{self.name} is eating")

            # خوردن به پایان رسید
            self.right_fork.release()
            self.left_fork.release()

            print(f"{self.name} is thinking")

if __name__ == "__main__":
    # تعریف چند فیلسوف و قاشق‌های آن‌ها
    forks = [threading.Lock() for n in range(5)]
    philosophers = [Philosopher(f"Philosopher {n}", forks[n], forks[(n + 1) % 5]) for n in range(5)]

    # شروع فرایند فلسفه خوردن
    for philosopher in philosophers:
        philosopher.start()

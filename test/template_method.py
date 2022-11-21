import abc
import time


# class Application(abc.ABC):
class Application(metaclass=abc.ABCMeta):
    def __init__(self):
        super(Application, self).__init__()
        self.is_done = False

    def _set_done(self):
        self.is_done = True

    def done(self):
        return self.is_done

    @abc.abstractmethod
    def init(self):
        print(f"{__class__} init...")
        pass

    @abc.abstractmethod
    def idle(self):
        pass

    @abc.abstractmethod
    def cleanup(self):
        pass

    def run(self):
        self.init()
        while not self.done():
            self.idle()
        self.cleanup()


# class Buffer(Application):
class Buffer(Application, abc.ABC):

    def __init__(self):
        super(Buffer, self).__init__()
        self.limit = 0

    def init(self):
        # super().init()
        print(f"{__class__} init...")

    def idle(self):
        if self.limit == 4:
            self._set_done()
        else:
            print(f"sleep 2s do some work")
            time.sleep(2)
            self.limit += 2

    def cleanup(self):
        self.limit = 0
        print(f"exit {self.limit}")


class BufferRead(Buffer):
    def __init__(self):
        super(BufferRead, self).__init__()

    def run(self):
        # super().run()
        print(f"do something")


if __name__ == '__main__':
    # b = Buffer()
    b = BufferRead()
    b.init()
    b.run()

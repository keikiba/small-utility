
class Singleton(type):
    # Hold an instance generated as Singleton
    _instances = {}

    def __call__(cls, *args, **kwargs):
        '''
        Invoked when the instance is called as function. 
        Args:
          cls:     class object
          args:    pass list type data to the Singleton instance
          kwargs:  pass dictionary type data to the Singleton instance
        Returns:
          a Singleton instance
        '''
        if cls not in cls._instances:
            cls._instances[cls] = super(
                Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class IncrementalCounter(metaclass=Singleton):
    __instance_counter = None

    def __init__(self):
        if self.__instance_counter is None:
            self.__instance_counter = 0

    def gen(self):
        self.__instance_counter += 1
        return self.read()

    def read(self):
        return self.__instance_counter

    # aliases
    def add(self):
        return self.gen()

def test_main():
    id_gen1 = IncrementalCounter()
    id_gen2 = IncrementalCounter()
    print(id_gen1.gen())
    print(id_gen2.gen())
    print(id_gen1.gen())
    print(id_gen2.gen())
    print(f'latest count (counter:1) = {id_gen1.read()}')
    print(f'latest count (counter:2) = {id_gen2.read()}')
    pass

if __name__ == "__main__":
    test_main()

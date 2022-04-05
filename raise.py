class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    def fly(self):                  #fly()함수 구현 x -> NotImplementedError 발생
        print("very fast")

eagle = Eagle()
eagle.fly()
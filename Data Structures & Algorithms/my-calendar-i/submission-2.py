class Event:
    def __init__(self) -> None:
        self.left = None
        self.right = None
        self.booked = False
        self.lazy = False
    

class MyCalendar:
    def __init__(self):
        self.root = Event()
        self.limit = 10 ** 9
    
    def update(self, event: Event, L: int, R: int, start: int, end: int) -> None:
        if start <= L and R <= end:
            event.booked = True
            event.lazy = True
            return
        
        M = L + (R - L) // 2
        if not event.left:
            event.left = Event()
        if not event.right:
            event.right = Event()
        
        if event.lazy:
            event.left.lazy = True
            event.left.booked = True
            event.right.lazy = True
            event.right.booked = True
            event.lazy = False

        if start <= M:
            self.update(event.left, L, M, start, end)
        if end > M:
            self.update(event.right, M + 1, R, start, end)

        event.booked = event.left.booked or event.right.booked

    def query(self, event: Event, L: int, R: int, start: int, end: int) -> bool:
        if not event or start > R or end < L:
            return False
        if start <= L and end >= R:
            return event.booked
        
        M = L + (R - L) // 2

        if not event.left:
            event.left = Event()
        if not event.right:
            event.right = Event()
        
        if event.lazy:
            event.left.lazy = True
            event.left.booked = True
            event.right.lazy = True
            event.right.booked = True
            event.lazy = False

        left_booked = self.query(event.left, L, M, start, end)
        right_booked = self.query(event.right, M + 1, R, start, end)
        return left_booked or right_booked        

    def book(self, startTime: int, endTime: int) -> bool:
        if self.query(self.root, 0, self.limit, startTime, endTime - 1):        
            return False
        
        self.update(self.root, 0, self.limit, startTime, endTime - 1)
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)
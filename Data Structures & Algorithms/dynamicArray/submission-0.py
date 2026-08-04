class DynamicArray:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        # Simulate a fixed-size array under the hood
        self.arr = [0] * capacity 

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        # If the array is full, resize it
        if self.size == self.capacity:
            self.resize()
        
        # Insert the element at the next available index
        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        # Decrement size first, then return the element at the new size index
        self.size -= 1
        return self.arr[self.size]

    def resize(self) -> None:
        # Double the capacity
        self.capacity *= 2
        
        # Create a new array with the new capacity
        new_arr = [0] * self.capacity
        
        # Copy elements from the old array to the new array
        for i in range(self.size):
            new_arr[i] = self.arr[i]
            
        # Point self.arr to the new array
        self.arr = new_arr

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
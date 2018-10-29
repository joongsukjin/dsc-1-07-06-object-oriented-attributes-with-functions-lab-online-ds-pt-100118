import copy

class School (object):
    def __inti__(self, name):
        self.name = name
        self._roster = {}
        
    def roster(self):
        return self._roster
    
    def add_student(self, name, grade):
        if grade in self._roster:
            self._roster[grade].append(name)
        else:
            self._roster[grade] = [name]
        return self._roster
    
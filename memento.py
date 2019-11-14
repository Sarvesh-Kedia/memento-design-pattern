class Memento:

    def __init__(self, state):
        self.state = state

    def getState(self):
        return self.state
    
    def setState(self, state):
        self.state = state


class Originator:

    def __init__(self):
        self.note = ''
    
    def setNote(self, note):
        self.note = note

    def getNote(self):
        return self.note
    
    def save(self):
        return Memento(self.note)

    def restore(self, memObj):
        self.note = memObj.getState()



class CareTaker:

    def __init__(self):
        self.history = []
        self.currState = -1
    
    def addMemento(self, memObj):
        self.history.append(memObj)
        self.currState = len(self.history) - 1

    def getMemento(self, index):
        return self.history[index]

    def undo(self):
        print('Undoing...')
        
        if(self.currState<=0):
            self.currState = 0
            return self.getMemento(0)
        else:
            self.currState = self.currState - 1
            return self.getMemento(self.currState)

    def redo(self):
        print('Redoing...')

        if self.currState >= len(self.history) - 1:
            self.currState = len(self.history) - 1
            return self.getMemento(self.currState)
        else:
            self.currState = self.currState + 1
            return self.getMemento(self.currState)



def printState(originatorObj):
    print('Current State: ' + originatorObj.getNote())


if __name__ == '__main__':
    originatorObj = Originator()
    caretakerObj = CareTaker()

    originatorObj.setNote("original sentence")
    caretakerObj.addMemento(originatorObj.save())
    printState(originatorObj)

    originatorObj.setNote("first time changed sentence")
    caretakerObj.addMemento(originatorObj.save())
    printState(originatorObj)

    originatorObj.setNote("second time changed sentence")
    caretakerObj.addMemento(originatorObj.save())
    printState(originatorObj)

    originatorObj.restore(caretakerObj.undo())
    printState(originatorObj)

    originatorObj.restore(caretakerObj.undo())
    printState(originatorObj)

    originatorObj.restore(caretakerObj.redo())
    printState(originatorObj)

    originatorObj.restore(caretakerObj.undo())
    printState(originatorObj)
    
    originatorObj.restore(caretakerObj.undo())
    printState(originatorObj)

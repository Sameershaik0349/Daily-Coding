# ABSTARCTION

# combination of abstraction method is caalled abstraction

# IT WILL ONLY SHOW THE OBJECT AND HIDE THE INTERNAL PROCESS
# ex:- atm machine  its hide internal moeny process😂


# imp
'''
1.there is no object for abstarction because we only use for declaration not a implementation
to implement:-
use concrete class-------
it is just a class 

by do syntax class "class name " (main class name):
        next give function
so we implement here ----------

by this we can create more classes for use multiple times with multiple classes 
 we can add festurs in concrete class
 we sure use abstraction fetures in concrete class other wise it rise error
'''



from abc import ABC,abstractmethod

class bank(ABC):
    @abstractmethod
    def create(self):
        pass


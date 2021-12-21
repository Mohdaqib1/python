# This is a Squirrel story base problem.
# Here in this user give (first input) place name where squirrel saw nutshell bundles.
# Second input gave after seen the bundles squirrel what, action taked.

# input format:

# fist input : okala

# second input : collect all and run away.


# output : 
# Squirrel was very hungry. She passed from okala and saw the bundles, and she feeling very happy and start jumpping, she collect and run away.

 # Creating class here
class Kingdom:                             
    def __init__(self, act , first , second , action):      
        self.act = act
        self.first = first
        self.second = second
        self.action = action
    
    def story(self):
        if self.act=="king":
            print("The Pot of the Wit")
            print("Once Emperor {0} became very angry at his favorite minister {1}. He asked {1} to leave the kingdom and go away. Accepting the command of the Emperor, {1} left the kingdom and started working in a {2}.".format(self.first, self.second, self.action))
        else:
            print("Crows in the Kingdom")
            print("One day Emperor {0} and {1} were taking a walk in the palace {2}. It was a nice summer morning and there were plenty of crows happily playing around the pond. While watching the crows, a question came".format(self.first, self.second, self.action))



if __name__ == '__main__':
    act = input("Enter the Story name (king or crows) : ")
    first = input("Enter the first name : ")
    second = input("Enter the second name : ")
    action = input("Enter the working place name like shope name : ")
    
    obj = Kingdom(act , first , second , action)
    obj.story()

''' 
This is a Squirrel story base problem.
Here in this user give (first input) place name where squirrel saw nutshell bundles.
Second input gave after seen the bundles squirrel what, action taked.

input format:

fisrt input : King name.

second input : Minister name.

working place name : farm,


output for The Pot of the Wit story : 
Once Emperor Akbar became very angry at his favorite minister Birbal. He asked Birbal to leave the kingdom and go away. Accepting the command of the Emperor, Birbal left the kingdom and started working in a farm,

output for Crows in the Kingdom story : 
One day Emperor Akbar and Birbal were taking a walk in the palace gardens. It was a nice summer morning and there were plenty of crows happily playing around the pond.

'''
class Kingdom:                             
    def __init__(self, act , first , second , action):      
        self.act = act   # Story name
        self.first = first  # First name (King name) print location 0
        self.second = second  # Second name (Minister name) print location 1
        self.action = action   # Location name (Shope name) print location 2
    
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

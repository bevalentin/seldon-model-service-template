

class CalrissianRunner(object):
    
    def __init__(self, conf, inputs, outputs):

        #self.zoo = zoo
        self.conf = conf
        self.inputs = inputs
        self.outputs = outputs
    
    def update_status(self, progress):

        self.zoo.update_status(self.conf, progress)
        
    def execute(self):

        # do something
        #print("hello world!")

        #self.update_status(20)

        #print("again")

        #self.update_status(100)

        result_key = list(self.outputs.keys())[0]
        self.outputs[result_key]["value"] = ("Success!")


        return True
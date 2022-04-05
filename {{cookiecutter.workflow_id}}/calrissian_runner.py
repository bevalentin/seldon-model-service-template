import sys

class CalrissianRunner(object):
    
    def __init__(self, conf, inputs, outputs):

        self.conf = conf
        self.inputs = inputs
        self.outputs = outputs
    
    def update_status(self, progress):

        self.zoo.update_status(self.conf, progress)
        
    def execute(self):

        print("Job started",file=sys.stderr)

        self.update_status(20)

        print("Job is running",file=sys.stderr)

        self.update_status(100)

        print("Job has finished running",file=sys.stderr)

        result_key = list(self.outputs.keys())[0]
        self.outputs[result_key]["value"] = ("Success!")

        return True
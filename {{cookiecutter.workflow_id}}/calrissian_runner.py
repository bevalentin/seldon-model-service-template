import sys
import zoo

class CalrissianRunner(object):

    def __init__(self, conf, inputs, outputs):

        self.conf = conf
        self.inputs = inputs
        self.outputs = outputs

    def execute(self):

        print("Job started",file=sys.stderr)
        self.conf["lenv"]["message"]="Started";
        zoo.update_status(self.conf, 20)

        print("Job is running",file=sys.stderr)
        self.conf["lenv"]["message"]="Running";
        zoo.update_status(self.conf, 50)

        print("Job has finished running",file=sys.stderr)
        self.conf["lenv"]["message"]="Completed";
        zoo.update_status(self.conf, 100)

        result_key = list(self.outputs.keys())[0]
        self.outputs[result_key]["value"] = ("Success!")

        return True
try:
    import zoo
except ImportError:
    print("Not running in zoo instance")  
    class ZooStub(object):
        def __ini__(self):
            self.SERVICE_SUCCEEDED = False
            self.SERVICE_FAILED = False
    pass

from .calrissian import CalrissianRunner

def {{cookiercutter.workflow_id}}(conf, inputs, outputs):

    runner = CalrissianRunner(zoo=zoo, conf=conf, inputs=inputs, outputs=outputs)

    exit_status = runner.execute()

    if exit_status: 
    
        outputs = runner.outputs
        return zoo.SERVICE_SUCCEEDED

    else: 

        return zoo.SERVICE_FAILED

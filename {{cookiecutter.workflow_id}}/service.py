# see https://zoo-project.github.io/workshops/2014/first_service.html#f1


try:
    import zoo
except ImportError:
    print("Not running in zoo instance")

    class ZooStub(object):
        def __init__(self):
            self.SERVICE_SUCCEEDED = 3
            self.SERVICE_FAILED = 4

        def update_status(self, conf, progress):
            print(f"Status {progress}")

        def _(self, message):
            print(f"invoked _ with {message}")
    conf = {}
    conf["lenv"] = {"message": ""}
    zoo = ZooStub()
    pass

from calrissian_runner import CalrissianRunner


def {{cookiecutter.workflow_id |replace("-", "_")  }}(conf, inputs, outputs):

    runner = CalrissianRunner(zoo=zoo, conf=conf, inputs=inputs, outputs=outputs)

    exit_status = runner.execute()

    if exit_status: 
    
        outputs = runner.outputs
        return zoo.SERVICE_SUCCEEDED

    else: 
        conf["lenv"]["message"] = zoo._("Execution failed")
        return zoo.SERVICE_FAILED

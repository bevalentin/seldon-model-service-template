# see https://zoo-project.github.io/workshops/2014/first_service.html#f1

import zoo

import importlib
importlib.import_module("{{cookiecutter.workflow_id |replace("-", "_")  }}.calrissian_runner","CalrissianRunner")
from dnbr.calrissian_runner import CalrissianRunner

def {{cookiecutter.workflow_id |replace("-", "_")  }}(conf, inputs, outputs):

    runner = CalrissianRunner(conf=conf, inputs=inputs, outputs=outputs)

    exit_status = runner.execute()

    if exit_status: 
    
        outputs = runner.outputs
        return zoo.SERVICE_SUCCEEDED

    else: 
        conf["lenv"]["message"] = zoo._("Execution failed")
        return zoo.SERVICE_FAILED

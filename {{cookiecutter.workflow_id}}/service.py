import zoo

from .calrissian import CalrissianRunner

def {{cookiercutter.workflow_id}}(conf, inputs, outputs):

    runner = CalrissianRunner(zoo=zoo, conf=conf, inputs=inputs, outputs=outputs)

    exit_status = runner.execute()

    if exit_status: 
    
        outputs = runner.outputs
        return zoo.SERVICE_SUCCEEDED

    else: 

        return zoo.SERVICE_FAILED

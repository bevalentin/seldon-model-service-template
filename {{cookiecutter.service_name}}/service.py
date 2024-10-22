try:
    import zoo
except ImportError:

    class ZooStub(object):
        def __init__(self):
            self.SERVICE_SUCCEEDED = 3
            self.SERVICE_FAILED = 4

        def update_status(self, conf, progress):
            print(f"Status {progress}")

        def _(self, message):
            print(f"invoked _ with {message}")

    zoo = ZooStub()

import json
import os
import requests
import sys

from datetime import datetime
from loguru import logger

# For DEBUG
import traceback

logger.remove()
logger.add(sys.stderr, level="DEBUG")


def execute():
    # Doc: https://docs.seldon.io/projects/seldon-core/en/latest/reference/apis/v2-protocol.html
    
    # TODO Obtain the infer URL template from configuration
    # model_namespace = conf["seldonModels"]["namespace"]
    # model_infer_port = conf["seldonModels"]["inferPort"]
    # model_infer_path = conf["seldonModels"]["inferPath"]
    model_infer_url = f"http://{{cookiecutter.service_name}}.exploitation.svc.cluster.local:8000/v2/models/classifier/infer" # noqa

    model_ready_url = model_infer_url.replace("/infer", "/ready")
    model_metadata_url = model_infer_url.replace("/infer", "")

    res = requests.get(model_ready_url)
    logger.info("Model ready status code (reason): %s %s", res.status_code, res.reason)
    logger.info("Model ready text: %s", res.text)

    res = requests.get(model_metadata_url)
    logger.info("Model metadata status code (reason): %s %s", res.status_code, res.reason)
    logger.info("Model metadata: %s", json.dumps(res.json(), indent=2))


def fix_inputs(inputs):
    # Issue: All input values are received as strings, even if they were int, float, etc.
    for key in inputs.keys():
        value = inputs[key].get("value", None)
        # Issue in the issue: The "float" datatype is not present in the inputs data
        dtype = inputs[key].get("dataType", "float")
        if dtype == "integer" and isinstance(value, str):
            inputs[key]["value"] = int(value)
        if dtype == "float" and isinstance(value, str):
            inputs[key]["value"] = float(value)


def {{cookiecutter.workflow_id |replace("-", "_") }}(conf, inputs, outputs): # noqa

    try:
        fix_inputs(inputs)
        logger.info("Config:\n" + json.dumps(conf, indent=2))
        logger.info("Inputs:\n" + json.dumps(inputs, indent=2))
        logger.info("Outputs:\n" + json.dumps(outputs, indent=2))

        # we are changing the working directory to store the outputs in a directory dedicated to this execution
        #working_dir = os.path.join(conf["main"]["tmpPath"], runner.get_namespace_name())
        now = datetime.now().isoformat()
        working_dir = os.path.join(conf["main"]["tmpPath"], f"{{cookiecutter.service_name}}_{now}")
        os.makedirs(working_dir, mode=0o777, exist_ok=True)
        os.chdir(working_dir)

        # TODO INVOKE THE MODEL HERE

        exit_status = zoo.SERVICE_SUCCEEDED

        if exit_status == zoo.SERVICE_SUCCEEDED:
            logger.info(f"Storing the model output on disk")
            model_outputs = { "model_outputs": [ 5.576883936610762 ] }
            data = {
                "outputs": [{
                    "data": model_outputs
                }]
            }
            logger.info(f"Setting model output into output key {list(outputs.keys())[0]}")
            outputs[list(outputs.keys())[0]]["value"] = json.dumps(model_outputs)
            with open('output.json', 'w') as f:
                json.dump(model_outputs, f, indent=2)
            logger.info("Outputs:\n" + json.dumps(outputs, indent=2))
            return zoo.SERVICE_SUCCEEDED

        else:
            conf["lenv"]["message"] = zoo._("Execution failed")
            return zoo.SERVICE_FAILED

    except Exception as e:
        logger.error("ERROR in processing execution template...")
        stack = traceback.format_exc()
        logger.error(stack)
        conf["lenv"]["message"] = zoo._(f"Exception during execution...\n{stack}\n")
        return zoo.SERVICE_FAILED

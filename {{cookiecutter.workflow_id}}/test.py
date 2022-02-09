from service import {{cookiecutter.workflow_id |replace("-", "_")  }}


def main():
    conf = {}

    inputs = {{cookiecutter.inputs }}
    outputs = {{cookiecutter.outputs }}

    {{cookiecutter.workflow_id | replace("-", "_")  }}(conf, inputs, outputs)


if __name__ == "__main__":
    main()

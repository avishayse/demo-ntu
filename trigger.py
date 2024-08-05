from cnvrgv2 import Cnvrg

cnvrg = Cnvrg()

myproj = cnvrg.projects.get("fastapi")

def test(input_params):
    userid = input_params['userid']
    jobid = input_params['jobid']
    command = f"python3 execute_experiment.py {userid} {jobid}"
    e = myproj.experiments.create(
        title="payload", 
        template_names=["medium"], 
        command=command
    )
    return "success"

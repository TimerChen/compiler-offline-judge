import subprocess
from . import testcase


def test(testcase, bash_path):
    res = subprocess.run(["bash", bash_path], universal_newlines=True,
                         input=testcase.src, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
    if testcase.assertion == "success_compile" and res.returncode != 0:
        message = "Build failed unexpectedly.\n"
        message += res.stderr
        return (False, message)
    if testcase.assertion == "failure_compile" and res.returncode == 0:
        return (False, "The build should fail")
    return (True, "")

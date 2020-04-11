import subprocess
import tempfile
import io
import os


def exec_via_temp(input_text, command_params, workdir="", outfile=False):
    temp = tempfile.NamedTemporaryFile(delete=False)
    if outfile:
        temp2 = tempfile.NamedTemporaryFile(delete=False)
    output = ""
    try:
        temp.write(input_text.encode("utf8"))
        temp.close()

        if outfile:
            command_params = [
                x
                if "tempfilename2" not in x
                else x.replace("tempfilename2", temp2.name)
                for x in command_params
            ]
        command_params = [
            x if "tempfilename" not in x else x.replace("tempfilename", temp.name)
            for x in command_params
        ]
        if workdir == "":
            proc = subprocess.Popen(
                command_params,
                stdout=subprocess.PIPE,
                stdin=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            (stdout, stderr) = proc.communicate()
        else:
            proc = subprocess.Popen(
                command_params,
                stdout=subprocess.PIPE,
                stdin=subprocess.PIPE,
                stderr=subprocess.PIPE,
                cwd=workdir,
            )
            (stdout, stderr) = proc.communicate()
        if outfile:
            output = io.open(temp2.name, encoding="utf8").read()
            temp2.close()
            os.remove(temp2.name)
        else:
            output = stdout.decode("utf8")
    except Exception as e:
        print(e)
    finally:
        os.remove(temp.name)
        return output

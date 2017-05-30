
import subprocess
import os

identifier = "1705.04304"
identifier = "1610.10099"
# subprocess.call(["wget", "--user-agent=Mozilla/1.2", "https://arxiv.org/e-print/" + identifier], cwd="/tmp/")
subprocess.call(["mkdir", "-p", identifier + "-src"], cwd="/tmp/")

# subprocess.call(["tar", "-xvf", identifier, "--directory", identifier + "-src"], cwd="/tmp/")

main_file = None

for directory, _, file_list in os.walk("/tmp/" + identifier + "-src"):
  for file_name in file_list:
    print("filename", directory, file_name)
    _, extension = os.path.splitext(file_name)
    if extension == ".tex":
      for line in open(os.path.join(directory, file_name)):
        if "\documentclass" in line or "\documentstyle" in line:
          main_file = os.path.join(directory, file_name)
          print("this is the main file")
      print("true")

subprocess.call(["/home/ubuntu/anaconda3/bin/plastex", "--split-level=-2", "--renderer=HTML5", '--dollars', main_file], cwd="/tmp/" + identifier + "-src")

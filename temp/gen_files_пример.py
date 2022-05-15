import subprocess
import os
out_dir = "../my_new_files"
students=["Иванов","Петров","Сидоров"]

courses=["курс 1","курс 1","курс 2"]

certificate ="""
            Сертификат

{name}

успешно окончил 

{course}
"""

for n, name in enumerate(students):
    filename=f"cert{n}.md"
    out_filename = filename.replace(".md",".docx")
    with open(filename,"w",encoding="utf8")  as fi:
      fi.write(certificate.format(
          name=name, course=courses[n]
          
      ))
    # print(os.access(out_filename,mode=os.W_OK) )
    subprocess.check_call(["pandoc","-o",out_filename,filename]) 

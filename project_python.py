import os
import re
import tarfile
import subprocess

# calling wc for line count
def wc_command(file):
    linecount = os.popen("wc -l " + file).read()
    return linecount.split(" ")[0]

# getting all the identifier in a set
def ids(file):
    ids_set = set()
    ids = re.compile("[a-zA-Z_]+\w*")
    ignore_comment = re.compile("((#.*)|\".*?\"|\'.*?\'|(//.*)|(--.*)$)|/\*.*\*/")
    for line in file:
        identifier = ids.findall(ignore_comment.sub("", line))
        ids_set |= set(identifier)
    return [os.path.basename(Any) for Any in ids_set]

# getting the path of directory where projects are stored
directory_path = input("Enter path: ")

#each project is called below for wc command and to get ids
# wc by giving the file names
# ids by open each file
c_filename = directory_path+"/project_c.c"
c_lines = wc_command(c_filename)

c_open = open(directory_path + r"/project_c.c", 'r')
c_ids = ids(c_open)

clj_filename = directory_path+"/project_clojure.clj"
clj_lines = wc_command(clj_filename)

clj_open = open(directory_path + r"/project_clojure.clj", 'r')
clj_ids = ids(clj_open)

scala_filename = directory_path+"/project_scala.scala"
scala_lines = wc_command(scala_filename)

scala_open = open(directory_path + r"/project_scala.scala", 'r')
scala_ids = ids(scala_open)

pl_filename = directory_path+"/project_prolog.pl"
pl_lines = wc_command(pl_filename)

pl_open = open(directory_path + r"/project_prolog.pl", 'r')
pl_ids = ids(pl_open)

py_filename = directory_path+"/project_python.py"
py_lines = wc_command(py_filename)

py_open = open(directory_path + r"/project_python.py", 'r')
py_ids = ids(py_open)

# loop to link the project`s line count and ids to html page to put everything together
for project in os.listdir(directory_path):
        if project == 'project_c.c':
            c_file = project
            c_html = open('summary_c.html', 'w')
            body = "<html> \
                        <head> \
                    <body bgcolor = 56A5EC> \
                    <h2>C Assignment</h2><link><br><a href=" + c_file + ">C Assignment </a></br></link> \
                    <h3> Line count is: </h3><p>" + str(c_lines) + "</p> \
                    <h3>Identifiers are: </h3><p>" + str(sorted(c_ids)) + " \
                    </p></body></html>"
            c_html.write(body)
            c_html.close()

        if project == 'project_clojure.clj':
            clj_file = project
            clj_html = open('summary_clj.html', 'w')
            body = "<html>\
                        <head> \
                    <body bgcolor = 5EFB6E> \
                    <h2>Clojure Assignment</h2><link><br><a href=" + clj_file + ">Clojure Project </a></br></link> \
                    <h3> Line count is: </h3><p> " + str(clj_lines) + "</p> \
                    <h3>Identifiers are: </h3>" + str(sorted(clj_ids)) + "\
                    </body></html>"
            clj_html.write(body)
            clj_html.close()

        if project == 'project_scala.scala':
            scala_file = project
            scala_html = open('summary_scala.html', 'w')
            body = "<html>\
                        <head> \
                    <body bgcolor = ff6666> \
                    <h2>Scala Assignment</h2><link><br><a href=" + scala_file + ">Scala Project </a></br></link> \
                    <h3> Line count is: </h3><p>" + str(scala_lines) + "</p> \
                    <h3>Identifiers are: </h3>" + str(sorted(scala_ids)) + "\
                    </body></html>"
            scala_html.write(body)
            scala_html.close()

        if project == 'project_prolog.pl':
            pl_file = project
            pl_html = open('summary_pl.html', 'w')
            body = "<html>\
                        <head> \
                    <body bgcolor = F88017> \
                    <h2>Prolog Assignment</h2><link><br><a href=" + pl_file + ">Prolog Project </a></br></link> \
                    <h3> Line count is: </h3><p>" + str(pl_lines) + "<p> \
                    <h3>Identifiers are: </h3>" + str(sorted(pl_ids)) + "\
                    </body></html>"
            pl_html.write(body)
            pl_html.close()

        if project == 'project_python.py':
            py_file = project
            py_name = 'summary_py.html'
            py_html = open(py_name, 'w')
            body = "<html>\
                        <head> \
                    <body bgcolor = FDD017> \
                    <h2>Python Assignment</h2><link><br><a href=" + py_file + ">Python Project </a></br></link> \
                    <h3> Line count is: </h3><p>" + str(py_lines) + "</p> \
                    <h3>Identifiers are: </h3>" + str(sorted(py_ids)) + "\
                    </body></html>"
            py_html.write(body)
            py_html.close()

# main/frontpage  html
html = open('index.html', 'w')
body = """<!DOCTYPE html>
        <html>
            <head><meta charset="UTF-8">
            <center>
            <br><br><br><br>
            <title>CSC 344</title></head>
            <body bgcolor= E3E4FA>
            <h1>CSC 344 - Programming Languages</h1>
            <font size = '5'>
            <p>Umang Patel</p>
            <ul style="list-style:none;">
            <li><a href="summary_c.html">Assignment 1:- C Project</a>     
        	<li><a href="summary_clj.html">Assignment 2:- Clojure Project</a>    
        	<li><a href="summary_scala.html">Assignment 3:- Scala Project</a>   
        	<li><a href="summary_pl.html">Assignment 4:- Prolog Project</a>    
        	<li><a href="summary_py.html">Assignment 5:- Python Project</a>
        	</ul></center>
        	</body>
        </html>"""
html.write(body)
html.close()

# tar to put everything together
tarName = 'csc344.tar.gz'
tar = tarfile.open(tarName, 'w:gz')
tar.add("./", arcname='csc344')
tar.close()

#sending email through mutt
sendTo = input("Sent email to ? ")
email = subprocess.Popen('mutt -s "csc Project Python" ' + sendTo + ' -a ' + tarName + ' ', shell=True)
email.communicate()
print("Email sent: " + sendTo)
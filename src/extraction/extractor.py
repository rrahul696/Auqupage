import os
import re
import sys
import json
from tika import parser


class Extractor:

  def readCourseInfo(input_file, output_file):
    parsedPDF = parser.from_file(input_file)
    with open(output_file,"w",encoding='utf-8') as stream:
      stream.write(parsedPDF["content"])

  def structureCourseInfo(input_file, output_file):
    subjects=dict()
    units=[]
    topics=[]
    title=dict()
    temp =""
    unit = False
    allsubjects=[]
    start=False
    currentsubject=""
    currentunit=""
    i=0
    temp=0
    with open(input_file,"r") as f:
              for line in f:
                      if re.match(r'[0-9][0-9]?\. UE[0-9][0-9]CS[0-9][0-9][0-9].*',line):
                         continue
                      elif re.match(r'(UE[0-9][0-9]CS[0-9][0-9][0-9] )(–) ([A-Za-z &-]*)(.*)',line) and start==True:
                         allsubjects.append(subjects)
                         m = re.match(r'(UE[0-9][0-9]CS[0-9][0-9][0-9] )(–) ([A-Za-z &-]*)(.*)',line)
                         start=True
                         i=0
                         temp=0
                         units=[]
                         subjects=dict()
                         print(m.group(4))
                         #allsubjects.append(subjects)
                         subjects["title"]=m.group(3).strip()
                         subjects["code"]=m.group(1).strip()
                         subjects["topics"]=units
                         #print(m.group(2))


                      elif re.match(r'(UE[0-9][0-9]CS[0-9][0-9][0-9] )(\:) ([A-Za-z &-]*)(.*)',line) and start==True:
                         allsubjects.append(subjects)
                         m = re.match(r'(UE[0-9][0-9]CS[0-9][0-9][0-9] )(\:) ([A-Za-z &-]*)(.*)',line)
                         start = True
                         i=0
                         temp=0
                         units = []
                         subjects=dict()
                         print(m.group(4))
                         #allsubjects.append(subjects)
                         #print(m.group(2))
                         #subjects=dict()
                         subjects["title"]=m.group(3).strip()
                         subjects["code"]=m.group(1).strip()
                         subjects["topics"]=units
                      elif re.match(r'(UE[0-9][0-9]CS[0-9][0-9][0-9])(\:) ([A-Za-z &-]*) (.*)',line) and start==True:
                        allsubjects.append(subjects)
                        m = re.match(r'(UE[0-9][0-9]CS[0-9][0-9][0-9])(\:) ([A-Za-z &-]*) (.*)',line)
                        start = True
                        i=0
                        temp=0
                        units = []
                        subjects=dict()
                        print(m.group(4))
                        #print(m.group(2))
                        #subjects=dict()
                        subjects["title"]=m.group(3).strip()
                        subjects["code"]=m.group(1).strip()
                        subjects["topics"]=units
                        #print(subjects[currentsubject])
                      elif re.match(r'(UE[0-9][0-9]CS[0-9][0-9][0-9] )(–) ([A-Za-z &-]*)(.*)',line) and start==False:
                        m = re.match(r'(UE[0-9][0-9]CS[0-9][0-9][0-9] )(–) ([A-Za-z &-]*)(.*)',line)
                        start=True
                        i=0
                        temp=0
                        units=[]
                        subjects=dict()
                        print(m.group(4))
                        #allsubjects.append(subjects)
                        subjects["title"]=m.group(3).strip()
                        subjects["code"]=m.group(1).strip()
                        subjects["topics"]=units
                        #print(m.group(2))
                      elif re.match(r'(UE[0-9][0-9]CS[0-9][0-9][0-9] )(\:) ([A-Za-z &-]*)(.*)',line) and start==False:
                        m = re.match(r'(UE[0-9][0-9]CS[0-9][0-9][0-9] )(\:) ([A-Za-z &-]*)(.*)',line)
                        start = True
                        i=0
                        temp=0
                        units = []
                        subjects=dict()
                        print(m.group(4))
                        #allsubjects.append(subjects)
                        #print(m.group(2))
                        #subjects=dict()
                        subjects["title"]=m.group(3).strip()
                        subjects["code"]=m.group(1).strip()
                        subjects["topics"]=units
                      elif re.match(r'(UE[0-9][0-9]CS[0-9][0-9][0-9])(\:) ([A-Za-z  &-]*) (.*)',line) and start==False:
                       m = re.match(r'(UE[0-9][0-9]CS[0-9][0-9][0-9])(\:) ([A-Za-z  &-]*) (.*)',line)
                       start = True
                       i=0
                       temp=0
                       units = []
                       subjects=dict()
                       #print(m.group(2))
                       #subjects=dict()
                       print(m.group(4))
                       subjects["title"]=m.group(3).strip()
                       subjects["code"]=m.group(1).strip()
                       subjects["topics"]=units
                      elif re.match(r'(UE[0-9][0-9]CS[0-9][0-9][0-9])(\:)([A-Za-z  &-]*)(.*)',line) and start==False:
                        m = re.match(r'(UE[0-9][0-9]CS[0-9][0-9][0-9])(\:)([A-Za-z  &-]*)(.*)',line)
                        start = True
                        i=0
                        temp=0
                        units = []
                        subjects=dict()
                        print(m.group(4))
                        #print(m.group(2))
                        #subjects=dict()
                        subjects["title"]=m.group(3).strip()
                        subjects["code"]=m.group(1).strip()
                        subjects["topics"]=units
                      elif re.match(r'.*Unit [1-9][1-9]?.*',line.rstrip()) and temp>0:
                         unit =True
                         i=i+1
                         title=dict()
                        # print(subjects[currentsubject])
                         subjects["topics"].append(title)
                         #print(subjects[currentsubject])
                     #elif unit==True and re.match(r'T[1-9].*',line):
                      elif re.match(r'.*Unit #[1-9][1-9]?',line.rstrip()) and temp>0:
                          unit =True
                          i=i+1
                          title=dict()
                          subjects["topics"].append(title)
                          #print(subjects[currentsubject])
                      elif re.match(r'.*Unit  #[1-9][1-9]?',line.rstrip()) and temp>0:
                           unit =True
                           i=i+1
                           title=dict()
                           subjects["topics"].append(title)
                           #print(subjects[currentsubject])
                      elif re.match(r'Unit#[0-9][0-9]?',line.rstrip()) and temp>0:
                           unit =True
                           i=i+1
                           title=dict()
                           subjects["topics"].append(title)
                           #print(subjects[currentsubject])
                      elif re.match(r'.*Unit [1-9][1-9]?.*',line.rstrip()) and temp==0:
                         unit =True
                         title=dict()
                         subjects["topics"].append(title)
                         #print(subjects[currentsubject])
                      elif re.match(r'.*Unit #[1-9][1-9]?',line.rstrip()) and temp==0:
                          unit =True
                          title=dict()
                          subjects["topics"].append(title)
                          #print(subjects[currentsubject])
                      elif re.match(r'.*Unit  #[1-9][1-9]?',line.rstrip()) and temp==0:
                          unit =True
                          title=dict()
                          subjects["topics"].append(title)
                          #print(subjects[currentsubject])
                      elif re.match(r'Unit#[0-9][0-9]?',line.rstrip()) and temp==0:
                           unit =True
                           title=dict()
                           subjects["topics"].append(title)
                           #print(subjects[currentsubject])
                      elif unit==True and re.match(r'([A-Za-z]* [A-Za-z]*)',line.rstrip()):
                         m = re.match(r'([A-Za-z]* [A-Za-z]*)',line.rstrip())
                         print(m.group(1))
                         topics=[]
                         #print(currentsubject)
                         subjects["topics"][i]["title"]=m.group(1).strip()
                         subjects["topics"][i]["subtopics"]=topics
                         #print(m.group(1))
                         #currentunit="title: "+m.group(1)+", subtopics:"
                         temp=temp+1
                         unit = False
                      elif unit==True and re.match(r'([A-Za-z-]*[/,][A-Za-z-]*)',line.rstrip()):
                         m = re.match(r'([A-Za-z-]*[/,][A-Za-z-]*)',line.rstrip())
                         #print(m.group(1))
                         topics=[]
                         #print(currentsubject)
                         subjects["topics"][i]["title"]=m.group(1).strip()
                         subjects["topics"][i]["subtopics"]=topics
                         #print(m.group(1))
                         #currentunit="title: "+m.group(1)+", subtopics:"
                         temp=temp+1
                         unit = False
                     #elif unit==True and not(re.match(r'T[1-9].*',line)) and i>0:
                      elif unit==False and re.match(r'([1-9][1-9]? )(.*)',line.rstrip()) and start==True:
                         m = re.match(r'([1-9][1-9]? )(.*)',line.rstrip())
                         #print(m.group(2))
                         #print(subjects["topics"][i]["subtopics"])
                         subjects["topics"][i]["subtopics"].append(m.group(2).strip())
                         #subjects[currentsubject][0].append(m.group(2))
                      elif unit==False and re.match(r'([0-9][0-9]?.  )(.*)',line.rstrip()) and start==True:
                         m = re.match(r'([0-9][0-9]?.  )(.*)',line.rstrip())
                         #print(m.group(2))
                         #print(subjects["topics"][i]["subtopics"])
                         subjects["topics"][i]["subtopics"].append(m.group(2).strip())
                         #subjects[currentsubject][0].append(m.group(2))
                      elif unit==False and re.match(r'([0-9][0-9]?, [0-9][0-9]? )(.*)',line.rstrip()) and start==True:
                         m = re.match(r'([0-9][0-9]?, [0-9][0-9]? )(.*)',line.rstrip())
                         #print(m.group(2))
                         subjects["topics"][i]["subtopics"].append(m.group(2).strip())
                         #subjects[currentsubject][0].append(m.group(2))
                      elif unit==False and re.match(r'([0-9][0-9]?-[0-9][0-9]? )(.*)',line.rstrip()) and start==True:
                         m = re.match(r'([0-9][0-9]?-[0-9][0-9]? )(.*)',line.rstrip())
                         #print(m.group(2))
                         subjects["topics"][i]["subtopics"].append(m.group(2).strip())
                         #subjects[currentsubject][0].append(m.group(2)
    allsubjects.append(subjects)
    with open(output_file,'w') as f:
        json.dump(allsubjects,f)


if __name__ == '__main__':
  Extractor.structureCourseInfo("C:\\Users\\Arvind\\Desktop\\test.txt")

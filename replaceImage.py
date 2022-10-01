import codecs
import os, sys

# initializing the database
rules = "rules.txt"

dict = {}
with codecs.open(rules, mode='r', encoding='utf8') as file:
  lines = file.read().splitlines()
  for line in lines:
    r = line.split()
    if len(r) > 1:
      dict[r[0]] = r[1]

# HTML annotation on Shift_JIS -> utf8
def replace_conentType(buf):
  prevType="""charset=Shift_JIS"""
  newType ="""charset=utf8"""

  result = ""
  pos = 0
  while True:
    npos = buf.find(prevType, pos)
    if npos < 0: break
    result += buf[:npos] + newType
    pos = npos+len(prevType)
  result += buf[pos:]
  return result 

# replacing an image to a character
def do_replace(buf, spattern, epattern):
  result = ""
  pos = 0
  hit, miss = 0, 0
  while True:
    npos = buf.find(spattern, pos)
    if npos < 0: break
    epos = buf.find(epattern, npos)
    if epos < 0: break
    image = os.path.basename(buf[npos+len(spattern):epos])  # removing dirname 
    n2pos = epos + len(epattern)
#    print ("testing ", image)
    if image == "html": print (buf[npos+len(spattern):epos])
    if image in dict:
#      print ("found ", image, dict[image])

      # replaced character is shown in red 
      #result += buf[pos:npos] + "<span style=\"color:red;\">" + dict[image] + "</span>"
      result += buf[pos:npos] + dict[image]
      hit += 1
    else:
      result += buf[pos:n2pos]
      miss += 1
    pos = n2pos

  result += buf[pos:]
  return result, hit, miss   

def replace_image(buf):
  # pattern for genzo
  spattern1 = "<img width=\"16\" height=\"16\" src=\""
  epattern1 = "\" border=\"0\">"
  # pattern for genzo title
  spattern2 = "<img width=\"24\" height=\"24\" src=\""
  epattern2 = "\" border=\"0\">"
  # pattern for others 
  spattern3 = "<img src=\""
  epattern3 = "\" width=\"16\" height=\"16\" border=\"0\">"

  if buf.find(spattern1) >= 0:
    buf1, hit1, miss1 = do_replace(buf, spattern1, epattern1)
    buf2, hit2, miss2 = do_replace(buf1, spattern2, epattern2)
    return buf2, (hit1+hit2), (miss1+miss2)  
  else:
    return do_replace(buf, spattern3, epattern3)

def main ():
  fromdir = "../shomonji/shomonji.or.jp/soroku"
  todir = "html"

  thit,tmiss = 0,0
  for (dirpath, dirnames, filenames) in os.walk(fromdir):
    ndirpath = todir + dirpath[len(fromdir):]
    if not os.path.isdir(ndirpath):
      os.mkdir(ndirpath)
  
    for file in filenames:
      #if file.find(".html") > 0: 
      if file.find(".htm") > 0: 
        
        fromfile = dirpath+"/"+file
        tofile = ndirpath+"/"+file

#        print (fromfile, tofile)

        with codecs.open(fromfile, mode='r', encoding='shiftjis') as file:
          buf = file.read()
          buf2, hit, miss = replace_image(buf)
          result = replace_conentType(buf2)
          print (fromfile, hit, miss)
          thit += hit
          tmiss += miss

        with codecs.open(tofile, mode='w', encoding='utf8') as file:
          file.write(result)

  print ("total:", thit, tmiss)

def main2():
  buf = sys.stdin.read()
  buf2, hit, miss = replace_image(buf)
  print (hit, miss)

  sys.stdout.write(buf2)



main()

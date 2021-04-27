import codecs
import os

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
      #result += buf[pos:npos] + dict[image]
      result += buf[pos:npos] + "<span style=\"color:red;\">" + dict[image] + "</span>"
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
  # pattern for others 
  spattern2 = "<img src=\""
  epattern2 = "\" width=\"16\" height=\"16\" border=\"0\">"

  if buf.find(spattern1) >= 0:
    return do_replace(buf, spattern1, epattern1)
  else:
    return do_replace(buf, spattern2, epattern2)

def main ():
  fromdir = "shomonji_orgdata"
  todir = "output"

  for (dirpath, dirnames, filenames) in os.walk(fromdir):
    ndirpath = todir + dirpath[len(fromdir):]
    if not os.path.isdir(ndirpath):
      os.mkdir(ndirpath)
  
    for file in filenames:
      if file.find(".html") > 0: 
        
        fromfile = dirpath+"/"+file
        tofile = ndirpath+"/"+file

#        print (fromfile, tofile)

        with codecs.open(fromfile, mode='r', encoding='shiftjis') as file:
          buf = file.read()
          buf2, hit, miss = replace_image(buf)
          result = replace_conentType(buf2)
          print (fromfile, hit, miss)

        with codecs.open(tofile, mode='w', encoding='utf8') as file:
          file.write(result)

main()

import codecs
import unicodedata
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

def main():
  sys.stdin.reconfigure(encoding='Shift_JIS')
  buf = sys.stdin.read()
  buf2, hit, miss = replace_image(buf)
  print (hit, miss)

  buf3 = unicodedata.normalize('NFC', buf2)
  sys.stdout.write(buf3)

main()

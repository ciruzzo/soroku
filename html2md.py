from markdownify import markdownify
import sys

def main():
#  print (sys.argv[1], sys.argv[2])
  infile = sys.argv[1]
  outfile = sys.argv[2]

  file = open(infile, "r").read()
  html = markdownify(file, heading_style="ATX")
 
  open(outfile, "w").write(html)

main()
  

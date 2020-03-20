from jinja2 import Template

def getHtml():
  with open('images.html') as f:
    s = f.read()
  return s

def main():
  image_list = [
    { 'title': 'apple', 'url': 'https://www.dw.com/image/48396304_303.jpg' }
  ]
  tmpl = Template(getHtml())
  print(tmpl.render({ 'images': image_list }))

main()
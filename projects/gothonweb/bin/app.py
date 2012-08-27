import web
import time

# maps paths to classes, e.g. whenever someone visits
# '/', an instance of 'index' will handle the request
urls = (
  '/', 'index',
  '/countdown/(.*)', 'count_down',
)

app = web.application(urls, globals())
render = web.template.render('templates/')

class index(object):
  def GET(self):
    greeting = "Hello World"
    return render.index(greeting)

class count_down:
  def GET(self, count):
    web.header('Content-type', 'text/html')
    web.header('Transfer-encoding', 'chunked')
    yield '<h2>Prepare for launch</h2>'
    yield '<ul>'
    count = int(count)
    template = '<li>Liftoff in %d...</li>'
    for i in range(count,0,-1):
      out = template % i
      time.sleep(1)
      yield out
    yield '</ul>'
    time.sleep(1)
    yield '<h1>Lift off!</h1>'

if __name__ == "__main__":
  app.run()


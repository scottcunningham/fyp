import gtk
import webkit
from pydht import DHT

class BrowserWindow(gtk.Window):

        def __init__(self, node):
            self.node = node

            gtk.Window.__init__(self)

            self.button = gtk.Button(label="Go")
            self.button.connect("clicked", self.on_button_clicked)

            self.view = webkit.WebView()
            self.view.load_html_string("<html>hello world</html>", "dunno")

            self.entry = gtk.Entry()

            hbox = gtk.HBox(False, spacing=1)
            hbox.add(self.entry)
            hbox.add(gtk.VSeparator())
            hbox.add(self.button)

            window = gtk.ScrolledWindow()
            window.add(self.view)

            vbox = gtk.VBox(False, spacing=1)
            vbox.add(hbox)
            vbox.add(window)

            self.add(vbox)
            self.set_default_size(800, 600)
            self.connect("delete-event", gtk.main_quit)
            self.show_all()

        def on_button_clicked(self, widget):
            print("Hello World")
            text = self.entry.get_text()
            print text
            content = self.node.retrieve(text)
            self.view.load_html_string(content, "dunno")

node = DHT("localhost", 4000)
node.bootstrap("localhost", 3000)
k = node.publish("woooooooooooooooooow spaaaaace SPAAAAAAAAAAAAAAAAAAACE <b>SPAAAACE</b>")
print k

browser = BrowserWindow(node)

gtk.main()

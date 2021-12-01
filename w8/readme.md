# W8 Learn Together

## ReadRSS *Class*
### Attributes:
- URL
> (string) url of website
- soup
> (BeautifulSoup) rss feed request using beautiful soup4

### Methods
- getTitles()
> returns an array of all titles found in the given url 
- getContent(title)
> takes the title of an article and returns all content associated with that
> title.

---

## FeedView *Class* 
**Inherits from QTreeView (PyQt5)**

### Attributes
- data
> (list) list of dictionaries of data containing url of rss sites
- root
> (invisibleRootItem) root node of tree
- model
> (QStandardItemModel) used to set tree data type model

### Methods
- importData()
> appends row of keys(url/rss site name) underneath each
> key appends row of corresponding titles
- addTitles(url)
> calls ReadRSS.getTitles(url)
- loadContent()
> matches the currently selected index in tree (title)
> with its key (url) and returns the selected content
- addFeed()
> prompts the user for a key (name of rss site/nickname) and url
> appends to data array in dictionary format
- removeFeed()
> checks if the selected index is equal to a key
> if it is, remove that key/url from data and treeview
- confirmDeletion(feedName)
> prompts user if they are sure the want to delete the rss feed
> displays the name of the selected feed

---

## Ui_MainWindow *class*
**inherits from QMainWindow (PyQt5.QtWidgets)**

### Attributes
- data
> (list) list of dictionaries
- centralWidget
> (QWidget) main widget child of the window
- treeview
> (FeedView) creates a custom QTreeView using FeedView class
- addButton
> (QPushButton) creates a button and sets its parent to central widget
-delButton
> (QPushButton) creates a button and sets its parent to central widget
- browser
> (QWebEngineView) creates a web view and sets its parent to the central widget

### Methods

- retranslateUi(MainWindow)
> adds multi-language implementation,
- loadFeed()
> from the selected title (url) load to the browser
> the content retrieved from FeedView.loadContent

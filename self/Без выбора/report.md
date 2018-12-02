В ходе выполнения работы были созданы:
* класс Post
```python
class Post:
    def __init__(self, author, content, title=None):
        import uuid
        import datetime
        self.author = author
        if title is not None:
            self.title = title
        self._content = content
        self.id = uuid.uuid4()
        self.date = "{0:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now())
        self.comments = list()
```
* класс Comment – наследник Post
```python
class Comment(Post):
    def __init__(self, author, content):
        super(Comment, self).__init__(author=author, content=content)
```
* специальные методы типа getter и setter для класса Post, наследуемые Comment
```python
@content.setter
    def content(self, content):
        self._content = content

    @content.getter
    def content(self):
        return self._content
```
* а также другие полезные методы класса Post, наследуемые Comment
```python
    @property
    def content(self):
        return self._content

    def add_comment(self, comment):
        self.comments.append(comment)
        
    def show(self):
        print("Date: " + str(self.date))
        print("Id: " + str(self.id))
        print("Author: " + str(self.author))
        print("Content: " + str(self._content))

    def show_comments(self):
        for comment in self.comments:
            comment.show()
            print()
```

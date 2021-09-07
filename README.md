# TF-IDF files calculator example
Example of an application for calculating a `term frequency–inverse document frequency` text file. The frontend part is omitted in this application because it is not the leading task.<br>
The application has one page that implements downloading a file and displaying the result of calculations. It is a table with a list of the last 50 words sorted by decreasing TF-IDF index.<br>
Columns of the table: `Word`, `TF`, `TF-IDF`.<br>
The application selects words from the text using the regular expression `([а-яА-Яa-zA-Z]+)`.<br>

## Postman [documentation](https://documenter.getpostman.com/view/9084501/U16gR8G5)

## Algorithm explanation: [wikipedia](https://en.wikipedia.org/wiki/Tf%E2%80%93idf)

---

## Clone project
```sh
$ git clone https://github.com/emeraldlynx/wargaming--tf-idf.git
```

## Build and run
### **Docker**
Start docker
```sh
$ sudo dockerd
```
Build and run app
```sh
$ docker-compose up
```

***Also you can manually install all dependencies with `reqiurements.txt` file:***<br>
```sh
$ pip install -r requirements.txt
```

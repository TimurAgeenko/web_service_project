from http.server import BaseHTTPRequestHandler, HTTPServer


hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    """
        Специальный класс, который отвечает за
        обработку входящих запросов от клиентов
    """
    def do_GET(self):
        """Метод для обработки входящих GET-запросов"""
        self.send_response(200) # Отправка кода ответа
        self.send_header("Content-type", "text/html") # Отправка типа данных, который будет передаваться
        self.end_headers() # Завершение формирования заголовков ответа
        with open("../html/contacts.html", "r", encoding="utf-8") as f:
            message = f.read()
        self.wfile.write(bytes(f"{message}", "utf-8")) # Тело ответа

    def do_POST(self):
        """Метод для обработки входящих POST-запросов"""
        user_name = self.headers.get("user_name")
        email = self.headers.get("user_email")
        message = self.headers.get("user_message")
        body = {
            "user_name": user_name,
            "email": email,
            "message": message,
        }
        print(body)
        self.send_response(200)
        self.end_headers()


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
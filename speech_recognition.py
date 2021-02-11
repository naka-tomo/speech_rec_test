from websocket_server import WebsocketServer

def message_received(client, server, message):
    # 日本語の文字コードがおかしいので修正
    message = bytes(message, "iso-8859-1").decode("utf8")
    print( "認識結果：", message )

def new_client(client, server):
    print("クライアント接続")

def client_left(client, server):
    print("クライアント切断")


def main():
    server = WebsocketServer(60000, host="127.0.0.1")
    server.set_fn_new_client(new_client)
    server.set_fn_client_left(client_left)
    server.set_fn_message_received(message_received) 
    server.run_forever()

if __name__=="__main__":
    main()
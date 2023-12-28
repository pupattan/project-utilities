with open("/etc/postgresql/15/main/postgresql.conf") as f:
    content = f.read()


content = content.replace("port = 5432", "port = 27007")
content = content.replace("#listen_addresses = 'localhost'",
                          "listen_addresses = '*'")

with open("/etc/postgresql/15/main/postgresql.conf", "w") as f:
    f.write(content)

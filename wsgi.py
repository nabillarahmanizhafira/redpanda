import redpanda

app = redpanda.create_app()

if __name__ == "__main__":
    app.run()

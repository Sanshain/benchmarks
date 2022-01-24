import vibe.vibe;

void main()
{
	// auto settings = new HTTPServerSettings;
	// settings.port = 8088;
	// settings.bindAddresses = ["::1", "0.0.0.0"];
	// auto listener = listenHTTP(settings, &hello);

    auto listener = listenHTTP("0.0.0.0:8088", (req, res) 
	{
        res.writeBody("Hello Vibe.d: " ~ req.path);
    });
	
	scope (exit)
	{
		listener.stopListening();
	}

	logInfo("Please open http://127.0.0.1:8088/ in your browser.");
	runApplication();
}

void hello(HTTPServerRequest req, HTTPServerResponse res)
{
	res.writeBody("Hello, World!");
}

import std.stdio;
import vibe.vibe;

import std.process;

// int n = 1
void startServer()  // nothrow
{
	// #1

	auto settings = new HTTPServerSettings;

	settings.port = 8088;
	// settings.options |= HTTPServerOption.reuseAddress;
	settings.options |= HTTPServerOption.reusePort;

	// settings.bindAddresses = ["::1", "0.0.0.0"];
	// settings.bindAddresses = ["::", "0.0.0.0"];	
	settings.bindAddresses = ["0.0.0.0"];

	auto listener = listenHTTP(settings, &hello);


	// #2

    // auto listener = listenHTTP("0.0.0.0:8088", (req, res) 
	// {
    //     res.writeBody("Hello Vibe.d: " ~ req.path);
    // });

	// runApplication();

	scope (exit)
	{
		// listener.stopListening();
	}

	logInfo("Please open http://127.0.0.1:8088/ in your browser.");	
}

void main(){
	
	version(Windows){
		startServer();
		
		// setupWorkerThreads(8);  //  has no effect
		// runWorkerTaskDist(&startServer);			

		runApplication();
	}
	else
	{
 		writeln("pid: ", thisProcessID);

		import core.sys.posix.unistd : fork, pid_t;

		writeln("pid: ", thisProcessID);

		for(int x=0; x<2; x++)
		{
			pid_t pid = fork();			
			writeln(pid);
		}

		startServer();
		// if (pid == 0){
		// 	startServer();
		// }		

	}	
}

void hello(HTTPServerRequest req, HTTPServerResponse res)
{
	res.writeBody("Hello, World!");
}


// seee also here https://github.com/tchaloupka/httpbench/blob/master/dlang/vibe-d/app.d
// https://vibed.org/api/vibe.http.server/HTTPServerSettings.bindAddresses
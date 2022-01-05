import std.stdio;
import hunt.http;

// void main()
// {
// 	writeln("Edit source/app.d to start your project.");
// }


void main()
{
    auto server = HttpServer.builder()
        .setListener(8080, "0.0.0.0")
        .setHandler((RoutingContext context) {
            context.write("Hello World!");
            context.end();
        }).build();

    server.start();
}

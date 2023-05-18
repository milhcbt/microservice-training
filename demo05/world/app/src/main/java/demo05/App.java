/*
 * This Java source file was generated by the Gradle 'init' task.
 */
package demo05;
import static spark.Spark.*;

public class App {

    public static void main(String[] args) {
        port(5001);
        before((request, response) -> 
            System.err.println(request.requestMethod() + " " + request.url()));

        get("/world/:name", (req, res) -> req.params(":name"));
        get("/:name", (req, res) -> req.params(":name"));
        get("/", (req, res) -> "world");
    }
}

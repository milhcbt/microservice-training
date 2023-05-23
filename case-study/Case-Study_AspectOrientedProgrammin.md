Aspect-Oriented Programming (AOP) in Spring Framework is a programming paradigm that aims to increase modularity by allowing separation of cross-cutting concerns. It does so by adding additional behavior (advice) to existing code (join points) without modifying the code itself, instead separately specifying (via pointcuts) where to modify.

Spring AOP is a powerful tool for improving code modularity, readability and separation of concerns. Here we will demonstrate some of the core AOP concepts using Spring AOP in a simple Spring Boot application.

First, let's start with setting up a Spring Boot project. You can do this through the [Spring Initializer](https://start.spring.io/). In this project, ensure you include the 'Spring AOP' dependency.

Now, let's define some basic business logic. We'll have a `MathService` that provides `add` and `subtract` methods.

```java
@Service
public class MathService {

    public int add(int x, int y) {
        return x + y;
    }

    public int subtract(int x, int y) {
        return x - y;
    }
}
```

Now, we will define a logging aspect that will run before and after our methods:

```java
@Aspect
@Component
public class LoggingAspect {
    @Before("execution(* com.example.demo.MathService.*(..))")
    public void before(JoinPoint joinPoint) {
        System.out.println("About to call function " + joinPoint.getSignature().getName());
    }

    @AfterReturning(pointcut = "execution(* com.example.demo.MathService.*(..))", returning = "result")
    public void afterReturning(JoinPoint joinPoint, Object result) {
        System.out.println("Function " + joinPoint.getSignature().getName() + " returned " + result);
    }
}
```

In this example, the `LoggingAspect` implements a simple logging mechanism. Whenever you call the `add` or `subtract` methods of `MathService`, the program logs information about the method call and its return value. This is a typical example of a cross-cutting concern - logging is needed in many parts of an application, and AOP helps you achieve that without cluttering your code.

Let's analyze the `LoggingAspect` in a bit more detail:

1. `@Aspect` and `@Component` are Spring annotations to denote that this class is an Aspect and it should be managed by Spring's dependency injection.

2. `@Before` and `@AfterReturning` are examples of "advice" types. They denote code to be run before a method execution and after a method returns respectively.

3. The string within the `@Before` and `@AfterReturning` annotations is a "pointcut" expression. This particular expression matches all methods in the `MathService` class. `execution(* com.example.demo.MathService.*(..))` says "match the execution of any method in `MathService` taking any number of arguments".

4. The `before` and `afterReturning` methods receive a `JoinPoint` parameter which provides metadata about the specific method execution that the advice is being applied to.

5. In `@AfterReturning`, the `returning` parameter is used to capture the returned result of the method. It matches the name of the second parameter in the advice method.

Now, whenever you run your Spring Boot application and a method from `MathService` is called, you will see the logging output from `LoggingAspect`.

This is a basic example. Spring AOP is a very powerful tool and it can do much more including exception handling advice, ordering aspects and much more.
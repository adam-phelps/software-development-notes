# Java Tips

Incrementing a value using prefix `++i` and postfix `i++` results in different results:
``` java
public class MyClass {
    public static void main(String args[]) {
        int i = 10;
        System.out.println(i++);
        int x = 10;
        System.out.println(++x);
    }
}
```
Output
```
10
11
```
[Source](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/op1.html)
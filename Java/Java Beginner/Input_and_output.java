import java.util.*;

/**
 * Input_and_output
 */
public class Input_and_output {
        public static void main(String args[]){

        //1. Varibales
        //1.1 int
           int x;
           x = 10;
           System.out.println(x);

           int y = 20;
           System.out.println(y);

           System.out.println("value is x : "+x);
           System.out.println("value of y : "+y); 

        // 1.2 long
           long l;
           l = 10000000000000000l;
           long n = 10000000000000000L;
           System.out.println(l);
           System.out.println(n);

        // 1.3
           float f = 1.234f;
           System.out.println(f);
           System.out.println("float value : " + f);
        
        // 1.4
           double d = 1.234d;
           System.out.println(d);
           System.out.println("Value of double d : " + d);

        // 1.5 boolean
            boolean b1 = true;
            boolean b2 = false;
            System.out.println(b1);
            System.out.println(b2);

        // 1.6 String
           String s1 = "Ajay";
           String s2 = "Yadav";
           System.out.println(s1);
           System.out.println(s2);

        // 2. Typecasting
            int i1 = 123;
            int i2 = 2345;
            long l1 = i1;
            long l2 = i2;
            System.out.println("typecasting l1 : "+ ((Object)l1).getClass().getSimpleName());
            System.out.println("typecasting l2 : "+ ((Object)l2).getClass().getSimpleName());
        }
}
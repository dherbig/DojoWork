using System;

namespace ConsoleApplication
{
    public class Program
    {
        public static void Main(string[] args)
        {
            // A
            for (int i = 1; i < 256; i++)
            {
                Console.WriteLine(i);
            }
            // B
            for (int j = 1; j < 101; j++)
            {
                bool three = (j % 3 == 0);
                bool five = (j % 5 == 0);
                if (three == five)
                {
                    Console.WriteLine(j);
                }
            }
            // C
            for (int j = 1; j < 101; j++)
            {
                bool three = (j % 3 == 0);
                bool five = (j % 5 == 0);

                if (three && five)
                {
                    Console.WriteLine("FizzBuzz");
                } 
                else if (five)
                {
                    Console.WriteLine("Buzz");
                } 
                else if (three)
                {
                    Console.WriteLine("Fizz");
                }
            }



        }
    }
}

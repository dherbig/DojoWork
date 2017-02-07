using System;
using System.Collections.Generic;
namespace ConsoleApplication
{
    public class Program
    {
        public static void Main(string[] args)
        {
            // Three basic arrays
            int[] basic1 = {0,1,2,3,4,5,6,7,8,9};
            string[] basic2 = {"Tim", "Martin", "Nikki", "Sara"};
            bool[] basic3 = new bool[10];
            for (int idx = 0; idx < 10; idx++)
            {
                if (idx % 2 == 0)
                {
                    basic3[idx] = true;
                }
                else
                {
                    basic3[idx] = false;
                }
            }

            // Multiplication Table
            int[,] multiTable = new int[10,10];
            for (int pos = 0; pos < 10; pos++)
            {
                for (int x = 0; x < 10; x++)
                {
                    multiTable[pos, x] = (pos + 1) * (x + 1);
                }
            }

            // User Info Dictionary
            Dictionary<string,Dictionary<string,string>> masterProfileList = new Dictionary<string,Dictionary<string,string>>();
            foreach (string person in basic2)
            {
                Dictionary<string,string> foo = new Dictionary<string,string>();    
                foo.Add("Name", person);
                foo.Add("Favorite Sport", "Big Game Hunting");
                foo.Add("Pet Name", "Mimsy");
                foo.Add("Ice Cream?", "No");
                masterProfileList.Add(person, foo);
            }
            
            foreach (KeyValuePair<string,Dictionary<string,string>> entry in masterProfileList)
            {
                string output = entry.Key;
                output += ": ";
                foreach (KeyValuePair<string,string> detail in entry.Value)
                {
                    output += detail.Key + ": " + detail.Value + "; ";
                }
                Console.WriteLine(output);
            }
            
        }
    }
}

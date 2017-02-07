using System;
using System.Collections.Generic;

namespace ConsoleApplication
{
    public class Program
    {
        public static void onetotwofiftyfive()
        {
            for (int i = 1; i < 256; i++)
            {
                Console.WriteLine(i);
            }
        }
        public static void oddonetotwofiftyfive()
        {
            for (int i = 1; i < 256; i = i + 2)
            {
                Console.WriteLine(i);
            }
        }
        public static void printSum()
        {
            int sum = 0;
            for (int i = 0; i < 256; i = i + 1)
            {
                sum += i;
                Console.WriteLine("New number: {0} Sum: {1}", i, sum);
            }
        }
        public static void iterate(int[] arr)
        {
            foreach (int val in arr)
            {
                Console.WriteLine(val);
            }
        }
        public static int findMax(int[] arr)
        {
            int max = arr[0];
            foreach (int val in arr)
            {
                if (val > max)
                {
                    max = val;
                }
            }
            return max;
        }
        public static int getAvg(int[] arr)
        {
            int sum = 0;
            foreach (int val in arr)
            {
                sum += val;
            }
            return sum / arr.Length;
        }
        public static Array oddArray()
        {
            List<int> nums = new List<int>();
            for (int i = 1; i < 256; i+=2)
            {
                nums.Add(i);
            }
            int [] ans = nums.ToArray();
            return ans;
        }
        public static int greaterThanY(int [] arr, int y)
        {
            int count = 0;
            foreach (int num in arr)
            {
                if (num > y)
                {
                    count++;
                }
            }
            return count;
        }
        
        public static Array squareTheValues(int[] arr)
        {
            for (int i = 0; i < arr.Length; i++)
            {
                arr[i] *= arr[i];
            }
            return arr;
        }

        public static Array eliminateNegatives(int[] arr)
        {
            for (int i = 0; i < arr.Length; i++)
            {
                if (arr[i] < 0)
                {
                    arr[i] = 0;
                }
            }
            return arr;
        }

        public static void minMaxAvg(int[] arr)
        {
            int sum = 0;
            int min = arr[0];
            int max = arr[0];
            foreach (int val in arr)
            {
                sum += val;
                if (val < min)
                {
                    min = val;
                }
                else if (val > max)
                {
                    max = val;
                }
            }
            Console.WriteLine("Min: {0}. Max: {1}. Avg: {2}.", min, max, sum/arr.Length);
        }

        public static Array shiftValLeft(int[] arr)
        {
            for (var i = 1; i < arr.Length; i++)
            {
                arr[i-1] = arr[i];
            }
            arr[arr.Length-1] = 0;
            return arr;
        }
        public static Array numberToString(int[] arr)
        {
            List<object> holder = new List<object>();
            foreach (int val in arr)
            {
                if (val < 0)
                {
                    holder.Add("Dojo");
                }
                else
                {
                    holder.Add(val);
                }
            }
            object[] ans = holder.ToArray();
            return ans;
        }

        public static void Main(string[] args)
        {
            onetotwofiftyfive();
            oddonetotwofiftyfive();
            printSum();
        }
    }
}

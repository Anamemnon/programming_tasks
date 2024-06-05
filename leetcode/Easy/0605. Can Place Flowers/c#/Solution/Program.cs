namespace Solution
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(CanPlaceFlowers([1, 0, 0, 0, 1], 1));
        }

        public static bool CanPlaceFlowers(int[] flowerbed, int n)
        {
            if (n == 0) return true;
            if (flowerbed is null || flowerbed.Length == 0) return false;
            if (flowerbed.Length == 1) return flowerbed[0] == 0;

            int i = 1;
            if (flowerbed[0] == 0 && flowerbed[1] == 0)
            {
                flowerbed[0] = 1;
                n--;
            }

            while (i < flowerbed.Length - 1 && n > 0)
            {
                if (flowerbed[i - 1] == 0 && flowerbed[i] == 0 && flowerbed[i + 1] == 0)
                {
                    n--;
                    flowerbed[i] = 1;
                    i += 2;
                }
                else
                {
                    i++;
                }

            }

            if (flowerbed[^2] == 0 && flowerbed[^1] == 0) n--;

            return n <= 0;
        }
    }
}

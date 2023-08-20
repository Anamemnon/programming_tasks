namespace TestProject1
{
    public class Tests
    {
        [SetUp]
        public void Setup()
        {
        }

        [TestCase(new int[] { 1, 2, 3, 4, 5, 6, 7 }, 3, new int[] { 5, 6, 7, 1, 2, 3, 4 })]
        [TestCase(new int[] { -1, -100, 3, 99 }, 2, new int[] {3, 99, -1, -100 })]
        public void Test1(int[] input, int k, int[] expected)
        {
            Solution.Rotate(input, k);
            Assert.That(input, Is.EqualTo(expected));
        }
    }
}
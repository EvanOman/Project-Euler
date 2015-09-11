#include<iostream>
#include<chrono>

using namespace std;

bool isPrime(int n);

int main()
{
	/* Begin Time */
	auto t1 = std::chrono::high_resolution_clock::now();
	clock_t start = clock();

    int numPrimes = 1;
    int n = 3;
    int primeSum = 2;
    while (numPrimes <= 2000000)
    {
        if (isPrime(n))
        {
            primeSum += n;
            numPrimes++;
            cout << n << "\n";
            cin;
        }
        n+=2;
    }
    std::cout << "Sum is " << primeSum << "\n";
	clock_t end = clock();
	

	/* End Time */
	auto t2 = std::chrono::high_resolution_clock::now();
	double timing = std::chrono::duration_cast<std::chrono::milliseconds>(t2-t1).count();
	double time = (double) (end-start) / CLOCKS_PER_SEC * 1000.0;

	cout << "Total time:\t" << timing / 1000.0 << endl;
	cout << "Total CPU time:\t" << time << endl;

}

bool isPrime(int n)
{
    for (int i = 2; i*i <= n; i++)
    {
        if (!(n % i))
        {
            return false;
        }
    }
    return true;
}

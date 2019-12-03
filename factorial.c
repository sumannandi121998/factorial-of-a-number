long factorial(int n) //function for calculating factorial
{
  long i,m=1;
  if (n<0)
      return -1;
  else
    {
     for (i=0;i<n;i++)
      m=m*(i+1);
     return m;
    }
}
  int main()
  {
    return 0;
  }


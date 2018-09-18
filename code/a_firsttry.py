import nsfg
import thinkstats2
import thinkplot

#chapter 1 code examples
df = nsfg.ReadFemPreg()
#print(df)
#df = nsfg.CleanFemPreg(df) how to make it work it is already cleaned ??
print(df.outcome.value_counts(sort=False))
print(df['birthwgt_lb'].value_counts(sort=False))

#chapter 2 code examples
myhist = thinkstats2.Hist([1,2,2,3,5])
print(myhist.Freq(2))
print(myhist.Values())
for val in sorted(myhist.Values()):
    print(val, myhist.Freq(val))

thinkplot.Hist(myhist)
thinkplot.Show(xlabel='value',ylabel='frequency',title='Anju')

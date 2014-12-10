# https://code.google.com/codejam/contest/4214486/dashboard#s=p0

# the basic idea is to use the dynamic programming.
# 
# the question is to arrange k different keys in m positions. m>k
# 
# define function f(k,m) is the the number of combinations of assigning k different keys in m positions;
# it can be solved if we know the answer of a small size problem.
# 
# C(i,j) is selecting i elements from j elements.
# 
# f(k,m) = f(k-1,m-1)C(1,m) + f(k-1,m-2)C(2,m) + f(k-1,m-3)C(3,m) + ... + f(k-1,k-1)C(m-(k-1), m)

# where f(k-1,k-1)=(k-1)!

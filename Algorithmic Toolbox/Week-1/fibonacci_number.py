FibList(n)

create an array F[0...n]
f[0] <- 0
f[1] <- 1
for i from 2 to n:
	F[i] <- F[i-1] + F[i-2]
return F[n]

--------------------Solution---------------------------

			def calc_fib(n):
				f = [0]*n
				(f[0], f[1]) = (0, 1)

				for i in range(2,n):
					f[i] = f[i-1] + f[i-2]
				return f[-1]

			n = int(input())
			print(calc_fib(n))

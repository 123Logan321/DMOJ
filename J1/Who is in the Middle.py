yi = int(input())
er = int(input())
san = int(input())

if yi < er and yi > san:
    print (yi)

elif yi < san and yi > er:
    print (yi)
    
elif er < san and er > yi:
    print (er)
    
elif er < yi and er > san:
    print (er)
    
elif san < yi and san > er:
    print (san)
    
elif san < er and san > yi:
    print (san)

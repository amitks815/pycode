def fun(arg1,*args,**kwargs):

    print('the first argument is :',arg1 )

    for i in args:
        print('remain args is ;',i)

    print('another value is :',kwargs)

fun('hello','amit','is ','here',place='bengaluru')


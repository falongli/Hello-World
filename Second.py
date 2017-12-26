
sTemp = 'haha'
print(sTemp)

def OneFunc():
    s = 'bee'
    '''def innerFunc():
        print('innerFunc')
        return None
    innerfunc()'''
    bLocal = 'innerFunc' in locals()
    print('innerFunc is local function:{0}'.format(bLocal))
    return  None

OneFunc()
bGlobal = 'OneFunc' in globals();
print('OneFunc is local function:{0}'.format(bGlobal))


fs = [(lambda n, i=i: i + n) for i in range(10)]
print(fs[4](3))
print(fs[5](3))
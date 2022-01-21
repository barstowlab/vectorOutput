from vectorOutput import generateOutputMatrix, generateOutputMatrixWithHeaders, writeOutputMatrix

headers = ['x', 'y']
x = arange(1,10,1)
y = 2*x

plot(x,y)
show()

oMatrixHeaders = generateOutputMatrixWithHeaders([x,y], headers, delimeter=',')

writeOutputMatrix('output.csv', oMatrixHeaders)


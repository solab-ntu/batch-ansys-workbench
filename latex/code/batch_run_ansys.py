# encoding: utf-8
# -- open wbpj
Open(FilePath="E:/temp/model_v192_student.wbpj")

# -- setup parameter value
p1 = Parameters.GetParameter(Name="P1")
p2 = Parameters.GetParameter(Name="P2")
p3 = Parameters.GetParameter(Name="P3")

p1.SetQuantityUnit("mm")
p2.SetQuantityUnit("mm")
p3.SetQuantityUnit("mm")

dp0 = Parameters.GetDesignPoint(Name="0")
dp0.SetParameterExpression(Parameter=p1, Expression="10")
dp0.SetParameterExpression(Parameter=p2, Expression="10")
dp0.SetParameterExpression(Parameter=p3, Expression="10")

# -- update
Update()

# -- write out result
fileIO = open("E:/temp/output.txt","w")

for parameter in Parameters.GetAllParameters():
    value = parameter.Value.ToString()
    fileIO.write(parameter.Name + ", " + value + "\n")
    fileIO.flush()
 
fileIO.close()

# -- save and close
Save(Overwrite=True)
exit
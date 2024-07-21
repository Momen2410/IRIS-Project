

def GetPredection(model, Inputs: list):

    result = {
                0: "Iris-setosa",
                1: "Iris-versicolor",
                2: "Iris-virginica"}
    
    
    predections = model.predict([Inputs])[0]

    return result[predections]
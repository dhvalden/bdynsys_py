import numpy as np
import pandas as pd
from preprocess_data import preprocess_data

df = pd.read_csv("data.csv")

data = preprocess_data("logGDP","EmanzV", "year", df)

def dysymod(paramnr, var1, var2, chVar1, chVar2, mvar1, mvar2):
    nterms = 17
    nmodelterms = paramnr
    nmodels = 3

    # definition of polynomial terms
    term = ["", "/x", "/y", "x", "y", "/(x*y)", "x/y", "y/x", "x*y", "x^2",
            "/x^2", "y^2", "/y^2", "x^3", "y^3", "/x^3", "/y^3"]
    print(term)
    
    # scaling terms with means
    scaling = []
    scaling.append(1)
    scaling.append(mvar1)
    scaling.append(mvar2)
    scaling.append(1/mvar1)
    scaling.append(1/mvar2)
    scaling.append(mvar1*mvar2)
    scaling.append(mvar2/mvar1)
    scaling.append(mvar1/mvar2)
    scaling.append(1/(mvar1*mvar2))
    scaling.append(1/(mvar1*mvar1))
    scaling.append(mvar1*mvar1)
    scaling.append(1/(mvar2*mvar2))
    scaling.append(mvar2*mvar2)
    scaling.append(1/(mvar1*mvar1*mvar1))
    scaling.append(1/(mvar2*mvar2*mvar2))
    scaling.append(mvar1*mvar1*mvar1)
    scaling.append(mvar2*mvar2*mvar2)
    
    # creating array were the selected models will be stored
    selmod1 = np.zeros((nmodelterms, nmodels, nmodelterms))
    selmod2 = np.zeros((nmodelterms, nmodels, nmodelterms))

    print(selmod1)
    print(selmod2)

dysymod(6, data["xs"], data["ys"], data["chxs"], data["chxs"], data["mx"], data["my"])

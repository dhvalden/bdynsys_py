def bdynsys(dataset, indnr, paramnr, x, y):
    if indnr == 2:
        procdata = preprocess_data(indnr, x, y)
        results = dysymod(indnr, paramnr, procdata["xs"], procdata["ys"],
                          procdata["chXs"], procdata["chYs"], procdata["mx"],
                          procdata["my"])
        bayesfactor = bayesfac(indnr, paramnr, results["SEtestx"],
                               results["SEtesty"], procdata["xs"],
                               procdata["ys"], procdata["chXs"],
                               procdata["chYs"])

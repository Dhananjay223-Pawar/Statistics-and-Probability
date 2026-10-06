import numpy as np

def detect_outliers(order_amounts):

    q1 = np.percentile(order_amounts, 25)
    q3 = np.percentile(order_amounts, 75)

    iqr = q3 - q1
    lower_limit = q1 - 1.5 * iqr
    upper_limit = q3 + 1.5 * iqr

    outliers = [
        x for x in order_amounts
        if x < lower_limit or x > upper_limit
    ]

    print("Q1:", q1)
    print("Q3:", q3)
    print("IQR:", iqr)
    print("Lower Limit:", lower_limit)
    print("Upper Limit:", upper_limit)
    print("Outliers:", outliers)


order_amounts = [250, 320, 280, 450, 300, 275, 350, 290, 310, 5000, 325, 270]
detect_outliers(order_amounts)

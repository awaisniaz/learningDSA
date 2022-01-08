import pandas as pd
import camelot

data = camelot.read_pdf("RFQ.pdf")

print(data)